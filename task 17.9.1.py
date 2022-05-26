list_num = list(map(int, input('Введите числа через пробел:').split()))
print(list_num)

while True:
    try:
        element = int(input("Введите число от 1 до 999: "))
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести число!")
    except Exception:
        print("Неправильный диапазон!")


list_num.append(element)
print(list_num) #новый список, в который добавили число

def merge_sort(list_num):
    if len(list_num) < 2:
        return list_num[:]
    else:
        middle = len(list_num) // 2
        left = merge_sort(list_num[:middle])
        right = merge_sort(list_num[middle:])
        return merge(left, right)
        print(merge)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_num_sort = merge_sort(list_num)
print(list_num_sort)  # отсортированный новый список

def binary_search(list_num_sort, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False
    middle = (right + left) // 2
    if list_num_sort[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < list_num_sort[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(list_num_sort, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(list_num_sort, element, middle + 1, right)

print(binary_search(list_num_sort, element, 0,  len(list_num_sort)))