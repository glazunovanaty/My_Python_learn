import hashlib
import uuid
from classes.users import User, Customer, Admin

class AuthenticationService:
    """
    Сервис для управления регистрацией и аутентификацией пользователей.
    """
    
    def __init__(self):
        self.current_user=None
        self.current_token=None      
    
    def register(self, user_class, username, email, password, *args):
        """
        регистрирует нового пользователя с проверкой уникальности имени пользователя 
        и хешированием пароля. Возвращает сообщение об успехе или ошибке
        """
        if any(user.username == username for user in User.users):
            return "Ошибка: Имя пользователя уже существует."
        
        if user_class == 'customer':
            new_user = Customer(username, email, password, *args)
        elif user_class == 'admin':
            new_user = Admin(username, email, password, *args)
        else:
            return "Ошибка: Неверный тип пользователя."
        
        return f"Пользователь {username} успешно зарегистрирован."
    
    def login(self, username, password):
        """
        аутентифицирует пользователя, проверяя его пароль, и
        генерирует токен сессии. Возвращает сообщение об успехе или ошибке.
        """
        user = next((user for user in User.users if user.username == username), None)
        if user and User.check_password(user.password, password):
            self.current_user = user
            self.current_token = uuid.uuid4().hex
            return f"Пользователь {username} успешно вошел в систему."
        return "Ошибка: Неверное имя пользователя или пароль."
    
    def logout(self):
        """
        Выход пользователя из системы.
        """
        if self.current_user is not None:
            username=self.current_user.username
            self.current_user = None
            self.current_token=None
            return f"Пользователь {username} успешно вышел из системы."
        return "Ошибка: Нельзя выйти из системы, так как пользователь отсутствует."
    

    

  