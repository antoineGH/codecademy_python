import utils
import sorts
from sorts import bubble_sort, quicksort

bookshelf = utils.load_books("E:/git/codeacademy_python/12_sorting/project_sorted_tale/a.csv")
long_bookshelf = utils.load_books("E:/git/codeacademy_python/12_sorting/project_sorted_tale/b.csv")
bookshelf_copy_v1 = bookshelf.copy()
bookshelf_copy_v2 = bookshelf.copy()
bookshelf_copy_v3 = bookshelf.copy()

def display_unicode(letter):
    if type(letter) == str:
        print("Unicode value for \'{}\': {}".format(letter, ord(letter)))
    else:
        print('Expect a string.')

def by_title_ascending(book_a, book_b):
    return book_a['title_lower'] > book_b['title_lower']

def by_author_ascending(book_a, book_b):
    return book_a["author_lower"] > book_b["author_lower"]

def by_total_length(book_a, book_b):
    return len(book_a["title_lower"]) + len(book_a["author_lower"]) > len(book_b["title_lower"]) + len(book_b["author_lower"])

sort_1 = bubble_sort(bookshelf, by_title_ascending)
sort_2 = bubble_sort(bookshelf_copy_v1, by_author_ascending)
quicksort(bookshelf_copy_v2, 0, len(bookshelf_copy_v2)-1, by_author_ascending)
sort_4 = bubble_sort(bookshelf, by_total_length)
quicksort(bookshelf_copy_v3, 0, len(bookshelf_copy_v3)-1, by_total_length)

print("\nBubble Sort - by_title_ascending")
for book in sort_1:
  print(book['title_lower'])

print("\nBubble Sort - by_author_ascending")
for book in sort_2:
  print(book['author_lower'])

print("\nQuick Sort - by_author_ascending")
for book in bookshelf_copy_v2:
  print(book['author_lower'])

print("\nBubble Sort - by_total_length")
for book in sort_2:
  print(book['author_lower'])

print("\nQuick Sort - by_total_length")
for book in bookshelf_copy_v3:
  print(book['author_lower'])





