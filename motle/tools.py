import sys
from os import getenv, getcwd, path
from pathlib import Path
import glob

DICTIONARIES = {
    'fr_ODS8':{
        'min':2,
        'max':21
    },
    'fr_TEST':{
        'min':4,
        'max':8
    }
}

def user_data_dir() -> Path:
    r"""
    Get OS specific data directory path for Motle.
    Typical user data directories are:
        macOS:    ~/Library/Application Support/Motle
        Unix:     ~/.local/share/Motle   # or in $XDG_DATA_HOME, if defined
        Win 10:   C:\Users\<username>\AppData\Local\Motle
    For Unix, we follow the XDG spec and support $XDG_DATA_HOME if defined.
    :return: full path to the user-specific data dir
    """
    # get os specific path
    if sys.platform.startswith('win'):
        os_path = getenv('LOCALAPPDATA')
    elif sys.platform.startswith('darwin'):
        os_path = '~/Library/Application Support'
    else:
        # linux
        os_path = getenv('XDG_DATA_HOME', '~/.local/share')

    return Path(os_path) / 'Motle'

def get_data_filepath(lang, dictionary, length):
    if '{}_{}'.format(lang.lower(), dictionary.upper()) in DICTIONARIES:
        return path.join(DICTIONARIES_DATA_DIR, '{}_{}_{}.json'.format(lang.lower(), dictionary.upper(), length))

def get_rawdata_filepath(lang, dictionary):
    if '{}_{}'.format(lang.lower(), dictionary.upper()) in DICTIONARIES:
        return path.join(CURRENT_DIR, 'data','dictionaries', '{}_{}.txt'.format(lang.lower(), dictionary.lower()))

def files_exists(lang, dictionary) -> bool:
    key = '{}_{}'.format(lang.lower(), dictionary.upper())
    files = glob.glob(path.join(DICTIONARIES_DATA_DIR, '{}_*.json'.format(key)))
    if len(files) == DICTIONARIES[key]['max']+1-DICTIONARIES[key]['min']:
        res = True
    else:
        res = False
    return res

WORKING_DIR = getcwd()
CURRENT_DIR = path.dirname(path.realpath(__file__))

USER_DATA_DIR = user_data_dir()
DICTIONARIES_DATA_DIR = path.join(USER_DATA_DIR,'dictionaries')

def create_ods(filename, out_filename=path.join('data','dictionary','ods_8.txt')):
    words = []
    with open(filename, 'r') as infile:
        for line in infile.readlines():
            words += line.strip().split(' ')

    with open(out_filename, 'w') as outfile:
        outfile.write('\n'.join(words))

    print('File {} saved with {} words'.format(out_filename, len(words)))
#create_ods(path.join('data','raw','wordle.txt'))