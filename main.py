from stats import text_from_book
from stats import count_char
from stats import sorted_list
import sys

book_path = None

if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
else:
	book_path = sys.argv[1]

def get_book_text(filepath):
	with open(filepath) as f:
		return f.read()
	
def main():
	book = get_book_text(book_path)
	sorted = sorted_list(count_char(book))
	chars = count_char(book)

	print(f"============ BOOKBOT ============")
	print(f"Analyzing book found at {book_path}")
	print(f"----------- Word Count ----------")
	xount = text_from_book(get_book_text(book_path))
	print(f"Found {xount} total words")
	print(f"--------- Character Count -------")
	for item in sorted:
		if not item["char"].isalpha():
			continue
		print(f"{item['char']}: {item['num']}")
	print(f"============= END ===============")
	
	# print(chars)
	# print(book)

main()