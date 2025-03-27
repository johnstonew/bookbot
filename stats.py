def text_from_book(text):
	count = 0
	new_text = text.split()
	for word in new_text:
		count += 1
	# print(f"{count} words found in the document")
	return count

def count_char(text):
	chars = {}
	lower_text = text.lower()
	for char in lower_text:
		if char in chars:
			chars[char] += 1
		else:
			chars[char] = 1
	return chars

def sort_on(dict):
    return dict["num"]

def sorted_list(num_chars_dict):
	sorted_list = []
	for ch in num_chars_dict:
		sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
	sorted_list.sort(reverse=True, key=sort_on)
	return sorted_list