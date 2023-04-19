import random


class game_manager():

    def __init__(self):
        self.color_lst = ["r", "g", "b", "p", "y", "o"]
        self.secret_code = []
        self.guess_lst = []
        self.count = 0

    def codeMaker(self):
        for i in range(4):
            random_num = random.randint(0,5)
            self.secret_code.append(self.color_lst[random_num])
            #print(f" secret code:{self.secret_code}")

    def request_guess(self):
        self.guess_lst = []
        for i in range(4):
            color = input(f"guess the number {i + 1} color ( r - red, g - green, b - blue,p -perple,y -yellow, 0 -orange)")
            self.guess_lst.append(color)
            print(f" guess_lst:{self.guess_lst}")

    def check_col_loc(self):
        pin_box = []

        for i in range(len(self.guess_lst)):
            if self.guess_lst[i] == self.secret_code[i]:
                print(f"i:{i}")
                pin_box.append("red pin")

            elif self.guess_lst[i] in self.secret_code:
                pin_box.append("white pin")



        print(pin_box)

    def count_guess(self):
        self.count += 1
        print(self.count)
        if self.count > 10:
            print(f"game ended you lost the code was {self.secret_code}")
            return True

    def win(self):
        if self.guess_lst == self.secret_code:
            print("you won, great job")
            return True

manager = game_manager()
def game_loop():
    while True:
        manager.request_guess()
        manager.check_col_loc()
        if manager.count_guess() or manager.win():
            break

def main():
    the_code = manager.codeMaker()
    game_loop()

if __name__ == '__main__':
    main()