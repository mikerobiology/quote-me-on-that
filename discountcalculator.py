from decimal import Decimal

prompt = '> '

print "Enter the price."
price = raw_input(prompt)

print "Enter the discount(percentage)."
discount_percent = raw_input(prompt)

print "Here is the net cost after discount."
discount = float(discount_percent)*float(price) / 100
net_price = float(price) - float(discount)
print ("%.2f" % net_price)

# Unable to do this live in django admin.
# Need JQuery or JaveScript to implement.