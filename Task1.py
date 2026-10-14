def calculateElectronicsGST(a,b):
    return (a+b)*1.18

def calaculateFashionGST(c,d):
    return (c+d)*1.13

def calculateFoodGST(e):
    return (e)*1.07

def totalBill(a,b,c,d,e):
    return (calculateElectronicsGST(a,b) + calaculateFashionGST(c,d) + calculateFoodGST(e))

def calculateDiscountedBill(a,b,c,d,e):
    total = totalBill(a,b,c,d,e)
    discount = total * .20
    return total - discount


a=100
b=100
c=100
d=100
e=100

electonics =calculateElectronicsGST(a,b)

fashion =calaculateFashionGST(c,d)

food =calculateFoodGST(e)

total =totalBill(a,b,c,d,e,)

discount= total*0.20

payble =calculateDiscountedBill(a,b,c,d,e)


print(f"Electronics :{electonics :.2f}")
print(f"Fashion :{fashion :.2f}")
print(f"Food: {food:.2f}")
print(f"Total after GST :{total:.2f}")
print(f"Discount :{discount:.2f}")
print(f"Final Payable amount :{payble:.2f}")