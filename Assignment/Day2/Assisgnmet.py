Products = [
    {
        "pid": "1",
        "name": "Asus1",
        "cost": 15000,
        "brand": "Asus",
        "rating": 4,
        "discount": 10,
        "category": "Laptop"
    },
    {
        "pid": "2",
        "name": "Hp1",
        "cost": 60000,
        "brand": "Hp",
        "rating": 4.5,
        "discount": 12,
        "category": "Laptop"
    },
    {
        "pid": "3",
        "name": "Lenovo1",
        "cost": 40000,
        "brand": "Lenovo",
        "rating": 4.2,
        "discount": 14,
        "category": "Laptop"
    },
    {
        "pid": "4",
        "name": "Asus2",
        "cost": 50000,
        "brand": "Asus",
        "rating": 4.4,
        "discount": 11,
        "category": "Laptop"
    },
    {
        "pid": "5",
        "name": "Hp2",
        "cost": 25000,
        "brand": "Hp",
        "rating": 4.5,
        "discount": 17,
        "category": "Laptop"
    },
    {
        "pid": "6",
        "name": "Lenovo2",
        "cost": 100000,
        "brand": "Lenovo",
        "rating": 4.7,
        "discount": 7,
        "category": "Laptop"
    }
]

choice = 0
while choice != 6:

    print("\nEnter 1 to sort by cost (Low to High)\nEnter 2 to sort by cost (High to Low)\n"
          "Enter 3 to sort by Rating\n"
          "Enter 4 to sort by discount (Low to High)\n"
          "Enter 5 to sort by discount (High to Low)\n"
          "Enter 6 to Exit\n")
    choice = int(input("Enter value: "))
    if choice == 6:
        print("Bye!!")
    else:
        fields = {
            1: ['cost', False],
            2: ['cost', True],
            3: ['rating', True],
            4: ['discount', False],
            5: ['discount', True]
        }
        Products.sort(key=lambda el: el[fields[choice][0]], reverse=fields[choice][1])
        print(Products)



    # elif choice == 2:
    #     Products.sort(key=lambda el: el['cost'], reverse=True)
    #     print(Products)
    # elif choice == 3:
    #     # Sort by Rating
    #     Products.sort(key=lambda el: el['rating'], reverse=True)
    #     print(Products)
    # elif choice == 4:
    #     # Sort by Discount L to H
    #     Products.sort(key=lambda el: el['discount'])
    #     print(Products)
    # elif choice == 5:
    #     # Sort by Discount H to L
    #     Products.sort(key=lambda el: el['discount'], reverse=True)
    #     print(Products)