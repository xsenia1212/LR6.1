class Tekhnica:
    def __init__(self, Model, Workstate, Price):
        self.Model = Model
        self.Workstate = Workstate
        self.Price = Price

    def get_Model(self):
        print(self.Model)

    def get_Workstate(self):
        print(self.Workstate)

    def get_Price(self):
        print(self.Price)


class TV(Tekhnica):
    def __init__(self, Model, Workstate, Price, size, resolution):
        Tekhnica.__init__(Model, Workstate, Price)
        self.size = size
        self.resolution = resolution
        TVs.append(self.Model)

    def turn_on(self, manager, customer):
        if (self.Workstate == 'working'):
            print('Телевизор работает')
            manager.sell(self, self.Model, customer)
        else:
            print('Телевизор не работает')
            manager.reject(self, self.Model, customer)


class Laptop(Tekhnica):
    def __init__(self, Model, Workstate, Price, size, resolution):
        Tekhnica.__init__(Model, Workstate, Price)
        self.size = size
        self.resolution = resolution
        Laptop.append(self.Model)

    def turn_on(self, Manager, customer):
        if (self.Workstate == 'working'):
            print('Ноутбук работает')
            Manager.sell(self.Model, customer)
        else:
            print('Ноутбук не работает')
            Manager.reject(self.Model, customer)


class Monitor(Tekhnica):
    def __init__(self, Model, Workstate, Price, size, resolution):
        Tekhnica.__init__(Model, Workstate, Price)
        self.size = size
        self.resolution = resolution
        Monitors.append(self.Model)

    def turn_on(self, Manager, customer):
        if (self.Workstate == 'working'):
            print('Монитор работает')
            Manager.sell(self.Model, customer)
        else:
            print('Монитор не работает')
            Manager.reject(self.Model, customer)


class Printer(Tekhnica):
    def __init__(self, Model, Workstate, Price, colors, dpi):
        Tekhnica.__init__(Model, Workstate, Price)
        self.colors = colors
        self.dpi = dpi
        Printers.append(self.Model)

    def turn_on(self, Manager, customer):
        if (self.Workstate == 'working'):
            print('Принтер работает')
            Manager.sell(self.Model, customer)
        else:
            print('Принтер не работает')
            Manager.reject(self.Model, customer)


class Microwave(Tekhnica):
    def __init__(self, Model, Workstate, Price, Power, Max_Timer):
        Tekhnica.__init__(Model, Workstate, Price)
        self.Power = Power
        self.Max_Timer = Max_Timer
        Microwaves.append(self.Model)

    def turn_on(self, Manager, customer):
        if (self.Workstate == 'working'):
            print('Монитор работает')
            Manager.sell(self.Model, customer)
        else:
            print('Монитор не работает')
            Manager.reject(self.Model, customer)

class Worker:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_name(self):
        print(self.name)

    def get_position(self):
        print(self.position)


class Manager(Worker):
     def __init__(self, name, position):
        Worker.__init__(name, position)
        Managers.append(self.name)

    def check(self, Tekhnica, customer):
        Tekhnica.turn_on(customer)

    def sell(self, Model, customer):
        print('Товар ', Model, ' исправен, будете брать?')
        customer.buy()

    def reject(self, Model, customer):
        print('Товар ', Model, ' снят с продажи из-за неисправности')
        customer.reject()


class Cashier(Worker):
    def __init__(self, name, position):
        super().__init__(name, position)
        Cashiers.append(self.name)

    def sell(self, Model, customer):
        print('*Пробивает товар ', Model, '*')
        customer.buy()
        self.receipt()


class Manager(Worker):
    def __init__(self, name, position):
        Worker.__init__(name, position)
        Managers.append(self.name)

    def check(self, Tekhnica, customer):
        Tekhnica.turn_on(customer)

    def sell(self, Model, customer):
        print('Товар ', Model, ' исправен, будете брать?')
        customer.buy()

    def reject(self, Model, customer):
        print('Товар ', Model, ' снят с продажи из-за неисправности')
        customer.reject()


class customer:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    def chosetv(self, chose):
        self.chose = chose

    def buy(self):
        print("Я покупаю этот телевизор")

    def reject(self):
        print("Давайте посмотрим другую модель")

TVs = []
Managers = []
Monitors = []
Notebooks = []
Printers = []
Microwaves = []
Cashiers = []

storage = [
        {'model': 'LG', 'price': 1000, 'condition': "OFF"},
        {'model': 'Samsung', 'price': 2000, 'condition': "ON"},
        {'model': 'Smart', 'price': 3500, 'condition': "ON"},
    ]

