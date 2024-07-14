import random
temperatures = []
good_days = []
for temp in range(7):
	temperatures.append(random.randint(26,40))

days_of_the_week = ["Sunday" , "Monday" , "Tuesday" , "Wednesday"
 ,"Thursday" , "Friday", "Saturday"]

highest_temp = 26
lowest_temp = 40
highest_temp_day = ""
lowest_temp_day = ""
for number in temperatures:
	indexNumber = temperatures.index(number)
	day = days_of_the_week[indexNumber]
	if number%2 == 0:
		print(day)
		good_days.append(day)

	if number > highest_temp:
		highest_temp = number
	elif number < lowest_temp:
		lowest_temp = number

indexNumber = temperatures.index(highest_temp)
highest_temp_day = days_of_the_week[indexNumber]

indexNumber = temperatures.index(lowest_temp)
lowest_temp_day = days_of_the_week[indexNumber]

allTemp = 0
for x in temperatures:
	 allTemp += x

avarageTemp = allTemp/7
above_avg = []
above_avg_days = []
for y in temperatures: 
	if avarageTemp < y:

		above_avg.append(y)
		indexnum = temperatures.index(y)
		above_avg_days = days_of_the_week[indexnum]


for e in range(7):
	print(f"{days_of_the_week[e]}: {temperatures[e]}")

print(f"\n \nShelly had {len(good_days)} good days")
print(f"\n\nThe hottest temperature was: {highest_temp} on {highest_temp_day}")
print(f"The coldest temperature was: {lowest_temp} on {lowest_temp_day}")
print(f"\n\nThe avarage temperature was: {avarageTemp}")
print(f"The days with above avarage temperature were:{above_avg_days}")



