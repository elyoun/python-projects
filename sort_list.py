from unittest import result

def sort_dict(word_list):
    #file = open(r'C:\Users\joaofesoares\Desktop\fizzbuzz\words.txt')
    #word_list = file.read().splitlines()
    #print(type(word_list))

    #def myFunc(e):
    #    return len(e)


    #word_list.sort(key=myFunc)
    #print(word_list)
    #result = list(map(myFunc, word_list))
    result = word_list
    #print(result)
    c = {k: [] for k in range(1,15)}

    #print(c)
    #print(c[1])
    for i in range (len(word_list)):
        key = len(word_list[i])
        c[key].append(word_list[i]) 
    return c
    #print(len(c[2]))
