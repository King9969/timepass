"""
def is_leap(y):
    if y%4==0 and y%100==0:
        print("False")
    elif y%4==0:
        print("True")
    else:
        print("False")

year = int(input("x"))
is_leap(year)

"""

# functions way
def is_leap(year):
    leap = False
    if year%4==0 and year%100==0 and year%400!=0:
        return False
    elif year%4==0:
        return True

    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))
