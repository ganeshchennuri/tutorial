# Steps to host django apps on Pythonanywhere

- Signup on [PythonAnywhere](https://www.pythonanywhere.com/) and setup username.
- Go to Console and select bash, clone your repo, cloning repo into users_proj directory

    > git clone https://github.com/ganeshchennuri/users-auth.git ./users_proj

- Create and activate Virtual environment
    > mkvirtualenv --python=/usr/bin/python3.8 mysite-virtualenv

- Install Project requirements
    > cd users_proj

    > pip install -r requirements.txt

- Go to homepage and open webapps, Select Manual Config
    - Change SourceCode dir in Code section
        /home/G4n3Sh/users_proj
    - set virtualenv directory
        /home/G4n3Sh/.virtualenvs/mysite-virtualenv
    - Open Wsgi Configuration file delete all the code and add below snippet, change project path & settings location in environment variable
        ```python
        import os
        import sys

        # assuming your Django settings file is at '/home/myusername/G4n3Sh/settings.py'
        path = '/home/G4n3Sh/users_proj'
        if path not in sys.path:
            sys.path.insert(0, path)

        os.environ['DJANGO_SETTINGS_MODULE'] = 'users_proj.settings'

        # for Django >=1.5:
        from django.core.wsgi import get_wsgi_application
        application = get_wsgi_application()
        ```
- come back to console and make migrations
    > chmod +x manage.py

    > ./manage.py migrate

- Go to Web and click on reload you app
    - go to files section and open manage.py in project directory, add to allowed hosts and save.
        ALLOWED_HOSTS = ['g4n3sh.pythonanywhere.com', ]
- Now the application is hosted successfully, but static file path need to be set in order to use static files.
    | URL            | Directory    |
    | :------------- | :---------- |
    |  C/static/ | /home/G4n3Sh/users_proj/static   |
    | /static/admin   | /home/G4n3Sh/.virtualenvs/mysite-virtualenv/lib/python3.8/site-packages/django/contrib/admin/static/admin |

- we need to setup admin static file directory, without that admin page won't be able to access static files and UI gets weird not user friendly.		 
    		 
