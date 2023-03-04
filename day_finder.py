#I didnt use this website but refer to it https://artofmemory.com/blog/how-to-calculate-the-day-of-the-week/

#getting data from user 
print("The program that calculates the day starting from dates!!!")
day = eval(input("Give us the day: "))
month = eval(input("Give the month (in number): "))
year = eval(input("Give the year: "))

#assigning value to each month 
if month in { 1,10 } :
    month_code = 1
elif month in { 2,3,11 }  :
    month_code = 4
elif month in { 4,7 } : 
    month_code = 0 
elif month in  { 5 } : 
    month_code = 2 
elif month in  { 6 } :
    month_code = 5 
elif month in { 9,12 } : 
    month_code = 6 
else : 
    month_code = 3

#generating a century from a specific year
for i in range (1,90,1): 
    century_loop = year -  i * 100
    if century_loop <= 0 :
        print(f" {year} is in {i*100-100} century ")
        century = i * 100 - 100 
        break

#generate and assign century code to each century         
century_code = ((century) / 100 )% 4
if century_code  == 0 : 
    century_real_code = 6 
elif century_code == 1 : 
    century_real_code = 4
elif century_code == 2 : 
    century_real_code = 2
else : 
    century_real_code = 0 

#calculating years
year_last = year - century 

#assigning year code to each year
#print (year_last)
if year_last in {  00, 6 , 17, 23, 28, 34, 45, 51, 56, 62, 73, 79, 84, 90 } :
    year_code = 0 
elif year_last in { 1, 7, 12, 18, 29, 35, 40, 46, 57, 63, 68, 74, 85, 91, 96 } :
    year_code = 1 
elif year_last in { 2, 13, 19, 24, 30, 41, 47, 52, 58, 69, 75, 80, 86, 97} : 
    year_code = 2 
elif year_last in { 3, 8, 14, 25, 31, 36, 42, 53, 54, 64, 70, 81, 87, 92, 98} : 
    year_code = 3 
elif year_last in { 9, 15, 20, 26, 37, 43, 48, 54, 65, 71, 76, 82, 93, 99} : 
    year_code = 4 
elif year_last in { 4, 10, 21, 27, 32, 38, 49, 55, 60, 66, 77, 83, 88, 94}:
    year_code = 5 
else : 
    year_code = 6 

#final formula
#days_code0 = year_code + day 
#days_code = days_code0 + month_code 
days_module = (day + month_code + year_code + century_real_code)% 7  

#final comparision to generate results
if days_module == 0 : 
    print( " Saturday ")
elif days_module == 1 :
    print("Sunday ")
elif days_module == 2 :
    print( "Monday ")
elif days_module == 3 :
    print("Tuesday ")
elif days_module == 4 :
    print( " Wendsday ")
elif days_module == 5 :
    print("Thursday ")
else : 
    print("Friday")
