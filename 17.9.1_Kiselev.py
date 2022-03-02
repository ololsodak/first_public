# функция сортировки
def sort(array):
    if len(array) <= 1: # условие выхода из рекурсии
        return array
    elem = array[0] # выбираем ведущий элемент
    left = [] # список элементов, которые меньше ведущего
    center = [] # список элементов, равных ведущему
    right = [] # список элементов, котрые больше ведущего
    for i in array:
        if i < elem:
            left.append(i)
        elif i > elem:
            right.append(i)
        else:
            center.append(i)
                
    return sort(left) + center + sort(right) # рекурсия 
    
# функция осуществляет поиск индекса элемента, который меньше введенного числа, а следующий элемент больше или равен этому числу
def bin_search(array, element, left, right): 
    if left > right:
        if element > array[-1]:
            return 'Решения нет - введеное число больше максимального в последовательности'
        elif element < array[0]:
            return 'Решения нет - введеное число меньше минимального в последовательности'
    if element == array[-1] and array[-2] != array[-1]:
        return 'Решения нет - введеное число является максимальным в последовательности'
    elif element == array[0]:
        return 'Решения нет - введеное число является минимальным в последовательности'     
            
    middle = (left + right)//2 # индекс середины
    if array[middle] >= element: 
        if array[middle-1] < element:
            return f'Номер позиции требуемого элемента "{array[middle-1]}" - {middle-1}'
        else: # если array[middle-1] == array[middle] (два одинаковых элемента рядом)
            return bin_search(array, element, left, middle-1) # рекурсия по списку слева от середины
    elif array[middle] > element:
        return bin_search(array, element, left, middle-1) # рекурсия по списку слева от середины
    elif array[middle] < element:
        return bin_search(array, element,middle+1, right) # рекурсия по списку справа от середины
        
  
        
    
a = list(map(int, (input('Введите целые числа через пробел:\n').split()))) # последовательность преобразуем в список чисел
print(a) # исходный список
b = sort(a) # отсортированный список
print(b)

# 7 8 5 10 3 -4 80 71 5 4 3 -3 7 18
# 3 1 9 0 7 5 9
element = int(input('Введите любое целое число\n'))
print(bin_search(b,element, 0, len(b)-1))