mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

check:
	flake8 .
	isort .

loaddata:
	python3 manage.py loaddata users
	python3 manage.py loaddata category
	python3 manage.py loaddata product
