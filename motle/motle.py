from motle import dictionary

class Motle(dictionary.Dictionary):

    def __init__(self, length, lang='fr', dictionary_name='ODS8'):
        
        self.dictionary = dictionary.Dictionary(lang, dictionary_name, length)
        self._reset()

    def _reset(self) -> None:
        self.words = self.dictionary.words
        self.count = self.dictionary.total_words

    def _valid_word(self, spelling, listH) -> bool:
        for c1, c2 in zip(spelling, listH):
            if c1.upper() != c2.upper() and c2.upper() != '':
                return False
        return True

    def filter(self, wth=[], wthot=[], contains=[]) -> None:
        for wo in wthot:
            data = []
            for word in self.words:
                if wo.upper() in word['without']:
                    data.append(word)
            self.words = list(data)
            self.count = len(self.words)

        for wt in wth:
            data = []
            for word in self.words:
                if wt.upper() in word['with']:
                    data.append(word)
            self.words = list(data)
            self.count = len(self.words)

        data = []
        for word in self.words:
            if self._valid_word(word['spelling'], contains):
                data.append(word)
            self.words = list(data)
            self.count = len(self.words)
        
    def words_str(self):
        res = []
        for word in self.words:
            res.append(word['word'])
        return res