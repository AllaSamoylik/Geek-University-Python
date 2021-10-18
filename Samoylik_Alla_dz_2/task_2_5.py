rand_prices = [97, 1.73, 11.8, 15, 14.68, 5.9, 89.56, 9, 17.8]

# Сортировка цен на увеличение
rand_prices.sort()
prices_less = rand_prices.copy()

for i in range(len(rand_prices)):
    rand_prices[i] = str(rand_prices[i])
    if rand_prices[i].find('.') == -1:
        rand_prices[i] += ' руб 00 коп'
    elif rand_prices[i].find('.') != -1:
        if rand_prices[i][-2:].find('.') != -1:
            rand_prices[i] = rand_prices[i][:-2] + ' руб ' + rand_prices[i][-1:] + '0 коп '
        else:
            rand_prices[i] = rand_prices[i][:-3] + ' руб ' + rand_prices[i][-2:] + ' коп '
print(', '.join(rand_prices))
print()

# ЦСортировка цен на уменьшение
prices_less.reverse()
max_prices = prices_less[0: 5]

for i in range(len(prices_less)):
    prices_less[i] = str(prices_less[i])
    if prices_less[i].find('.') == -1:
        prices_less[i] += ' руб 00 коп'
    elif prices_less[i].find('.') != -1:
        if prices_less[i][-2:].find('.') != -1:
            prices_less[i] = prices_less[i][:-2] + ' руб ' + prices_less[i][-1:] + '0 коп '
        else:
            prices_less[i] = prices_less[i][:-3] + ' руб ' + prices_less[i][-2:] + ' коп '
print(', '.join(prices_less))
print()

# 5 максимальных цен по возрастанию
max_prices.reverse()

for i in range(len(max_prices)):
    max_prices[i] = str(max_prices[i])
    if max_prices[i].find('.') == -1:
        max_prices[i] += ' руб 00 коп'
    elif max_prices[i].find('.') != -1:
        if max_prices[i][-2:].find('.') != -1:
            max_prices[i] = max_prices[i][:-2] + ' руб ' + max_prices[i][-1:] + '0 коп '
        else:
            max_prices[i] = max_prices[i][:-3] + ' руб ' + max_prices[i][-2:] + ' коп '
print(', '.join(max_prices))
