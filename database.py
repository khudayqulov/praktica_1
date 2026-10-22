"""Ma’lumotlar ombori (hozircha faqat xotirada, list va dict ko‘rinishida).

Dastur yopilganda ma’lumotlar yo‘qoladi.
"""

# Boshlang‘ich kitoblar ro‘yxati.
books = [
    {
        "id": 1,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "year": 2008,
        "available": True,
    },
    {
        "id": 2,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "year": 1999,
        "available": True,
    },
    {
        "id": 3,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "year": 2015,
        "available": False,
    },
]

# Keyingi kitob ID si. Butun son o‘rniga dict ishlatilgan, chunki boshqa
# modul ichida o‘zgartirilganda ham qiymat hamma joyda bir xil bo‘lib qoladi.
counter = {"next_book_id": 4}


def get_next_id():
    """Yangi, takrorlanmaydigan ID qaytaradi va hisoblagichni oshiradi."""
    new_id = counter["next_book_id"]
    counter["next_book_id"] += 1
    return new_id
