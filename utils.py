"""Yordamchi funksiyalar: input tekshirish, kitob topish, chiroyli chiqarish."""

from datetime import date


# ---------- Input tekshirish ----------

def read_text(prompt):
    """Bo‘sh bo‘lmagan matn kiritilguncha so‘raydi."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Xato: bo‘sh qiymat kiritib bo‘lmaydi.")


def read_int(prompt, allow_blank=False, min_value=None, max_value=None):
    """Butun son kiritilguncha so‘raydi.

    allow_blank=True bo‘lsa, bo‘sh kiritish (Enter) None qaytaradi.
    """
    while True:
        raw = input(prompt).strip()

        if raw == "":
            if allow_blank:
                return None
            print("Xato: bo‘sh qiymat kiritib bo‘lmaydi.")
            continue

        try:
            number = int(raw)
        except ValueError:
            print("Xato: butun son kiriting (masalan: 5).")
            continue

        if min_value is not None and number < min_value:
            print(f"Xato: son {min_value} dan kichik bo‘lmasligi kerak.")
            continue
        if max_value is not None and number > max_value:
            print(f"Xato: son {max_value} dan katta bo‘lmasligi kerak.")
            continue

        return number


def read_year(prompt, allow_blank=False):
    """Nashr yilini so‘raydi (1 dan joriy yilgacha)."""
    return read_int(
        prompt,
        allow_blank=allow_blank,
        min_value=1,
        max_value=date.today().year,
    )


# ---------- Kitob topish ----------

def find_book_by_id(books, book_id):
    """ID bo‘yicha kitobni qaytaradi, topilmasa None."""
    for book in books:
        if book["id"] == book_id:
            return book
    return None


def ask_book(books, prompt="Kitob ID sini kiriting"):
    """Foydalanuvchidan ID so‘rab, kitobni topib beradi.

    Muammo bo‘lsa (ro‘yxat bo‘sh, ID topilmadi, bekor qilindi) xabar
    chiqarib None qaytaradi.
    """
    if not books:
        print("Kitoblar ro‘yxati bo‘sh.")
        return None

    book_id = read_int(f"{prompt} (bekor qilish uchun Enter): ", allow_blank=True)
    if book_id is None:
        print("Amal bekor qilindi.")
        return None

    book = find_book_by_id(books, book_id)
    if book is None:
        print(f"Xato: ID = {book_id} bo‘lgan kitob topilmadi.")
    return book


# ---------- Chiroyli chiqarish ----------

def get_status_text(book):
    """Kitob holatini matn ko‘rinishida qaytaradi."""
    return "Mavjud" if book["available"] else "Berilgan"


def format_book(book, title_width=5, author_width=7):
    """Bitta kitobni jadval qatori ko‘rinishida formatlaydi."""
    return (
        f"{book['id']:<5}| {book['title']:<{title_width}} | "
        f"{book['author']:<{author_width}} | {book['year']:<6} | "
        f"{get_status_text(book)}"
    )


def print_books(books, heading, empty_message="Kitoblar topilmadi."):
    """Kitoblar ro‘yxatini jadval ko‘rinishida chiqaradi."""
    print(f"\n--- {heading} ---")

    if not books:
        print(empty_message)
        return

    title_width = max(len("Nomi"), max(len(b["title"]) for b in books))
    author_width = max(len("Muallif"), max(len(b["author"]) for b in books))

    header = (
        f"{'ID':<5}| {'Nomi':<{title_width}} | "
        f"{'Muallif':<{author_width}} | {'Yil':<6} | Holati"
    )
    print(header)
    print("-" * len(header))
    for book in books:
        print(format_book(book, title_width, author_width))
    print(f"Jami: {len(books)} ta kitob")
