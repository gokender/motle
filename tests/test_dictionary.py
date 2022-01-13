import unittest

from motle import dictionary

class Dictionary(unittest.TestCase):

    def setUp(self):
        self.dicti = dictionary.Dictionary('fr','test',5)

    def test_object(self):
        self.assertEqual(self.dicti.lang, 'fr')
        self.assertEqual(self.dicti.name, 'test')
        self.assertEqual(self.dicti.length, 5)
        
    def test__exists(self):
        self.assertEqual(self.dicti._exists(), True)

    def test__generate_word(self):
        res = {
            'word': 'ABAT',
            'nb_letters': 4,
            'spelling': ['A', 'B', 'A', 'T'],
            'with': ['A', 'B', 'T'],
            'without': [
                'C',
                'D',
                'E',
                'F',
                'G',
                'H',
                'I',
                'J',
                'K',
                'L',
                'M',
                'N',
                'O',
                'P',
                'Q',
                'R',
                'S',
                'U',
                'V',
                'W',
                'X',
                'Y',
                'Z'
            ]
        }

        self.assertEqual(self.dicti._generate_word('ABAT'), res)