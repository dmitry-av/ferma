## Запуск
Перед запуском надо задать переменную docker.env в корне проекта со следующим содержимым:

> SECRET_KEY = *любое*  
> DB_NAME = postgres  
> DB_USERNAME = postgres   
> DB_PASSWORD = postgresword  
> DB_HOST = db  
> DB_PORT = 5433   
> SITE_URL="http://localhost"  
> ALLOWED_HOSTS = "*"  
> DEBUG = True   
> EMAIL_HOST = *хост для отправки email, например*  'smtp-mail.outlook.com'   
> EMAIL_PORT = *порт для хоста отправки email, например* 587 
> EMAIL_HOST_USER = *учетная запись email*   
> EMAIL_HOST_PASSWORD = *пароль учетной записи*

Затем запуск через docker-compose:

    docker-compose -f docker-compose.yml --env-file ./docker.env up --build
