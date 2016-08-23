# JDP
from faker import Factory
random = open("random.csv","w")
fake = Factory.create()
for _ in range(0,10000):
	random.write(fake.ean13())
	random.write(fake.random_letter())

	
	
