import random


class COLORS:
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"


class Game:
    score = {"computer": 0, "usr": 0}
    choices = ["Rock", "Scissors", "paper"]
    print(f"{COLORS.GREEN}Welcome back to the game! \n {COLORS.RESET}")

    def start(self):
        global choices, score
        while True:
            print("1- Continue Playing.\n2.Exit the game")
            ch = int(input("Enter your choice (1, 2): \n"))
            if ch == 1:
                com_pl = random.choice(self.choices)
                usr_pl = input("Enter your play (Rock, Scissors, paper) : \n")
                if com_pl == usr_pl:
                    print("It's a tie! \n ———————————————————————————————{ ")
                elif (
                    com_pl == "Rock"
                    and usr_pl == "Scissors"
                    or com_pl == "paper"
                    and usr_pl == "Rock"
                    or com_pl == "Scissors"
                    and usr_pl == "paper"
                ):
                    print(f"{usr_pl} vs {com_pl}!")
                    print(
                        f"{COLORS.RED}you lose!\n ————————————————————————————{COLORS.RESET}"
                    )

                    self.score["computer"] += 1
                else:
                    print(f"{usr_pl} vs {com_pl}!")
                    print(
                        f"{COLORS.GREEN}you win! \n ——————————————————————————{COLORS.RESET}"
                    )
                    self.score["usr"] += 1
            elif ch == 2:
                print(
                    f"score!\n {COLORS.GREEN} \
                    You: {self.score['usr']} vs Comp: {self.score['computer']}\
                    {COLORS.RESET}"
                )
                break
            else:
                print(f"{COLORS.RED} Enter a valid choice")
                continue


if __name__ == "__main__":
    game = Game()
    game.start()
