# 2025-11-14 Read some CSV data from a file.
import random

def main():
    input_file = "tmp_shuffled_deck.txt"
    input_file_with_header = "tmp_shuffled_deck_header.txt"
    process_csv_with_split(input_file)
    process_csv_with_module(input_file)
    process_csv_with_dictionary_hints(input_file_with_header)
    #sort_csv_data(input_file)


def process_csv_with_split(input_file):
    with open(input_file , 'r') as file_handle:
        i=0
        for line in file_handle:
            i += 1
            # Example of unpacking a list of known length...
            rank , suit , uid , score = line.rstrip().split(',')
            uid = int(uid)
            score = float(score) 
            new_row = [rank , suit , uid , score]
            print("item # " , i , "-" , new_row)


def process_csv_with_module(input_file):
    print("\n\nINFO: In 'process_csv_with_module'.")
    import csv #You can import a module in a function if the module would only be used in the module.
    
    with open(input_file) as file_handle:
        # csv module provides the reader object which handles the comma delimiting and edge cases that split would not.
        reader = csv.reader(file_handle)
        for items in reader:
            rank , suit , uid , score = items[:4]
            card = {"rank" : rank , "suit" : suit , "uid" : int(uid) , "score" :float(score)}
            print(card)


def process_csv_with_dictionary_hints(input_file):
    print("\n\nINFO: In 'process_csv_with_dictionary_hints'.")
    import csv
    
    with open(input_file) as file_handle:
        #DictReader leverages the first row as a header row. Converts the subsequent CSV lines into dictionaries...
        reader = csv.DictReader(file_handle)
        for r in reader:
            card = {"rank" : r["rank"] , "suit" : r["suit"] , "uid" : int(r["uid"]) , "score" :float(r["score"])}
            print(card)


# def sort_csv_data(input_file):
#     with open(input_file , 'r') as file_handle:
#         for line in file_handle:
#             items = line.rstrip().split(',')
#             print(list)
#          #   paired=list( zip( list[::2] , list[1::2] ) )
#             paired = [(items[i], items[i+1]) for i in range(0, len(items) - 1, 2)]
#             print(paired)


if __name__ == '__main__':
    main()