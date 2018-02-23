#!/usr/bin/env python3

# PROGRAM NAME: Gale-Shapely Algorithm DEMO
# CREATED BY: Naz Islam
# DATE: 02/23/2018
# PURPOSE: 
# INPUT(S):
# OUTPUT(S):



import random
import time


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

def stable_matching(free_men, suitors, suitors_pref, girls_pref, 
            tentative_engagements, girls):
    # keep looping and find match until every man is engaged
    while(len(free_men) > 0):
        for man in free_men:
            begin_matching(man, suitors, suitors_pref, girls_pref,
                    free_men, tentative_engagements, girls)

def begin_matching(man, suitors, suitors_pref, girls_pref, 
            free_men, tentative_engagements, girls):
    index = suitors.index(man)
    for woman in suitors_pref[index]:

        print('{} proposes to {}'.format(man, woman))
        
        # Get a tuple of women and her associated match. If it exists
        # the tuple will be the suitor, and the girl.
        # Otherwise it will return an empty list 
        taken_match = [couple for couple in tentative_engagements 
                if woman in couple]
        
        if (len(taken_match) == 0):
            # The woman is free.
            # The man is engaged and no longer a free man.
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            print('{} is engaged to {}'.format(man, woman))
            break
        elif (len(taken_match) > 0):
            # The woman is not free.

            current_guy = girls_pref[girls.index(woman)].index(
                    taken_match[0][0])
            potential_guy = girls_pref[girls.index(woman)].index(man)

            if (current_guy > potential_guy):
            # She will check if she prefers 
            # potential_guy over the current_guy
            # else the man proposes his next prefered woman
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

def generate_random_time():
    """
    Generates a random number between 1 and 10.
    """
    return random.randint(1, 10)

def main():
    while True:
        start_time = time.time()
        start_clock = time.clock()

        # Generates random time (between 1 and 10s) to sleep for each execution
        time_to_sleep = generate_random_time()
        time.sleep(time_to_sleep)

        suitors = ['Abe', 'Bob', 'Col', 'Dan', 'Ed', 
                   'Fred', 'Gav', 'Hal', 'Ian', 'Jon']
        girls = ['Abi', 'Bea', 'Cath', 'Dee', 'Eve', 
                 'Fay', 'Gay', 'Hope', 'Ivy', 'Jan']


        print('\nParticipants:')
        print_participants(suitors, girls)

        suitors_pref = []
        girls_pref = []

        # Suitors who are still free and not yet engaged
        free_men = []


        # Generates preference list for suitors
        for i in range(0, len(suitors)):
            random.shuffle(girls)
            suitors_pref.append(girls)
            girls = ['Abi', 'Bea', 'Cath', 'Dee', 'Eve', 
                     'Fay', 'Gay', 'Hope', 'Ivy', 'Jan']

        # Generates preference list for girls
        for i in range(0, len(girls)):
            random.shuffle(suitors)
            girls_pref.append(suitors)
            suitors = ['Abe', 'Bob', 'Col', 'Dan', 'Ed', 
                       'Fred', 'Gav', 'Hal', 'Ian', 'Jon']
        

        print('\nPreferences:')
        print_suitors_preferences(suitors, suitors_pref)
        print_girls_preferences(girls, girls_pref)

        # Keeps track of the people that "may" end up together
        tentative_engagements = []
        init_free_men(suitors, free_men)
        stable_matching(free_men, suitors, suitors_pref, girls_pref, 
                tentative_engagements, girls)


        print('\nPairing:')
        print_pairings(tentative_engagements)

        end_time = time.time()
        end_clock = time.clock()
        taken_time = round(end_time - start_time, 6)
        taken_clock = round(end_clock - start_clock, 6)
        print('Elapsed wall clock time:\t {}'.format(taken_time))
        print('Elapsed CPU time:\t\t {}'.format(taken_clock))
        print('Stable matchup')

        k = input("\nAnother trial? (y)es, (n)o\n").lower()
        if (k == 'n' or k == 'no'):
            break
        else:
            continue





if __name__ == '__main__':
    main()
