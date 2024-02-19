import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Function that returns a string of page text and its size
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    end_symbol = ['.', ',', '!', ':', ';', '?']
    end = start+page_size
    while text[end:][:1] in end_symbol:
        end -= 1
    text = text[start:end]
    text = text[: max(map(text.rfind, end_symbol))+1]
    return text, len(text)


# The function that forms the book's dictionary
def prepare_book(path: str) -> None:
    with open(path, 'r', encoding='utf-8') as f:
        cnt = 1
        text = f.read()
        while text:
            val, page = _get_part_text(text, 0, PAGE_SIZE)
            book[cnt] = val.lstrip()
            cnt += 1
            text = text[page:]


# Call the prepare_book function to prepare a book from a text file
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
