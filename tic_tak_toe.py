def sum(a,b,c):
    return (a + b + c)
#-------------------------------------------------now here we stat the function 
def print_Board(Xstate,Zstate):
    zero = 'X' if Xstate[0] else ('O' if Zstate[0] else 0)
    one = 'X' if Xstate[1] else ('O' if Zstate[1] else 1)
    two = 'X' if Xstate[2] else ('O' if Zstate[2] else 2)
    three = 'X' if Xstate[3] else ('O' if Zstate[3] else 3)
    four = 'X' if Xstate[4] else ('O' if Zstate[4] else 4)
    five = 'X' if Xstate[5] else ('O' if Zstate[5] else 5)
    six = 'X' if Xstate[6] else ('O' if Zstate[6] else 6)
    seven = 'X' if Xstate[7] else ('O' if Zstate[7] else 7)
    eight = 'X' if Xstate[8] else ('O' if Zstate[8] else 8)
    print(f"{zero} | {one} | {two}")
    print(f"--|---|---")
    print(f"{three} | {four} | {five}")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight}")
    print(f"--|---|---")
#-------------------------------------------so we define the board and its display way and we also set the conditions here-----------

def check_win(Xstate,Zstate):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(Xstate[win[0]],Xstate[win[1]],Xstate[win[2]]) == 3 ):
            print("X won the match!")
            return 1
        if(sum(Zstate[win[0]],Zstate[win[1]],Zstate[win[2]]) == 3):
            print("O won the match!")
            return 0
    return -1
if __name__ == "__main__":
        Xstate = [0,0,0,0,0,0,0,0,0]
        Zstate = [0,0,0,0,0,0,0,0,0]
        turn=1
        print("welcome to tic tac toe!!!!!!!1")

        while(True):
            print_Board(Xstate,Zstate)
            if (turn==1):
                print("X,s chance")
                value = int(input("enter the value: "))
                Xstate[value]=1
            else:
                print("O,s chance")
                value=int(input("enter the value: "))
                Zstate[value]=1

            cwin=check_win(Xstate,Zstate)
            if (cwin != -1):
                print("Match over!!!")
                break
            turn = 1-turn


