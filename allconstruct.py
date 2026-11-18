def allconstruct(target,wordbank):
    if target == '': return [[]]
    
    result = []
    for word in wordbank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffixways = allconstruct(suffix,wordbank)
            targetways = list(map(lambda way: [word, *way], suffixways))
            
            result.extend(targetways)
    
    return result


#Driver function
#m = targetsum
#Time complexity:: Brute force n^m * m^2, memoised n * m
#Space complexity:: height of the tree m, memoised m*m
print(allconstruct("abcdef",["ab","abc","ce","def","abcd"]))
