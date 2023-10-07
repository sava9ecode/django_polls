# Polls

Polls is a Django app to conduct web-based polls. For each question,
visitors can choose between a fixed number of answers.

Detailed documentation is in the "[docs](https://docs.djangoproject.com/en/4.2/)" directory.

# Quick start

1. Make sure that your virtual env is activated.
2. Run the following commands (if you're on Windows you may use ```py``` or ```py -3``` instead of ```python``` to start Python):
```
pip3 install -r requirements.txt
python3 manage.py migrate
python3 manage.py test # Run the standard tests. These should all pass.
python3 manage.py createsuperuser # Create a superuser.
python3 manage.py runserver
```
4. Open a browser to ```http://127.0.0.1:8000/admin/``` to open the admin site.
5. Create a few test objects of each type.
6. Open tab to ```http://127.0.0.1:8000``` to see the main site, with your new objects.
