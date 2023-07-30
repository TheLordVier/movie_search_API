## Movie search API (the API allows you to register, log into your account, retrieve movies, directors and genres)

Project developed by: Mikhailov Alexander

## Application structure:

**app.py** - *main application*

**setup_db.py** - *SQLAlchemy object that is used in the application*

**config.py** - *application configuration settings*

**constants.py** - *application constants*

**decorators.py** - *application access decorators*

**implemented.py** - *file to create DAO and services to import them everywhere*

**movies.db** - *database with tables (movies, directors, genres and users)*

**requirements.txt** - *application dependencies*

**.gitignore** - *files and folders to ignore in the Git version control system*

**test_api.http** - *file for testing http requests of our application (API)*

- **Directory dao** - *Data Access Files (DAO)*
    - **director.py** - *Data Access Object for director* <br>
    - **genre.py** - *Data Access Object for genre* <br>
    - **movie.py** - *Data Access Object for movie* <br>
    - **user.py** - *Data Access Object for user* <br>
      **Directory model** - **Models and their schemes**
        - **director.py** - *Model and scheme for the director* <br>
        - **genre.py** - *Model and scheme for the genre* <br>
        - **movie.py** - *Model and scheme for the movie* <br>
        - **user.py** - *Model and scheme for the user* <br>

- **Directory service** - *Business logic of the application in the form of classes*
    - **director.py** - *Class DirectorService* <br>
    - **genre.py** - *Class GenreService* <br>
    - **movie.py** - *Class MovieService* <br>
    - **user.py** - *Class UserService* <br>
    - **auth.py** - *Class AuthService* <br>

- **Directory tests** - *All application tests*
    - **conftest.py** - *fixture file for pytest module* <br>
      **Directory test_service** - **service tests**
        - **test_director.py** - *pytest tests for director* <br>
        - **test_genre.py** - *pytest tests for genre* <br>
        - **test_movie.py** - *pytest tests for movie* <br>

- **Directory views** - *All views of the application*
    - **directors.py** - *Views with directors* <br>
    - **genres.py** - *Views with genres* <br>
    - **movies.py** - *Views with movies* <br>
    - **users.py** - *Views with Users* <br>
    - **auth.py** - *Views for user authentication* <br>