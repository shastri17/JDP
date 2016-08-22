from faker.factory import Factory
import csv

def writeTo_csv(fake):
	with open ('test.csv','wb') as csvfile:
		write_to_csv = csv.writer(csvfile,delimiter = ' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		write_to_csv.writerow(['NAME'])
		firstname1="first_name"
		firstnameList=[(firstname1,getattr(fake,firstname1)())]
		print "%s = %s" %(firstname1,getattr(fake,firstname1)())
		print firstnameList
		write_to_csv.writerow((firstnameList[0][1]))
 		write_to_csv.writerow(['ssn'])
       		ssn1="ssn"
       		ssnList=[(ssn1,getattr(fake,ssn1)())]
           	print "%s = %s" %(ssn1,getattr(fake,ssn1)())
              	print ssnList
         	write_to_csv.writerow((ssnList[0][1]))
		
if __name__=="__main__":
	fake = Factory.create('en_GB')
	writeTo_csv(fake) 
