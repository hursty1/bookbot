def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    words = text.lower().split()
    dic = {}
    for word in words:
        for char in word:
            if char in dic.keys():
                dic[char] = dic[char] + 1
            else:
                dic[char] = 1
    
    #sort
    sorted_dic = dict(sorted(dic.items(), key=lambda item:item[1], reverse=True))
    return sorted_dic