# Импортируем библиотеку subprocess
import subprocess
# Определяем функцию git_config_list, которая будет выполнять команду Git 
# (нужно в консоль вывести результат работы команды git: git config --global --list)
def git_config_list():
    result = subprocess.run(
        ["git", "config", "--global", "--list"], 
        capture_output=True, 
        text=True
    )
 
    # Выводим результат
    print("Настройки Git:")
    print(result.stdout)

# Запуск функции
git_config_list()
    

# вызываем git_config_list()
