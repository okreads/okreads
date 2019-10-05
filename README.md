# Ok reads


## To use through docker:

docker-compose up

## To install new libs:

docker-compose build


## Enter the python container:

docker-compose exec web bash


## Running the webserver locally


FLASK_ENV=development FLASK_APP=app.py python app.py
python3 cli.py --dumpfile ~/Desktop/ol_dump_works_2019-09-30.txt
