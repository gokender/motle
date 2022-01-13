import unittest

from motle import motle

class Motle(unittest.TestCase):

    def setUp(self):
        self.mot = motle.Motle(5, 'fr','test')

    def test_object(self):
        self.assertEqual(self.mot.dictionary.lang, 'fr')
        self.assertEqual(self.mot.dictionary.name, 'test')
        self.assertEqual(self.mot.dictionary.length, 5)

    def test__reset(self):
        self.mot.count = 20
        self.assertEqual(self.mot.count, 20)
        self.mot._reset()
        print(self.mot.count)
        self.assertEqual(self.mot.count, 3)

    def test__valid_word(self):
        word = ['A', 'A']
        self.mot._reset()
        self.assertTrue(self.mot._valid_word(word,['A', '']))
        self.assertTrue(self.mot._valid_word(word,['', 'A']))
        self.assertTrue(self.mot._valid_word(word,['a', '']))
        self.assertFalse(self.mot._valid_word(word,['D', '']))

    def test_filter(self):

        self.mot.filter(wthot=['R'])
        self.assertEqual(self.mot.count, 1)
        self.mot._reset()

        self.mot.filter(wthot=['D'])
        self.assertEqual(self.mot.count, 3)
        self.mot._reset()

        self.mot.filter(wth=['R'])
        self.assertEqual(self.mot.count, 2)
        self.mot._reset()

        self.mot.filter(wth=['E'])
        self.assertEqual(self.mot.count, 1)
        self.mot._reset()

        self.mot.filter(wth=['H'])
        self.assertEqual(self.mot.count, 0)
        self.mot._reset()

        self.mot.filter(contains=['A','','','',''])
        self.assertEqual(self.mot.count, 1)
        self.mot._reset()

        self.mot.filter(contains=['J','','','',''])
        self.assertEqual(self.mot.count, 0)
        self.mot._reset()

    def test_words_str(self):
        self.mot.filter(contains=['A','B','','C',''])
        self.assertEqual(self.mot.count, 1)
        self.assertListEqual(self.mot.words_str(), ['ABACA'])