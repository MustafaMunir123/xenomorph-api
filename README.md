
# xenomorph-api


### Getting started and running locally:


Make directory
```bash
  mkdir xenomorph_api
```
```bash
  cd xenomorph_api
```

Initialized empty git repository
```bash
  git init
```

Set remote origin
```bash
  git remote add origin https://github.com/MustafaMunir123/xenomorph-api.git
```
------------If above command does not work, then run---------------
```bash
  git pull https://github.com/MustafaMunir123/xenomorph-api.git master
```
-----------------------Otherwise-----------------------

```bash
  git pull origin master
```

Install packages
```bash
  pip install -r requirements.txt
```
Make database migrations
```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```

Run django-backend
```bash
  python manage.py runserver
```
