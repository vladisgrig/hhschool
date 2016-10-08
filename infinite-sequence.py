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
    if (start + step) <= len(sub):
        while (start + step) <= len(sub):
            first_item = sub[start:start + step]
            first_item_num = int(first_item)
            second_item_num = first_item_num + 1
            second_item = str(second_item_num)
            if (start + step + len(second_item)) <= len(sub):
                if sub[start + step:start + step + len(second_item)] == second_item:
                    start += step
                    step = len(second_item)
                else:
                    break
            else:
                right_part = sub[start + step:]
                if right_part:
                    if check_rightshift(right_part, first_item):
                        return True
                    else:
                        return False
                else:
                    return True
        else:
            return True
        return False
    else:
        return True

def check_leftshift(sub, step, shift):
    """Функция проверяет может ли левый сдвиг быть частью предыдущего числа"""
    if sub[shift:shift+1] != '0':
        if (shift + step) <= len(sub):
            first_item = sub[shift:shift + step]
            first_item_num = int(first_item)
            zero_item_num = first_item_num - 1
            zero_item = str(zero_item_num)
            if sub[:shift] == zero_item[-shift:]:
                return (True, zero_item_num)
            else:
                return (False,)
        else:
            part_of_first_item = sub[shift:]
            part_of_zero_item = sub[:shift]
            index = 0
            for i in part_of_zero_item:
                if i == '0':
                    index += 1
                else:
                    break
            else:
                index -= 1
            right = int(part_of_zero_item[index:]) + 1
            if len(str(right)) > len(part_of_zero_item[index:]):
                part_of_zero_item_plus_one = part_of_zero_item[:index-1] + str(right)
            else:
                part_of_zero_item_plus_one = part_of_zero_item[:index] + str(right)
            first_item = part_of_first_item + part_of_zero_item_plus_one[-(step - len(part_of_first_item)):]
            zero_item_num = int(first_item) - 1
            if part_of_zero_item == str(zero_item_num)[-shift:]:
                return (True, zero_item_num)
            else:
                return (False,)
    else:
        return (False,)

def check_subsequence(sub, step):
    """Функция возвращает числа и сдвиги, если удалось обнаружить числовую последовательность"""
    numbers = []
    for left_shift in range(1, step):
        data = check_leftshift(sub, step, left_shift)
        if data[0]:
            if check_main(sub, step, left_shift):
                numbers.append((data[1], left_shift))
    if sub[0] != '0':
        if check_main(sub, step, 0):
            numbers.append((int(sub[:step]), step))
    else:
        if step == len(sub):
            numbers.append((int('1' + sub), 1))
    return numbers

def main():
    while True:
        A = input('Введите числовую последовательность: ')
        if A.isdigit():
            A_lenght = len(A)
            for step in range (1, A_lenght + 1): #пробегаемся по последовательности увеличивая шаг
                check = check_subsequence(A, step) # получаем возможные числа
                if check:
                     num  = min(check)
                     break
            position = get_position(num[0]) + (len(str(num[0])) - num[1]) + 1
            print(position)
        else:
            break

if __name__ == '__main__':
    main()
