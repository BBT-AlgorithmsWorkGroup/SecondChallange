def isogram(word):
    temp = word[0]
    count=1
    repeated_list_words = []
    repeated_list_counts = []
    for i in range(1,len(word)):
        if word[i] == temp:
            count+=1
        else:
            if count != 1:
                repeated_list_words.append(temp)
                repeated_list_counts.append(count)
                count = 1
            temp = word[i]
        if i == len(word) - 1 and count !=1:
            repeated_list_words.append(temp)
            repeated_list_counts.append(count)
    return repeated_list_words,repeated_list_counts



print(isogram("aaabbcc"))
print(isogram("furkan"))
print(isogram("fukkra"))