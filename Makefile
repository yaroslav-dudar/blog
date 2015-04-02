run:
	python manage.py runserver

dump:
	python manage.py dumpdata --format=json polls > initial_data.json

syncdb:
	python manage.py syncdb --noinput

