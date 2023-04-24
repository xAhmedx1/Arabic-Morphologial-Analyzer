# Import modules
import preprocessing as pre

input = "وأيمن"
i_split = input.split()

root_list = []

for w in i_split:
    norm_word = pre.normalize(w)
    wordv2 = pre.pref_handler(norm_word)
    root_list.append(wordv2)

print(root_list)
