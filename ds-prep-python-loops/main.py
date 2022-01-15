record = (1, "Grimdiana", "Bones", "boulders")
row = ""
for x in record:
  print(x)
for x in record:
  row = row + str(x) + ","
print(row)
values_list = [1, 1, 2, 3, 5, 8, 13, 21, 34]
for x in values_list:
  print(x)
index_list = []
for x in range(len(values_list)):
  index_list.insert(0 , x)
print(index_list)
for x in index_list:
  if x % 2 != 0:
    values_list.pop(x)
print(values_list)
vowels = {"A", "E", "I", "O", "U"}
parts_of_the_big_letter = {"L", "M", "N", "O", "P"}
for x in vowels:
  print(parts_of_the_big_letter.discard(x))
player_position = {"Who": "1B" , "What": "2B" , "I Don't Know": "3B", "Why": "LF", "Because": "CF", "Tomorrow": "P", "Today": "C" , "I Don't Care": "SS"}
players = [""]
for x in player_position.keys():
  players.append(x)
print(players)
positions = [""]
for x in player_position.values():
  positions.append(x)
print(positions)
for x , y in player_position.items():
  print(x , "is on" , y)
