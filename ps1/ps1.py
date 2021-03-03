annualsal = float(input("Annual salary = "))
monthlysal = annualsal/12

totalcost = float(input("Total cost = "))
totaldp = (totalcost*.25)

portion = float(input("Portion = "))
 
savings = 0
counter = 0

while savings < totaldp:
    savings = (savings + (savings*0.4)/12 + monthlysal*portion)
    counter += 1

print(f' months {counter}')