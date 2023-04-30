import pandas as pd
import os, sys
import preprocessing as pre
import pattern_recognition as pat_r

dir_path = os.path.join(sys.path[0])

data = pd.read_excel(os.path.join(dir_path, r'Testing data\Book.xlsx'))

words = list(data['Word'])
roots = list(data['Root'])
score = 0

root_list = []
err = []
correct_root = []
f_words = []
for i in range(len(words)):
    possible_roots = []

    normalized_word = pre.normalize(words[i])
    wordv2, possible_roots = pre.pref_handler(normalized_word, possible_roots)
    wordv2, possible_roots = pre.suff_handler(wordv2, possible_roots)
    
    if pre.check_lexicon(wordv2) == False:
        possible_roots = pat_r.normalize_root(possible_roots)
    
    if len(possible_roots) == 0: 
        possible_roots.append(wordv2)
        possible_roots = pat_r.normalize_root(possible_roots)
    root_list.append(set(possible_roots))
    if roots[i] in root_list[i]: score +=1
    else: 
        err.append(root_list[i])
        correct_root.append(roots[i])
        f_words.append(words[i])


for i in range(len(err)):
    print(f"{f_words[i]} : {err[i]} ---> {correct_root[i]}")

print(f'Accuracy: {round(score/len(words)*100, 2)}%')
