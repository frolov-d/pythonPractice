# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
#     3. Валюту пользователя определите сами.

print("Введите количество денег для перевода:")

input_amount = int(input())
usd_to_rub_course = 0.0126
eur_to_rub_course = 0.01125
chf_to_rub_course = 0.01196
gbp_to_rub_course = 0.00959
cny_to_rub_course = 0.08184
converted_to_usd = input_amount * usd_to_rub_course
converted_to_eur = input_amount * eur_to_rub_course
converted_to_chf = input_amount * chf_to_rub_course
converted_to_gbp = input_amount * gbp_to_rub_course
converted_to_cny = input_amount * cny_to_rub_course

print("Вы ввели", input_amount, "RUB")
print("Конвертированная сумма в USD =", converted_to_usd)
print("Конвертированная сумма в EUR =", converted_to_eur)
print("Конвертированная сумма в CHF =", converted_to_chf)
print("Конвертированная сумма в GBP =", converted_to_gbp)
print("Конвертированная сумма в CNY =", converted_to_cny)