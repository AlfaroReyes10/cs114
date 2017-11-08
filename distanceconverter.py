print("This is a distance units converter")
print("Enter the ammount you want to convert")
units = int(input())
print("Is this mi,km,ft or m ?)
origin = input()
print("What to convert to? Enter mi for miles or km for kilometers,Enter ft for feet or m for meters.")
target = input()


# print("Enter A Distance")
# input()
# print("Enter Target Units")
# input()
# miles =
# conversion_factor = 0.62137119
#
# kilometers = miles / conversion_factor
# print (kilometers)

if origin == 'mi':
    output = units * 1.609
elif origin == 'km':
    output = units * .621371

if target == 'mi':
    print(units, " km equals", output, " mi")
elif target == 'km':
    print(units, " mi equals", output, " km")

if origin == 'ft':
    output = units * 0.3048
elif origin == 'm':
    output = units * 3.2808

if target == 'ft':
    
# mi = km * .621371
#
# km = mi * 1.609
