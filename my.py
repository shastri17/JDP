#run this code you get the idea!!
from faker import Factory
random = open("random.csv","w")
fake = Factory.create()
stuff = ["name", "address","city","state"]
for _ in range(0,10):
   for item in stuff:
     print "%s = %s" % (item, getattr(fake, item)())
 
	
	