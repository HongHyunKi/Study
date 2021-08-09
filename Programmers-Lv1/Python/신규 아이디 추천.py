def solution(new_id):
    new_id = new_id.lower()
    ns = []
    for i in range(0,len(new_id)):
        if not(new_id[i].isalnum()) and new_id[i] not in ['-','_','.']:
            ns.append(new_id[i])
    
    ns = list(set(ns))
    for i in ns:
        new_id = new_id.replace(i,'')
    
    temp =''
    for i in range(0,len(new_id)-1):
        if new_id[i] == '.' and new_id[i+1] == '.':
            pass
        else:
            temp += new_id[i]
    temp += new_id[-1:]  
    new_id = temp.strip('.')
    
    if new_id.strip() == '':
        new_id = 'a'
    if len(new_id) > 15:
        new_id = new_id[:15].rstrip('.')
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1:]
    
    return new_id