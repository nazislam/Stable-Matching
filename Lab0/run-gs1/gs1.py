#!/usr/bin/env python3

import random
import time
import sys
import run_gs1

try:
    user_input = int(sys.argv[1])
except:
    user_input = run_gs1.generate_random_number()

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
    while(len(free_men) > 0):
        for man in free_men:
            begin_matching(man, suitors, suitors_pref, girls_pref, 
                    free_men, tentative_engagements, girls)

def begin_matching(man, suitors, suitors_pref, girls_pref, free_men, 
        tentative_engagements, girls):
    index = suitors.index(man)
    for woman in suitors_pref[index]:

        taken_match = [couple for couple in tentative_engagements if woman in couple]
        
        if (len(taken_match) == 0):
            tentative_engagements.append([man, woman])
            free_men.remove(man)
            break
        elif (len(taken_match) > 0):

            current_guy = girls_pref[girls.index(woman)].index(taken_match[0][0])
            potential_guy = girls_pref[girls.index(woman)].index(man)

            if (current_guy > potential_guy):

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
    return random.randint(1, 10)

def main(user_input):
    start_time = time.time()
    start_clock = time.clock()
    time_to_sleep = generate_random_time()
    time.sleep(time_to_sleep)

    length = user_input

    suitors = list(range(length)) # 20 (0 - 19)
    girls = list(range(len(suitors), 2*(len(suitors))))


    suitors_pref = []
    girls_pref = []

    free_men = []


    for i in range(0, len(suitors)):
        random.shuffle(girls)
        suitors_pref.append(girls)
        girls = list(range(len(suitors), 2*(len(suitors))))

    for i in range(0, len(girls)):
        random.shuffle(suitors)
        girls_pref.append(suitors)
        suitors = list(range(length)) # 20 (0 - 19)
    

    tentative_engagements = []
    init_free_men(suitors, free_men)
    stable_matching(free_men, suitors, suitors_pref, girls_pref, tentative_engagements, girls)


    end_time = time.time()
    end_clock = time.clock()
    taken_time = round(end_time - start_time, 6)
    taken_clock = round(end_clock - start_clock, 6)

    try:
        sys.argv[1]  # It will print participants and time if there is any user input
        print('{}\t{}'.format(length, taken_clock))
    except:
        fh = open('data.txt', 'a+')
        fh.write(str(length))
        fh.write('\t')
        fh.write(str(taken_clock))
        fh.write('\n')




if __name__ == '__main__':
    main(user_input)

