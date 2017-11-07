import time

### Mad Libs ###
### https://i.pinimg.com/736x/cd/9d/7b/cd9d7b67e0c1893d8d4f17e8c66627cf--madlibs-trip-games.jpg
while True:
    adj = "Give me an adjective"
    noun = "Give me a noun"

    print(adj)
    adj1 = input()

    print(adj)
    adj2 = input()

    print(adj)
    adj3 = input()

    print(noun)
    noun1 = input()

    print(noun)
    noun2 = input()

    print("Give me a verb in the past tense")
    verbpast1 = input()

    print("Give me a color")
    color = input()

    print(adj)
    adj4 = input()

    print("Give me an exclamation")
    exclamation = input()

    print("Give me an animal")
    animal = input()

    ### Start the Mad Lib ###

    print("Mrs. Fifi Vanderbold, the " + adj1 + " and " + adj2 + " heiress, has filled for divorce from her husband, percy Vanderbold, the former " + adj3 + " " + noun1 + " of harvard, class of 38' now in the " + noun2 + " business.")
    print("Mrs. Vanderbold claimed that her husband had " + verbpast1 + " her bed of " + color + " flowers and tracked " + adj4 + " mud into the house.")
    print("He also critized her cooking.")
    print("Mr. Vanderbold, when asked to comment, said,'" + exclamation + " ! I didn't do it.")
    print("The pet " + animal + " ruined the flowers.")
    print("And I offered to take out to restuants more often!'")

    print("Play again? Y/N")
    ansewer = input()

    if ansewer == "N":
        print("Goodbye")
        time.sleep(3)
        break
