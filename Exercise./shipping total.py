

#Declare variables
orderTotal = 0
shippingCost = 0
totalWithShipping = 0

#Ask user for their order total and convert the answer to a number
orderTotal = float(input("What was the total for your order? " ))

#Calculate the shipping cost based on the order total
if orderTotal >= 50 :
    shippingCost = 0
else :
    shippingCost = 10

#Calculate order total including shipping
totalWithShipping = orderTotal + shippingCost

#Tell the user their final total
print("Your final total, including shipping, will be: $%.2f " % totalWithShipping)




