from datetime import datetime
from datetime import timedelta
#from exception import EndingExpirationDate
class EndingExpirationDate(Exception):
    pass
class Good:
  def __init__(self, name, count, price, production_date, expiration_day):
      self.name = name
      self.count = count
      self.price = price
      self.production_date = datetime.strptime(production_date, '%Y-%m-%d')
      self.expiration_day = expiration_day

  def __str__(self):
      return f'{self.name}'

  def check_expiration_date(self):
      '''Проверка срока годности товара'''

      date_now = datetime.now()
      date_ending_expiration = self.production_date + timedelta(days=int(self.expiration_day))

      if date_ending_expiration > date_now:
          return True
      else:
          raise EndingExpirationDate

class GoodList:


  def __init__(self):
      self.good_list = []

  def add_good_in_list(self, good: Good):


      try:
          good.check_expiration_date()
          self.good_list.append(good)
      except EndingExpirationDate:
          print(f"Товар {good} с истекшим сроком годности")
          return None

  def remove_good_from_list(self, name: str):

      for index, good in enumerate(self.good_list):
          if good.name == name:
              del self.good_list[index]
              break

  def clear_by_expiration_date(self):


      for good in self.good_list:
          try:
              good.check_expiration_date()
          except EndingExpirationDate:
              self.remove_good_from_list(good.name)

  def get_mean_price(self):


      sum_price = 0
      sum_count = 0

      for good in self.good_list:
          sum_price += int(good.price)
          sum_count += int(good.count)

      print(f'sum goods = {sum_price}')
      print(f'sum count = {sum_count}')
      mean = 0

      if sum_count != 0:
          mean = sum_price / sum_count

      return mean


  def get_good_with_max_price(self):


      name = ''
      max_price = 0

      for good in self.good_list:
          if good.price > max_price:
              max_price = good.price
              name = good.name

      return name

  def get_good_with_min_price(self):


      name = ''
      min_price = 10000

      for good in self.good_list:
          if good.price < min_price:
              min_price = good.price
              name = good.name

      return name

  def get_good_with_max_count(self):


      name = ''
      max_count = 0

      for good in list_with_goods:
          if good.count > max_count:
              max_count = good.count
              name = good.name

      return name

  def get_good_with_min_count(self):


      name = ''
      min_count = 0

      for good in list_with_goods:
          if good.count < min_count:
              min_count = good.count
              name = good.name

      return name


