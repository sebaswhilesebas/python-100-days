##Welcome to the tip calculator!
##What was the total bill? $124.56
##How much tip would you like to give? 10, 12, or 15? 12
##How many people to split the bill? 7
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
cuenta= float(input("What was the total bill?\n$"))
propina= float(input("How much tip would you like to give? 10, 12, or 15?\n"))
personas= float(input("How many people to split the bill?\n"))

print (f"Each person should pay: ${propina/100+1*cuenta/personas:0.2f}\n")

##print (f"Each person should pay: ${cadaunopaga: .2f}\n")       
#cadaunopaga= cuentamaspropina/personas                  
#print ("Each person should pay"+cadaunopaga
