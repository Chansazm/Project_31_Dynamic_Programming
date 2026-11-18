def bestsum(targetsum,numbers):
    table = [None] * (targetsum + 1)
    table[0] = []
    
    
    for i in range(len(table)):
        if table[i] is not None:
            for num in numbers:
                if i+num <= targetsum:
                    combination = [*table[i], num]
                    if (table[i+num] is None or 
                        len(combination) < len(table[i+num])):
                        table[i+num] = combination
    return table[targetsum]


#Driver function
# m is target and n is len(numbers)
#Time complexity:: 
#Space complexity::
print(bestsum(7,[5,3,4,7])) #7
print(bestsum(8,[2,3,5])) # [5,3]
print(bestsum(100,[1,2,5,25]))