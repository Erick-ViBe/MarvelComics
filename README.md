# Marvel Comics
Microservice for user management(Marvel Comics).

> FastAPI

## Table of contents
* [Technologies](#technologies)
* [Requirements](#requirements)
* [Setup](#setup)
* [Run Project](#run-project)
* [Documentation](#documentation)
* [Contact](#contact)

<p align='center'>
  <img src="https://p4.wallpaperbetter.com/wallpaper/830/235/606/comics-marvel-comics-daredevil-deadpool-wallpaper-preview.jpg" width="500" >
</p>

## Technologies
* Python
* FastAPI
* Docker
* MongoDB
* Swagger UI Documentation

## Requirements
* Git
* Python
* Docker
* MongoDB

## Setup
1. Clone and enter the repository:\
`git clone https://github.com/Erick-ViBe/MarvelComics.git`\
`cd MarvelComics`

2. Set .env file:\
`cp env.template .env`
> Set credentials in .env file

3. Build docker container:\
`docker build -t marvel_comics .`


## Run Project
`docker run -d --name marvel_comics -p 80:80 marvel_comics`
> To see docs visit http://localhost/docs

## Documentation
* [@Swagger UI](http://localhost/docs)
* [@JSON](http://localhost/openapi.json)

## Contact
Created by [@ErickViBe](https://erickvibe.xyz/) - feel free to contact me!
