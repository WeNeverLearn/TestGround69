def encryptor(word):
    tor = 0
    a = "abcdefghijklmnopqrstuvwxyz" * 5
    output_string = ' '
    boom = word.replace('.', ' ')
    input_list1 = boom.split()
    for index, single in enumerate(word):
        list_word = len(input_list1[tor])
        if single.isalpha() or single.isdigit():
            output_string = output_string + a[(a.index(single)+ list_word)]
        else:
            output_string = output_string + single
        if single == ' ':
            if tor <= len(input_list1[tor]):
                tor +=1
    return output_string


def decryptor(word):
    tor = 0
    a = "abcdefghijklmnopqrstuvwxyz" * 5
    b=''
    for i in range(len(a)-1,0,-1):
        b=b+a[i]
    output_string = ' '
    output_string = ' '
    boom = word.replace('.', ' ')
    input_list1 = boom.split()
    for single in word:
        list_word = len(input_list1[tor])
        if single.isalpha() or single.isdigit():
            output_string = output_string + b[(b.index(single)+list_word)]
        else:
            output_string = output_string + single
        if single == ' ':
            if tor <= len(input_list1[tor]):
                tor +=1
    return output_string



print(decryptor('mjqqt. btwqi'))

