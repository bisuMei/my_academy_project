# my_academy_project
Для установки следует сделать следующее:
  Если не установлен pip:
      Следующие инструкции подойдут для Windows 7, Windows 8.1 и Windows 10.

      Скачайте установочный скрипт get-pip.py. 
      
      https://bootstrap.pypa.io/get-pip.py

      В любом случае щелкайте правой кнопкой мыши на ссылке и нажмите “Сохранить как…” 
      и сохраните скрипт в любую безопасную папку, например в “Загрузки”.
      Откройте командную строку и перейдите к каталогу с файлом get-pip.py.
      Запустите следующую команду: python get-pip.py
  Далее: 
  Делаем клон с  проекта с git
  Далее:
  1. pip install django
  2. активируй виртуальное окружение: python -m venv myvenv
                                      myenv/bin/activate
  3. установи зависимости: pip install -r requirements.txt
  4. проведи миграции: python manage.py makemigrations
                       python manage.py migrate
  5. cоздай superuser:   python manage.py createsuperuser
  5. запусти локальный сервер python manage.py runserver
  
  Ну и всё)
