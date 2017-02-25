# https://www.reddit.com/r/dailyprogrammer/comments/5seexn/20170206_challenge_302_easy_spelling_with/
import requests
from bs4 import BeautifulSoup

periodic_table = {'name' : '', 'symbol': ''}
elements_list = list()

with open('periodic_table.html', 'r') as myfile:
    content = myfile.read()

soup = BeautifulSoup(content ,"html.parser")

table_rows = soup.find_all('tr')

for row in table_rows:
    table_cells = row.find_all('td', limit=2)
    new_element = {'name': '', 'symbol': ''}
    cell_count = 0
    name = ''
    symbol = ''
    for cell in table_cells:
        if cell_count == 0:
            name = cell.text
        else:
            symbol = cell.text
        cell_count += 1
    periodic_table[symbol] = name

del periodic_table['']
del periodic_table['name']
del periodic_table['symbol']

periodic_keys = {k.lower():k for k in periodic_table.keys()}
# print(periodic_keys)
# print(periodic_table)

def break_word(input, original = "", elements = []):
    if(len(input) < 2):
        # print(original)
        # print(elements)
        print('{} ({})'.format(original, elements.split(", ")))
        return break_word(input[0], original, elements)
    else:
        substring = input[0:2]
        if substring in periodic_keys:
            print(periodic_table[periodic_keys[substring]])
            original = original + periodic_keys[substring]
            elements = elements.append(periodic_table[periodic_keys[substring]])
            return break_word(input[2:], original, elements)
        else:
            print(periodic_table[periodic_keys[input[0]]])
            original = original + periodic_keys[input[0]]
            elements = elements.append(periodic_table[periodic_keys[input[0]]])
            return break_word(input[1:], original, elements)

'''
1: take word as input
2: take first 2 letters of word
 - if letters are in periodic_key, add to original and elements
 - else, pass one letter to function

 original word is the word printed as symbols
 elements is list of elements in periodic table
'''
def break_wordtwo(input, original_word = "", elements = []):
    if len(input) >= 2:
        substring = input[0:2]
        remaining = input[2:]
    else:
        substring = input[0]
        remaining = input[1:]
    if substring in periodic_keys:
        original_word = original_word + periodic_keys[substring]
        elements = elements.append(periodic_table[periodic_keys[substring]])
        print(original_word)
        print(elements)
        return break_word(remaining, original_word, elements)
    

# print(break_word("functions"))
print(break_wordtwo("fun"))
print("\n")
# print(break_word("bacon"))
# print("\n")
# print(break_word("poison"))