def distinct_characters(words: list) -> dict:
    d = {}
    for word in words:
        d.update({word: 0})
        unique = set()
        for letter in word:
            if letter not in unique:
                unique.add(letter)
                d[word] += 1
    return d 

if __name__  == "__main__":
    print(distinct_characters(["check", "look", "try", "pop"]))                                             
    #{ "check" : 4, "look" : 3, "try" : 3, "pop" : 2}.