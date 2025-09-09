# 1. Базовый класс User и производные классы для различных типов пользователей

import hashlib
import uuid

class User:
    """
    Базовый класс, представляющий пользователя.
    """
    users = [] # Список для хранения всех пользователей
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.hash_password(password)
        User.users.append(self)
        
    @staticmethod
    def hash_password(password):
        """
        Хеширование пароля с использованием SHA-256 и соли.
        """
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
    
    @staticmethod
    def check_password(stored_password, provided_password):
        """
        Проверка пароля.
        """
        password, salt = stored_password.split(':')
        return password == hashlib.sha256(salt.encode() + provided_password.encode()).hexdigest()

    def get_details(self):
        """
        Метод для получения деталей пользователя.
        """
        return {
            'username': self.username,
            'email': self.email
        }
    
class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """

    def __init__(self, username, email, password, address):
        super().__init__(username, email, password)
        self.address = address
    
    def get_details(self):
        details = super().get_details()
        details.update({'address': self.address})
        return details
    
class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, password, admin_level):
        super().__init__(username, email, password)
        self.admin_level = admin_level
    
    def get_details(self):
        details = super().get_details()
        details.update({'admin_level': self.admin_level})
        return details
    
    @staticmethod
    def list_users(auth_service):
        """
            Выводит список всех пользователей.
        """
        if auth_service.current_user is None or not isinstance(auth_service.current_user, Admin):
            return "Ошибка: Только администратор может просматривать список пользователей." 
        else :
            return [user.get_details() for user in User.users]
    
    @staticmethod
    def delete_user(username, auth_service):
        """
        Удаляет пользователя по имени пользователя.
        """
        if auth_service.current_user is None or not isinstance(auth_service.current_user, Admin):
            return "Ошибка: Только администратор может удалять пользователей."  
        elif auth_service.current_user.username == username:
            return "Ошибка: Администратор не может удалить сам себя."
        else:   
            user_to_delete = next((user for user in User.users if user.username == username), None)
            if user_to_delete:
                User.users.remove(user_to_delete)
                return f"Пользователь {username} успешно удален."
            return "Ошибка: Пользователь не найден."

