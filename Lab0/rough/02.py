#!/usr/bin/env python3

import random

boys = ['Abe', 'Bob', 'Col']
girls = ['Abi', 'Bea', 'Cath']

boys_pref = []
girls_pref = []

free_men = []

# producing random preference for boys and girls
for i in range(0, len(boys)):
    random.shuffle(girls)
    boys_pref.append(girls)
    girls = ['Abi', 'Bea', 'Cath']
for i in range(0, len(girls)):
    random.shuffle(boys)
    girls_pref.append(boys)
    boys = ['Abe', 'Bob', 'Col']

print(boys_pref)
print(girls_pref)

for i in range(0, len(boys)):
    print(boys[i], ':', end='  ')
    for j in boys_pref[i]:
        print(j, end='  ')
    print()

for i in range(0, len(girls)):
    print(girls[i], ':', end='  ')
    for i in girls_pref[i]:
        print(i, end='  ')
    print()


def init_free_men():
    for boy in boys:
        free_men.append(boy)

def stable_matching():
    while(len(free_men) > 0):
        for man in free_men:
            begin_matching(man)

# people that 'may' be end up together
tentative_engagements = []

def begin_matching(man):
    index = boys.index(man)
    print('DEALING WITH {}'.format(man))
    for woman in boys_pref[index]:

        # 0 means woman is single 
        taken_match = [couple for couple in tentative_engagements if woman in couple]
        
        if (len(taken_match) == 0):
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            print('{} is no longer a free man and is now tentatively engaged to {}'.format(man, woman))
            break
        elif (len(taken_match) > 0):
            print('{} is taken already...'.format(woman))

            current_guy = girls_pref[girls.index(woman)].index(taken_match[0][0])
            potential_guy = girls_pref[girls.index(woman)].index(man)

            if (current_guy < potential_guy):
                print('She is satisfied with {}'.format(taken_match[0][0]))
            else:
                print('{} is better than {}'.format(man, taken_match[0][0]))
                print('Making {} free again... and then tentatively accept dance between {} and {}'.format(taken_match[0][0], man, woman))

                # the new guy is engaged
                free_men.remove(man)

                # the old guy is now single
                free_men.append(taken_match[0][0])

                # update the fiance of the woman
                taken_match[0][0] = man
                break



def main():
    init_free_men()
    stable_matching()

    print('COMPLETE LIST OF ACCEPTANCE')
    print(tentative_engagements)


if __name__ == '__main__':
    main()








