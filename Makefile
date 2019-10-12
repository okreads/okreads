#this file is for human consumption never do scripting over this file, rather use the commands this file use directly

#docker commands below

docker_create_databse:
	docker-compose exec web python cli.py create-database


docker_import_works:
	docker-compose exec web python cli.py import-open-library --limit 100

docker_import_authors:
	docker-compose exec web python cli.py import-open-library-authors

docker_downup:
	docker-compose down
	docker-compose up

docker_update_dependenceis:
	docker-compose build
	make docker_downup


#local development commands below
local_install:
	sudo pip install -r requirements.txt

# local_web:
# 	gunicorn -t 500 --worker-class eventlet -w 2 --access-logfile - -b 0.0.0.0:8080 app:app


# all things production
production_deploy:
	gcloud app deploy
