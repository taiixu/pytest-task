import random

class FunRandomName:
    def __init__(self, gender):
        self.gender = gender
        self.__adj_list = open('adj_m.txt', 'r', encoding='utf-8').read().split('\n')
        self.__nouns_m = open('nouns_m.txt', 'r', encoding='utf-8').read().split('\n')
        self.__nouns_f = open('nouns_f.txt', 'r', encoding='utf-8').read().split('\n')
    
    def __mToF(self, word):
        return word[:-2] + 'ая'
    
    def __get_name_by_gender(self):
        adj = random.choice(self.__adj_list) if self.gender == 'male' else self.__mToF(random.choice(self.__adj_list))
        noun = random.choice(self.__nouns_m) if self.gender == 'male' else random.choice(self.__nouns_f)
        return f"{adj} {noun}"
    
    def get_name(self):
        return self.__get_name_by_gender()
