house = {
	      "rent": [34000, 32000, 50000, 22000, 24000, 27000],
	      "house area": [1350, 1300, 1600, 1000, 1200, 1250],
	      "number of bed rooms": [3, 3, 4, 2, 3, 3],
	      "number of wash rooms": [2, 2, 4, 2, 2, 2],
	      "number of varenda": [3, 3, 4, 1, 2, 3]
        }

output = {}

for key in house:
    current_min = house[key][0]
    for i in house[key][1:]:
        if i < current_min:
            current_min = i
    output[key] = current_min
        

print(output)




    

     