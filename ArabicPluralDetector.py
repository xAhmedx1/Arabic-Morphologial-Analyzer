import os, sys
import preprocessing as pre


suffix_path = pre.suffix_path
w_n = pre.ch_func(suffix_path, 'ون')
y_n = pre.ch_func(suffix_path, 'ين')
a_t = pre.ch_func(suffix_path, 'ات')
class ArabicPluralDetector:
    def __init__(self):
        self.patterns = ['فعلة','أفعل','أفعلة','أَفْعلة','أَفْعل','أفعال','فِعْلة',
                         'فُعْل','فُعُل','فُعَل','فُعَّل','فَعَلة','فُعَلة','فِعَلة','فعلة','فَعْلى',
                         'فَعْلى','فعلى','فُعّال','فِعَال','فُعّال','فعال','فَعِيل','فعيل'
                         ,'فُعْلان','فِعْلان','فعلان','أفعلاء','أَفْعِلاء','فعلاء','فِعَل','فُعَلاء',
                         'مفاعل','مفاعيل','فواعل','فواعيل','فعائل',
                         'فَعالِي','مفاعيل','فَعالَى','فعالى','فُعالى','فعالل','فَعالى',
                         'أفاعل','فعاليل','أفاعيل','تفاعل','تفاعيل','يفاعيل',
                         'يفاعيل','فياعل','فعالين','فعاعيل']
        self.original = ['ف', 'ع', 'ل','عُ','عَ','عِ','عْ','عّ','عَّ','فُ','فِ','فْ','فّ','فَ','لِ','لْ','لّ','لُ','لَ']
        # self.w_n_words = {'ثغون','ثرون','تصون','تعون','تفون','تقون'}
        # self.a_t_words = {'بات','حات'}
        self.t_g_k = ['فعلة','أفعل','أفعلة','أَفْعلة','أَفْعل','أفعال','فِعْلة']
        self.t_g_ks = ['فُعْل','فُعُل','فُعَل','فُعَّل','فَعَلة','فُعَلة','فِعَلة','فعلة','فَعْلى',
                       'فَعْلى','فعلى','فُعّال','فِعَال','فُعّال','فعال','فَعِيل','فعيل'
                       ,'فُعْلان','فِعْلان','فعلان','أفعلاء','أَفْعِلاء','فعلاء','فِعَل','فُعَلاء']
        self.t_g_mnt = ['مفاعل','مفاعيل','فواعل','فواعيل','فعائل',
                        'فَعالِي','فَعالَى','فعالى','فُعالى','فعالل','فَعالى',
                        'أفاعل','فعاليل','أفاعيل','تفاعل','تفاعيل','يفاعيل',
                        'يفاعيل','فياعل','فعالين','فعالين','فعاعيل']

    def find_last(self, word):
        w_n=''
        for i in range(2):
            w_n += word[len(word)-i-1] 
        return w_n

    def find_patt(self, input):
        possible_pat = []
        for pattern in self.patterns:
            poss_r = ''
            if len(pattern) == len(input):
                for cha in range(len(pattern)):
                    if pattern[cha] in self.original:
                        poss_r += input[cha]
                    elif pattern[cha] == input[cha]:
                        continue
                    else: 
                        poss_r = ''
                        break
                if len(poss_r) != 0: 
                    possible_pat.append(pattern)
        return possible_pat
    
    def detect_plural(self, word):
        finall = []
        last = self.find_last(word)
        if last == 'نو':
           if word in w_n:
                finall.append("ليست جمع")
                return finall
           else:
                finall.append('جمع مذكر سالم')
                return finall
        elif last=='ني':
            if word in y_n :
                finall.append("ليست جمع")
                return finall
            else:
                finall.append('جمع مذكر سالم')
                return finall
        elif last == 'تا':
            if word in a_t:
                finall.append("ليست جمع")
                return finall
            else:
                finall.append('جمع مؤنث سالم')
                return finall
        else:
            pat = self.find_patt(word)
            if not pat:
                finall.append("ليست جمع")
                return finall
            else:
                if pat[0] in self.t_g_k:
                    finall.append('جمع قلة')
                    if pat[0] in self.t_g_ks:
                        finall.append('جمع تكسير من نوع جمع كثرة')
                    return finall   
                elif pat[0] in self.t_g_ks:
                    finall.append('جمع تكسير من نوع جمع كثرة')
                    return finall
                elif pat[0] in self.t_g_mnt :
                    finall.append("جمع منتهي الجموع")
                    return finall