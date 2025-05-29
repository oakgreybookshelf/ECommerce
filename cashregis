class CashRegister:
    def __init__(self):
    self.__inventory_list = []
    self.__cart_list = []
  
  def stock_item(self, RetailItem):
    self.__inventory_list.append(RetailItem)
  
  def add_to_cart(self, Cart):
    self.__cart_list.append(Cart)
  
  def get_items(self):
    return self.__inventory_list
  
  def get_cart(self):
    return self.__cart_list
  
  def print_inv(self):
    print("Item" + "\t" + "Descr" + "\t" + "Price" + "\t" + "Avail")
    for item in self.__inventory_list:
      print(item, '\t')
  
  def print_cart(self):
    print("Item" + "\t" + "Descr" + "\t" + "Price" + "\t" + "Quantity")
    for item in self.__cart_list:
      print(item, '\t')
  
  def clear_cart(self, cart_list):
    self.__cart_list = []
