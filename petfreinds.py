from const_cat import Animal

cats = [
    {
        "name": "Барон",
        "age": "2",
        "gender":"Мальчик"
    },
    {
        "name": "Сэм",
        "age": "2",
        "gender":"Мальчик"
    }
]
for item in cats:
    cat_item = Animal(name=item.get("name"),
                      age=item.get("age"),
                      gender=item.get("gender"))
    print(f"Возраст: {cat_item.getAge()} года,\nИмя: {cat_item.getName()},\nПол: {cat_item.getGender()}")