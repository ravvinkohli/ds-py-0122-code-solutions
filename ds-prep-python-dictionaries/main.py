person = {"first_name": "Ravleen" , "last_name": "Kaur" , "hobby": "Dancing"}
print(person)
first_name = person["first_name"]
last_name = person.get("last_name")
middle_name = person.get("middle_name")
print(first_name , middle_name , last_name)
person["job"] = "Scientist"
print(person["job"])
person["hobby"] = "Singing"
print(person["hobby"])
person.pop("last_name")
print(person)
