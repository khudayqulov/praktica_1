# Library Management System

Terminal orqali ishlaydigan kutubxona boshqaruv tizimi (faqat Python standart kutubxonasi, `class`siz).

## Ishga tushirish

Python 3.8+ kerak. Loyiha papkasida:

```bash
cd library_management
python main.py        # Windows'da: python main.py yoki py main.py
                      # Linux/macOS'da: python3 main.py
```

Menyudan `0` ni tanlasangiz, dastur tugaydi. Ma’lumotlar faqat xotirada saqlanadi — dastur yopilganda yo‘qoladi.

## Fayllar va vazifalari

| Fayl | Vazifasi |
|------|----------|
| `main.py` | Menyuni ko‘rsatadi, tanlovni o‘qiydi va mos funksiyani chaqiradi (`0` gacha takrorlanadi). |
| `books.py` | Kitoblar ustidagi barcha asosiy amallar. |
| `utils.py` | Input tekshirish va qayta ishlatiladigan yordamchi funksiyalar. |
| `database.py` | Boshlang‘ich `books` ro‘yxati va `next_book_id` hisoblagichi. |

## Asosiy funksiyalar

**`books.py`**
- `show_all_books()` — barcha kitoblarni jadval ko‘rinishida chiqaradi.
- `add_book()` — nom, muallif, yilni tekshirib, avtomatik ID bilan kitob qo‘shadi.
- `edit_book()` — ID bo‘yicha topib, nom/muallif/yilni yangilaydi; Enter bosilsa eski qiymat saqlanadi.
- `delete_book()` — kitobni o‘chiradi; foydalanuvchida turgan (berilgan) kitobni o‘chirishga ruxsat bermaydi.
- `search_books()` — nom yoki muallif bo‘yicha, katta-kichik harfni farqlamasdan qidiradi.
- `issue_book()` — faqat mavjud kitobni beradi (`available=False`).
- `return_book()` — faqat berilgan kitobni qaytaradi (`available=True`).
- `show_available_books()` / `show_issued_books()` — mos holatdagi kitoblarni chiqaradi.

**`utils.py`**
- `read_text()` — bo‘sh bo‘lmagan matn kiritilguncha so‘raydi.
- `read_int()` / `read_year()` — butun son (va yil) kiritilishini tekshiradi.
- `find_book_by_id()` — ID bo‘yicha kitobni topadi.
- `ask_book()` — ID so‘raydi, ro‘yxat bo‘sh yoki ID topilmagan holatlarni boshqaradi (takroriy tekshiruv bitta joyda).
- `format_book()` / `print_books()` — kitoblarni chiroyli jadval ko‘rinishida chiqaradi.

**`database.py`**
- `books` — kitoblar ro‘yxati (3 ta namunaviy kitob bilan).
- `counter["next_book_id"]` va `get_next_id()` — takrorlanmaydigan ID berish.

## Sinab ko‘rish uchun holatlar

1. Menyuga noto‘g‘ri qiymat (`abc`, `99`) kiriting.
2. ID o‘rniga matn kiriting; mavjud bo‘lmagan ID (`999`) kiriting.
3. Kitob qo‘shishda bo‘sh nom/muallif va matnli yil kiriting.
4. Bir kitobni ikki marta bering; mavjud kitobni qaytarishga urinib ko‘ring.
5. Berilgan kitobni (`3` ID) o‘chirib ko‘ring — ruxsat berilmaydi.
6. Hamma kitobni o‘chirib, ro‘yxat bo‘sh holatini tekshiring.
7. Qidiruvda `CLEAN`, `clean`, `MaRtIn` kabi turli harflarni sinang.
