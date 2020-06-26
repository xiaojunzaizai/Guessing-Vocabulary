import random
import vocabulary


words,words_dic = vocabulary.get_vocabulary()


def check (origin, new):
    a = len(origin)
    b = 0
    for i in range(len(new)):
        if new[i] == origin[i]:
            b +=1
    similarity = b/a
    return similarity


words_list = []
f = open('save.txt','r')
lines = f.readlines()
f.close()
for line in lines:
    line = line.strip('\n')
    if line in words_list:
        continue
    else:
        words_list.append(line)

#remove duplicate words and save again
f = open('save.txt','w')
for i in range(len(words_list)):
    f.write(words_list[i]+'\n')
f.close()


w = words_list.copy()
words_freq = {word:0 for word in words_list}

# guessing part
iscontinue = 'y'
while iscontinue == 'y' or iscontinue == 'Y':
    if len(w) == 0:
        w = words_list.copy()
    wd = random.choice(w)
    w.remove(wd)
    words_freq[wd]+=1
    correct_wd = wd


    while True:
        a = ''
        while wd:
            position = random.randrange(len(wd))
            a += wd[position]
            wd = wd[:position]+wd[position+1:]
        b = check(a,correct_wd)
        wd = correct_wd
        if b < 0.2:
            break
    print('\n After shuffling: ', a) 

    #3次机会

    guess = input('\n Type your answer: ')
    chance = 3
    while guess != correct_wd and guess != '':
        chance -=1
        print('\n Wrong word, please try again')
        print('\n Remining chance: ', str(chance))
        if chance ==1:
            print('\n Give you a hint, the meaning of the vocabulary is: ')
            print(words_dic[correct_wd])
        if chance ==0:
            break
        guess = input('\n Guessing: ')


    if guess == correct_wd:
        print('\n Correct!\n The meaning of the vocabulary is ')
        print(words_dic[correct_wd])
    if chance == 0:
        print('\n Correct answer is :', correct_wd)
        print('\n The meaning of the vocabulary is ')
        print(words_dic[correct_wd])

    iscontinue = input('\n Do you want to continue? (Y/N): ')
    while True:
        if iscontinue == 'Y' or iscontinue == 'y' or iscontinue == 'n' or iscontinue == 'N' or iscontinue == 'YES' or iscontinue == 'yes' or iscontinue == 'NO' or iscontinue == 'no' or iscontinue == 'Yes' or iscontinue == 'No':
            break
        else:
            iscontinue = input ('\n please type "Y" or "N":  ')

