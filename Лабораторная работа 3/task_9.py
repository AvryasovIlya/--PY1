salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
def try_to_alive(months, spend, need_money, salary):
    for i in range(months):
        if i >= 1:
            spend = spend + spend * increase
            need_money = need_money - salary + spend
        else:
            need_money = need_money - salary + spend
    print(round(need_money))
try_to_alive(months,spend,need_money,salary)