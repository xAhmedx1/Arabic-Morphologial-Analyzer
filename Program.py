# Import modules
import preprocessing as pre
import pattern_recognition as pat_r
# input = "ذهب سامي ليشتري ذهبا من المحل المقابل لبيته أذكياء"
# input = "الأوزان في اللغة العربية متعددة، فهي من أهم أساسيات علم الصرف حيث تساعدنا تلك الأوزان على قياس وزن الكلمات في لغتنا العربية، حيث إن الكلمة في اللغة العربية إما ثلاثية أو رباعية أو خماسية أو سداسية، وسوف نعرض لكم عبر موقع زيادة الأوزان في اللغة العربية"
input = 'مومياء'
i_split = input.split()

root_list = []

for w in i_split:
    norm_word = pre.normalize(w)
    wordv2 = pre.pref_handler(norm_word)
    if not pre.check_lexicon(wordv2):
        wordv2 = pre.suff_handler(wordv2)
        wordv2 = pat_r.normalize_root(wordv2)
    
    root_list.append(wordv2)

for i in range(len(i_split)):
    print(f"Original: '{i_split[i]}' , possible roots --> {root_list[i]}")
