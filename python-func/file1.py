def greeting():
    person1 = {
        "name": "John",
        "age": 36,
        "country": "Norway"
    }

    person2 = {
        "name": "Vadim",
        "age": 8,
        "country": "Israel"
    }

    print("Person 1:")
    for key, value in person1.items():
        print(f"{key.capitalize()}: {value}")

    print("\nPerson 2:")
    for key, value in person2.items():
        print(f"{key.capitalize()}: {value}")

greeting()
