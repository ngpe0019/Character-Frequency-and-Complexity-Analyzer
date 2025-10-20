# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 15:33:16 2025

@author: joeyj
"""

passage=input('enter a txt file:')
passage=open(passage)
passage_r=passage.readlines()
character=dict()
import re

#organize all the characters into a list
for p in passage_r:
    p=p.rstrip()
    p=p.lower()
    p=re.sub(r'[^\w\s]', '', p)
    w=p.split()
    
for wa in w:
    character[wa]=character.get(wa,0)+1
 #character is a dictionary that shows the word and the frequency of the word.

#determining the average word length
word_length=[]

character_k=list(character.keys())

for k in character_k:
    l=len(k)
    word_length.append(l)

ave_word_l=sum(word_length)/len(word_length)
    
#determine total number of unique words
unique_w_no=len(character_k)

#calculate complexity score = (average word length × number of unique words) ÷ 100
com_score=(ave_word_l*unique_w_no)/100

#finding top 10 letters
alphabet=[]
for g in character_k:
    for t in g:
        alphabet.append(t)
        
alphabet_fre=dict()

for a in alphabet:
    alphabet_fre[a]=alphabet_fre.get(a,0)+1
    
al_list=[]
for aa,ff in alphabet_fre.items():
    al_list.append((ff,aa))
    

al_list.sort()
al_list.reverse()

al_list_top10=al_list[:10]
top_10_a=[]
for al,bl in al_list_top10:
    top_10_a.append(bl)

print('Average word length:',ave_word_l)
print('Unique words:',unique_w_no)
print("Top 10 letters: " + ", ".join(top_10_a))
print('Complexity score:',com_score)