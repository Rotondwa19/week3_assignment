#Discount Price Calculator
def calculateDiscount(price,percentageDiscount):
  discount = price * percentageDiscount / 100
  discount = round(discount,2)
  return discount

#Main Program  
item = input("Enter the name of the item to buy?")
if item!="X":
  itemPrice=float(input("Enter a price for your item: R"))
  percentageDiscount = int(input("Enter a percentage discount for your item: %"))
  discount = calculateDiscount(itemPrice, percentageDiscount)
  newPrice = itemPrice - discount
  print("Discounter price: R" + str(newPrice))
  item = input("Enter the name of another item to buy?")