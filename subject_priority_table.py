from faker import Factory
import csv as csv
fake = Factory.create()
subject_priority_table = open('subject_priority_table.csv','w')
s =csv.writer(subject_priority_table)
s.writerow(["Subject","CreditValues"])
for _ in range(0,10000):
	s.writerow([fake.job(),fake.random_letter()])



	
	