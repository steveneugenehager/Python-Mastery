# 2025-11-14 Generate some CSV data in a file.
import random

def main():
    deck = build_deck()

    output_file = "tmp_shuffled_deck.txt"
    with open(output_file , 'w') as file_handle:
        for card in deck:
            file_handle.write(card + '\n')
     

def build_deck():
    suits = ['Hearts' , 'Diamonds' , 'Spades' , 'Clubs']
    ranks = list('A23456789TJQK')
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(','.join((rank , suit , str(random.randrange(0,10**18)) , str(round(random.random()*100,2)))))
    random.shuffle(deck)
    return(deck)


if __name__ == '__main__':
    main()