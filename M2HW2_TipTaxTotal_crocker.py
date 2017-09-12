#get the total charge of food.
food= float(input('enter the total charge for food: '))

#get the percentage they want to tip of travel.
tip=.18

#get the sales tax %.
sales_tax=.07

#Get the total amount of bill with tip.
whole_bill = (food+ (food *18))*.07


#display total distance.
print('The total bill is $', format(whole_bill, ',.2f'))
