# Web-приложение для сайта постов

## Необходимые связи:

* alembic==1.14.0
* blinker==1.8.2
* click==8.1.7
* colorama==0.4.6
* Flask==3.0.3
* greenlet==3.1.1
* itsdangerous==2.2.0
* Jinja2==3.1.4
* Mako==1.3.6
* MarkupSafe==3.0.2
* SQLAlchemy==2.0.36
* typing_extensions==4.12.2
* Werkzeug==3.1.2
  
![image](https://github.com/user-attachments/assets/789f12f4-6be1-4f8d-a75e-75ef6a90ba43)

## Возможности:

### 1. Идентификация:
   * Регистрация пользователя с хешированием пароля;
     
   ![image](https://github.com/user-attachments/assets/f88c6c64-e073-4d4d-857c-d3f5a827dbc5)

   * Однофакторная аутентификация пользователя;
  
   ![image](https://github.com/user-attachments/assets/cf01b59f-1cdf-4ea7-8e58-79e884601ba2)

   * Хранение пользовательской информации в базе данных.

   ![image](https://github.com/user-attachments/assets/c4dc6b72-0471-472c-a2cb-2f2244024263)
   
### 2. Посты:
   * Хранение постов в базе данных;
  
   ![image](https://github.com/user-attachments/assets/3ca2482a-56dd-4454-b0fc-e6f9e67b5443)

   * Связь пользователя с постом (один к многим).
### 3. Стена:
   * Стена (страница с полем размещения всех постов);

   ![image](https://github.com/user-attachments/assets/58a57ef2-62f5-4ca1-8eb3-842f13287094)

### 4. Профиль пользователя:
   * Создание постов;

   ![image](https://github.com/user-attachments/assets/d9646bb9-2828-4824-83ab-0a5cf49bc04a)

   * Удаление постов;
   * Стена (страница с полем размещения своих постов).

   ![image](https://github.com/user-attachments/assets/70c8b3c3-b3b8-4c57-b287-cfe0b070d197)

## Шаблоны страниц:

### 1. Authorisation 
   * base.html - базовый шаблон для идентификации пользователей;
   * login.html - шаблон страницы авторизации;
   * registration.html - шаблон страницы регистрации.

### 2. main_base
   * base.html - базовый шаблон для страниц с постами;
   * main_page.html - шаблон главной страницы с постами;
   * your_profile.html - шаблон страницы профиля.

### 3. make_post
   * base.html - базовый шаблон для страницы создания постов;    
   * create_post.html - шаблон страницы создания постов.
