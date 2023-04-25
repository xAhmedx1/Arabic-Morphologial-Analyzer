# Import modules
import preprocessing as pre

input = "ذهب سامي ليشتري ذهبا من المحل المقابل لبيته"
i_split = input.split()

root_list = []

for w in i_split:
    norm_word = pre.normalize(w)
    wordv2 = pre.suff_handler(norm_word)
    wordv3 = pre.pref_handler(wordv2)
    
    root_list.append(wordv3)

print(root_list)
