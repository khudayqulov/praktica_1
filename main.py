"""Library Management System — dasturning kirish nuqtasi.

Ishga tushirish:  python main.py
"""

from books import (
    add_book,
    delete_book,
    edit_book,
    issue_book,
    return_book,
    search_books,
    show_all_books,
    show_available_books,
    show_issued_books,
)

MENU_TEXT = """
===== LIBRARY MANAGEMENT =====
1. Barcha kitoblarni ko‘rish
2. Kitob qo‘shish
3. Kitob ma’lumotlarini tahrirlash
4. Kitobni o‘chirish
5. Kitob qidirish
6. Kitobni foydalanuvchiga berish
7. Kitobni qaytarish
8. Mavjud kitoblarni ko‘rish
9. Berilgan kitoblarni ko‘rish
0. Chiqish"""

# Menu raqami -> bajariladigan funksiya
ACTIONS = {
    "1": show_all_books,
    "2": add_book,
    "3": edit_book,
    "4": delete_book,
    "5": search_books,
    "6": issue_book,
    "7": return_book,
    "8": show_available_books,
    "9": show_issued_books,
}


def show_menu():
    """Menyuni ekranga chiqaradi."""
    print(MENU_TEXT)


def main():
    """Foydalanuvchi 0 ni tanlamaguncha menyuni takrorlaydi."""
    while True:
        show_menu()
        choice = input("Tanlovingiz: ").strip()

        if choice == "0":
            print("Dasturdan chiqildi. Xayr!")
            break

        action = ACTIONS.get(choice)
        if action is None:
            print("Xato: noto‘g‘ri tanlov. 0 dan 9 gacha raqam kiriting.")
            continue

        action()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nDastur to‘xtatildi. Xayr!")
