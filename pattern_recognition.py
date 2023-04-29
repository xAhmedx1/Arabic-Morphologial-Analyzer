patterns = ['فاعل','فعل','أفعل','تفعل','انفعل','افتعل','افعل','استفعل',
            'يفاعل','يتفعل','يتفاعل','ينفعل','يفتعل','يفعل','يستفعل',
            'متفاعل','منفعل','مفتعل','مفعل','مستفعل','مفعول','مفاعل',
            'متفعل', 'مفاعلة','إفعال','تفعيل','تفاعل','انفعال','افتعال',
            'افعلال','استفعال', 'مفعال', 'تستفعل', 'نستفعل', 'نفعال', 'فعال',
            'فتعل', 'فعائل', 'مفاعيل', 'فعول', 'فاعول', 'فعيل', 'فعاليل', 'افعال'
            'فعلال', 'فعلال', 'مفعلة']
original = ['ف', 'ع', 'ل']

def pattern_finder(input):
    possible_roots = []
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
                if pattern == 'افعلال': possible_roots.append(poss_r[:-1])
                else: possible_roots.append(poss_r)
    if len(possible_roots) != 0: return possible_roots
    else: return False

def normalize_root(possible_roots):
    norm_list = []
    for root in possible_roots:
        norm_root = ""
        for i in range(len(root)):
            if root[i] in ['ئ', 'ؤ']:
                norm_root += 'ء'
            elif root[i] == 'ة':
                norm_root += 'ت'
            else: norm_root += root[i]
        
        norm_list.append(norm_root)

    return norm_list