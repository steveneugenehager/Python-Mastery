# Given a list of intervals, merge all overlapping intervals and 
# return a list of non-overlapping intervals that cover all the intervals in the input.

def main():
#GIVEN:
#input_intervals = [(1, 3), (2, 4), (5, 7), (6, 8) , (-1,5)]
# input_intervals = [(1, 3), (2, 4), (5, 7), (6, 8)  ]
    #input_intervals = [[ 1, 3], [2, 4], [5, 7], [6, 8]  , [-1,2] , [1,2] ]
    input_intervals = [[5,6] , [ 1, 3], [0.1,3], [0,1], [-0.1,2] , [2,4] ,[9,10]]

    print( merge_intervals( input_intervals) )

def merge_intervals(intervals):
    # Sort intervals based on start time
    #intervals.sort(key=lambda x: x[0])
    intervals.sort(key=lambda x: (x[0] , x[1]))
    
    merged = []
    for interval in intervals:
        print(interval)
        if not merged or merged[-1][1] < interval[0]:
            # No overlap, add the interval
            merged.append(interval)

        else:
            # Overlap, merge by updating the end
            merged[-1][1] = max(merged[-1][1], interval[1])
        print('\t' , merged)
    return merged

# #sort the intervals on their lower limit.

# sorted_intervals = sorted(input_intervals, key= lambda s : s[0] )
# print(sorted_intervals)

# for i in range(len(sorted_intervals)-1):
#     if sorted_intervals[i][1] >= sorted_intervals[i+1][0]:



# input = input_intervals[:]
# more_merging_to_try = True
# while more_merging_to_try:
#     # Skip the last input interval. There is no "next" one to consider merging.
#     for i in range(len(input) - 1):
#         print( input[i])
#         min_1 , max_1 = input[i][0] , input[i][1]
#         for j in range(i+1, len(input)):
#             print('\t' , input[j])
#             min_2 , max_2 = input[j][0] , input[j][1]
#             if min_2 < min_1 < max_2:
#                 input[i][0] = min_2
#             if max_2 < max_1  

#     print(input)        
#     break

main()