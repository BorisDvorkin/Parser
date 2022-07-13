with open('ПрогИнж.txt', 'r') as file:
    text = file.read().splitlines()

contest = []
olymp = 0
for x in range(len(text)):
    l = [x for x in text[x].split('\t') if x != '']
    if l[2] == 'РќРµС‚' or l[2] == 'Нет':
        contest.append(int(l[3]) + int(l[4]) + int(l[5]))
    else:
        olymp += 1

contest.sort()
contest.reverse()
print('--БВИ--\n')
print(olymp)
print('\n\n--ОБЩИЙ КОНКУРС--\n\n')
print(contest)

