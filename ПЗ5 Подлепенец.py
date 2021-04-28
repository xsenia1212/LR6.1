
storage = [
        {'model': 'LG', 'price': 1000, 'condition': "OFF"},
        {'model': 'Samsung', 'price': 2000, 'condition': "ON"},
        {'model': 'Smart', 'price': 3500, 'condition': "ON"},
    ]

class TV:
    model = "LG"
    price = 1000
    condition = True

    def get_model(self):
        print(self.model)

    def get_price(self):
        print(self.price)

    def get_condition(self):
        print(self.condition)

class manager:
    name = "Иванов Иван Иванович"
    position = "Главный менеджер"

    def get_name(self):
        print(self.name)

    def get_position(self):
        print(self.position)

    def showtv(self, show):
        self.show = show

    def saletv(self):
        if(self.condition)
            print("Хотите купить этот телевизор?")
        else:
            print("К сожалению, телевизор сломан")

class customer:
    name = "Сидоров Николай Семенович"

    def get_name(self):
        print(self.name)

    def chosetv(self, chose):
        self.chose = chose


