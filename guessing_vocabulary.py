import random
words = ('python','jumble','easy','difficult','answer','continue','phone','position','game')
w = list(words)
words_dic = {word:0 for word in words}

def check (origin, new):
    a = len(origin)
    b = 0
    for i in range(len(new)):
        if new[i] == origin[i]:
            b +=1
    similarity = b/a
    return similarity


iscontinue = 'y'

while iscontinue == 'y' or iscontinue == 'Y':
    if len(w) == 0:
        w = list(words)
    wd = random.choice(w)
    w.remove(wd)
    words_dic[wd]+=1
    correct_wd = wd 
    
    '''
    考虑原单词的情况
    '''
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
        if chance ==0:
            break
        guess = input('\n Guessing: ')


    if guess == correct_wd:
        print('\n Correct!')
    if chance == 0:
        print('\n Correct answer is :', correct_wd)


    iscontinue = input('\n Do you want to continue? (Y/N): ')
    while True:
        if iscontinue == 'Y' or iscontinue == 'y' or iscontinue == 'n' or iscontinue == 'N' or iscontinue == 'YES' or iscontinue == 'yes' or iscontinue == 'NO' or iscontinue == 'no' or iscontinue == 'Yes' or iscontinue == 'No':
            break
        else:
            iscontinue = input ('\n please type "Y" or "N":  ')

if iscontinue =='n' or iscontinue == 'N' or iscontinue == 'NO' or iscontinue == 'no'  or iscontinue == 'No':
    print(words_dic)







