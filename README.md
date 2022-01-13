# Motle

**Work in progress**

Motle is a library that allows you to search for words based on a dictionary by filtering various criteria.

For now I only have the French scrabble dictionary (OD_8)

## How to use it

```python
from motle import motle

mot = motle.Motle(length=5)

mot.count
>> 7980

mot.words
>> [{"word": "ABACA", "nb_letters": 5, "spelling": ["A", "B", "A", "C", "A"], "with": ["A", "B", "C"], "without": ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]}, ..., {"word": "CARRE", "nb_letters": 5, "spelling": ["C", "A", "R", "R", "E"], "with": ["A", "C", "E", "R"], "without": ["B", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "S", "T", "U", "V", "W", "X", "Y", "Z"]}]

# words with letter R
mot.filter(wth=['R']) 
mot.words
>> [{"word": "CARRE", "nb_letters": 5, "spelling": ["C", "A", "R", "R", "E"], "with": ["A", "C", "E", "R"], "without": ["B", "D", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "S", "T", "U", "V", "W", "X", "Y", "Z"]}]

mot.count
>> 1

mot._reset()
mot.count
>> 7980

# words without letter A
mot.filter(wthot=['A']) 
mot.words
>> []

# words containing following letters in the order
mot._reset()
mot.filter(contains=['A','B','','','']) 
mot.words
>> [{"word": "ABACA", "nb_letters": 5, "spelling": ["A", "B", "A", "C", "A"], "with": ["A", "B", "C"], "without": ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]}]
```