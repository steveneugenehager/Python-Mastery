# 2025-11-14 Generate some CSV data in a file.
import random
import csv

def main():
    deck = build_deck()

    output_file = "tmp_shuffled_deck_v2.csv"
    with open(output_file , 'w', encoding='utf-8') as file_handle:
        writer = csv.DictWriter(file_handle, fieldnames=["rank","suit","uid","score"])
        for card in deck:
            writer.writerow(card) 
     

def build_deck():
    suits = ["\u2665" , "\u25C6" , "\u2660" , "\u2663" ]
    ranks = list('A23456789TJQK')
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append( {"rank" : rank , "suit" : suit , "uid" : f"{random.randrange(0,10**18):018}" , "score" : str(round(random.random()*50+50,2)) })
    random.shuffle(deck)
    return(deck)


if __name__ == '__main__':
    main()