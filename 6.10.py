print('Задание 6.10.1')
class Figure:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def describe_figure(self):
        sides = self.x, self.y, self.width, self.height
        return str(sides)

print('Трапеция')
trapeze = Figure(10, 20, 10, 20)
print(trapeze.describe_figure())

print('Квадрат')
square = Figure(5, 5, 5, 5)
print(square.describe_figure())

print('Параллелограм')
parallelogram = Figure(6, 8, 7, 9)
print(parallelogram.describe_figure())

print('Задание 6.10.2')
class Rectangle:

    def __init__(self, lenght, height):
        self.lenght = lenght
        self.height = height

    def rect_sides(self):
        sides = self.lenght, self.height
        return sides

rect_1 = Rectangle(10, 5)
print(rect_1.rect_sides())

print('Задание 6.10.3')
class OnlineWallet:

    def __init__(self, client, balance):
        self.client = client
        self.balance = balance

    def data_client(self):
        print(f'Клиент "{self.client.title()}".Баланс: {self.balance} руб.')

client_1 = OnlineWallet('Монти Пайтон' , 1000)
client_1.data_client()

print('Задание 6.10.4')
class GuestList:

    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status

    def describe_guest(self):
        full_name = (f'{self.name.title()}, г.{self.city.title()}, статус "{self.status.title()}"')
        return full_name

guest_1 = GuestList('геральт', 'ривия', 'ведьмак')
print(guest_1.describe_guest())