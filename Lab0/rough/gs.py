#!/usr/bin/env python3

import random


# def produce_preference_for_suitors(suitors, girls, suitors_pref):
#     for i in range(0, len(suitors)):
#         random.shuffle(girls)
#         suitors_pref.append(girls)
# 
# def produce_preference_for_girls(suitors, girls, girls_pref):
#     for i in range(0, len(girls)):
#         random.shuffle(suitors)
#         girls_pref.append(suitors)

def print_suitors_preferences(suitors, suitors_pref):
    for i in range(0, len(suitors)):
        print(suitors[i], ':', end='  ')
        for j in suitors_pref[i]:
            print(j, end='  ')
        print()

def print_girls_preferences(girls, girls_pref):
    for i in range(0, len(girls)):
        print(girls[i], ':', end='  ')
        for i in girls_pref[i]:
            print(i, end='  ')
        print()


def init_free_men(suitors, free_men):
    for boy in suitors:
        free_men.append(boy)

def stable_matching(free_men, suitors, suitors_pref, girls_pref, tentative_engagements, girls):
    while(len(free_men) > 0):
        for man in free_men:
            begin_matching(man, suitors, suitors_pref, girls_pref, free_men, tentative_engagements, girls)

def begin_matching(man, suitors, suitors_pref, girls_pref, free_men, tentative_engagements, girls):
    index = suitors.index(man)
    for woman in suitors_pref[index]:

        print('{} proposes to {}'.format(man, woman))
        # 0 means woman is single 
        taken_match = [couple for couple in tentative_engagements if woman in couple]
        
        if (len(taken_match) == 0):
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            print('{} is engaged to {}'.format(man, woman))
            break
        elif (len(taken_match) > 0):

            current_guy = girls_pref[girls.index(woman)].index(taken_match[0][0])
            potential_guy = girls_pref[girls.index(woman)].index(man)

            if (current_guy > potential_guy):
                print('{} dumps {}'.format(woman, man))

                # the new guy is engaged
                free_men.remove(man)

                # the old guy is now single
                free_men.append(taken_match[0][0])

                # update the fiance of the woman
                taken_match[0][0] = man
                break

def print_pairings(tentative_engagements):
    for couple in tentative_engagements:
        print('{} - {}'.format(couple[0], couple[1]))

def print_participants(suitors, girls):
    for suitor in suitors:
        print(suitor, end=' ')
    print()
    for girl in girls:
        print(girl, end=' ')
    print()

def main():
    suitors = ['Abe', 'Bob', 'Col', 'Dan', 'Ed', 'Fred', 'Gav', 'Hal', 'Ian', 'Jon']
    girls = ['Abi', 'Bea', 'Cath', 'Dee', 'Eve', 'Fay', 'Gay', 'Hope', 'Ivy', 'Jan']


    print('\nParticipants:')
    print_participants(suitors, girls)

    suitors_pref = []
    girls_pref = []

    free_men = []

    for i in range(0, len(suitors)):
        random.shuffle(girls)
        suitors_pref.append(girls)
        girls = ['Abi', 'Bea', 'Cath', 'Dee', 'Eve', 'Fay', 'Gay', 'Hope', 'Ivy', 'Jan']

    for i in range(0, len(girls)):
        random.shuffle(suitors)
        girls_pref.append(suitors)
        suitors = ['Abe', 'Bob', 'Col', 'Dan', 'Ed', 'Fred', 'Gav', 'Hal', 'Ian', 'Jon']
    

    print('\nPreferences:')
    print_suitors_preferences(suitors, suitors_pref)
    print_girls_preferences(girls, girls_pref)

    tentative_engagements = []
    init_free_men(suitors, free_men)
    stable_matching(free_men, suitors, suitors_pref, girls_pref, tentative_engagements, girls)


    print()
    print('Pairing:')
    print_pairings(tentative_engagements)

if __name__ == '__main__':
    main()
