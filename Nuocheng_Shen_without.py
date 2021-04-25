print("Input the year you want to check if the year is a leap year")
years = int(input("Enter the year:"))

divisible_4 = years%4

if divisible_4 == 0:
    
    divisible_100 = years%100
    
    if divisible_100 == 0:
        
        divisible_400 = years%400
        
        if divisible_400 == 0:
            print(years, "is leap year")
        else:
            print(years, "is not leap year")
    
    else:
        print(years, "is leap year")
    
else:
    print(years, "is not leap year")