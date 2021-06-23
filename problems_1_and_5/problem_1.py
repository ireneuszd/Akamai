
def sort_string(raw_str):
	"""Sorts string by frequency of occurance
	
	if two or more characters had occured same amount of time
	alfabethical order decides about the order
	:param raw_str: string to sort
	:type raw_str: str
	:return: sorted string
	:rtype: str
	"""
    char_counter = {}
    final_str = ''
    
    for element in raw_str:
        if element not in char_counter:
            char_counter[element] = 1
        else:
            char_counter[element] += 1
    
    sorted_counter = sorted(char_counter.items(), key=lambda x: (x[1], x[0]))
    for letter, amount in sorted_counter:
        final_str += letter * amount
    return final_str
    
    
