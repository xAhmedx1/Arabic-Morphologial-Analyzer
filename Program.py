import preprocessing as pre
import pattern_recognition as pat_r

class program:

    def run(input):
        i_split = input.split()

        root_list = []

        for word in i_split:
            possible_roots = []

            normalized_word = pre.normalize(word)
            wordv2, possible_roots = pre.pref_handler(normalized_word, possible_roots)
            wordv2, possible_roots = pre.suff_handler(wordv2, possible_roots)
            # wordv2, possible_roots = pre.pref_handler(normalized_word, possible_roots)

            if pre.check_lexicon(wordv2) == False:
                possible_roots = pat_r.normalize_root(possible_roots)

            if len(possible_roots) == 0:
                possible_roots.append(wordv2)
                possible_roots = pat_r.normalize_root(possible_roots)
            root_list.append(set(possible_roots))

        # for i in range(len(i_split)):
            # print(f"Original: '{i_split[i]}' , possible roots --> {root_list[i]}")

        return i_split,root_list
