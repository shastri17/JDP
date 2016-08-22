from faker import Factory

import random

import csv 

fake = Factory.create()

final_table = open('final_table.csv','w')

tabl = csv.writer(final_table)

tabl.writerow(['id','Major','Minor','Final Cgpa','Domain','Salary'])

for _ in range(0,10000):
       tabl.writerow([fake.random_int(),fake.job(),fake.job(),random.uniform(1.0,4),fake.job(),fake.random_int()*1000])

