# -*- coding: utf8 -*-
import Goods
if __name__ == "__main__":
    good_list = GoodList()

    with open('prob.txt', 'r') as file:
        list_with_goods = file.readlines()

        for str_good in list_with_goods:
            list_good = str_good.split(':')

            name = list_good[0]
            price = list_good[1]
            count = list_good[2]
            production_date = list_good[3]
            expiration_day = list_good[4]

            good_list.add_good_in_list(Good(name, price, count, production_date, expiration_day))
            good_list.get_mean_price()

