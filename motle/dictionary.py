from collections import defaultdict
from datetime import datetime
import json
import os
import string

from motle import tools

class Dictionary:
    
    def __init__(self, lang, name, length) -> None:
        r"""
        Create a dictionary object for Motle.
        Create an application data directory based on the OS
            macOS:    ~/Library/Application Support/Motle
            Unix:     ~/.local/share/Motle   # or in $XDG_DATA_HOME, if defined
            Win 10:   C:\Users\<username>\AppData\Local\Motle
        Generate automaticaly the json files for the specified dictionary.
        :lang: ISO 639-1 language code
        :name: name of the dictionary to load
        :length: length of the words
        """
        self.lang = lang
        self.name = name
        self.length = length

        self.data_filepath = tools.get_data_filepath(self.lang, self.name, self.length)
        self.rawdata_filepath = tools.get_rawdata_filepath(self.lang, self.name)

        if not os.path.exists(tools.USER_DATA_DIR):
            print('Directories not found, creating data directories :')
            os.mkdir(tools.USER_DATA_DIR)
            os.mkdir(tools.DICTIONARIES_DATA_DIR)
            print(' - {} created'.format(tools.USER_DATA_DIR))
            print(' - {} created'.format(tools.DICTIONARIES_DATA_DIR))

        if not tools.files_exists(lang, name):
            print('Data not found, generating data json :')
            self._generate()
        
        self.data = self._load()

        self.total_words = self.data['total_words']
        self.words = self.data['words']
        self.last_update = datetime.fromisoformat(self.data['update'])

    def _exists(self) -> bool:
        r"""
        Check if the dictionary json file exists exists
        :return: bool
        """
        return os.path.exists(self.data_filepath)

    def _generate_word(self, word) -> dict:
        r"""
        Generate a word description dict
        :word: a word in string
        :return: dict for a specified word
        """
        word_dict = {}
        word_dict['word'] = word.upper()
        word_dict['nb_letters'] = len(word)
        word_dict['spelling'] = list(word.upper())
        word_dict['with']= sorted(list(set(word.upper())))
        word_dict['without']=sorted(list(set(string.ascii_uppercase)-set(word.upper())))
        return word_dict
    

    def _generate(self) -> None:
        r"""
        Generate all json words files.
        There will be multiple files for a specified language,
        dictionary and length. 
        """
        with open(self.rawdata_filepath, 'r') as infile:
            words = infile.readlines()

        defdic = defaultdict(list)
        for word in words:
            wor = word.strip()
            defdic[len(wor)].append(self._generate_word(wor))

        for key in defdic.keys():
            filepath = tools.get_data_filepath(self.lang, self.name, key)

            result_dict = {
                'total_words':len(defdic[key]),
                'update':datetime.now().isoformat(),
                'dictionary':self.name.upper(),
                'language':self.lang.lower(),
                'words':defdic[key]
            }
        
            with open(filepath, 'w') as outfile:
                outfile.write(json.dumps(result_dict))
            print(' - {} created'.format(filepath))

    def _load(self) -> dict:
        r"""
        Load the json file.
        :return: dict data
        """
        with open(self.data_filepath, 'r') as infile:
            return json.loads(infile.read())