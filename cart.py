class Cart:
  def __init__(self, item, description, price, purchase_quanity):
    self.__item = item
    self.__description = description
    self.__price = price
    self.__purchase_quanity = purchase_quanity
  
  def get_item(self):
    return self.__item
  
  def get_description(self):
    return self.__description
  
  def get_price(self):
    return self.__price
  
  def get_purchase_quanity(self):
    return self.__purchase_quanity
  
  def __str__(self):
    return self.__item + "\t" + self.__description + "\t" + self.__price + "\t" + purchase_quanity
