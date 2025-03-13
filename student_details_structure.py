student1 = {
  "first_name": "Serhat",
  "last_name": "Kalkan",
  "index_number": "35522",
  "nationality": "Turkish",
  "starting_date": "2025-03-01",
  "courses": ["Object Oriented Programming","Basics of Telecomunication","Mathematics"]
}

print(f"First Name: 
{student1['first_name']}")
print(f"Last Name: 
{student1['last_name']}")
print(f"Index Number: 
{student1['index_number']}")
print(f"Nationality: 
{student1['nationality']}")
print(f"Starting Date: 
{student1['starting_date']}")
print(f"Courses:{', 
'.join(student1['courses'])}")
