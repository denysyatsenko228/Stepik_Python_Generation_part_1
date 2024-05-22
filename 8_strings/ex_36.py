"""
Используя метод format(), дополните приведенный код так, чтобы он вывел текст:
In 2010, someone paid 10k Bitcoin for two pizzas.
"""
a, b, c = 2010, "10k", "Bitcoin"
s = 'In {0}, someone paid {1} {2} for two pizzas.'
print(s.format(a, b, c))

