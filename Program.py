# Import needed packages
import os, sys
import arabic_reshaper
from bidi.algorithm import get_display
# prefix.append(get_display(arabic_reshaper.reshape(t[:-1])))
import nltk
from nltk.stem.isri import ISRIStemmer
from nltk import word_tokenize
st = ISRIStemmer()
# nltk.download('punkt')

# Main folder path
dir_path = os.path.join(sys.path[0])

# List to store files names
extra_c_dir = os.path.join(dir_path, 'files') # the directory of the files that contains the extra characters
extra_c = []

# Iterate directory
for path in os.listdir(extra_c_dir):
    # check if current path is a file
    if os.path.isfile(os.path.join(extra_c_dir, path)): 
        extra_c.append(path)

# Creating unique lists, each contains the extra characters of their type
for i in extra_c:
    with open(os.path.join(extra_c_dir, i), "r", encoding = "utf-8") as f:
        if i == 'prefix.txt':
            d = f.readlines()
            prefix = []
            for t in d:
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
        elif i == 'infix.txt':
            d = f.readlines()
            infix = []
            for t in d:
                infix.append(t[:-1])
            

lexicon_dir = os.path.join(extra_c_dir, 'lexicon')
prefix_dir = os.path.join(lexicon_dir, 'prefix')
suffix_dir = os.path.join(lexicon_dir, 'suffix')
infix_dir = os.path.join(lexicon_dir, 'infix')

input_phrase = 'ألقي د. أحمد كلمة علي الحضور في أحد القاعات الدراسية و سلم علي صديقه عثمان الكاتب و قال له انهم سيكتبون المقال الأسبوع القادم'
words_list = input_phrase.split()

root_list = []

for word in words_list:
    if word in special_words:
        root_list.append(word)
    else:
        w_index = words_list.index(word)
        special = ''
        flag = True
        # the flag job is to iterate in a single word repeatedly until it removes all the extra words in it
        # ex: 'فسيكتب' = has prefix characters 'ف' and 'س', so it will iterate untill it removes them all
        while flag:
            flag = False
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
                            # root_list.append(word)
                            special = word
                        else:
                            # root_list.append(st.stem(word))
                            word = word[len(p):]
                            flag = True

                            
        flag = True
        while flag and special == '':
            flag = False    
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
                            # root_list.append(word)
                            special = word
                        else:
                            # root_list.append(st.stem(word))
                            word = word[:-1 * len(s)]
                            flag = True
                

        if special != '': root_list.append(special)
        else: root_list.append(word)
        
        
print(root_list)