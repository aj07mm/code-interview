run:
	docker-compose up -d
	docker-compose run flask python src/populate_database.py 0
populate_database:
	docker-compose run flask python src/populate_database.py 0
test:
	docker-compose run flask pytest src/tests
