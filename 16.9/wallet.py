# 16.9.3
# электронный кошелек для Дома питомца
# Вам нужно написать программу, обрабатывающую данные, и на выходе в консоль получить следующее: Клиент "Иван Петров". Баланс: 50 руб.
class Clients:
    def __init__(self, name, surname, balance):
        self.name = name
        self.surname = surname
        self.balance = balance
    
    # метод вывода информации
    def get_info(self):
        return f'Клиент "{self.name} {self.surname}". Баланс: {self.balance} руб.'
        
        
client_1 = Clients('Иван','Петров', 125)
client_2 = Clients('Федор','Коршунов', 500)

print(client_1.get_info())
print(client_2.get_info())