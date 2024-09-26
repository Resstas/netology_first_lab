import os

# Сбрасываем все изменения в отслеживаемых файлах
os.system('git reset --hard')

# Удаляем все неотслеживаемые файлы и директории
os.system('git clean -fd')