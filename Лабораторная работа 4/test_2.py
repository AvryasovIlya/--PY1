import re
def get_count_char(main_str):
    #main_str_ = re.sub(r'[^\w\s]', '', main_str.splitlines())
    #main_str_ = main_str_.replace(" ", "")
    main_str = ''.join(b for b in main_str.lower() if b.isalpha())

    dict_1 = {symbol: main_str.count(symbol) for symbol in main_str}

    return dict_1

def frequency(main_str):
      ...


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
main_str = get_count_char(main_str)
print(main_str)


def frequency(main_str):
    sum_ = sum(main_str.values())/ 100


    for key in main_str:
        main_str[key] = round(main_str[key] / sum_,2)
    return main_str

qwerty = frequency(main_str)
print(qwerty)