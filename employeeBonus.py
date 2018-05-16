#Laura Davis
#11 March 2016
#This program will demonstrate how to use
#decision statements in Python.
#This program's purpose is to calculate a store bonus and
#an employee bonus based on monthly sales and sales increases, respectively.
#It then prints them according to predetermined values for the 
#bonus amounts in each category. 

#This is the main function.
def main():
	monthlySales = getSales() #call to get sales.
	salesIncrease = getIncrease() #call to get sales increase.
	storeAmount = storeBonus(monthlySales) #call to get store bonus.
	empAmount = empBonus(salesIncrease) #call to get employee bonus.
	printBonus(storeAmount, empAmount) #call to print amounts.
	
#This function gets the monthly sales
def getSales():
	monthlySales = input("Please enter the monthly sales $ ")
	monthlySales = float(monthlySales)
	return monthlySales
	
#This function gets the percent increase in sales.
#Percent values should be expressed in decimal format.
def getIncrease():
	salesIncrease = input("Please enter percent of sales increase as a decimal. \nFor example, 4% should be entered as .04: ")
	salesIncrease = float(salesIncrease)
	return salesIncrease
	
#This function determines the store bonus; variable storeAmount.
def storeBonus(monthlySales):
	if monthlySales >= 110000:
		storeAmount = 6000
	elif monthlySales >= 100000:
		storeAmount = 5000
	elif monthlySales >= 90000:
		storeAmount = 4000
	elif monthlySales >= 80000:
		storeAmount = 3000
	else:
		storeAmount = 0
	return storeAmount

#This function determines the employee bonus; variable empAmount.
def empBonus(salesIncrease):
	if salesIncrease >= .05:
		empAmount = 75
	elif salesIncrease >= .04:
		empAmount = 50
	elif salesIncrease >= .03:
		empAmount = 40
	else:
		empAmount = 0
	return empAmount
	
#This function prints the bonus information.
def printBonus(storeAmount, empAmount):
	print "The store bonus amount is $", storeAmount
	print "The employee bonus amount is $", empAmount
	if storeAmount == 6000 and empAmount == 75:
		print "Congrats! You have reached the highest bonus amount possible! "

#Calls main.
main()
