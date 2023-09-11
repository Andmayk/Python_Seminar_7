# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
# (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.

operation_mul = lambda r, c: r * c
operation_add = lambda r, c: r + c
operation_pow2 = lambda r, c: (r*10+c)**2 
operation_pow = lambda r, c: r**c 

def print_operation_table(operation, num_rows=6, num_columns=6):
    tb = len(str(max(operation(num_rows, num_columns),operation(1, num_columns),operation(num_rows, 1))))+2
    for r in range(num_rows+1):
        for c in range(num_columns+1):
            if r==c==0:
                print(' '*(len(str(num_rows))+1), end='')        
            elif r==0: # выводим номера колонок
                print(str(c).rjust(tb), end='') 
            elif c==0: # выводим номера строк
                print(str(r).rjust(len(str(num_rows))+1), end='') 
            else:
                print(str(operation(r, c)).rjust(tb), end='')
        print()

print("Таблица умножения")
print_operation_table(operation_mul,12,15)
print()
print("Таблица сложения")
print_operation_table(operation_add,12,12)
print()
print("Таблица квадратов (по строкам десятки по колонкам единицы)")
print_operation_table(operation_pow2,9,9)
print()
print("Таблица степеней")
print_operation_table(operation_pow)