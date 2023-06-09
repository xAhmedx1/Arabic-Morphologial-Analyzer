# Import Needed Modules
import os, sys
import pattern_recognition as pat_r

# Defining folders pathes
dir_path = os.path.join(sys.path[0])
files_path = os.path.join(dir_path, 'files')
lexicon_path = os.path.join(files_path, 'lexicon')
prefix_path = os.path.join(lexicon_path, 'prefix')
suffix_path = os.path.join(lexicon_path, 'suffix')

characters = ['ا', 'أ', 'آ', 'إ', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 
              'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 
              'ه', 'و', 'ي', 'ء', 'ؤ', 'ئ', 'ة']

def normalize(word):
    """
    Removing diacritics in g given word (except the shaddah '  ّ' the letter that contains it will be duplicated)

    trasfoming the character 'إ'and 'آ' to 'ا'
    
    e.g. "كُتَّاب" --> "كتتاب"
    """
    n_word = ""
    for i in range(len(word)):
        k = word[i]
        if word[0] in ['إ', 'آ'] and n_word == "":
            n_word += 'ا'
        elif k == 'ّ': n_word += word[i-1]   # shaddah ' ّ'
        elif k in characters: n_word += k
        elif k == 'ى': n_word += 'ي'
        else: continue
    return n_word

def ch_func(path, ch):
    """
    creating a list of each in a text file of a specified name
    - path - the path of the folder that contians the file
    - ch - the character name that we want to create a list of (each file are named as the character's name)
    """
    with open(os.path.join(path, ch + '.txt'), "r", encoding = "utf-8") as f:
                d = f.readlines()
                ch_list = []
                for t in d:
                    ch_list.append(t[:-1])
    return ch_list

def known_root(x, lexicon_list):
    if len(x) != 0: #  and x[-1] != 'ة'
        root_list = []
        for l in lexicon_list:
            if l in x:
                root_list.append(l)
        if len(root_list) != 0: return max(root_list, key=len)
    return False

def suff_finder(word):
    y, suf = '', ''
    for i in word[::-1]:
        y = i + y
        if y in suff_comb:
            suf = y
    if len(word) - len(suf) > 2:
        return suf
    else: return ''

def check_lexicon(word):
    if len(word) != 0:
        root_list = []
        r = known_root(word, specialwords_list)
        if r and len(r) > (len(word) - len(r)):
            root_list.append(r)
        elif word[0:2] in prefix_ch:
            ch_list = ch_func(prefix_path, word[0:2])
            r = known_root(word, ch_list)
            if r and len(r) > (len(word) - len(r)):
                root_list.append(r)
        elif word[0] in prefix_ch:
            ch_list = ch_func(prefix_path, word[0])
            r = known_root(word, ch_list)
            if r and len(r) > (len(word) - len(r)):
                root_list.append(r)
            
        suff = suff_finder(word)
        if len(suff) != 0:
            if len(suff) >= 2:
                if suff[0:2] in suffix_ch:
                    ch_list = ch_func(suffix_path, suff[0:2])
                    r = known_root(word, ch_list)
                    if r and len(r) > (len(word) - len(r)):
                        root_list.append(r)
                elif suff[0] in suffix_ch:
                    ch_list = ch_func(suffix_path, suff[0])
                    r = known_root(word, ch_list)
                    if r and len(r) > (len(word) - len(r)):
                        root_list.append(r)
            else: 
                ch_list = ch_func(suffix_path, suff[0])
                r = known_root(word, ch_list)
                if r and len(r) > (len(word) - len(r)):
                    root_list.append(r)
        if len(root_list) != 0: return max(root_list, key=len)
        return False
    else : return None

specialwords_list = ch_func(files_path, 'special_words')

prefix_ch = ['س', 'ال', 'أ', 'ل', 'ب', 'ك', 'ف', 'و']
suffix_ch = ['ين', 'ان', 'و', 'ه', 'ك', 'ا', 'ي', 'ن', 'ت', 'ات', 'ون', 'وا', 'تم', 'هم', 'كم', 'ة', 'ء', 'اء']
suff_comb = ['يا', 'ت', 'ة', 'ك', 'تم', 'هم', 'ي', 'اء', 'ان', 'هما'
             , 'كم', 'وها', 'ا', 'ه', 'ين', 'يه', 'ون', 'ها', 'وا', 'ء'
             , 'ات', 'ية', 'نا', 'تموها', 'تن', 'هنن', 'ني', 'اتي', 'تي', 'هن']

# Creating a list of each prefix and suffix
sen_list = ch_func(prefix_path, 'س')
al_list = ch_func(prefix_path, 'ال')
hamza_list = ch_func(prefix_path, 'أ')
lam_list = ch_func(prefix_path, 'ل')
baa_list = ch_func(prefix_path, 'ب')
kaph_list = ch_func(prefix_path, 'ك')
faa_list = ch_func(prefix_path, 'ف')
waw_list = ch_func(prefix_path, 'و')

# Creating a function for each prefix to check if it is really a prefix based or our roles we put, or not
def sen_pref(word, p):
    """
    check if the sen 'س' is a prefix of not, and remove it if it was
    """
    if len(word) > 3:
        pat = pat_r.pattern_finder(word, p)
        if check_lexicon(word): 
            p.append(check_lexicon(word))
            return '', p
        elif len(pat) != 0:
            p = pat
        if word[1] in ['أ', 'ي', 'ت', 'ن']:
            return word[2:], p
        else: return word, p
    else: return word, p

def al_pref(word, p):
    """
    check if the al 'ال' is a prefix of not, and remove it if it was
    """
    if len(word) > 4:
        pat = pat_r.pattern_finder(word, p)
        if check_lexicon(word): 
            p.append(check_lexicon(word))
            return '', p
        elif check_lexicon(word[1:]): 
            p.append(check_lexicon(word[1:]))
            return '', p
        elif len(pat) != 0:
            p = pat
        if word[2] in ['أ', 'ا', 'آ', 'إ']:
            return word[2:], p
        else: return word[2:], p
    else: return word, p

def hamza_pref(word, p):
    """
    check if the hamza 'أ' is a prefix of not, and remove it if it was
    """
    if len(word) > 3:
       pat = pat_r.pattern_finder(word, p)
       if check_lexicon(word): 
            p.append(check_lexicon(word))
            return '', p
       elif len(pat) != 0:
            p = pat
       if word[1] == 'أ':
            return word[1:], p
       else: return 'ا' + word[1:], p
    else: return word, p

def lam_pref(word, p):
    """
    check if the lam 'ل' is a prefix of not, and remove it if it was
    """
    if len(word) > 3:
        pat = pat_r.pattern_finder(word, p)
        if check_lexicon(word): 
            p.append(check_lexicon(word))
            return '', p
        elif len(pat) != 0:
            p = pat
        if word[1] in ['أ', 'ي', 'ت', 'ن']:
            return word[2:], p
        else: return word, p
    else: return word, p

def baa_pref(word, p):
    """
    check if the baa 'ب' is a prefix of not, and remove it if it was
    """
    if len(word) > 3:
        pat = pat_r.pattern_finder(word, p)
        if check_lexicon(word): 
            p.append(check_lexicon(word))
            return '', p
        elif len(pat) != 0:
            p = pat
        if word[1:3] == 'ال':
            return al_pref(word[1:], p)
        else: return word, p
    else: return word, p

def kaph_pref(word, p):
    """
    check if the kaph 'ك' is a prefix of not, and remove it if it was
    """
    if len(word) > 3:
        pat = pat_r.pattern_finder(word, p)
        if check_lexicon(word): 
            p.append(check_lexicon(word))
            return '', p
        elif len(pat) != 0:
            p = pat
        if word[1:3] == 'ال':
            return al_pref(word[1:], p)
        else: return word, p
    else: return word, p

def faa_pref(word, p):
    """
    check if the faa 'ف' is a prefix of not, and remove it if it was
    """
    if len(word) > 3:
        pat = pat_r.pattern_finder(word, p)
        if check_lexicon(word): 
            p.append(check_lexicon(word))
            return '', p
        elif len(pat) != 0:
            p = pat
        if word[1] == 'ب':
            return baa_pref(word[1:], p)
        elif word[1] == 'ك':
            return kaph_pref(word[1:], p)
        elif word[1:3] == 'ال':
            return al_pref(word[1:], p)
        elif word[1] == 'س':
            return sen_pref(word[1:], p)
        elif word[1] == 'ل':
            return lam_pref(word[1:], p)
        elif word[1] == 'أ':
            return hamza_pref(word[1:], p)
        else: return word, p
    else: return word, p

def waw_pref(word, p):
    """
    check if the waw 'و' is a prefix of not, and remove it if it was
    """
    if len(word) > 3:
        pat = pat_r.pattern_finder(word, p)
        if check_lexicon(word): 
            p.append(check_lexicon(word))
            return '', p
        elif len(pat) != 0:
            p = pat
        if word[1] == 'ب':
            return baa_pref(word[1:], p)
        elif word[1] == 'ك':
            return kaph_pref(word[1:], p)
        elif word[1:3] == 'ال':
            return al_pref(word[1:], p)
        elif word[1] == 'س':
            return sen_pref(word[1:], p)
        elif word[1] == 'ل':
            return lam_pref(word[1:], p)
        elif word[1] == 'أ':
            return hamza_pref(word[1:], p)
        else: return word, p
    else: return word, p

duplicate_p_letters = ['تت', 'بب', 'كك', 'فف', 'لل', 'وو']
multiletter = ['نست', 'لن', 'مست', 'سي', 'سن', 'ست', 'سأ', 'تنن', 'است', 'ات']

def multiletter_pre(word):
    x, p = '', ''
    for i in word:
        x += i
        if x in multiletter:
            p = x
    if p != '': return word[len(p):]
    else: return False

def pref_handler(word, possible_roots):
    """
    Handling the prefix of a word
    """
    if len(word) > 3:
        pos_r = possible_roots
        p = pat_r.pattern_finder(word, pos_r)
        possible_roots = []
        if word[0:2] in duplicate_p_letters: 
            possible_roots.append(word[1:])
            return '', possible_roots
        elif multiletter_pre(word): 
            possible_roots.append(multiletter_pre(word))
            return multiletter_pre(word), []
        elif check_lexicon(word): 
            possible_roots.append(check_lexicon(word))
            return '', possible_roots
        elif len(p) != 0:
            possible_roots = p
        if word[0] == 'س':
            return sen_pref(word, possible_roots)
        elif word[0:2] == 'ال' and len(word) > 4:
            return al_pref(word, possible_roots)
        elif word[0] == 'أ':
            return hamza_pref(word, possible_roots)
        elif word[0] == 'ل':
            return lam_pref(word, possible_roots)
        elif word[0] == 'ب':
            return baa_pref(word, possible_roots)
        elif word[0] == 'ك':
            return kaph_pref(word, possible_roots)
        elif word[0] == 'ف':
            return faa_pref(word, possible_roots)
        elif word[0] == 'و':
            return waw_pref(word, possible_roots)
    else: return word, possible_roots
    return word, possible_roots

def suff_handler(word, possible_roots):
    c = suff_finder(word)
    p = pat_r.pattern_finder(word, possible_roots)
    if len(p) != 0:
        possible_roots = p
    if len(word) != 0 and c != '': 

        if check_lexicon(word): 
            possible_roots.append(check_lexicon(word))
            return '', possible_roots
        return suff_handler(word[0:len(word)-len(c)], possible_roots)
    else: return word, possible_roots
