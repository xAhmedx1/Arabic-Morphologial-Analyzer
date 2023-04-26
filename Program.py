# Import modules
import preprocessing as pre

input = "ذهب سامي ليشتري ذهبا من المحل المقابل لبيته أذكياء"

i_split = input.split()

root_list = []

for w in i_split:
    norm_word = pre.normalize(w)
    wordv2 = pre.pref_handler(norm_word)
    if not pre.check_lexicon(wordv2):
        wordv2 = pre.suff_handler(wordv2)
    
    root_list.append(wordv2)

for i in range(len(i_split)):
    print(f"Original: '{i_split[i]}' , possible roots --> {root_list[i]}")
