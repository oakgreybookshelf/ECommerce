import retailitem
import cart
import cashregister

mycashregister = cashregister.CashRegister()

item1 = retailitem.RetailItem(1, "Jacket", 59.95, 10)
item2 = retailitem.RetailItem(2, "Jeans", 34.95, 2)
item3 = retailitem.RetailItem(3, "Shirt", 24.95, 4)

mycashregister.stock_item(item1)
mycashregister.stock_item(item2)
mycashregister.stock_item(item3)

mycashregister.print_inv()
print()
#print(cart.get_item())
inv_list = mycashregister.get_items()

for thing in inv_list:
  print(thing)
  availability = thing.get_available_quantity()
  purchase = int(input("How many would you like to buy? "))
  if purchase > availability:
    print("Stock low, you must buy less than ", availability)
  else:
    #purchase > 0
    mycashregister.add_to_cart(thing) 
    thing.update_avail(purchase)

print()
mycashregister.print_cart()

print()
print(purchase)

#mycart = cart.Cart()

cart_list = mycashregister.get_cart()

for thing in cart_list:
  print(int(cart_list.get_purchase_quanity(thing) * thing.get_price()))

#mycashregister.print_inv()'''