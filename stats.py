from typing import List
from models import Book

def show_all_books(books: List[Book]):
    """Выводит красиво отформатированный список всех книг."""
    if not books:
        print("\n Пока нет ни одной прочитанной книги.")
        return

    print("\n" + "=" * 80)
    print("--- СПИСОК ВСЕХ ПРОЧИТАННЫХ КНИГ ---")
    print(f"{'Название':<30} | {'Автор':<29} | {'Оценка':<5} | {'Дата':<12}")
    print("-" * 80)
    for book in books:
        print(str(book))
    print("=" * 80)


def calculate_average_rating(books: List[Book]) -> float:
    """Вычисляет общую среднюю оценку всех книг."""
    if not books:
        return 0.0
    total_rating = sum(book.rating for book in books)
    average = total_rating / len(books)
    print(f"\n Общая средняя оценка всех книг: {average:.2f} из 5.0")
    return average

def analyze_author_statistics(books: List[Book]) -> None:
    """Выводит статистику по всем авторам."""
    if not books:
        print("\n Нет данных для анализа авторов.")
        return

    author_ratings = {}

    for book in books:
        author = book.author.lower()
        rating = book.rating
        
        if author not in author_ratings:
            author_ratings[author] = [0, 0]
        
        author_ratings[author][0] += rating 
        author_ratings[author][1] += 1    

    print("\n Статистика по авторам:")
    print("=" * 65)
    for author, (total_rating, count) in author_ratings.items():
        average = total_rating / count
        formatted_author = author.title()
        print(f"Автор: {formatted_author:<15} | Книг: {count:<3} | Средняя оценка: {average:.2f}")
    print("=" * 65)
