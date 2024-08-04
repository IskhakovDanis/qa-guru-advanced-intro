
# ДЗ №1 QA.GURU | Python Advanced 

1. Разработать несколько API-автотестов на https://reqres.in (если обучались на основном курсе python - можно взять код автотестов из домашнего задания)

Можно также за основу взять https://github.com/qa-guru/qa_guru_python_9_19

2. Вместо https://reqres.in разработать свой микросервис в стеке Python + FastAPI (допускается также Flask, Django).
Пример - https://github.com/qa-guru/python-advanced-intro

- Автотесты должны также успешно проходить.

- В коде микросервиса не должно быть хардкода.
  - Например, не должно быть эндпоинтов типа /api/users/2 -  правильнее /api/users/{user_id}

3. Данные для ответа пока что можно хранить в текстовом файле, в следующих занятиях мы перенесем их в базу данных

4. Желательно оформить README.md - https://school.qa.guru/teach/control/stream/view/id/465999013 в тренинге есть несколько занятий по оформлению красивой документации.


В качестве ответа нужно приложить ссылку на код в github (как микросервис, так и тесты можно в одном репозитории)
## Технологии
1. Микросервис: FastAPI
2. Тесты: Pytest, Requests

## Запросы
#### Получение списка пользователей 
###### GET /api/users
#### Получение информации по конкретному пользователю 
###### GET /api/users/{user_id}
#### Создание пользователя 
###### POST /api/users
```
{
    "name": "example_name",
    "job": "exaple_job"
}
```
#### Обновление данных по пользователю 
###### PUT /api/users/{user_id}
```
{
    "name": "Гаврила",
    "job": "Почтальон"
}
```
#### Обновление данных по пользователю 
###### PATCH /api/users/{user_id}
```
{
    "name": "Гаврила",
    "job": "Охотник"
}
```
#### Удаление пользователя 
###### DELETE /api/users/{user_id}

## Запуск проекта (локально)
1. python -m venv venv
2. source venv/Scripts/activate
3. pip install -r requirements.txt
4. uvicorn main:app —reload
5. pytest
