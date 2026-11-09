def ft_water_reminder():
    if (int(input("Days since last watering: ")) <= 2):
        print("Plants are fine")
    else:
        print("Water the plants!")
