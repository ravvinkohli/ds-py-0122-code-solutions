record = (1, "Grimdiana", "Bones", "boulders")
row = ""
for x in record:
  print(x)
for x in record:
  for y in row:
    print(x , "," , y)
values_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
for x in range(len(values_list)):
  print(values_list[x])
index_list = []
for x in values_list:
  for y in index_list:
    print(x , y)
for x in index_list:
  print(x)
vowels = {"A", "E", "I", "O", "U"}
parts_of_the_big_letter = {"L", "M", "N", "O", "P"}
for x in vowels:
  print(x)
print(parts_of_the_big_letter.difference(vowels))
player_position = {"Who": "1B" , "What": "2B" , "I Don't Know": "3B", "Why": "LF", "Because": "CF", "Tomorrow": "P", "Today": "C" , "I Don't Care": "SS"}
players = [""]
for x in player_position:
  for y in players:
    print(x , y)
positions = {""}
for x in player_position:
  for y in positions:
    print(x , y)
for x in player_position:
  for y in positions:
    print(x , "is on" , y)
