from faker import Factory
import csv as csv
fake = Factory.create()
project_table = open('project_table.csv','w')
p = csv.writer(project_table)
p.writerow(['s_id','Project','ProjectDomain','EventualDomain'])
for _ in range(0,10000):
	p.writerow([fake.random_int(),fake.job(),fake.job(),fake.job()])
