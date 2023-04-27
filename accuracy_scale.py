import pandas as pd
import os, sys
import preprocessing as pre

dir_path = os.path.join(sys.path[0])

data = pd.read_excel(os.path.join(dir_path, r'Testing data\Book.xlsx'))

words = list(data['Word'])
roots = list(data['Root'])
score = 0

root_list = []

for i in range(len(words)):
    norm_word = pre.normalize(words[i])
    wordv2 = pre.pref_handler(norm_word)
    if not pre.check_lexicon(wordv2):
        wordv2 = pre.suff_handler(wordv2)
    
    root_list.append(wordv2)
    if roots[i] in root_list[i]: score +=1

print(f'Accuracy: {round(score/len(words)*100, 2)}%')