import re

def get_position(number):
    """Возвращает позицию числа в бесконечной последовательности"""
    num_length = len(str(number))
    position = 0
    for i in range(1, num_length):
        position += (10 ** i - 10 ** (i - 1)) * i
    position += (number - 10 ** (num_length - 1)) * num_length
    return position

def check_rightshift(sub, last_elem):
    """Функция проверяет, может ли правый кусок быть частью следующего числа"""
    num = int(last_elem)
    if sub == str(num+1)[:len(sub)]:
        return True
    else:
        return False

def check_main(sub, step, start):
    """Функция проверяет, сформирована ли последовательность числами"""
    while (start + step) < len(sub):
        first_item = sub[start:start + step]
        first_item_num = int(first_item)
        second_item_num = first_item_num + 1
        second_item = str(second_item_num)
        if (start + step + len(second_item)) < len(sub):
            if sub[start + step: start + step + len(second_item)] == second_item:
                start += step
                step = len(second_item)
            else:
                break
        else:
            right_part = sub[start + step:]
            if check_rightshift(right_part, first_item):
                return True
            else:
                return False
    else:
        return True
    return False

def check_leftshift(sub, step, shift):
    """Функция проверяет может ли левый сдвиг быть частью предыдущего числа"""
    first_item = sub[shift:shift + step]
    first_item_num = int(first_item)
    zero_item_num = first_item_num - 1
    zero_item = str(zero_item_num)
    if sub[:shift] == zero_item[-shift:]:
        return (True, zero_item_num)
    else:
        return (False,)

def check_subsequence(sub, step):
    """Функция возвращает номер позиции первого числа, если удалось обнаружить числовую последовательность"""
    for left_shift in range(1, step):
        data = check_leftshift(sub, step, left_shift)
        if data[0]:
            if check_main(sub, step, left_shift):
                number = data[1]
                position = get_position(number) + (len(str(number)) - left_shift) + 1
                break
    else:
        if check_main(sub, step, 0):
            number = int(sub[:step])
            position = get_position(number) + 1
            return position
        else:
            return 0
    return position

def main():
    while True:
        A = input('Введите числовую последовательность: ')
        if A.isdigit():
            A_leght = len(A)
            for step in range (1, A_leght): #пробегаемся по последовательности увеличивая шаг
                num = check_subsequence(A, step) # проверяем, можно ли уследить последовательность чисел
                if num:
                    break
            else: # если ни для какого шага не обнаружили последовательность
                if A[0] != '0': # если не начинается с нуля, то вычисляем позицию числа
                    num = get_position(int(A)) + 1
                else: # добавляем 1 и вычисляем позицию нового числа
                    num = get_position(int('1' + A)) + 1
            print(num)
        else:
            break

if __name__ == '__main__':
    main()
