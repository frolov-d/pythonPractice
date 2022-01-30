currency_rate_dict = {'USD': 0.0126, 'EUR': 0.01125, 'CHF': 0.01196, 'GBP': 0.00959, 'CNY': 0.08184}

print("Введите количество денег для перевода:")
input_amount = int(input())

print("Вы ввели", input_amount, "RUB")

for i, j in currency_rate_dict.items():
    result = input_amount * j
    print("Конвертированная сумма в", i, "=", result)