  class RetailItem:
    def __init__(self, item, description, price, available_quantity):
    self.__item = item
    self.__description = description
    self.__price = price
    self.__available_quantity = available_quantity
  
  def get_item(self):
    return self.__item
  
  def get_description(self):
    return self.__description
  
  def get_price(self):
    return self.__price
  
  def get_available_quantity(self):
    return self.__available_quantity
    
  def update_avail(self, purchase):
    self.__available_quantity -= purchase
  
  def __str__(self):
    return str(self.__item) + "\t" + str(self.__description) + "\t" + str(self.__price) + "\t" + str(self.__available_quantity)
