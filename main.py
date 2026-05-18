import re
from models import Book
from storage import load_books, save_books, add_book_to_list, remove_book_from_list
from stats import show_all_books, calculate_average_rating, analyze_author_statistics

def display_menu():
    """Выводит главное текстовое меню."""
    print('\n' + '=' * 40)
    print('1. Добавить книгу')
    print('2. Показать все книги')
    print('3. Показать среднюю оценку')
    print('4. Статистика по авторам')
    print('5. Удалить книгу')
    print('6. Выход')
    print('=' * 40)


def get_validated_date() -> str:
    """Циклически запрашивает у пользователя дату в формате ГГГГ-ММ-ДД."""
    while True:
        date_input = input('Введите дату прочтения книги (ГГГГ-ММ-ДД) или оставьте пустым для сегодняшней даты: ').strip()
        if not date_input:
            return ""
        try:
            # Проверка формата YYYY-MM-DD
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Неправильный формат даты. Пожалуйста, используйте ГГГГ-ММ-ДД.")

def get_validated_rating() -> int | None:
    """Циклически запрашивает рейтинг (1-5) и возвращает число."""
    while True:
        try:
            rating_input = input("Введите рейтинг книги (1-5): ").strip()
            if not rating_input:
                return None
            rating = int(rating_input)
            if 1 <= rating <= 5:
                return rating
            else:
                print('Неправильный формат рейтинга. Используйте число от 1 до 5.')
        except ValueError:
            print("Некорректный ввод. Введите целое число.")

def add_book(books):
    """Основная логика добавления книги с валидацией ввода."""
    title = input("Введите название книги: ").strip()
    if not title:
        print("Название не может быть пустым.")
        return

    author = input("Введите автора книги: ").strip()
    if not author:
        print("Автор не может быть пустым.")
        return

    date_added = get_validated_date()
    if date_added:
        try:
            from datetime import datetime
            datetime.strptime(date_added, "%Y-%m-%d") 
        except ValueError:
            pass

    rating = get_validated_rating()
    if rating is None:
        print("Добавление отменено.")
        return
    
    new_book = Book(title, author, rating, date_added if not date_added else datetime.now().strftime('%Y-%m-%d'))

    if add_book_to_list(books, new_book):
        print("\n Книга успешно добавлена в библиотеку!")


def delete_book(books: list[Book]):
    """Логика удаления книги по индексу."""
    if not books:
        print("\n Список пуст, удалять нечего.")
        return

    show_all_books(books) 
    
    while True:
        try:
            index_input = input("\n Введите НОМЕР книги, которую хотите удалить (или 'отмена'): ").strip()
            if index_input.lower() == 'отмена':
                return

            index = int(index_input) - 1
            if not (0 <= index < len(books)):
                print("Пожалуйста, введите корректный номер книги.")
                continue

            book_to_delete = books[index]
            confirm = input(f"Вы уверены, что хотите удалить '{book_to_delete.title}' от {book_to_delete.author}? (да/нет): ").lower()
            
            if confirm == 'да':
                removed_book = remove_book_from_list(books, index)
                if removed_book:
                    print(f"\n Книга '{removed_book.title}' успешно удалена.")
                return 

            else:
                print("Удаление отменено.")
                return
        except ValueError:
            print("Некорректный ввод. Попробуйте ввести число или 'отмена'.")


def main():
    """Главная функция приложения."""
    books = load_books()

    while True:
        display_menu()
        choice = input('Выберите действие (1-6): ').strip()

        if choice == '1':
            add_book(books)
        elif choice == '2':
            show_all_books(books)
        elif choice == '3':
            calculate_average_rating(books)
        elif choice == '4':
            analyze_author_statistics(books)
        elif choice == '5':
            delete_book(books)
        elif choice == '6':
            print("\n Спасибо за использование приложения! Данные сохранены.")
            break
        else:
            print('Неверный выбор. Пожалуйста, выберите число от 1 до 6.')


if __name__ == '__main__':
    from datetime import datetime
    main()
