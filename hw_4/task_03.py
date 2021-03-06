# Задача №3
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#                 "конвертированная сумма в EUR = int"
#                 "конвертированная сумма в CHF = int"
#                 "конвертированная сумма в GBP = int"
#                 "конвертированная сумма в CNY = int"
#
#     3. Скипт должен выдать сообщение
#                 "Введите положительное число." Если число меньше 0.
#                 "Вы ввели не число. Введите число." Если введены буквы.
#                 "Вы ввели пустое поле. Введите число." Если введено пустое значение.
#     4. Валюту пользователя определите сами.

currency_rate_dict = {'USD': 0.0126, 'EUR': 0.01125, 'CHF': 0.01196, 'GBP': 0.00959, 'CNY': 0.08184}
print("Введите количество денег для перевода:")
input_amount = input()

if input_amount.strip() == "" or len(input_amount) == 0:
    print("Вы ввели пустое поле. Введите число.")
else:
    try:
        if int(input_amount) >= 0:
            print("Вы ввели", input_amount, "RUB")
            for i, j in currency_rate_dict.items():
                result = int(input_amount) * j
                print("Конвертированная сумма в", i, "=", result)
        elif int(input_amount) < 0:
            print("Введите положительное число.")
    except:
        print("Вы ввели не число. Введите число.")
