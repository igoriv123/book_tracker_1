import json
from typing import List
from models import Book 

DATA_FILE = "books.json"

def load_books() -> List[Book]:
    """Загружает книги из JSON файла, преобразуя их в объекты Book."""
    print("--- Загрузка данных библиотеки...")
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)

            return [Book.from_dict(book_data) for book_data in data]
    except FileNotFoundError:
        print("Файл данных не найден. Начинаем с пустой библиотекой.")
        return []
    except json.JSONDecodeError:
        print("Ошибка чтения файла данных (books.json). Файл поврежден, начинаем с пустого списка.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при загрузке данных: {e}")
        return []

def save_books(books: List[Book]):
    """Сохраняет список объектов Book в JSON файл."""
    try:
        book_data = [book.to_dict() for book in books]
        with open(DATA_FILE, "w", encoding='utf-8') as f:
            json.dump(book_data, f, indent=4, ensure_ascii=False)
        print("\n Данные успешно сохранены в базу.")
    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")

def add_book_to_list(books: List[Book], new_book: Book) -> bool:
    books.append(new_book)
    save_books(books)
    return True

def remove_book_from_list(books: List[Book], index: int) -> Book | None:
    """Удаляет книгу по индексу и сохраняет изменения."""
    if 0 <= index < len(books):
        removed_book = books.pop(index)
        save_books(books)
        return removed_book
    return None

