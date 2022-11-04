import pytest

num_list = []

def add_in_list(num):
    state = True
    if type(num) == int:
        if num >= 0:
            num_list.append(num)
            state = True
        else:
            state = False
    else:
        state = False
    return state

def is_prime_number(num):
    state = True
    multiply = 0

    if num == 1:
        state = False
    else:
        for count in range(2,num):
            if (num % count == 0):
                multiply += 1
        
        if multiply == 0:
            state = True
        else:
            state = False
    return state

def is_empty_list(num):
    state = True
    if len(num) == 0:
        state = True
    else:
        state = False
    return state

def check_last_2_not_prime_numbers_in_list(num):
    count = 0
    state = num
  
    if len(num) == 1 or len(num) == 2:
        for i in range(len(num)):
            if is_prime_number(num[i]) != True:
                count += 1

        for i in range(count):
            state.pop()
    
    return state

def smallest_not_prime_number_in_list(num):
    smaller = 0
    state = smaller
    
    for item in num:
        if is_prime_number(item) != True:
            if smaller == 0:
                smaller = item
            else:
                if item < smaller:
                    smaller = item
    state = smaller
    return state

def greatest_not_prime_number_in_list(num):
    greatest = 0
    state = greatest
    
    for item in num:
        if is_prime_number(item) != True:
            if greatest == 0:
                greatest = item
            else:
                if item > greatest:
                    greatest = item
    state = greatest
    return state

def main():

    # Inicializando todos os valores
    insert_list = [2, 3, 5, 4, 6, 7, 11, 13, 17, 19, 23]
    print("Lista inicial: ", insert_list)
    for item in insert_list:
        add_in_list(item)
    
    if (is_empty_list(num_list)):
        print("Lista vazia!")
    else:
        while(True):
            small = smallest_not_prime_number_in_list(num_list)
            great = greatest_not_prime_number_in_list(num_list)
            print("Menor número não primo: ", small)
            print("Maior número não primo: ", great)

            if small == 0 and great == 0:
                print("Não há números não primos na lista!")
                break
            elif len(num_list) <= 2:
                check_last_2_not_prime_numbers_in_list(num_list)
                break
            else:
                try:
                    num_list.remove(small)
                    num_list.remove(great)
                except:
                    continue

    print("Lista final: ", num_list)


if __name__ == "__main__":
    main()