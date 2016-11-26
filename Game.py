import os, sys, random

loop = 1
bound = (1,100)
yg = 0

while loop:
    print("I am thinking of a number between %r and %r." % bound)
    guesses = 1
    NumToGuess = random.randrange(*bound)
    if "debug" in sys.argv:
        print(NumToGuess)
    while yg == 0:
        try:
            yourGuess = int(input("What is your guess?\n"))
            yg = 1
        except ValueError:
            print("A number, preferably?")
            yg = 0

    while (NumToGuess != yourGuess):
        if (yourGuess > NumToGuess):
            print("Too high. Try again.")
        elif (yourGuess < NumToGuess):
            print("Too low. Try again.")
        yg = 0
        while yg == 0:
            try:
                yourGuess = int(input("What is your guess?\n"))
                yg = 1
            except ValueError:
                print("A number, preferably?")
                yg = 0
        guesses += 1

    if guesses > 1:
        print("Good job! You got it in " + str(guesses) + " tries!")
    elif guesses == 1:
        print("Whoa! It only took you 1 try!")
    else:
        print("Aw snap...")
        print("""\
_____       _____
  |   |   | |
  |   |---| |---
  |   |   | |____
Program has
----   ----    ---   -   -  -----  -   -
-   -  -   -  -   -  - --   -      --  -
----   ----   -   -  --     ----   - - -
-   -  -   -  -   -  - -    -      -  --
----   -   -   ---   -  -   -----  -   -
(Mwa, mwa mwawawa...)

Oh well. I'll count that as you win. ;-)""")
    lc = input("Do you want to guess a different number? (y/n)")
    if (lc[0] == "y" or lc == "1"):
        loop = 1
    else:
        print("Ok. Bye!")
        loop = 0

sys.exit()
