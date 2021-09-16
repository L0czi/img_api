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
docker exec -it {conteinder id} bash
```
- Inside conteiner migrete database
```
python manage.py migrate
```
- Inside conteiner create a new superuser
```
python manage.py createsuperuser
```
- Open in your browser
```
http://127.0.0.1:8000/admin
```
- After log in with your credentials, create new User.
- Next go to "ACCOUNTS" and assign new User to proper tier.
- Log out and go back to:
```
http://127.0.0.1:8000/
```
- Log in to your user account
- Send a picture with Postman (remember about authorisation) to endpoint: 
```
http://127.0.0.1:8000/api/upload/
```
