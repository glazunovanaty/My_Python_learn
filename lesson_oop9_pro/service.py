# 3. Сервис аутентификации и авторизации
from classes.users import Customer, Admin
from classes.authenticationService import AuthenticationService

auth_service = AuthenticationService()


# Регистрируем пользователей
print(auth_service.register('customer', "Nataly","glazunova.naty@gmail.com", "123321", "Rostov, Russia"))
print(auth_service.register('admin', "root", "admin@admin.ru", "rootpass", 1))
print()

# Пытаемся зарегистрировать пользователя с уже существующим именем
print(auth_service.register('customer', "Nataly", "аааа@aaa.ru", "123321", "Rostov, Russia"))

# Пытаемся войти с неправильным паролем
print(auth_service.login("Nataly", "wrongpassword"))
# Входим с правильным паролем
print(auth_service.login("Nataly", "123321"))
# Получаем текущего пользователя
current_user = auth_service.get_current_user()
if current_user!=None:
    print("Текущий пользователь:", current_user.get_details())
else:   
    print(current_user)
# Выходим из системы
print(auth_service.logout())        
# Пытаемся получить текущего пользователя после выхода
print(auth_service.get_current_user()) 
# Пытаемся выйти из системы, когда пользователь уже вышел
print(auth_service.logout())                        

# Входим как администратор
print(auth_service.login("root", "rootpass"))
# Получаем список всех пользователей
print("Список всех пользователей:", Admin.list_users(auth_service))
# Удаляем пользователя Nataly
print(Admin.delete_user("Nataly",auth_service))
# Получаем список всех пользователей после удаления
print("Список всех пользователей после удаления Nataly:", Admin.list_users(auth_service))
#Выходим из системы
print(auth_service.logout())                

# Пытаемся получить список пользователей без входа в систему
print(Admin.list_users(auth_service))
# Пытаемся удалить пользователя без входа в систему
print(Admin.delete_user("root",auth_service))                    
# Пытаемся войти с неправильным именем пользователя
print(auth_service.login("nonexistent", "nopass"))
# Пытаемся зарегистрировать пользователя с неверным типом
print(auth_service.register('invalid_type', "user", "1","pass"))        
#Создаем еще одного пользователя
print(auth_service.register('customer', "Alex","alex@gmail.com", "123321", "Moscow, Russia"))   
# Входим как Alex
print(auth_service.login("Alex", "123321"))
# Пытаемся получить список пользователей как неадминистратор
print(Admin.list_users(auth_service))
# Пытаемся удалить пользователя как неадминистратор
print(Admin.delete_user("root",auth_service))
# Выходим из системы
print(auth_service.logout())    

# Входим как администратор
print(auth_service.login("root", "rootpass"))
# Получаем список всех пользователей
print("Список всех пользователей:", Admin.list_users(auth_service))
# Удаляем пользователя Alex
print(Admin.delete_user("Alex",auth_service))
# Получаем список всех пользователей после удаления
print("Список всех пользователей после удаления Alex:", Admin.list_users(auth_service))
# Удаляем сам себя
print(Admin.delete_user("root",auth_service))
# Удаляем пользователя Alex (который уже не существует)
print(Admin.delete_user("Alex",auth_service))
# Выходим из системы
print(auth_service.logout())


