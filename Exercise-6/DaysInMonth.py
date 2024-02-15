#greetings
print("!!  Welcome  !!")

def leaf_year(year):
    if(not year%4):
        if(not year%100):
            if(not year%400):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year = int(input("Please provide year\n"))
month = int(input("Please provide which number of month (january as 1)\n"))
days = [31,28,31,30,31,30,31,31,30,31,30,31]
if(leaf_year(year)==True):
     if(month==2):
         temp = days[month-1]
         temp +=1
         print(f"Their are {temp} number of days in {month} month of {year} year")
     else:
         print(f"Their are {days[month-1]} number of days in {month} month of {year} year")
else:
    print(f"Their are {days[month-1]} number of days in {month} month of {year} year")
