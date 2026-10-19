weather = (1,1,0,0,1,0,1)
hot_weather = 0
rainy_weather = 0

for i in range (0,7):
    if weather [i] == 0:
        rainy_weather += 1
    else:
        hot_weather += 1

if hot_weather > rainy_weather:
    print ("Hot weather.")
else:
    print ("Rainy weather")