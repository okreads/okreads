# Ok reads



## To use through docker:

docker-compose up

## To install new libs:

docker-compose build
docker-compose down
docker-compose up


## Create database

docker-compose exec web python cli.py create-database
docker-compose exec web python cli.py import-open-library --limit 100

## Enter the python container:

docker-compose exec web bash


## Running the webserver locally


FLASK_ENV=development FLASK_APP=app.py python app.py
python3 cli.py --dumpfile ~/Desktop/ol_dump_works_2019-09-30.txt


## The website is served locally at:

```
http://localhost:5000/
```
