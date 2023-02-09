import random

color_lst = ["red","green","blue","perple","yellow","orange"]

def codeMaker(colors):
    code = []
    for i in range(4):
        random_num = random.randint(0,5)
        code.append(colors[random_num])
    print(code)
    return code
def request_guess():
    guess_lst = []
    for i in range(4):
        color = input(f"guess the number {i + 1} color (red,green,blue,perple,yellow,orange)")
        guess_lst.append(color)
    return guess_lst
def check_col_loc(guess_lst,code_lst):
    pin_box = []
    for i in guess_lst:
        for j in code_lst:
            try:
                if guess_lst.index(i,0,5) == code_lst.index(i,0,5):
                    pin_box.append("red pin")
                elif i == j:
                    pin_box.append("white pin")
            except:
                pass
    print(pin_box)

def count_guess():
    pass

def game_loop(code):
    while True:
        check_col_loc(request_guess(),code)
        count_guess()

def main():
    the_code = codeMaker(color_lst)
    game_loop(the_code)

if __name__ == '__main__':
    main()