"""Kitoblar ustida bajariladigan asosiy amallar (CRUD, qidirish, berish, qaytarish)."""

from database import books, get_next_id
from utils import ask_book, print_books, read_text, read_year


def show_all_books():
    """1. Barcha kitoblarni ko‘rsatadi."""
    print_books(books, "Barcha kitoblar", "Kutubxonada hozircha kitob yo‘q.")


def add_book():
    """2. Yangi kitob qo‘shadi (ID avtomatik beriladi)."""
    print("\n--- Yangi kitob qo‘shish ---")
    title = read_text("Kitob nomi: ")
    author = read_text("Muallifi: ")
    year = read_year("Nashr yili: ")

    book = {
        "id": get_next_id(),
        "title": title,
        "author": author,
        "year": year,
        "available": True,
    }
    books.append(book)
    print(f"Kitob qo‘shildi. ID = {book['id']}")


def edit_book():
    """3. Kitob nomi, muallifi yoki yilini tahrirlaydi.

    Bo‘sh qiymat (Enter) kiritilsa, eski qiymat saqlanib qoladi.
    """
    print("\n--- Kitobni tahrirlash ---")
    book = ask_book(books)
    if book is None:
        return

    print("Eski qiymatni saqlab qolish uchun shunchaki Enter bosing.")

    new_title = input(f"Yangi nom [{book['title']}]: ").strip()
    new_author = input(f"Yangi muallif [{book['author']}]: ").strip()
    new_year = read_year(f"Yangi yil [{book['year']}]: ", allow_blank=True)

    if new_title:
        book["title"] = new_title
    if new_author:
        book["author"] = new_author
    if new_year is not None:
        book["year"] = new_year

    print("Kitob ma’lumotlari yangilandi.")


def delete_book():
    """4. Kitobni ID bo‘yicha o‘chiradi (berilgan kitobni o‘chirib bo‘lmaydi)."""
    print("\n--- Kitobni o‘chirish ---")
    book = ask_book(books)
    if book is None:
        return

    if not book["available"]:
        print("Xato: bu kitob hozir foydalanuvchida, uni o‘chirib bo‘lmaydi.")
        return

    books.remove(book)
    print(f"'{book['title']}' kitobi o‘chirildi.")


def search_books():
    """5. Nom yoki muallif bo‘yicha qidiradi (katta-kichik harf farq qilmaydi)."""
    print("\n--- Kitob qidirish ---")
    if not books:
        print("Kitoblar ro‘yxati bo‘sh.")
        return

    query = read_text("Qidiruv so‘zi (nom yoki muallif): ").lower()

    results = [
        book
        for book in books
        if query in book["title"].lower() or query in book["author"].lower()
    ]
    print_books(results, f"Qidiruv natijalari: '{query}'", "Hech narsa topilmadi.")


def issue_book():
    """6. Kitobni foydalanuvchiga beradi."""
    print("\n--- Kitob berish ---")
    book = ask_book(books)
    if book is None:
        return

    if not book["available"]:
        print("Xato: bu kitob allaqachon berilgan.")
        return

    book["available"] = False
    print(f"'{book['title']}' kitobi berildi.")


def return_book():
    """7. Berilgan kitobni qaytarib oladi."""
    print("\n--- Kitobni qaytarish ---")
    book = ask_book(books)
    if book is None:
        return

    if book["available"]:
        print("Bu kitob allaqachon kutubxonada mavjud, qaytarish shart emas.")
        return

    book["available"] = True
    print(f"'{book['title']}' kitobi qaytarildi.")


def show_available_books():
    """8. Faqat mavjud kitoblarni ko‘rsatadi."""
    available = [book for book in books if book["available"]]
    print_books(available, "Mavjud kitoblar", "Hozir mavjud kitob yo‘q.")


def show_issued_books():
    """9. Faqat berilgan kitoblarni ko‘rsatadi."""
    issued = [book for book in books if not book["available"]]
    print_books(issued, "Berilgan kitoblar", "Berilgan kitoblar yo‘q.")
