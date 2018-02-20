#!/usr/bin/env python3

import random

boys = ['Abe', 'Bob', 'Col', 'Dan', 'Ed', 'Fred', 'Gav', 'Hal', 'Ian', 'Jon']
girls = ['Abi', 'Bea', 'Cath', 'Dee', 'Eve', 'Fay', 'Gay', 'Hope', 'Ivy', 'Jan']

boys_pref = []
girls_pref = []

free_men = []

# producing random preference for boys and girls
for i in range(0, len(boys)):
    random.shuffle(girls)
    boys_pref.append(girls)
    girls = ['Abi', 'Bea', 'Cath', 'Dee', 'Eve', 'Fay', 'Gay', 'Hope', 'Ivy', 'Jan']
for i in range(0, len(girls)):
    random.shuffle(boys)
    girls_pref.append(boys)
    boys = ['Abe', 'Bob', 'Col', 'Dan', 'Ed', 'Fred', 'Gav', 'Hal', 'Ian', 'Jon']

def print_boys_preferences():
    for i in range(0, len(boys)):
        print(boys[i], ':', end='  ')
        for j in boys_pref[i]:
            print(j, end='  ')
        print()

def print_girls_preferences():
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
    for woman in boys_pref[index]:

        print('{} proposes to {}'.format(man, woman))
        # 0 means woman is single 
        taken_match = [couple for couple in tentative_engagements if woman in couple]
        
        if (len(taken_match) == 0):
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            print('{} is engaged to {}'.format(man, woman))
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

def print_pairings():
    for couple in tentative_engagements:
        print('{} - {}'.format(couple[0], couple[1]))

def main():
    print_boys_preferences()
    print_girls_preferences()
    init_free_men()
    stable_matching()

    print()
    print('Pairing:')
    print_pairings()



if __name__ == '__main__':
    main()

