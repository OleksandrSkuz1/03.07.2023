if __name__ == '__main__':


    # # Primitive Date
    # a = 1
    # b = a
    # b += 1
    # print(a, b)
    #
    # # Complex Date
    # c = [1]
    # d = c
    # d[0] += 1
    # print(c, d)
    #
    # # Complex Date
    # c = [1]
    # d = c.copy()
    # d[0] += 1
    # print(c, d)

   #  users = [
   #      {"name" : "John",
   #       "age" : 31
   #      },
   #      {"name" : "Jane",
   #       "age" : 27
   #      },
   #      {"name": "Jack",
   #       "age": 15
   #       },
   #      {"name": "Jack",
   #       "age": 15
   #       },
   #  ]
   # temp_age



    print("___ START PROGrAM ___ \n\n")
    system_metrics = input(f"Please choise system metrscs:\n"
                           f"c - Celsius\n"
                           f"f - Farengei\n"
                           f"k - Kalvin")
    temperature_value = int(input("Please input temperature value: "))
    # conditional temp

    if system_metrics.lower() == "c":
        print(f"INPUT VALUE: {temperature_value} C\n\n")
        print(f"Kalvin: {temperature_value + 273.75}")
        print(f"Farengeit: {temperature_value * (9/5) + 32}")
    elif system_metrics.lower() == "f":
        print(f"INPUT VALUE: {temperature_value} F\n\n")
        print(f"Kalvin: {temperature_value + 273.75}")
        print(f"Farengeit: {temperature_value * (9 / 5) + 32}")
    else:
        print("CALC SELF!")

