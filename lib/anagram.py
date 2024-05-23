# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    def match(self, possibleAnagrams):
        letter_list = [letter for letter in self.word]
        return [possible_anagram for possible_anagram in possibleAnagrams if sorted(letter_list) == sorted(possible_anagram)]

