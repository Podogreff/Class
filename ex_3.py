
class Dog():
    """Простая модель собаки."""

    def __int__(self, name, age):
        """Инициализирует атрибуты name и age."""
        self.name = name
        self.age = age

    def sit(self):
        """Собака садится по команде"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Собака перекатывается по команде"""
        print(f"{self.name} rolled over!")


my_dog = Dog("Will", 7)

print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
