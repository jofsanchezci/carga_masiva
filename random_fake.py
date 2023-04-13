from faker import Faker
from faker.providers import bank, company, internet, person
fake=Faker('es_CO')
fake.add_provider(bank)
fake.add_provider(company)
fake.add_provider(internet)
fake.add_provider(person)
for n in range(5):
	#print(fake.name())
	#print(fake.address())
	#print(fake.text())
	#print(fake.bban())
	#print(fake.first_name())
	print(fake.company())
