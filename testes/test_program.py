try:
    import sys
    import os
    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), '..'
            )
        )
    )
except:
    raise

from src import program
import pytest

num_list = []

def main():
    print("inicializou")

# Testa adição de strings em lista de inteiros == False
@pytest.mark.parametrize('num', ["a", "b", "Monta", "Julia", "Jeremias"])
def test_add_string_in_list(num):
    #num_list.append(num)
    result = program.add_in_list(num)
    #assert type(num) == int
    assert result != True

# Testa adição de int em lista e todos serem inteiros == True
@pytest.mark.parametrize('num', [4, 3, 2, 1])
def test_add_int_in_list(num):
    #num_list.append(num)
    result = program.add_in_list(num)
    #assert type(num) == int
    assert result == True

# Testa adição de int negativo em lista == False
@pytest.mark.parametrize('num', [-4, -3, -2, -1])
def test_add_negative_number_in_list(num):
    result = program.add_in_list(num)
    assert result != True

# Testa adição de int positivo em lista == True
@pytest.mark.parametrize('num', [4, 3, 2, 1])
def test_add_naturals_numbers_in_list(num):
    result = program.add_in_list(num)
    assert result == True

# Testa se numero não é primo == False
@pytest.mark.parametrize('num', [4, 6, 8, 10, 12, 18])
def test_is_not_prime_number(num):
    result = program.is_prime_number(num)
    assert result != True

# Testa se a lista passada está com elementos == False
@pytest.mark.parametrize('num', [[1,2,3],[4,4,4],[3,3,1,5]])
def test_is_not_empty_list(num):
    state = True
    if len(num) == 0:

        state = True
    else:
        state = False
    assert state == False

# Testa se a lista passada está vazia == True
@pytest.mark.parametrize('num', [[],[],[]])
def test_is_empty_list(num):
    state = True
    if len(num) == 0:

        state = True
    else:
        state = False
    assert state == True

#Consegue adicionar elementos inteiros na lista == True
@pytest.mark.parametrize('num', [4, 3, 2, 1])
def test_add_in_list(num):
    state = True
    if type(num) == int:
        if num >= 0:
            num_list.append(num)
            state = True
        else:
            state = False
    else:
        state = False
    assert state == True

# Verifica se numeros são primos == True
@pytest.mark.parametrize('num', [2, 3, 5, 7, 11, 13, 17, 19, 23])
def test_is_prime_number(num):
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
    assert state == True

# Testa se na lista só existe 2 números não primos == []
@pytest.mark.parametrize('num', [[4, 6]])
def test_last_2_not_prime_numbers_in_list(num):
    count = 0
    state = num
    if len(num) == 1 or len(num) == 2:
        for i in range(len(num)):
            if program.is_prime_number(num[i]) != True:
                count += 1
        
        for i in range(count):
            state.pop()
    
    assert state == []

# Testa se na lista só existe mais de 2 números não primos != []
@pytest.mark.parametrize('num', [[4, 6, 12]])
def test_most_than_2_not_prime_numbers_in_list(num):
    count = 0
    state = num
  
    if len(num) == 1 or len(num) == 2:
        for i in range(len(num)):
            if program.is_prime_number(num[i]) != True:
                count += 1

        for i in range(count):
            state.pop()
    
    assert state != []

# Testa se na lista só existe 1 número não primo == []
@pytest.mark.parametrize('num', [[4]])
def test_1_not_prime_numbers_in_list(num):
    count = 0
    state = num
    if len(num) == 1 or len(num) == 2:
        for i in range(len(num)):
            if program.is_prime_number(num[i]) != True:
                count += 1
        
        for i in range(count):
            state.pop()
    
    assert state == []

# Testa menor número não primo da lista == 4
@pytest.mark.parametrize('num', [[2, 3, 4, 5, 6, 7, 11, 13, 17, 19, 23]])
def test_smallest_not_prime_number_in_list(num):
    smaller = 0
    state = smaller
    
    for item in num:
        if program.is_prime_number(item) != True:
            if smaller == 0:
                smaller = item
            else:
                if item < smaller:
                    smaller = item
    state = smaller
    assert state == 4

# Testa maior número não primo da lista == 6
@pytest.mark.parametrize('num', [[2, 3, 4, 5, 6, 7, 11, 13, 17, 19, 23]])
def test_greatest_not_prime_number_in_list(num):
    greatest = 0
    state = greatest
    
    for item in num:
        if program.is_prime_number(item) != True:
            if greatest == 0:
                greatest = item
            else:
                if item > greatest:
                    greatest = item
    state = greatest
    assert state == 6


if __name__ == "__main__":
    main()