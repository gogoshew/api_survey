# API for user surveys
Задача: спроектировать и разработать API для системы опросов пользователей


### Документация API (автодокументирование на swagger (drf-yasg) доступно по адресу http://127.0.0.1:8000/swagger/ )

## Описание ТЗ:

### _Функционал для администратора системы:_
- авторизация в системе (регистрация не нужна)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

### _Функционал для пользователей системы:_
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя


## Окружение проекта:
  * python 3.8
  * Django 4.0.3
  * djangorestframework

Склонируйте репозиторий с помощью git

    https://github.com/gogoshew/api_survey.git
Перейти в папку:
```bash
cd survey_api_drf
```
Создать и активировать виртуальное окружение Python.

Установить зависимости из файла **requirements.txt**:
```bash
pip install -r requirements.txt
```

# Выполнить следующие команды:

* Команда для создания миграций приложения для базы данных
```bash
python manage.py makemigrations
python manage.py migrate
```
* Создание суперпользователя
```bash
python manage.py createsuperuser
```
Будут выведены следующие выходные данные. Введите требуемое имя пользователя, электронную почту и пароль:

```bash
Username (leave blank to use 'admin'): admin
Email address: admin@admin.com
Password: ********
Password (again): ********
Superuser created successfully.
```
* Команда для запуска приложения
```bash
python manage.py runserver
```
* Приложение будет доступно по адресу: http://127.0.0.1:8000/


### _Документация API_ (создал автодокументирование API на swagger доступно по адресу http://127.0.0.1:8000/swagger/)
### Авторизация пользователя: 
* Request method: GET
* URL: http://127.0.0.1:8000/api/drf-auth/login/
* Body: 
    * username: 
    * password: 


### Просмотр существующих опросов или создание нового:
* Request method: GET, POST
* URL: http://127.0.0.1:8000/api/survey/
* Body:
    * survey_name: Название опроса
    * pub_date: Дата и время публикации опроса, format: YYYY-MM-DD HH:MM:SS
    * end_date: Дата и время окончания опроса, format: YYYY-MM-DD HH:MM:SS
    * survey_description: Описание опроса
    

### Обновить или удалить опрос:
* Request method: GET, PUT, PATCH, DELETE
* URL: http://127.0.0.1:8000/api/survey/[survey_id]/
* Param:
    * survey_id


### Просмотр существующих вопросов или создание нового:
* Request method: GET, POST
* URL: http://127.0.0.1:8000/api/question/
* Body:
    * type_choices: предоставляет только три варианта вопросов
    * survey: id опроса
    * question_text: 
    * question_type:


### Обновить или удалить вопрос:
* Request method: GET, PUT, PATCH, DELETE
* URL: http://127.0.0.1:8000/api/question/[question_id]/
* Param:
    * question_id
* Body:
    * type_choices: предоставляет только три варианта вопросов
    * survey: id опроса
    * question_text: 
    * question_type:
    

### Просмотр существующих ответов или создание нового:
* Request method: GET, POST
* URL: http://127.0.0.1:8000/api/answer/
* Body:
    * user: id пользователя
    * question: id вопроса
    * choice: список вариантов ответа
    * answer_text: поле для текстового ответа


### Обновить или удалить ответ:
* Request method: GET, PUT, PATCH, DELETE
* URL: http://127.0.0.1:8000/api/answer/[answer_id]/
* Param:
    * answer_id
* Body:
    * user: id пользователя
    * question: id вопроса
    * choice: список вариантов ответа
    * answer_text: поле для текстового ответа


### Просматриваем ответы пользователя:
* Request method: GET
* URL: http://127.0.0.1:8000/api/user_answers/
