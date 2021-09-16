## Setup
- Clone the repository 
```
git clone https://github.com/L0czi/img_api.git
```

- Run docker images
```
docker-compose up
```

- Go inside WEB container
```
docker ps //list all conteiners
```

- Make your migrations
```
python manage.py makemigrations
python manage.py migrate
```

- Create a new superuser
```
python manage.py createsuperuser
```

- Final checks
```
python manage.py runserver
```
- Open in your browser
```
http://127.0.0.1:8000/
```
