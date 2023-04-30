patterns = ['فاعل','أفعل','تفعل','انفعل','افتعل','افعل','استفعل',
            'يفاعل','يتفعل','يتفاعل','ينفعل','يفتعل','يفعل','يستفعل',
            'متفاعل','منفعل','مفتعل','مفعل','مستفعل','مفعول','مفاعل',
            'متفعل', 'مفاعلة','إفعال','تفعيل','تفاعل','انفعال','افتعال',
            'افعلال','استفعال', 'مفعال', 'تستفعل', 'نستفعل', 'نفعال', 'فعال',
            'فتعل', 'فعائل', 'مفاعيل', 'فعول', 'فاعول', 'فعيل', 'فعاليل',
            'فعلال', 'مفعلة', 'فاعلة', 'فعالل', 'فعلل', 'فعتل', 'افعال', 'فوعل', 'فواعل', 'افاعل'] 
# , 
original = ['ف', 'ع', 'ل']

def pattern_finder(input, pos_r):
    for pattern in patterns:
        poss_r = ''
        if len(pattern) == len(input):
            for cha in range(len(pattern)):
                if pattern[cha] in original:
                    poss_r += input[cha]
                elif pattern[cha] == input[cha]:
                    continue
                else: 
                    poss_r = ''
                    break
            if len(poss_r) != 0: 
                if pattern == 'افعلال': pos_r.append(poss_r[:-1])
                else: pos_r.append(poss_r)
    if len(pos_r) != 0: return pos_r
    else: return pos_r

def normalize_root(possible_roots):
    norm_list = []
    norm_root = ""
    for j in range(len(possible_roots)):
        if type(possible_roots) == list:
            norm_root = ""
            for i in range(len(possible_roots[j])):
                # if possible_roots[j] in ['ئ', 'ؤ'] and j != len(possible_roots[j]) - 1:
                if possible_roots[j][i] in ['ئ', 'ؤ']:
                    if i == len(possible_roots[j][i]) - 1: norm_root += 'ء'
                    else: norm_root += 'ي'
                elif possible_roots[j][i] == 'ة':
                    norm_root += 'ت'
                else: norm_root += possible_roots[j][i]
            if len(norm_root) == 3 and norm_root[1] == 'ا':
                x = norm_root.replace('ا', 'و')
                norm_list.append(x)
                y = norm_root.replace('ا', 'ي')
                norm_list.append(y)
            else: norm_list.append(norm_root)
        else:
            if possible_roots[j] in ['ئ', 'ؤ'] and j != len(possible_roots[j]) - 1:
                    norm_root += 'ء'
            elif possible_roots[j] == 'ة':
                    norm_root += 'ت'
            else: norm_root += possible_roots[j]
        
    if type(possible_roots) != list: norm_list.append(norm_root)

    return norm_list