import random


class User:

    def __init__(self,name, money):
        self.name = name
        self.money = money
        if money < 0:
            raise Exception("The amount of money can`t be a negative number")

    def play(self,money,casino):
        game_machine_number = random.randint(0, len(casino.game_machines)-1)
        self.money -= money
        if self.money < 0:
            raise Exception("There is not enough money to play!")

        casino.game_machines[game_machine_number].play(money)



class Casino:

    def __init__(self,name):
        self.name = name
        self.game_machines = []

    def getMoney(self):
        sum = 0
        for i in self.game_machines:
            sum += i.number
        return sum

    def GetMachineCount(self):

        return len(self.game_machines)




class SuperAdmin(User):
    def __init__(self, name, money):
        super().__init__(name, money)
        self.casinos = []


    def NewCasino (self, casino_name):

        self.casinos.append(Casino(casino_name))
        return Casino(casino_name)


    def NewGameMachine(self, number, casino):

        self.money -= number
        if self.money < 0:
            raise Exception(" There is a lack of money to set up a new Game Machine!")

        casino.game_machines.append(GameMachine(number))



    def GetMoney(self,number,casino):

        sorted_list = sorted(casino.game_machines, key = lambda machine: machine.number, reverse=True)
        current_number = number

        sum = 0
        for x in sorted_list:
            sum += x.number

        if sum < number:
            raise Exception ("There is no such amount of money! ")

        for i in sorted_list:
            new_number = i.number - current_number
            if new_number < 0:
                i.number = 0
                current_number = - new_number
                continue

            elif new_number >= 0:
                i.number -= current_number
                return number


    def AddMoney(self,number,casino,game_machine_number):

        self.money -= number

        if self.money < 0:
            raise Exception(" You don`t have such amount of money! ")

        casino.game_machines[game_machine_number].number += number



    def DeleteGameMachine(self,casino,game_machine_number):

        if game_machine_number >  len(casino.game_machines)-1:
            raise Exception(" This game machine doesn`t exist ")

        money = casino.game_machines[game_machine_number].number / (len(casino.game_machines) - 1)
        del casino.game_machines[game_machine_number]

        for i in casino.game_machines:
            i.number += money





class GameMachine:

    def __init__(self,number):

        self.number = number

    def get_number(self):
        return self.number

    def get_money(self,number):
        self.number -= number

        if self.number < 0:
            raise Exception(" There is no such amount of money!")

        return number

    def put_money(self,number):
        self.number += number


    def play(self,number):

        self.number += number

        rand = str(random.randint(100, 999))
        similar = 1
        for i in range(len(rand)-1):
            for j in range(i,len(rand)-1):
                if rand[i] == rand [j+1]:
                    similar +=1

        if similar > 1:
            number *= similar
            self.number -= number
            return number

        else:
            return 0




person1 = SuperAdmin("Nata",2000)
casino1 = person1.NewCasino("CASINO")
person1.NewGameMachine(200,casino1)
person1.NewGameMachine(300,casino1)
person1.NewGameMachine(100,casino1)
person1.DeleteGameMachine(casino1,1)

casino2 = person1.NewCasino("Fanta")
person1.NewGameMachine(100,casino2)
person1.NewGameMachine(300,casino2)
person1.NewGameMachine(200,casino2)


person2 = User("Peter", 200)
person2.play(100,casino1)



