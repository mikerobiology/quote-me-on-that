# Needs Cat#, Item Desc, Vendor, Quote, Exp Dat

prompt = '> '

print "This will add a new quote to the spreadsheet."

print "What is the Catalog Number?"
catnumb = raw_input(prompt)

print "What is the Item Description?"
itdesc = raw_input(prompt)

print "Who is the Vendor?"
vendor = raw_input(prompt)

print "What is the Quote?"
quote = raw_input(prompt)

print "What is the List Price of the item?"
list_price = raw_input(prompt)

print "What is the Discounted Amount?"
discount = raw_input(prompt)

print "What is the Net Price?"
net_price = raw_input(prompt)

print "When is the Expiration Date(DD/MM/YY)?"
expdate = raw_input(prompt)

print "Here is the quote you have entered."
print "Catalog Number: %r" % catnumb
print "Item Description: %r" % itdesc
print "Vendor: %r" % vendor
print "Quote: %r" % quote
print "List Price: %r" % list_price
print "Discount: %r" % discount
print "Net Price: %r" % net_price
print "Expiration Date: %r" % expdate

print "Does this look right?  Enter Y or N."
answer = raw_input(prompt)
if answer == "y" or answer == "Y":
	print("Adding to the spreadsheet...")

# Need a 'while loop' if want this to return to top is answer "N/n"
