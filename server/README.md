# server development

``` bash
# install dependencies
pip install -r requirements.txt

# setup development database
python manage.py makemigrations api --noinput
python manage.py migrate --noinput

# load data
python manage.py createsuperuser --username=root --email=root@example.com --noinput
python manage.py create_fixtures

# run development server
python manage.py runserver --settings=server.settings
```

**Note:** You should install [pipenv](https://docs.pipenv.org/) before installing any python dependencies.
