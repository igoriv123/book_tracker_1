class Book:
    """Класс для представления книги в системе."""
    def __init__(self, title: str, author: str, rating: int, date_added: str):
        self.title = title
        self.author = author
        self.rating = rating
        self.date_added = date_added

    def to_dict(self) -> dict:
        """Преобразует объект Book в словарь для JSON-хранения."""
        return {
            "title": self.title,
            "author": self.author,
            "rating": self.rating,
            "date_added": self.date_added
        }

    @staticmethod
    def from_dict(data: dict) -> 'Book':
        """Создает объект Book из словаря (при загрузке данных)."""
        return Book(
            title=data['title'],
            author=data['author'],
            rating=int(data['rating']),
            date_added=data['date_added']
        )

    def __str__(self):
        """Красивое строковое представление объекта для вывода."""
        return f"{self.title:<30} | {self.author[:29]:<29} | {self.rating:<5} | {self.date_added:<12}"

