from praktika.praktika_3.book import Book

library = [
    Book("До Адама", "Джек Лондон"),
    Book("Война и Мир", "Лев Толстой"),
    Book("Герой нашего времени", "Михаил Лермонтов")
]

for book in library:
    print(f"{book.name} - {book.avtor}")
