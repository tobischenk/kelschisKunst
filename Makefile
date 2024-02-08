run:
	python manage.py runserver

tailwind:
	python manage.py tailwind start

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser --noinput
