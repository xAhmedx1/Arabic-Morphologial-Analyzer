import os, sys
import arabic_reshaper
from bidi.algorithm import get_display
import nltk
from nltk.stem.isri import ISRIStemmer
from nltk import word_tokenize
st = ISRIStemmer()
# nltk.download('punkt')

# Main folder path
dir_path = os.path.join(sys.path[0])

# list to store files
extra_c_dir = os.path.join(dir_path, 'files') # the directory of the files that contains the extra characters
extra_c = []

# Iterate directory

for path in os.listdir(extra_c_dir):
    # check if current path is a file
    if os.path.isfile(os.path.join(extra_c_dir, path)): 
        extra_c.append(path)

for i in extra_c:
    with open(os.path.join(extra_c_dir, i), "r", encoding = "utf-8") as f:
        if i == 'prefix.txt':
            d = f.readlines()
            prefix = []
            for t in d:
                # prefix.append(get_display(arabic_reshaper.reshape(t[:-1])))
                prefix.append(t[:-1])

        elif i == 'suffix.txt':
            d = f.readlines()
            suffix = []
            for t in d:
                suffix.append(t[:-1])
        elif i == 'special_words.txt':
            d = f.readlines()
            special_words = []
            for t in d:
                special_words.append(t[:-1])
            

lexicon_dir = os.path.join(extra_c_dir, 'lexicon')
prefix_dir = os.path.join(lexicon_dir, 'prefix')
suffix_dir = os.path.join(lexicon_dir, 'suffix')

input_phrase = 'ألقي د. أحمد كلمة علي الحضور في أحد القاعات الدراسية و سلم علي صديقه عثمان الكاتب'
words_list = input_phrase.split()

root_list = []

for word in words_list:
    if word in special_words:
        root_list.append(word)
    else:
        y, p = '', ''
        for i in word:
            y += i
            if y in prefix:
                p = y
        
        if p != '':
            filename = p + '.txt'
            with open(os.path.join(prefix_dir, filename), "r", encoding = "utf-8") as f:

                    x = f.readlines()
                    if word + '\n' in x:
                        root_list.append(word)
                    else:
                        # root_list.append(st.stem(word))
                        word = word[len(p):]
                        root_list.append(word)
                        continue
        
        y, s = '', ''
        for i in word[::-1]:
            y = i + y
            if y in suffix:
                s = y
        
        if s != '':
            filename = s + '.txt'
            with open(os.path.join(suffix_dir, filename), "r", encoding = "utf-8") as f:

                    x = f.readlines()
                    if word + '\n' in x:
                        root_list.append(word)
                    else:
                        # root_list.append(st.stem(word))
                        word = word[:-1 * len(s)]
                        root_list.append(word)
                        continue
        
        
print(root_list)