'''Напишите функцию-генератор all_variants(text),
 которая принимает строку text и возвращает объект-генератор,
 при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
Напишите функцию-генератор all_variants(text).
Опишите логику работы внутри функции all_variants.
Вызовите функцию all_variants и выполните итерации.
Пример результата выполнения программы:
Пример работы функции:
a = all_variants("abc")
for i in a:
    print(i)
Вывод на консоль:
a
b
c
ab
bc
abc

Примечания:
Для функции генератора используйте оператор yield.'''

def all_variants(text):
    x = len(text)
    for i in range(x):
        for j in range(i + 1, x + 1):
            yield text[i:j]


a = all_variants("abc")
for i in a:
    print(i)