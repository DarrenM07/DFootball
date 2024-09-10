DFootball

link_deploy = darren-marcello-darrenecommerce.pbp.cs.ui.ac.id
1. Explain how you implemented the checklist above step-by-step (not just following the tutorial).
    1. Make a new Django project:
    Run django-admin startproject ecommerce
    2. Make an application named main :
    Run python manage.py startapp main (to create the application like views.py, models.py and urls.py)
    3. Run routing for "main" app:
    add this in the urls.py

    ```
    from django.urls import path, include
    urlpatterns = [
        path('', include('main.urls')),
    ]
    ```
    4. Make a product model :
    Define the models in models.py name with a character field with the max length of 100, price with and IntegerField, and description with a Text Field.

    from django.db import models
    class Item(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()

        def __str__(self):
            return self.name
    
    After defining the model, run : 
    python manage.py makemigrations
    
    5. Make html file :
    In main directory, create a html file named main in the main.html and input this. 
```
    <h1>DFootball Store</h1>
    <h5>Name app: </h5>
    <p>{{ name_app }}</p> <!-- Change according to your npm -->
    <h5>Name: </h5>
    <p>{{ name }}</p> <!-- Change according to your name -->
    <h5>Class: </h5>
    <p>{{ class }}</p> <!-- Change according to your class -->
    <h5>Sepatu: </h5> <!-- Change according to your product -->
    <p>Price : Rp.100.000</p> <!-- Change according to your class -->
    <p>Description : Sepatu Bola Nike Mercurial</p> <!-- Change according to your class -->
    <h5>Jersey </h5> <!-- Change according to your product -->
    <p>Price : Rp.1.000.000</p> <!-- Change according to your class -->
    <p>Descritpion : Jersey Real Madrid</p> <!-- Change according to your class -->
    <h5>NameSet Baju Bola: </h5> <!-- Change according to your product -->
    <p>Price = Rp 50.000</p> <!-- Change according to your class -->
    <p>Description : Ronaldo 7</p> <!-- Change according to your class -->
```


   6. Create a view in views.py :
    This is for display your name and class.This is for handle an HTTP  request and returns the appropriate view, and will pass the data from context dict. In views.py, define a function 

    from django.shortcuts import render
    def show_main(request):
        context = {
            'name': 'Darren Marcello Sidabutar',
            'class': 'PBP KKI',
            'name_app': 'E-Commerce',
        }

        return render(request, "main.html", context)

   7. Route the view in urls.py :
    In urls.py of the main app, write this code

    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]

   8. Deployin to PWS :
    Access the PWS at https://pbp.cs.ui.ac.id and login into your account. Create a new project, and store it. Add the PWS deployment URL to allowed host in settings.py

    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "<your pws deploy url>"]
    Run the project command instruction in the PWS page.

2. Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the 
relationship between urls.py, views.py, models.py, and the html file.
![](image/diagram.jpg)


3. Explain the use of git in software development!
Git is a version control that allowing developers to track changes in their codebase, collaborate with others, and manage code history of all modifications. And it supports teams to work on different branches for working on a new features without affect the codebabase and merge their work efficiently for integrating those features without problem.

4. In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?

Django is a high-level Python framework that promotes rapid development with clean and pragmatic design. It handles much of the heavy lifting, such as routing, database management, and user authentication, which makes it a good starting point for beginners to focus on learning core development concepts without getting lost in the complexity of lower-level details.


5. Why is the Django model called an ORM?
Django's models are an ORM (Object-Relational Mapping) system. It allows developers to interact with databases using Python objects. It simplifies management of database operations while keeping the flexibility to handle complex queries when needed.
