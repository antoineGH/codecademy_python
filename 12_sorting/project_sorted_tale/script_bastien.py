import utils
import sorts

bookshelf = utils.load_books('books_small.csv')

print(ord('a'))
print(ord(' '))
print(ord('A'))

def by_title_ascending(book_a, book_b):
  if book_a['title_lower'] > book_b['title_lower']:
    return True
  else:
    return False
  
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)
print(sort_1)

def by_author_ascending(book_a, book_b):
  if book_a['author_lower'] > book_b['author_lower']:
    return True
  else:
    return False
  
bookshelf_v1 = bookshelf.copy()

sort_2 = sorts.bubble_sort(bookshelf_v1, by_author_ascending)
print(sort_2)

bookshelf_v2 = bookshelf_v1.copy()
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)
print(bookshelf_v2)

def by_total_length(book_a, book_b):
  if len(book_a['title_lower']) + len(book_a['author_lower']) > len(book_b['title_lower']) + len(book_b['author_lower']):
    return True
  else:
    return False
  
long_bookshelf = utils.load_books('books_small.csv')
print(sorts.bubble_sort(long_bookshelf, by_total_length))
by_total_length))
