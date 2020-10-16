import pandas as pd
from pulp import *
import sys
import copy


def algorithm():
    #Тестовый датафрейм, сюда будут добавляться позиции в процессе (рандомно)
    
    df = pd.DataFrame({'Variable': ['x1', 'x2', 'x3','x4'], #Название товаров
                       'Price': [184, 55, 90, 61.5],        #Цена за единицу
                       'Number': [1,1,1,1],                 #Кол-во (инициализация)
                       'Items': [200, 200, 200,200]       #Сколько всего доступно
                        })

    sum_res = 40850 #Поле желаемоей суммы
    '''
    df = pd.DataFrame({'Variable': ['x1', 'x2', 'x3'], #Название товаров
                       'Price': [10,50,90],        #Цена за единицу
                       'Number': [1,1,1],                 #Кол-во (инициализация)
                       'Items': [200, 200, 200]       #Сколько всего доступно
                        })

    sum_res = 205 #Поле желаемоей суммы
    '''
    items_ratio = 2.5 #Допустимое отношение максимального кол-ва элементов к минимальному
    price_ratio = 0.01 #Допустимое различие между заданной и полученной суммой

    finish = True
    max_item = sys.maxsize
    max_name = None

    prob = LpProblem('Sell', LpMaximize) # Objective function

    inv_items = list(df['Variable']) # Variable name

    items = dict(zip(inv_items, df['Items'])) # Function
    prices = dict(zip(inv_items, df['Price'])) 
    print(items)

    inv_vars = LpVariable.dicts('Var', inv_items, lowBound = 1, cat = 'Integer')

    prob += lpSum([prices[i] * inv_vars[i] for i in inv_items])
    prob += lpSum([prices[i] * inv_vars[i] for i in inv_items]) <= sum_res, 'Общая функция'

    for val in items:
        prob += inv_vars[val] <= items[val], val+' Demand'


    vals_check = [None,None]
    while finish:
        if max_name:
            prob += inv_vars[max_name] <= max_item

        prob.solve()
        values_list = []

        print('The optimal answer\n'+'-'*70)
        for v in prob.variables():
            item = v.varValue
            if item > 0:
                values_list.append(item)

        max_item = max(values_list) - 1
        balance = float(max_item / min(values_list))
        max_name = 'x' + str(values_list.index(max(values_list))+1)
        print(values_list,max_item, max_name)


        t = list(prices.values())
        if len(values_list) == len(t):
            price_res = [t[i] * values_list[i] for i in range(len(t))]
            price_res = sum(price_res)
            print(price_res)
        else:
            #В настройках функции стоит, что минимум должен быть один элемент.
            #Если уже меньше, чем нужно - то значит 100% ошибка. Значит выходим.
            print("Обыграть перевызов функции с новым датасетом")
            return
        
        curr_price_ratio = (sum_res - price_res) / sum_res
        if balance <= items_ratio and  curr_price_ratio <= price_ratio:
            finish = False


    print("Ответ:")
    for i in range(len(values_list)):
        print(inv_items[i],":, ",values_list[i])
    return



algorithm()
