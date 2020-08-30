from List import pick
from Draw import draw

run = True

while run:
    x = pick()
    chance = 7
    y = len(x)
    m = []
    usedChar = ""

    while y > 0:
        m.append("_")
        y = y - 1

    reset = True

    while reset:
        draw(chance)
        print("\n\n")
        if chance == 0:
            print('You have lost')
            print('The answer is:\n', x)
            again = input("do you want to play again? y/n: ")
            reset = False
            if again == 'n':
                run = False

        elif m.count('_') > 0:

            print("\nYou have", chance, "chances\n")
            print("  ".join(m), "\n\n\n")
            print("Used Letters:", usedChar)

            z = input("\n\nEnter a letter: ")
            usedChar += z + " "
            
            print("\n\n\n\n\n")
            if x.count(z) > 0:
                i = 0
                for ch in x:
                    if ch == z:
                        m[i] = ch
                    i = i + 1

            else:
                chance = chance - 1
                print("\nWrong answer!!\n")

        else:
            print(''.join(m), "\n\n\n")
            print("!!!  YOU WON  !!!")
            again = input("do you want to play again? y/n: ")
            if again == 'n':
                run = False
            reset = False
