def main():
    import random

    deck = []

    print('This is WAR! A card game where the player with the highest card wins! \n Drawing Cards... \n')
    def makeDeck(): #make card numbers and suits
        for suit in ("Hearts","Diamonds","Clubs","Spades"):
            for rank in range(2,15):
                deck.append((rank,suit))

    def nameFaceCard(card): #function that names cards
        if card[0] <= 10: rank = str(card[0])
        if card[0] == 11: rank = "J"
        if card[0] == 12: rank = "Q"
        if card[0] == 13: rank = "K"
        if card[0] == 14: rank = "A"
        name = rank +" of " + card[1]
        return name

    def drawCard(user): #draws player cards
        card=deck[0]
        deck.remove(deck[0])
        print(user + " drew " + nameFaceCard(card))
        return card

    makeDeck()

    random.shuffle(deck)#randomize deck


    while True: #loop determines which player has the highest card

        p1Card = drawCard("Player 1")
        p2Card = drawCard("Player 2")

        if p1Card[0] > p2Card[0]:
            winner = "\nPlayer 1"
        elif p1Card[0] < p2Card[0]:
            winner = "\nPlayer 2"
        else: winner = "Neither"

        print( winner + " wins!")
        break

    playAgain =input("\nPress Y to play again and N to Stop\n") #ask player to play again, of yes loops back to main function

    if playAgain == "Y":
        main()
    else:
        print("Goodbye!") #exit game
    exit()

main()
