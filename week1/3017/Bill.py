"""Calculates the total bill"""
price = int(input())
service_charge = (10/100)*price
if service_charge < 50:
    service_charge = 50
elif service_charge > 1000:
    service_charge = 1000
vat = (7/100)*(service_charge+price)
total_price = vat+price+service_charge
print(f"{total_price:.2f}")
