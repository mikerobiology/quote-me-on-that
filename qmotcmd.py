# Needs Cat#, Item Desc, Vendor, Quote, Exp Dat

prompt = '> '

print "What is the Catalog Number?"
catnumb = raw_input(prompt)

print "What is the Item Description?"
itdesc = raw_input(prompt)

print "Who is the Vendor?"
vendor = raw_input(prompt)

print "What is the Quote?"
quote = raw_input(prompt)

print "When is the Expiration Date(DD/MM/YY)?"
expdate = raw_input(prompt)

print "So the %r %r from %r has the quote '%r' until %r?" % (catnumb,
  itdesc, vendor, quote, expdate)

answer = raw_input("Does this look right?  Enter Y or N.")
if answer == "y" or answer == "Y":
	print("Adding to the spreadsheet...")
else # NEED A "WHILE LOOP" TO RETURN TO TOP IF "NO"

