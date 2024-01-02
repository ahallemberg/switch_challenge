from src.fn import switch_challenge_level1, switch_challenge_level2
from pylibs.uinput import Input, Init, ExitProgram, ExitInputState

class SwitchLevel(Exception): 
    pass 

Init.setCommands({"q": ExitProgram, "": ExitInputState, "sw": SwitchLevel})

def run() -> None: 
    print("This is a program for solving the Switch Challenge.\nType 'q' to quit the program any time.\nWrite the first letter of the colors of the objects in order, and the program will return the number of the combination.\nExample:\ncomb1:'gbry'\ncomb2: 'bygr'\nwill return '2413'.\n\nWhen you reach the point wehere you need to select multiple numbers, type 'sw' to switch to level 2.\nHere you need to start with doing the same as in level 1 and wrtiing the two combinations of colors. Then write each row with numbers, separated by commas.\nWhen you have written all the rows, hit enter one more time to get the solution.\nExample:\ncomb1: 'gryb'\ncomb2: 'rbgy'\nnumbers: '2341,2431,3241'\nnumbers: '2341,2431,3241'\nnumbers: ''\nwill return [3241, 2341], so you should select these numbers for the repective rows.\n\n")
    try: 
        fn_level = 1

        while True:
            try: 
                comb1 = Input("comb1: ").str
                comb2 = Input("comb2: ").str
                if len(comb1) != 4 or len(comb2) != 4: 
                    print("Invalid combination")
                    continue
                
                if fn_level == 1: 
                    print(switch_challenge_level1(comb1, comb2), end="\n\n")
                
                else: 
                    levels = []
                    try: 
                        while True: 
                            try: 
                                level = Input("numbers: ").str
                                if level == "c" and len(levels) >= 1: 
                                    levels.append(levels[-1])
                                    raise ExitInputState
                                else: 
                                    level = level.split(",")
                                    new_list = []
                                    for numb in level: 
                                        new_list.append(int(numb))
                                    levels.append(new_list)

                            except ValueError: 
                                pass

                    except ExitInputState: 
                        pass
                    
                    print(switch_challenge_level2(comb1, comb2, *levels), end="\n\n")

            except SwitchLevel:
                print("Switching to level 2\n")
                fn_level = 2
                
    except ExitProgram: 
        quit()
        

if __name__ == "__main__":
    run()