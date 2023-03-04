#the program is a basic version of input in our bot 
#now we have to make a method for transforming gregorian to hijry
#Latitude: 34° 25' 59.99" N
#Longitude: 35° 50' 59.99" E

Y = eval(input("Give us the year: "))
M = eval(input("Give us the month: "))
D = eval(input("Give us the day: "))

while D>=32 :
  print("Gregorian and Julian months never have more than 31 days.\n Try again.")
  D = eval(input("Give us the day: "))
   
while D==31 :
    while M in [2,4,6,7,11]: 
        print("This month doesn't have 31 days. \n Try again.")
        D = eval(input("Give us the day: "))

while M==2 and D==30:
  print("February never has 30 days. \n Try again.")
  D = eval(input("Give us the day: "))

#check for leap years
while M==2 and D==29: 
    Leap = false
    if (Y%4==0) :
        Leap = true
    if ((Y%100==0) and (Y%400>0)) :
        Leap = false
    if (Y%4000==0) :
        Leap = false
    if (Leap==false) :
       print(Y + " is not a leap year in the Gregorian calendar. Please enter a real date.")
       Y =eval(input("Give us the year: "))
