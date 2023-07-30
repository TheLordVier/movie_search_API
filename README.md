## Movie search API (the API allows you to register, log into your account, retrieve movies, directors and genres)

Project developed by: Mikhailov Alexander

## Application structure:

**app.py** - *основное приложением*

**setup_db.py** - *объект SQLAlchemy, который используется в приложении*

**config.py** - *настройки конфигурации приложения*

**constants.py** - *константы приложения*

**decorators.py** - *декораторы доступа приложения*

**implemented.py** - *файл для создания DAO и сервисов, чтобы импортировать их везде*

**movies.db** - *база данных с таблицами (фильмы, режиссёры, жанры и пользователи)*

**requirements.txt** - *зависимости приложения*

**.gitignore** - *файлы и папки для игнорирования в системе контроля версий Git*

**test_api.http** - *файл для тестирования http-запросов нашего приложения (API)*

- **Директория dao** - *Файлы для доступа к данным (DAO)*
    - **director.py** - *Data Access Object для режиссёра* <br>
    - **genre.py** - *Data Access Object для жанра* <br>
    - **movie.py** - *Data Access Object для фильма* <br>
    - **user.py** - *Data Access Object для пользователя* <br>
      **Директория model** - **Модели и их схемы**
        - **director.py** - *Модель и схема для режиссера* <br>
        - **genre.py** - *Модель и схема для жанра* <br>
        - **movie.py** - *Модель и схема для фильма* <br>
        - **user.py** - *Модель и схема для пользователя* <br>

- **Директория service** - *Бизнес логика приложения в виде классов*
    - **director.py** - *Класс DirectorService* <br>
    - **genre.py** - *Класс GenreService* <br>
    - **movie.py** - *Класс MovieService* <br>
    - **user.py** - *Класс UserService* <br>
    - **auth.py** - *Класс AuthService* <br>

- **Директория tests** - *Все тесты приложения*
    - **conftest.py** - *файл с фикстурами для модуля pytest* <br>
      **Директория test_service** - **тесты для сервисов**
        - **test_director.py** - *тесты pytest для режиссера* <br>
        - **test_genre.py** - *тесты pytest для жанра* <br>
        - **test_movie.py** - *тесты pytest для фильма* <br>

- **Директория views** - *Все представления (views) приложения*
    - **directors.py** - *Представления (view) с режиссёрами* <br>
    - **genres.py** - *Представления (view) с жанрами* <br>
    - **movies.py** - *Представления (view) с фильмами* <br>
    - **users.py** - *Представления (view) с пользователями* <br>
    - **auth.py** - *Представления (view) для аутентификации пользователей* <br>