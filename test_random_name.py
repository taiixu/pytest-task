import random_name

adj = open('adj_m.txt', 'r', encoding='utf-8').read().split('\n')
nouns_m = open('nouns_m.txt', 'r', encoding='utf-8').read().split('\n')
nouns_f = open('nouns_f.txt', 'r', encoding='utf-8').read().split('\n')

male_name = random_name.FunRandomName('male')
female_name = random_name.FunRandomName('female')

def test_name():
    assert male_name.get_name().split(' ')[0] in adj
    assert male_name.get_name().split(' ')[1] in nouns_m
    assert female_name.get_name().split(' ')[0][-2:] == 'ая'
    assert female_name.get_name().split(' ')[1] in nouns_f