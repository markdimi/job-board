# Take home project
## job board

### For this task the following technologies where used

 - Python and Django for the backend.
 - PostgreSQL for the required database.
 - Bootstrap and JavaScript for the frontend.
 - Docker & docker-compose for setting up the development environment (optional).

### Setting up the environment

#### For the backend you'll need the following:

- Python (3.5>) and the following packages:
    - Django, psycopg2-binary, djangorestframework, requests and django-cors-headers
- PostgreSQL with a database, user and its password, all set to 'postgres' (as it’s defined in the settings.py file in the DATABASES section).
    - Otherwise if your database setup is different you’ll need to change the settings accordingly. 
- Then you can clone this project. The django project's name is `jobs_coard` and `core` is the name of the app.
- Now you can run the migrations for the 'Searches' model to take place. 
    - 'python manage.py makemigrations core'
    - 'python manage.py migrate'
- (Optional) You can also create a superuser to access Django's admin where you could observe the `Searches` model.
    - `python manage.py createsuperuser`
- Lastly you can run django server in port '9898' 
    - 'python manage.py runserver 0.0.0.0:9898'

#### For the frontend

- The frontend is an `html` file inside the `Simple frontend` folder.
- You will need an http server for serving the file in port '8000'
    - I used Python's Simple HTTP Server: 'python -m http.server'

### Execution

Now you can navigate to `0.0.0.0:8000` and you will see the form where you can choose a description and a location. With every search, the Django API is fetching results from Github's Jobs API and saves the client's data (description, location, ip and time) in the `Searches` model (and in a db table with the same name). 

### Final notes

Using Django for a project like this could be an overkill. However I used it because of my familiarity with it and its powerfull tools. Especially the Models API where you can create models that represent your data. Alternatively I could create a table inside the database and write all the logic in PHP or Node.

Also I could fetch Github's results directly from the frontend. Instead now, I get the form data in the backend and fetch the results from there.