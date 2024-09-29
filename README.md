
```shell
docker run --name db_docker -e POSTGRES_USER=my_django -e POSTGRES_PASSWORD=pass_my_django -e POSTGRES_DB=my_django -p 5432:5432 -d postgres

pip install django
pip install djangorestframework
pip install -r requirements.txt

django-admin startproject myproject .
python manage.py startapp blog

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --username horse --email vadongera@gmail.com
python manage.py runserver
python manage.py runserver 127.0.0.1:8000 --settings=myproject.settings

docker compose build
docker compose up -d

```