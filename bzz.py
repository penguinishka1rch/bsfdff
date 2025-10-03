def get_age(u_name):
    try:
        print(f"{u_name}, скажи какой у тебя возраст?")
        u_age = int(input("Введите свой возраст:"))
        return u_age
    except:
        print("Некоретные данные ведите возраст еще раз")
        get_age()
        return False

def get_type():
    try:
        u_type = input("А какая у тебя профелизация (dragon,mage,warrior): ")       
        if not(u_type == "dragon" or u_type == "mage" or u_type == "warrior"):
             get_type()
             return False
        return u_type
    except:
        print("Некоретные данные ведите возраст еще раз")
        get_type()
        return False

def get_person():
    u_name = ""
    u_age = 0
    u_health = 0
    u_dmg = 0
    u_type = ""
    print("Привет, герой, как твое имя? ")
    u_name = input("Введиете имя: ")
    # Получить возраст
    u_age = get_age(u_name)
    print(f"{u_name}, да ты стар уже в {u_age} лет!")
    # Получить проффессию
    u_type = get_type()

    if u_type == "dragon":
        print(f"{u_name}, ты совсем не похож на дракона.")
    elif u_type == "mage":
        print(f"{u_name}, неплохой посох.")
    elif u_type == "warrior":
            print(f"{u_name}, был у нас один славный герой, так его дракон проглотил,надеюсь с тобай такого не произойдет.")
            
    return {
        "name": u_name,
        "age": u_age,
        "profesion": u_type,
        "health": u_health,
        "damage": u_dmg
    }
            
     
person = get_person()
print(person)

msg = f"""
{"Имя:":-<10}{person['name']:->40}
{"возраст:":-<10}{person['age']:->40}
"""
print(msg)






