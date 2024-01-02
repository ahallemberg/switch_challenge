from src.fn import switch_challenge_level1, switch_challenge_level2
from pylibs.uinput import Input, Init, ExitProgram, ExitInputState

class SwitchLevel(Exception): 
    pass 

Init.setCommands({"q": ExitProgram(), "": ExitInputState(), "sw": SwitchLevel()})

def run() -> None: 
    try: 
        fn_level = 1

        while True:
            try: 
                comb1 = Input("comb1: ").str
                comb2 = Input("comb2: ").str
                if len(comb1) != 4 or len(comb2) != 4: 
                    print("ugyldig comb")
                    continue
                
                if fn_level == 1: 
                    print(switch_challenge_level1(comb1, comb2), end="\n\n")
                
                else: 
                    levels = []
                    try: 
                        while True: 
                            try: 
                                level = Input("Numbers: ").str
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
                print("Switching level to 2\n")
                fn_level = 2
                
    except ExitProgram: 
        quit()
        

if __name__ == "__main__":
    run()