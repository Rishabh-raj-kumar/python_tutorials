#list comprehension -> way to create a new list with less syntax..
#[print,condition(opt),for loop]

lists = [i * i for i in range(1,11)]
print(lists)
check = [i if i>=60 else "Foil" for i in lists]
print(check)

#dictionary comprehension -> {key : expression for(key,value) in iterable}

dicti = {"new":10,"few":50,"pew":80,"chew":40}

citi_in = {key : () for (key,value) in dicti.items()}
print(citi_in)

def check_Temp(value):
    if value>=70:
        return "HOT"
    elif value<=69 and value>=40:
        return "WARM"
    else:
        return "COLD"

cities = {"new":60,"few":40,"pew":38,"chew":69,"mew":90};

citi_of = {key : check_Temp(value) for (key,value) in cities.items()}
print(citi_of)