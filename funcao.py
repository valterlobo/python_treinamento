
def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print ("With tax: %f" % bill)
    return bill
	

bill = 	100.89
tax = tax(bill)
print (tax)



fin = open("data.py")
print ("----------------INICIO---------------")
for  line in fin:
    print (line)

print ("----------------FIM---------------")
fin.close()
