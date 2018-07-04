#Write a program (function!) that takes a list and returns a new list that contains all
#  the elements of the first list minus all the duplicates.
#Extras:
#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.
import random

def make_distinct_using_set(input_list):
    temp_set = set(input_list)
    output_list = list(temp_set)
    return output_list

def make_distinct_using_cycle(input_list):
    output_list = list()
    for suspect in input_list:
        if not suspect in output_list:
            output_list.append(suspect)
    return output_list

def main():
    test_list = list()
    l1 = range(1, random.randrange(1, 30))
    for x in l1:
        test_list.append(x)
        test_list.append(x)
    print(test_list)
    cycle_victim = make_distinct_using_cycle(test_list)
    set_victim = make_distinct_using_set(test_list)
    print(cycle_victim)
    print(set_victim)

main()
