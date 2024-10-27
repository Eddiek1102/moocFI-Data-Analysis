def reverse_dictionary(dictionary: dict):
    if len(dictionary.keys()) == 0:
        return
    
    reversed_dictionary = {}
    for key, values in dictionary.items():
        for value in values:
            if value in reversed_dictionary:
                reversed_dictionary[value].append(key)
            else:
                reversed_dictionary.update({value: [key]})

    dictionary.clear()
    dictionary.update(reversed_dictionary)
    
if __name__ == "__main__":
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    reverse_dictionary(d)
    print(d)
	#{'liikuttaa': ['move'], 'piilottaa': ['hide'], 'salata': ['hide'], 'kuusi': ['six', 'fir']}
