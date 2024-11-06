from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import insert, select, delete

import datetime

from backend.db import SessionLocal
from models import *


app = Flask(__name__)
app.secret_key = 'my-secret-key'

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/', methods=['post', 'get'])
def login():

    with SessionLocal() as db:
        info = {}

        # Если GET
        if request.method == 'GET':
            pass

        # Если POST
        if request.method == 'POST':

            # Получаем данные из формы
            username = request.form.get('username')
            password = request.form.get('password')

            # Если не все поля заполнены
            if username != '' and password != '':
                user = db.scalar(select(Users).where(Users.username == username))
                # Пользователь существует
                if user is not None:
                    # Пароли совпадают
                    if check_password_hash(user.password, password):
                        session['username'] = user.username
                        session['user_id'] = user.id
                        return redirect('/main_page/')
                    else:
                        info.update({'error': 'Неверный пароль!'})
                else:
                    info.update({'error': 'Неверный логин!'})
            else:
                info.update({'error': 'Заполните все поля!'})

        # Ответ
        return render_template('Authorisation/login.html',
                               info=info,
                               title='Авторизация',
                               title_command='Войдите в ваш профиль!',
                               href='/')

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/registration/', methods=['post', 'get'])
def registration():

    with SessionLocal() as db:
        info = {}

        # Если GET
        if request.method == 'GET':
            pass

        # Если POST
        if request.method == 'POST':

            # Получаем данные из формы
            username = request.form.get('username')
            password = request.form.get('password')
            repeat_password = request.form.get('repeat_password')

            # Если не все поля заполнены
            if username != '' and password != '' and repeat_password != '':
                user = db.scalar(select(Users).where(Users.username == username))
                # Пользователь новый
                if user is None:
                    # Пароли совпадают
                    if password == repeat_password:
                        db.execute(insert(Users).values(username=username, password=generate_password_hash(password)))
                        db.commit()
                        return redirect('/')
                    else:
                        info.update({'error': 'Пароли не совпадают!'})
                else:
                    info.update({'error': f'Логин {username} занят!'})
            else:
                info.update({'error': 'Заполните все поля!'})

        # Ответ
        return render_template('Authorisation/registration.html',
                               info=info,
                               title='Регистрация',
                               title_command='Заполните форму!',
                               href='/')

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/main_page/', methods=['post', 'get'])
def main_page():

    with SessionLocal() as db:

        # Если GET
        if request.method == 'GET':
            pass

        # Ответ
        post_list = []
        for i in db.scalars(select(Posts)).all():
            post_list.append(i)
        post_list.reverse()

        if request.method == 'GET':
            return render_template('main_base/main_page.html',
                                   title='Главная страница',
                                   user=session["username"],
                                   href_main='#',
                                   href_prof='/your_profile',
                                   post_list=post_list,)

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/your_profile/', methods=['post', 'get'])
def your_profile():

    with SessionLocal() as db:

        # Если GET
        if request.method == 'GET':
            pass

        # Если POST
        if request.method == 'POST':
            if 'delete' in request.form:
                print('-------id--------', request.form.get('delete'))
                db.execute(delete(Posts).where(Posts.id == request.form.get('delete')))
                db.commit()

        # Ответ
        post_list = []
        for i in db.scalars(select(Posts).where(Posts.user_id == session["user_id"])):
            post_list.append(i)
        post_list.reverse()

        return render_template('main_base/your_profile.html',
                               title='Ваш профиль',
                               user=session["username"],
                               href_main='/main_page',
                               href_prof='#',
                               post_list=post_list, )

#-----------------------------------------------------------------------------------------------------------------------

@app.route('/your_profile/create_post/', methods=['post', 'get'])
def create_post():

    with SessionLocal() as db:
        info = {}

        # Если GET
        if request.method == 'GET':
            pass

        # Если POST
        if request.method == 'POST':

            # Получаем данные из формы
            title = request.form.get('title')
            description = request.form.get('description')

            # Если не все поля заполнены
            if title != '' and description != '':
                db.execute(insert(Posts).values(title=title,
                                                description=description,
                                                date_of_creation=datetime.date.today(),
                                                user_id=session["user_id"],))
                db.commit()
                return redirect('/your_profile/')
            else:
                info.update({'error': 'Заполните все поля!'})

        # Ответ
        return render_template('make_post/create_post.html',
                               info=info,
                               title='Создание поста',
                               title_command='Заполните форму!',
                               href='/your_profile')