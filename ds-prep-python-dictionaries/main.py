from sys import set_coroutine_origin_tracking_depth


person = {"first_name": "Ravleen" , "last_name": "Kaur" , "hobby": "Dancing"}
print(person)
print(person["first_name"])
first_name = person["first_name"]
print(first_name)
x = person.get("last_name")
print(x)
last_name = person.get("last_name")
print(last_name)
x = person.get("middle_name")
print(x)
middle_name = person.get("middle_name")
print(middle_name)
print(person["first_name"] , ["middle_name"] , ["last_name"])
person["job"] = "Scientist"
print(person)
person["hobby"] = "Singing"
print(person["hobby"])
person.pop("last_name")
print(person)
