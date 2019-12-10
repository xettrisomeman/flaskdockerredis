# SImple flask app using redis and docker

## Docker-compose.yml

```docker
version: '3.7'

services:
    web:
        build: .
        ports:
            - 5000:5000

    redis:
        image: redis
```

## version- it states which version of dockercompose you want to use

## services: it is second thing we write after writing version in our docker-compose file

## Then we write our app name , here ive given it (Web)

## Build-> it means which files we are going to use to build the app. Here i am using the files from current directory

## ports-> the ports we are using to run our app

## we give redis name to our second app which uses image redis

## image-> it means download images from docker hub for later use. we are downloading redis image because our app uses redis images
