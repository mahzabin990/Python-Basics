house = {
	      "rent": [34000, 32000, 50000, 22000, 24000, 27000],
	      "house area": [1350, 1300, 1600, 1000, 1200, 1250],
	      "number of bed rooms": [3, 3, 4, 2, 3, 3],
	      "number of wash rooms": [2, 2, 4, 2, 2, 2],
	      "number of varenda": [3, 3, 4, 1, 2, 3]
        }
min1 = house['rent'][0]
for i in range(len(house['rent'])) :
    if house['rent'][i] < min1 : # If the other element is min than first element
      min1 = house['rent'][i]
min2 = house['house area'][0]
for i in range(len(house['house area'])) :
    if house['house area'][i] < min2 : # If the other element is min than first element
      min2 = house['house area'][i]
min3 = house['number of bed rooms'][0]
for i in range(len(house['number of bed rooms'])) :
    if house['number of bed rooms'][i] < min3 : # If the other element is min than first element
      min3 = house['number of bed rooms'][i]
min4 = house['number of wash rooms'][0]
for i in range(len(house['number of wash rooms'])) :
    if house['number of wash rooms'][i] < min4 : # If the other element is min than first element
      min4 = house['number of wash rooms'][i]
min5 = house['number of varenda'][0]
for i in range(len(house['number of varenda'])) :
    if house['number of varenda'][i] < min5 : # If the other element is min than first element
      min5 = house['number of varenda'][i] 

output = {
	"rent": min1,
	"house area": min2,
	"number of bed rooms": min3,
	"number of wash rooms": min4,
	"number of varenda": min5
}

print(output)




    

     