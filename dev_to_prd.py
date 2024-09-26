import os

# Переход на ветку prd
os.system('git checkout prd')

# Обновление ветки prd
os.system('git pull origin prd')

# Слияние изменений из dev в prd
os.system('git merge dev')

# Установка тэга (аргумент передается через командную строку)
tag = input("Введите имя тэга: ")
os.system(f'git tag {tag}')

# Отправка изменений и тэга на сервер
os.system('git push origin prd')
os.system(f'git push origin {tag}')
