# 1) Создать переменную типа String
string_variable = 'String'
print('Variable', string_variable, 'with', type(string_variable), 'type')

# 2) Создать переменную типа Integer
integer_variable = 321
print('Variable', integer_variable, 'with', type(integer_variable), 'type')

# 3) Создать переменную типа Float
float_variable = 3.21
print('Variable', float_variable, 'with', type(float_variable), 'type')

# 4) Создать переменную типа Bytes
bytes_variable = b"Bytes"
print('Variable', bytes_variable, 'with', type(bytes_variable), 'type')

# 5) Создать переменную типа List
# lists are mutable
list_variable = ["Stark", "Targaryen", "Lannister", "Baratheon"]
print('Variable', list_variable, 'with', type(list_variable), 'type')

# 6) Создать переменную типа Tuple
# tuples are immutable
tuple_variable = ("Robb", "Sansa", "Arya", "Bran", "Rickon")
print('Variable', tuple_variable, 'with', type(tuple_variable), 'type')

# 7) Создать переменную типа Set
set_variable = {"Tyrion", "Cersei", "Jaime", "Tyrion"}
print('Variable', set_variable, 'with', type(set_variable), 'type')

# 8. Создать переменную типа Frozen set
frozen_set_variable = frozenset(set_variable)
print('Variable', frozen_set_variable, 'with', type(frozen_set_variable), 'type')

# 9) Создать переменную типа Dict
dict_variable = {"book_name": "A Clash of Kings", "year": 1998}
print('Variable', dict_variable, 'with', type(dict_variable), 'type')

# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
# 11) Создать 2 переменные String, создать переменную в которой суммируете эти переменные. Вывести в консоль.
the_first_string = 'Daenerys '
the_second_string = 'Targaryen'
the_third_and_final = the_first_string + the_second_string
print('The final variable is', the_third_and_final)

# 12) Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
book_name = 'A Clash of Kings'
date = 1998
print(book_name, date)

# 13) Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
print(book_name + str(date))
