from faker import Factory
import csv as csv
from faker.providers import BaseProvider
fake = Factory.create()
def num(self):
	return fake.random_int()%5
class MyProvider(BaseProvider):
	def domain(self):
		x=num()
		if (x==1):
			return 'comp science'
		if (x==0):
			return 'data'
		if (x==2):
			return 'software'
	def paper(self):
		x=num()
		if (x==1):
			return 'algorithm'
		if (x==2):
			return 'management'
		if (x==3):
			return 'ML'
		if (x==4):
			return 'data structure'
		if (x==0):
			return 'IP'
fake.add_provider(MyProvider)
paper = open('paper.csv','w')
p = csv.writer(paper)
p.writerow(['s_id','paper','paperDomain','EventualDomain'])
for _ in range(0,100):
	p.writerow([fake.random_int(),fake.paper(),fake.domain(),fake.job()])
