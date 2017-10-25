print("Here is your change")
total = int(input())
quarter_value = 25
dimes_value = 10
nickles_value = 5
pennies_value = 1
num_quarters = total//quarter_value
total -= (num_quarters * 25)
num_dimes = total // dimes_value
total -= (num_dimes * 10)
num_nickles = total // nickles_value
total -= (num_nickles * 5)
num_pennies = total // pennies_value
total -= (num_pennies * 1)
print('quarters', num_quarters)
print('dimes', num_dimes)
print('nickles', num_nickles)
print('pennies', num_pennies)
