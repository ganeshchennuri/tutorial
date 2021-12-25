# Django
- django install command line tool django-admin
```
    python -m venv env
    env/scripts/activate

    $ pip install django
    $ django-admin --version
    $ django-admin startproject basicProj
    $ cd basicProj
    $ python manage.py basicProj
```
- Project Directories
    - basicProj
    |- basicProj
      |- settings.py   -> app
      |- urls.py    -> all the url paths
      |- wsgi & asgi -> web-server gateway
    |- manage.py

- Django project is collection of django apps, multiple apps can be created in django project
    > python manage.py startapp firstapp
- App drectories
- basicProj
    |- basicProj
    |- firstapp
      |- migrations directory -> database specific info
      |- admin.py   -> config to admin interface
      |- apps.py    -> app configuration
      |- models.py  -> data models
      |- tests.py   -> test function
      |- views.py   -> handle requests and responses
    |- manage.py

- Creating and mapping index Page
    - go to settings.py in project dir & add app name in into installed app list
    - views.py in app folder, add function and return HttpResponse (import from django.http)
    - urls.py import views and add path to urlpatterns list (path('', views.index))

- Isloating urls of apps and projects
    ```python
    #Projects urls.py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('firstapp', include('firstapp.urls'))
    ]

    #firsapp urls.py
    from django.urls import path
    from firstapp import views

    urlpatterns = [
        path('', views.index, name='index'),
    ]
    ```
- templates
    - create templates directory in project dir (top dir), for separate templates of app create directories named as app name and add html templates
    - Create templatedir using basedir in settings.py (TEMPLATE_DIR = Path(BASE_DIR).joinpath('templates'))
    - add templatedir to templates list -> DIRS in settings.py
    - create function in apps views.py , add url in urls.py, template variables(dict) can be sent as context
        ```python
        #views.py
        def index(request):
            # return HttpResponse("<strong><em> Hell Yeah </em></strong>")
            cont_dict = {"boi": "Legendary"}
            return render(request, 'firstapp/index.html', context=cont_dict)
        ```
        ```python
        #url.py
        from django.urls import path
        from . import views

        urlpatterns = [
            path('', views.index, name='index'),
        ]
        ```
        ```html
        #templates/appname/index.html
        <!DOCTYPE html>
        <head>
            <meta charset="UTF-8">
            <title>First App Template</title>
        </head>
        <body>
            <h1>Hell Yeah</h1>
            <h2>foking template {{boi}} bitch</h2>
        </body>
        ```
    - Static Files
        - create static file dir similar to template dir 
        ```python
        #settings.py

        STATICFILE_DIR = Path(BASE_DIR).joinpath('static')

        STATICFILES_DIRS = [STATICFILE_DIR,]
        
        # Accesed at
        http://127.0.0.1:8000/static/images/overview.png
        ```
        - css files and loading static files to html pages

        ```html
        #firstapp/index.html
        <!DOCTYPE html>
        {% load static %}
        <html>
        <head>
            <meta charset="UTF-8">
            <title>First App Template</title>
            <link rel="stylesheet" href="{% static 'css/home.css' %}">
        </head>
        <body>
            <h1>Hell Yeah</h1>
            <h2>foking template {{boi}} bitch</h2>
            <img src="{% static 'images/overview.png' %}" alt="Didn't load Oerview of django"/>
        </body>
        </html

        #static/css/home.css
        h1{
            color: red;
        }
        ```
## Models
Models helps in creating manage database tables using ORM(Oject relational mapper)
- Creating model in project/app/models.py
    ```python
    from django.db import models
    from django.db.models.deletion import CASCADE

    # Create your models here.
    class Topic(models.Model):
        topic_name = models.CharField(max_length=200, unique=True)

        def __str__(self):
            return self.topic_name


    class Webpage(models.Model):
        topic = models.ForeignKey(Topic,on_delete=CASCADE)
        name = models.CharField(max_length=50, unique=True)
        url = models.URLField(unique=True)

        def __str__(self):
            return self.name   
    ```
- for forein key relationship on_delete is manadatory from django2
    - CASCADE   -> Deletes the records in referenced table(2nd table)
    - PROTECT   -> Protects the deletion of record in primary table(raise ProtectedError)
    - RESTRICT  -> Similar to protect, but restricts the deleting of record even if there's any CASCADE columns are available(raise RestrictedError)
    - SETDEFAULT-> value to default if row i primary table is deleted (eg users deleted, his comments  referenced to null or deleted user)
    - SETNULL   -> value to null 
    - SET       -> 
    - DO_NOTHING-> No action is taken leads to integrity issues in database

- Creating tables
    > python manage.py makemigrations

    > python manage.py migrate
- Inteacting with db using python shell
    > python manage.py shell
    ```
    >>> from firstapp.models import Topic
    >>> print(Topic.objects.all())
    >>> t1 = Topic(topic_name="Django tutorial")
    >>> t1.save()
    >>> print(Topic.objects.all())
        <QuerySet [<Topic: Django tutorial>]>
    ```
- registering models with with admin
    ```python
    from django.contrib import admin
    from .models import Topic, Webpage, AccessRecord

    admin.site.register(Topic)
    admin.site.register(Webpage)
    admin.site.register(AccessRecord)
    ```
- Accessing db and models through admin UI
    > python manage.py createsuperuser

        Username (leave blank to use 'gannu'): root
        Email address: root@test.com
        Password: 
        Password (again): 
    > python manage.py runserver
        http://127.0.0.1:8000/admin

- creating fake data or can be migration data
    > pip install faker

    ```python
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",'exercise2.settings')

    import django
    django.setup()

    from faker import Faker
    from people.models import Users

    fake = Faker()

    for _ in range(10):
        fake_name = fake.name()
        fake_first = fake_name.split(" ")[0]
        fake_last = fake_name.split(" ")[1]
        fake_email = fake.email()

        # Create Fake Data
        user = Users.objects.get_or_create(first_name = fake_first, last_name = fake_last, email = fake_email)[0]
    ```

## Django MVT (Model View Template)
- Creating model
    ```python
    #proj/app/models.py
    from django.db import models

    class Users(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        email = models.EmailField(max_length=100, unique=True)
    ```
- Creating View
    ```python
    #proj/app/views.py
    from django.shortcuts import render
    from .models import Users

    def index(request):
        return render(request,'people/index.html')

    def users(request):
        users = Users.objects.all()
        user_dict = {"Users": users}
        return render(request,'people/users.html', context=user_dict)
    ```
- templates
    ```html
    #proj/templates/app/users.html
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Users</title>
        </head>
        <body>
            <h1>Welcome! Here are your users</h1>
                {% if Users %}
                    <ol>
                        {% for user in Users %}
                            <li>Userinfo</li>
                            <ul>
                                <li>First Name : {{ user.first_name }}</li>
                                <li>Last Name : {{ user.last_name }}</li>
                                <li>Email : {{ user.email }}</li>
                            </ul>
                        {% endfor %}
                    </ol>
                {% else %}
                    <h3>No users Found</h3>
                {% endif %}
        </body>
    </html>
    ```
# Django Forms
- creating form using Django forms
    ```python
    #proj/formsapp/forms.py
    from django import forms

    class FormName(forms.Form):
        name = forms.CharField(max_length=50)
        email = forms.EmailField()
        text = forms.CharField(widget=forms.Textarea)
    ```
- templating django forms
    ```html
    #proj/templates/formsapp/form_page.html
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>FORMS</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-wEmeIV1mKuiNpC+IOBjI7aAzPcEZeedi5yW5f2yOq55WWLwNGmvvx4Um1vskeMj0" crossorigin="anonymous">
        </head>
        <body>
            <div class="container">
                <h1> Fill the Form!</h1>
                <form method="POST">
                    {% csrf_token %}
                    {{ form.as_p }}
                    <input type="submit" class="btn btn-primary" value="submit">
                </form>   
            </div>
        </body>
    </html>
    ```
- Validating for form input in views.py
    ```python
    from django.shortcuts import render
    from .forms import FormName

    def index(request):
        return render(request, 'formsapp/index.html')

    def forms(request):
        if request.method == "POST":
            form = FormName(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                text = form.cleaned_data['text']
                print(name, email, text)
        form = FormName()
        return render(request, 'formsapp/form_page.html', {"form": form})
    ```
- django form validators
    ```python
    from django import forms
    from django.core import validators
    from django.core.exceptions import ValidationError

    class FormName(forms.Form):
        name = forms.CharField(max_length=50, validators=[validators.minlength(4)])
        email = forms.EmailField()
        verify_email = forms.EmailField()
        text = forms.CharField(widget=forms.Textarea)

        def clean(self):
            all_clean_data = super().clean()
            email = all_clean_data['email']
            verify_email = all_clean_data['verify_email']

            if email != verify_email:
                raise ValidationError("Make Sure email and verify email mataches")
    ```
## ModelForms
- creating model in models.py
    ```python
    #models.py
    from django.db import models

    class User(models.Model):
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        email = models.EmailField(max_length=100, unique=True)
    ```
- creating model form by imprting model and creating metaclass
    ```python
    #forms.py
    from django import forms
    from .models import User

    class NewUserForm(forms.ModelForm):
        class Meta:
            model = User
            fields = '__all__'
    ```
- parsing the forms and saving to db
    ```python
    #viewspy
    from django.shortcuts import render
    from .forms import NewUserForm

    def index(request):
        return render(request, 'modelformsapp/index.html')

    def users(request):
        form = NewUserForm()
        if request.method == "POST":
            form = NewUserForm(request.POST)

            if form.is_valid():
                form.save(commit=True)
                return index(request)
        return render(request, 'modelformsapp/users.html',{"form": form})
    ```
- viewing form on template
    ```html
    #users.html
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>users</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-wEmeIV1mKuiNpC+IOBjI7aAzPcEZeedi5yW5f2yOq55WWLwNGmvvx4Um1vskeMj0" crossorigin="anonymous">
        </head>
        <body>
            <div class="container">
                <h1> Sign Up Boi!</h1>
                <br>
                <form method="POST">
                    {% csrf_token %} 
                    {{ form.as_p }}
                    <input type="submit" class="btn btn-primary" value="Submit">
                </form>
            </div>
        </body>
    </html>
    ```

## Relative URL Templating/Template Tagging
- creating a bse.html in templates which can be inhereted to other pages
- urls.py should contain an app_name which can be used in templates to tag other functions
    ```python
    #urls.py
    from django.urls import path
    from .views import index, other, relative

    app_name = "templates"

    urlpatterns = [
        path('', index, name='index'),
        path('other/', other, name='other'),
        path('relative/', relative, name='relative'),
    ]
    ```
- base.html should contain common elements across the applications like navbar, other things can be created das blocks
    ```html
    #base.html
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-+0n0xVW2eSR5OomGNYDnhzAbDsOXxcvSN1TPprVMTNDbiYZCxYbOOl7+AMvyTG2x" crossorigin="anonymous">
            {% block title %}
            {% endblock %}
        </head>
        <body>
            <!-- <nav class="navbar navbar-light navbar-static-top"> -->
                <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="{% url 'templates:index' %}">Home</a>
                        <ul class="navbar-nav me-auto">
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'admin:index' %}">Admin</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'templates:other' %}">Other</a>
                        </li>
                        </ul>
                    </div>
                </nav>
            <div class="container">
                {% block body %}
                {% endblock %}
            </div>
        </body>
    </html>
    ```
- index.html inheriting the base.html
    ```html
    #index.html
    <!DOCTYPE html>
    {% extends 'basic_templating/base.html' %}

    {% block title %}
        <title>HomePage</title>
    {% endblock %}

    {% block body %}
        <h1>Welcome! Index page</h1>
    {% endblock %}
    ```
## Template default and custom filters
- using default filters
    ```html
    <h3>{{ text | upper }}</h3>
    ```
- creating custom filters
    - create directory proj/app/templatetags and add __init__.py to make it a module
    - create custom_filters.py
        ```python
        from django import template

        register = template.Library()

        @register.filter(name='rm_arg')
        def rmrg(value, arg):
            """Removes all values of arg from the given string"""
            return value.replace(arg, '')
        ```
- Loading custom filters and using in index.html
    ```html
    <!DOCTYPE html>
    {% extends 'basic_templating/base.html' %}
    {% load custom_filters %}

    {% block title %}
        <title>HomePage</title>
    {% endblock %}

    {% block body %}
        <h1>Welcome! Index page</h1>
        <ul>
            <h3>{{ text | length }}</h3>
            <h3>{{ text | upper }}</h3>
            <h3>{{ num | add:"10" }}</h3>
            <h3>{{ text | rm_arg:"Lets" }}</h3>
        </ul>
    {% endblock %}
    ```
- [docs](https://docs.djangoproject.com/en/3.2/howto/custom-template-tags/)

# User authentication
- django in-built authorization is provided by below django apps
    ```
    'django.contrib.auth',
    'django.contrib.contenttypes',
    ```
- By default password hashing in django is PBKDF2 but also supports
    ```
    > pip install django[argon2]
    > pip install django[bcrypt]
    ```
- default User model has fields like first_name, last_name, username, email, password, we can add other fields by creating Model which would have OneToOneField Relationship rather than extending the User class(might cause issues in db, one user would have multiple instances)
    ```python
    #models.py
    from django.db import models
    from django.contrib.auth.models import User

    class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)

        portfolio_site = models.URLField(blank=True)
        profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

        def __str__(self):
            return self.user.username
    ```
- Creating model forms for User and UserprofileModel
    ```python
    from django import forms
    from django.contrib.auth.models import User
    from .models import UserProfile


    class UserForm(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput())

        class Meta:
            model = User
            fields = ('username','email','password')

    class UserProfileForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ('portfolio_site','profile_pic')
    ```
- Coding logic for registration and login Views.py
    ```python
    https://github.com/ganeshchennuri/users-auth/blob/master/users_app/views.py
    ```

# Class Based Views
- Http and Template Response with classbasedviews
    ```python
    #views.py
    from django.http.response import HttpResponse
    from django.views.generic import View, TemplateView

    class ClsView(View):
        def get(self, request):
            return HttpResponse("<h1> Hell Yeah </h1>")

    class ClsTempView(TemplateView):
        template_name  = 'basic_app/index.html'
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['bitch'] = 'LASSANIA'
            return context
    ```
    ```python
    #urls.py
    from django.contrib import admin
    from django.urls import path
    from basic_app.views import ClsView, ClsTempView

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',ClsView.as_view()),
        path('temp/',ClsTempView.as_view())
    ]
    ```
- List and Detail View
    ```python
    #models.py
    from django.db import models

    class School(models.Model):
        name = models.CharField(max_length=200)
        principal = models.CharField(max_length=100)
        location = models.CharField(max_length=300)

        def __str__(self):
            return self.name
        
    class Student(models.Model):
        name = models.CharField(max_length=100)
        age = models.PositiveIntegerField()
        school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

        def __str__(self) -> str:
            return self.name
    ```
    ```python
    #views.py
    from .models import School
    from django.views.generic import TemplateView, ListView, DetailView

    class SchoolsListView(ListView):
        template_name = 'schools_app/schools_list.html'
        context_object_name = 'schools' #default is object_list
        model = School

    class SchoolsDetailedView(DetailView):
        model = School
        template_name = 'schools_app/schools_detailed.html'
        context_object_name = 'school' #default is object
    ```

    ```html
    <!--Rendering List View in Templates-->
    {% for school in schools %}
            <li><h5><a href="{{ school.id }}">{{ school.name }}</a></h5></li>
    {% endfor %}
    ```
    ```html
    <!--Rendering Detail View-->
    <h5>School</h5>
    <p>Name : {{ school.name }}</p>
    <p>Principal : {{ school.principal }}</p>
    <p>Location : {{ school.location }}</p>

    <h5>Students</h5>
    {%for student in school.students.all %}
        <p>{{ student.name }}</p>  
    {% endfor %}
    ```

## Default user model
```python
    for Foreign Key usermodel
    from django.conf import settings
    User = settings.AUTH_USER_MODEL

    for other purpose
    from django.contrib import get_user_model
    User = get_user_model()


    # Reversely accessing with foreign key
    userObj.modelName_set.all()

    Blogpost.objects.filter(user=userObj)
    Blogpost.objects.filter(user__id=userObj.id)
```

# Customizing admin panel

## Changing Heading
- create admin folder in templates folder and add admin_site.html
- copy the contents from django github code repo
- Add the following changes
    ```html
        {% extends "admin/base.html" %}

        {% block title %}{% if subtitle %}{{ subtitle }} | {% endif %}{{ title }} | {{ site_title|default:_('Django site admin') }}{% endblock %}

        {% block branding %}
        <!-- <h1 id="site-name"><a href="{% url 'admin:index' %}">{{ site_header|default:_('Django administration') }}</a></h1> Remove extra things and templatetags-->

        <h1 id="site-name"><a href="{% url 'admin:index' %}">My administration</a></h1>
        {% endblock %}

        {% block nav-global %}{% endblock %}
    ```
## Changing fields on admin panel, 
- edit admin.py
```python
from django.contrib import admin
from .admin import Videos

class VideoAdmin(admin.ModelAdmin):
    fields = ['title','year','length']

    #Adding search in objects list view
    search_fields = ['title', 'length']

    # Adding filters to the model on admin page
    list_filter = ['year','length']

    # Displaying multiple fields in list view, can sprt from there too
    list_display = ['title','year','length']

    # editing on list view
    list_editable = ['length']

admin.site.register(Video)

```

# DRF (DJango Rest Framework)

## UserForm
- installing drf with pip
- adding 'rest_framework' to the installed apps
- for tokens 'rest_framework.authotoken'
- for altering django default user model
    ```python
    from django.contrib.auth.models import AbstractBaseUser
    from django.contrib.auth.models import PermissionsMixin

    class UserProfileManager(BaseUserManager):
        """model manager for userprofile"""
    

    class UserProfile(AbstractBaseUser,PermissionsMixin):
        """User model for datbase"""
    ```
- setting custom user profile model in the django project
    - AUTH_USER_MODEL = 'users_api.UserProfile'

# REST Framework Views
- Simple APIView can be constructed using rest_framework.views.APiView
- complex views can be constructed using viewsets
- serializers.py can be used to create serializers to validate post, put data (similar to form validators)
    ```python
     def post(self,request):
        """Adds to the List"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = "Hello "+name
            return Response({"message": message})
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)
    ```
- urls for viewset generated using router


## setting memcache

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

Database Cache

python manage.py createcachetable
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

## Logging

```python
#views.py
import logging

logger = logging.getLogger(__name__)
logger.error("")
logger.info("") # cant see in production
```

Logging components
- Logger - creates a log
- filter - Rules to whether keep or igore log
- handler - printing out to console or output file
- formatter - controls how logs converted to text

Log Levels
- Debug - low level app info only developers can see
- info - General info
- Warning - A minor Problem
- Error -  A problem occured
- Critical - A major problem