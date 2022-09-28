# задание 136
dict = {"one" : "1",
       "один" : "1",
        
        "two" : "2",
        "два" : "2",
        
        "three" : "3",
        "три" : "3",
        "tres" : "3"
    }


print( [key for key in dict if dict[key] == "1"])
print( [key for key in dict if dict[key] == "2"])
print( [key for key in dict if dict[key] == "3"])




