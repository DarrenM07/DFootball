**DFootball**

**---------------------------------------------------------------**

**Assignment 2**

**link_deploy = darren-marcello-darrenecommerce.pbp.cs.ui.ac.id**

**1. Explain how you implemented the checklist above step-by-step (not just following the tutorial).**
   1. Make a new Django project:
   Run django-admin startproject ecommerce
   2. Make an application named main :
   Run python manage.py startapp main (to create the application like views.py, models.py and urls.py)
   3. Run routing for "main" app:
   add this in the urls.py

    
    from django.urls import path, include
    urlpatterns = [
        path('', include('main.urls')),
    ]
   4. Make a product model :
    Define the models in models.py name with a character field with the max length of 100, price with and IntegerField, and description with a Text Field.

  ```
   from django.db import models
    class Item(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        def __str__(self):
            return self.name
   
   ```
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
    <h5>Sepatu: </h5> 
    <p>Price : Rp.100.000</p> 
    <p>Description : Sepatu Bola Nike Mercurial</p> 
    <h5>Jersey </h5> 
    <p>Price : Rp.1.000.000</p> 
    <p>Descritpion : Jersey Real Madrid</p>
    <h5>NameSet Baju Bola: </h5> 
    <p>Price = Rp 50.000</p> 
    <p>Description : Ronaldo 7</p> 
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

**2. Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the**
relationship between urls.py, views.py, models.py, and the html file.
![](image/diagram.jpg)

**3. Explain the use of git in software development!**
Git is a version control that allowing developers to track changes in their codebase, collaborate with others, and manage code history of all modifications. And it supports teams to work on different branches for working on a new features without affect the codebabase and merge their work efficiently for integrating those features without problem.

**4. In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?**
Django is a high-level Python framework that promotes rapid development with clean and pragmatic design. It handles much of the heavy lifting, such as routing, database management, and user authentication, which makes it a good starting point for beginners to focus on learning core development concepts without getting lost in the complexity of lower-level details.

**5. Why is the Django model called an ORM?**
Django's models are an ORM (Object-Relational Mapping) system. It allows developers to interact with databases using Python objects. It simplifies management of database operations while keeping the flexibility to handle complex queries when needed.


**------------------------------------------------------------------------------------------------**

**Assignment 3**

**1. Explain why we need data delivery in implementing a platform.**
 Data delivery is critical in platform implementation because it allows information to be transferred between systems, users or others. The platform cannot interact with external services without efficient data delivery, and it provides real-time updates, or maintains a consistent user experience. And data delivery can ensure that various platform components can communicate with each other properly.

**2. In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?**
In my opinion, JSON is better than XML. The reason is that JSON is easier to read because its syntax is easier to understand. JSON also produces smaller data loads so it is more bandwidth efficient. JSON is becoming more popular than XML in web development, because of its compatibility with JS and wide adoption in modern frameworks.

**3. Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms.**
The is_valid() method is used to validate form data, and check whether the data provided by the user matches the requirements of the form fields.

If the data is valid, is_valid() returns True and also populates the cleanse_data attribute, which stores the cleaned form data.
If the data is invalid, is_valid() returns False and stores the error message in the errors attribute.

We need this method to ensure that the data submitted through the form is correct and safe to use before processing it. Without proper validation, the platform can face issues such as storing invalid data, security vulnerabilities, or crashes.

**4. Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?**
The csrf_token is used to prevent Cross-Site Request Forgery (CSRF) attacks. A CSRF attack occurs when an attacker tricks a user into taking an action they don’t want to take, such as submitting a form on their behalf without their knowledge.

Without the crsf_token, an attacker could cause unauthorized actions, such as changing account information or executing transactions without the user’s consent, by exploiting the lack of protection by creating a malicious form that automatically submits data to your site on behalf of an unsuspecting user.

**5. Explain how you implemented the checklist above step-by-step (not just following the tutorial).**
1. Create a form input to add a model object.
    1. Create a new file in the main directory with the name forms.py and add the following code :
    ```
    from django.forms import ModelForm
    from main.models import ObjectEntry

    class ModelObjectForm(ModelForm):
        class Meta:
            model = ObjectEntry  #indicate the model that will be used for the form.
            fields = ["name", "price", "description"] #indicate the fields of the ObjectEntry model.
    ```

    2. Open the views.py and add this code :
    ```
    from django.shortcuts import render, redirect
    ```

    3. Create a new function with the name model_object and add the following code below :
    ```
    def model_object(request):
    form = ModelObjectForm(request.POST or None) #is used to create a new ModelObjectForm with the input from the user in request.POST entered into the QueryDict.

    if form.is_valid() and request.method == "POST": #is used to validate the input from the form.
        form.save() #is used to create and save the data from the form.
        return redirect('main:show_main') #is used to perform a redirect to the show_main function in the main application's views after the form data is successfully saved.

    context = {'form': form}
    return render(request, "create_model_object.html", context)
    ```
    the function is to produce a form that can automatically add a ObjectEntry data when data is submitted.

    4. Change the show_main function in the views.py :
    ```
    def show_main(request):
    object_entries = ObjectEntry.objects.all() #retrieve all objects of the ObjectEntry objects stored in the database.
    context = {
        'name': 'Darren Marcello Sidabutar',
        'class': 'PBP KKI',
        'name_app': 'E-Commerce',
        'object_entries': object_entries
    }
    print(object_entries)

    return render(request, "main.html", context)
    ```
    5. Open the urls.py file in the main directory and import the model_object function.
    ```
    from main.views import show_main, model_object
    ```
    6. Add the URL path to the urlpatterns variable in the urls.py :
    ```
    path('model-object', model_object , name='model_object'),
    ```
    7. Create a new HTML file with the name create_model_object.html in the main/templates directory and fill in with the following code.
    ```
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add Item</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Item" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```    
    8. Open the main.html and add the following code within the {% block content %} block :
    ```
    {% if not object_entries %}
    <p>There are no object data in DFootball Store.</p>
    {% else %}
    <table>
    <tr>
        <th>name</th>
        <th>price</th>
        <th>description</th>
    </tr>

    {% comment %} This is how to display object data
    {% endcomment %} 
    {% for model_object in object_entries %}
    <tr>
        <td>{{model_object.name}}</td>
        <td>{{model_object.price}}</td>
        <td>{{model_object.description}}</td>
    </tr>
    {% endfor %}
    </table>
    {% endif %}

    <br />

    <a href="{% url 'main:model_object' %}">
    <button>Add Item</button>
    </a>
    {% endblock content %}
    ```
    it is to display the data in the form in the form of a table and the "Add Item" button.

    9. Run the Django project 

2. Add 4 views to view the added objects in XML, JSON, XML by ID, and JSON by ID formats.
    1. Open the views.py and add the HttpResponse and Serializer imports.
    ```
    from django.http import HttpResponse
    from django.core import serializers
    ```
    2. Create a new function that receives a parameter request with the name show_xml and create a variable in the function itself that stores the result of the query of all data in the ObjectEntry.
    ```
    def show_xml(request):
    data = ObjectEntry.objects.all()
    ```
    3. Add the return function as an HttpResponse that contains the serialised data result as XML and the content_type="application/xml".
    ```
    def show_xml(request):
    data = ObjectEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    4. Open the urls.py file in the main directory and import the function that you just created.
    ```
    from main.views import show_main, model_object, show_xml
    ```
    5. Add the URL path to the urlpatterns variable in the urls.py file in the main directory to access the function that was imported in the previous point.
    ```
    path('xml/', show_xml, name='show_xml'),
    ```
    6. Open the views.py file in the main directory and create a new function that receives a parameter request with the name show_json with a variable in the function itself that stores the result of the query of all data in the ObjectEntry.
    ```
    def show_json(request):
    data = ObjectEntry.objects.all()
    ```
    7. Open the urls.py file in the main directory and import the function that you just created.
    ```
    rom main.views import show_main, model_object, show_xml, show_json
    ```
    8. Add the URL path to the urlpatterns variable in the urls.py file in the main directory to access the function that was imported in the previous point.
    ```
    path('json/', show_json, name='show_json'),
    ```
    9. Add the return function as an HttpResponse that contains the serialised data result as JSON and the content_type="application/json".
    ```
    def show_json(request):
        data = ObjectEntry.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    10. Run the Django project with the python manage.py runserver command and go to http://localhost:8000/json/ and  http://localhost:8000/xml/ in your browser of choice to see the result.

    11. Open the views.py file in the main directory and create two new functions that receive a parameter request and id with the names show_xml_by_id and show_json_by_id. And Create a variable in the function itself that stores the result of the query of data with the specific ID that exists in the ObjectEntry, and add the return function as an HttpResponse that contains the serialised data result as JSON or XML and the content_type with the value "application/xml" (for XML) or "application/json" (for JSON).

    XML :
    ```
    def show_xml_by_id(request, id):
    data = ObjectEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    JSON :
    ```
    def show_json_by_id(request, id):
        data = ObjectEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    12. Open the urls.py file in the main directory and import the function that you just created.
    ```
    from main.views import show_main, create_object_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
    ```
    13. Add the URL path to the urlpatterns variable in the urls.py file in the main directory to access the function that was imported in the previous point.
    ```
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ```
    14. go to http://localhost:8000/xml/[id]/ or http://localhost:8000/json/[id]/ change the "id" by ur pk


**6. Access the four URLs in point 2 using Postman, take screenshots of the results in Postman, and add them to README.md.**
![](image/JSON_Postman.jpg)
![](image/XML_Postman.jpg)
![](image/JSONID_Postman.jpg)
![](image/XMLID_Postman.jpg)


**-------------------------------------------------------------------------------------------------**

**ASSIGNMENT 4**

**1. What is the difference between HttpResponseRedirect() and redirect()?**
HttpResponseRedirect() : is a Django class-based response. It takes a URL as a parameter and returns an HTTP response that redirects the user to that URL.

redirect(): is a Django shortcut function that simplifies redirection. It automatically resolves the URL and can take various types of inputs, such as a URL path, view name, or an object. And it is more convenient and flexible than HttpResponseRedirect() as it handles URL resolution automatically.

**2. Explain how the ObjectEntry model is linked with User?**
To link each ObjectEntry to a user, first import Django's built-in User model in models.py with from django.contrib.auth.models import User, then add user = models.ForeignKey(User, on_delete=models.CASCADE) to the ObjectEntry model, allowing each entry to be associated with a user. Next, modify the model_object function to process the form, assign the logged-in user to the entry using commit=False (which delays saving so the user can be added), save the entry, and redirect to the main page. Finally, update the show_main function to filter and display only ObjectEntry objects for the logged-in user, while showing their username. After making these changes, do makemigrations and migrate before starting the server. I'll explain step by step below.

- First of all, we must add this code below in models.py
    ```
    from django.contrib.auth.models import User
    ```
    and add this code in the ObjectEntry model that previously been created.
    ```
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```
    it is for imports Django's built-in User model, which is used for managing user accounts, handling authentication (like logging in), storing user information (such as usernames, passwords), and assigning permissions. It also allows creating relationships with other models, so you can link specific data (like posts or entries) to a particular user.

- After that, we should modify the model_object function into like this code below
    ```
    def model_object(request):
    form = ModelObjectForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        model_object = form.save(commit=False)
        model_object.user = request.user
        model_object.save()
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_model_object.html", context)
    ```
    The model_object function processes a form to create a new ObjectEntry, assigns the logged-in user to the entry, and saves it to the database, then redirects the user to the main page if the form is valid; otherwise, it renders the form again for the user. And commit=False parameter delays saving the form object to the database, allowing you to modify it first. In this case, it lets you assign the logged-in user to the user field before saving the object.

- Last, we should change the value of object_entries and the context in the show_main function
    ```
        def show_main(request):
        object_entries = ObjectEntry.objects.filter(user=request.user)
        context = {
            'name': request.user.username,
                ...
        }
        ...
    ```
    The code filters and retrieves only the ObjectEntry objects belonging to the logged-in user and displays them, while request.user.username is used to show the user's name on the main page. And after that we should do makemigrations and migrate before we run the server.

**3. What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.**
Authentication verifies a user's identity, while authorization determines what actions they can perform. In Django, authentication is managed by the django.contrib.auth module, which checks user credentials and creates a session with login(). Authorization uses Django's permission system to control user access to resources or actions, ensuring users can only access what they are allowed.

**4. How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.**
Django uses session cookies to remember logged-in users by assigning a session ID to the user, which is stored in their browser and sent with every request to maintain their authenticated state. Cookies also serve various functions, like storing user preferences, tracking shopping carts, and enabling analytics. While secure cookies, such as those marked Secure and HttpOnly, provide better protection against interception and attacks, third-party cookies can pose privacy risks due to cross-site tracking. Proper use of cookies is essential for balancing functionality, security, and privacy.

**5. Explain how did you implement the checklist step-by-step (apart from following the tutorial)**
1. Implementing Function and Registration Froms.
    First, add this code in views.py
    ```
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages
    ```
    the UserCreationForm and messages are imported to simplify user registration and provide feedback. UserCreationForm is a built-in Django form that automatically handles user registration, including fields like username and password, eliminating the need to create custom forms for this purpose. The messages import allows you to display success or error messages to the user during the registration process, improving the user experience by giving feedback on actions like successful signups or errors.

    Second, we should add the register function in the same file as before.
    ```
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
    ```
    The register function in views.py handles user registration by generating and processing the UserCreationForm. When the form is submitted via a POST request, form = UserCreationForm(request.POST) captures the user's input. The function then checks if the form is valid with form.is_valid(), ensuring the data meets the required criteria. If valid, form.save() creates and saves the new user account. After the account is created, messages.success(request, 'Your account has been successfully created!') displays a confirmation message to the user. Finally, return redirect('main:login') redirects the user to the login page after successful registration. If the form isn't submitted or is invalid, the registration page is rendered with the form.

    Third, we create a HTML named register.html, and fill with this code
    ```
    {% extends 'base.html' %} {% block meta %}
    <title>Register</title>
    {% endblock meta %} {% block content %}

    <div class="login">
    <h1>Register</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input type="submit" name="submit" value="Register" /><td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    </div>

    {% endblock content %}
    ```
    The register.html template extends the base layout and provides a simple registration form for user sign-up. The form is created using the {{ form.as_table }} tag, which automatically renders the UserCreationForm fields in a table format, simplifying the HTML structure. It includes a CSRF token for security and a submit button for users to register. If any messages (such as success or error messages) are present, they are displayed below the form using a loop to iterate through the messages context. This approach streamlines form creation and user feedback within the registration page.

    Last for the first section, we must import the register function in urls.py and import this register function
    ```
    from main.views import register
    ```
    and add URL path
    ```
    path('register/', register, name='register'),
    ```
    In urls.py, the register function is imported from the main.views module to link the user registration functionality to a URL path. A new URL pattern, path('register/', register, name='register'), is added to the urlpatterns list, allowing users to access the registration page via the /register/ URL. This setup connects the registration form and view to the application. With the registration mechanism in place, the next step is to create a login form, allowing users to authenticate and log into their accounts after registering.

2. Implementing Login and Logout Function
    First, import authenticate, login and AuthenticationForm in the views.py.
    ```
    from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
    from django.contrib.auth import authenticate, login
    ```
    In views.py, the authenticate, login and AuthenticationForm are imported to manage user authentication for login. The authenticate function checks a user's credentials to verify their identity, while the login function logs the user into the system if authentication is successful. AuthenticationForm is a built-in Django form used to create a login form. Together, these imports handle the process of authenticating users and logging them in, enabling secure access to the application. 

    Add the login_user function in the same file as before
    ```
    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')
    else:
      form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
    ```

    The login_user function in views.py handles user authentication and login. When the form is submitted via a POST request, AuthenticationForm(data=request.POST) processes the login credentials. If the form is valid, it retrieves the user with form.get_user() and logs them in using login(request, user), which creates a session for the authenticated user. After logging in, the user is redirected to the main page. If the request is not a POST or the form is invalid, the login form is displayed again. This function ensures proper user authentication and session management in the application. 

    Make a new HTML named login.html
    ```
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
    </div>

    {% endblock content %}
    ```
    The login.html template creates a simple login page using Django's template system. It extends a base layout and includes a form for user authentication, rendered as a table using {{ form.as_table }}. The form uses a POST method, includes a CSRF token for security, and has a submit button to log the user in. If there are any messages, such as errors or success notifications, they are displayed to the user. Additionally, the template provides a link to the registration page for users who don't yet have an account, allowing easy navigation between login and registration.

    Last for the second section, we import the function that we just created in urls.py
    ```
    from main.views import login_user
    ```
    and add the URL path
    ```
    path('login/', login_user, name='login'),
    ```
    In urls.py, the login_user function is imported and a new URL pattern, path('login/', login_user, name='login'), is added to the urlpatterns list, enabling access to the login page through the /login/ URL. This completes the setup for the login mechanism, allowing users to authenticate and log into the application. The next step is to implement the logout functionality and add a logout button to the main page, enabling users to securely log out of their accounts once they are finished using the application.

3. Implementing Logout
    Add the logout import in the views.py
    ```
    from django.contrib.auth import logout
    ```
    after that, add the function in the same file as before
    
    ```
    def logout_user(request):
    logout(request)
    return redirect('main:login')
    ```
    The logout function is imported from Django to implement the logout mechanism. The logout_user function uses logout(request) to terminate the session of the currently logged-in user, effectively logging them out by deleting their session data. After logging out, the user is redirected to the login page with return redirect('main:login'). This ensures users can securely log out and be prompted to log in again when trying to access the application.

    Add the following code in the main.html
    ```
    <a href="{% url 'main:logout' %}">
    <button>Logout</button>
    ```
    In main.html, the code snippet adds a logout button using the Django URL template tag {% url 'main:logout' %}. This tag dynamically generates the URL for the logout view based on the app_name and view_name defined in urls.py. Here, 'main' refers to the app name, and 'logout' refers to the view name assigned to the logout path in urls.py. When the button is clicked, it triggers the logout functionality, which logs the user out and redirects them to the login page. This setup simplifies URL management by referencing views via their assigned names rather than hardcoded URLs.

    Import the logout_user function that just been created earlier to urls.py
    ```
    from main.views import logout_user
    ```
    and add the URL path
    ```
    path('logout/', logout_user, name='logout'),
    ```

4. Restricting Access
    In the views.py, add login_required import.
    ```
    from django.contrib.auth.decorators import login_required
    ```
    and add @login_required(login_url='/login') above the show_main function
    ```
    @login_required(login_url='/login')
    def show_main(request):
    ```
    In views.py, the login_required decorator is imported from Django's authentication system to restrict access to certain views. By adding the @login_required(login_url='/login') decorator above the show_main function, access to the main page is restricted to authenticated users only. If a user tries to access the main page without being logged in, they will be redirected to the login page. This ensures that only logged-in users can view object entries, enhancing security and user privacy. After implementing this, running the Django server will redirect unauthenticated users to the login page when attempting to access the main page.

6. Using Data (Cookies)
    In this update, we are enhancing the Django application to store and display the user's last login time using cookies. First, in the login_user function, after a successful login, a cookie named last_login is created with the current date and time using the response.set_cookie() method. This stores the last login time as a cookie on the user's browser. 

    ```
    if form.is_valid():  
        user = form.get_user()  
        login(request, user)  
        response = HttpResponseRedirect(reverse("main:show_main"))  
        response.set_cookie('last_login', str(datetime.datetime.now()))  
        return response
    ```

    In the show_main function, the last login time is extracted from the cookie and passed to the context:

    ```
    context = {  
        'name': 'Pak Bepe',  
        'class': 'PBP D',  
        'npm': '2306123456',  
        'object_entries': object_entries,  
        'last_login': request.COOKIES['last_login'],
    }
    ```

    In logout_user, the last_login cookie is deleted when the user logs out:

    ```
    def logout_user(request):  
        logout(request)  
        response = HttpResponseRedirect(reverse('main:login'))  
        response.delete_cookie('last_login')  
        return response
    ```

    In main.html, a new element is added to display the last login information on the page:

    ```
    <h5>Last login session: {{ last_login }}</h5>
    ```

    This code allows you to track and display the last login time for a user, storing this data in cookies, which are viewable in the browser's developer tools. When the user logs out, the last_login cookie is deleted, and it is recreated upon the next login. This implementation also shows how cookies work to store session-related information like the last login and how they are deleted and recreated upon logout and login.

7. Connecting the ObjectEntry model to the User model

    First of all, we must add this code below in models.py
    ```
    from django.contrib.auth.models import User
    ```
    and add this code in the ObjectEntry model that previously been created.
    ```
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```
    it is for imports Django's built-in User model, which is used for managing user accounts, handling authentication (like logging in), storing user information (such as usernames, passwords), and assigning permissions. It also allows creating relationships with other models, so you can link specific data (like posts or entries) to a particular user.

    After that, we should modify the model_object function into like this code below
    ```
    def model_object(request):
    form = ModelObjectForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        model_object = form.save(commit=False)
        model_object.user = request.user
        model_object.save()
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_model_object.html", context)
    ```
    The model_object function processes a form to create a new ObjectEntry, assigns the logged-in user to the entry, and saves it to the database, then redirects the user to the main page if the form is valid; otherwise, it renders the form again for the user. And commit=False parameter delays saving the form object to the database, allowing you to modify it first. In this case, it lets you assign the logged-in user to the user field before saving the object.

    Last, we should change the value of object_entries and the context in the show_main function
    ```
        def show_main(request):
        object_entries = ObjectEntry.objects.filter(user=request.user)
        context = {
            'name': request.user.username,
                ...
        }
        ...
    ```
    The code filters and retrieves only the ObjectEntry objects belonging to the logged-in user and displays them, while request.user.username is used to show the user's name on the main page. And after that we should do makemigrations and migrate before we run the server.

**-------------------------------------------------------------------------------------------**
**ASSIGNMENT 5**
### 1. If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!

When multiple CSS selectors apply to the same HTML element, the browser determines which styles to apply based on the concept of specificity. Specificity is calculated based on the types of selectors used: inline styles have the highest priority, followed by IDs, classes, attributes, and pseudo-classes, and finally, element selectors and pseudo-elements. Inline styles, written directly in the HTML element, override all other styles. ID selectors, denoted by a `#`, come next and are more specific than class selectors, which are prefixed with a `.`. Following these, class selectors and attribute selectors have higher specificity than type selectors (e.g., `div`, `p`). If selectors have the same specificity, the one that appears last in the CSS will take precedence. This hierarchy ensures that developers have a systematic way to control styling in their applications.

### 2. Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!

Responsive design is crucial in web application development as it ensures that a website functions well on a variety of devices and screen sizes, from mobile phones to large desktop monitors. The importance of this approach stems from the increasing use of mobile devices to access the internet, making it vital for a seamless user experience across all platforms. Applications like Facebook and Twitter exemplify effective responsive design; they automatically adjust layouts and content based on the user's device, enhancing usability and engagement. Conversely, websites that do not implement responsive design, such as older government sites, may display poorly on mobile devices, leading to user frustration and a higher bounce rate. This highlights the need for developers to prioritize responsive design in their projects to meet user expectations.

### 3. Explain the differences between margin, border, and padding, and how to implement these three things!

Margin, border, and padding are essential concepts in CSS that dictate spacing and layout around HTML elements. Margin is the outermost space that creates distance between elements, effectively controlling the spacing around a box without affecting its dimensions. The border surrounds the padding and content, providing a visible line that can vary in thickness and style, allowing for decorative elements around an element. Padding, on the other hand, is the space between the content of the box and its border; it increases the size of the element while affecting how the content is visually positioned. To implement these properties, developers can use the shorthand CSS properties `margin`, `border`, and `padding`, specifying values for each side (top, right, bottom, left) or using the shorthand syntax for all sides at once.

### 4. Explain the concepts of flex box and grid layout along with their uses!

Flexbox and Grid are powerful CSS layout models designed to create complex responsive layouts more efficiently. Flexbox, or the Flexible Box Layout, allows for one-dimensional layouts, where items can be arranged in either a row or a column. It provides flexible spacing, alignment, and distribution of items within a container, making it ideal for components like navigation bars or image galleries where items need to adjust according to available space. In contrast, CSS Grid Layout is a two-dimensional layout system that enables developers to design complex web layouts with rows and columns. It allows for precise placement of elements on a grid, making it suitable for entire page layouts where the positioning of various sections is critical. Both Flexbox and Grid enhance the ability to create responsive designs, ensuring that web applications look great on any device.

### 5. Explain how you implemented the checklist above step-by-step (not just following the tutorial)!
1. Adding Tailwind to the Django Project:
    To incorporate Tailwind into your Django project, you start by ensuring that your HTML structure is ready to handle responsive designs. In base.html, you add a <meta name="viewport"> tag to ensure the page adjusts well on different device sizes. Then, to integrate Tailwind, you simply link the Tailwind CDN by placing the script tag in the <head> section. This will allow you to use Tailwind's utility classes throughout your application without needing to install it locally.

    Make sure this code below is already in base.html :
    ```
    <head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
    </head>
    ```

    and add tailwind cdn script:
    ```
    <script src="https://cdn.tailwindcss.com">
    </script>
    ```

2. Adding the Edit Object Feature:
    To add an edit feature for object entries, you need to create a new function edit_object in views.py. This function fetches the specific object entry using its id, initializes a form with that entry’s data, and allows users to modify and submit the form. If the form is valid and the request method is POST, the changes are saved, and the user is redirected to the main page. You also need to create an HTML template edit_object.html, which will render the form. To make this functionality accessible, a corresponding URL path must be added in urls.py, and an "Edit" button should be included for each object entry in main.html.

    edit_object function :
    ```
    def edit_object(request, id):
    # Get object entry based on id
    object = ObjectEntry.objects.get(pk = id)

    # Set object entry as an instance of the form
    form = ModelObjectForm(request.POST or None, instance=object)

    if form.is_valid() and request.method == "POST":
        # Save form and return to home page
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_object.html", context)
    ```

    and dont forget to add the imports in views.py!
    ```
    from django.shortcuts import render, redirect, reverse
    from django.http import HttpResponse, HttpResponseRedirect
    ```

    and create edit_object.html and fill with the following code :
    ```
    {% extends 'base.html' %}

    {% load static %}

    {% block content %}

    <h1>Edit Object</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Edit Object"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```

    and dont forget to put the import in urls.py and the path
    ```
    from main.views import edit_object
    ```

    ```
    path('edit-object/<uuid:id>', edit_object, name='edit_object'),
    ```

    and in the main.html add this code below to build a URL by adding the primary key (pk) of the object_entry object as a parameter.
    ```
    <tr>
     
        <td>
            <a href="{% url 'main:edit_object' object_entry.pk %}">
                <button>
                    Edit
                </button>
            </a>
        </td>
    </tr>
    ```



3. Adding the Delete Object Feature:
    To add the feature that allows users to delete object entries in your Django application, you first need to create a function named `delete_object` in the `views.py` file located in the main folder. This function takes two parameters: `request` and `id`. The function retrieves the specific object entry from the database using its unique `id`, and once the object is found, it calls the `delete()` method to remove the entry from the database. After the deletion, the user is redirected back to the main page using `HttpResponseRedirect` and the `reverse()` function, which navigates to the `'main:show_main'` page. The code for this function looks like this:

    ```
    def delete_object(request, id):
        # Get object based on id
        object = ObjectEntry.objects.get(pk = id)
        # Delete object
        object.delete()
        # Return to home page
        return HttpResponseRedirect(reverse('main:show_main'))
    ```

    Next, in the `urls.py` file located in the main folder, you need to import the `delete_object` function so that it can be accessed through a URL. This is done by adding the import statement for `delete_object` at the top of the file:

    ```
    from main.views import delete_object
    ```

    After importing, you need to add a URL path to the `urlpatterns` list that will map the URL to the `delete_object` function. If your `id` field in the `ObjectEntry` model is a UUID, the path will look like this:

    ```
    path('delete/<uuid:id>', delete_object, name='delete_object'),
    ```

    If your `id` field is an integer, modify the path by changing `<uuid:id>` to `<int:id>` to match the data type of the `id`.

    Now, to display a "Delete" button for each object entry on the main page, open the `main.html` file in the `main/templates` folder. Modify the code so that there is a delete button in the table row for each object entry. This is done by adding a URL link to the `delete_object` view using the primary key (`pk`) of the `object_entry` object. The code looks like this:

    ```
    <tr>
        ...
        <td>
            <a href="{% url 'main:edit_object' object_entry.pk %}">
                <button>Edit</button>
            </a>
        </td>
        <td>
            <a href="{% url 'main:delete_object' object_entry.pk %}">
                <button>
                    Delete
                </button>
            </a>
        </td>
    </tr>
    ```

4. Adding a Navigation Bar:
    To add a navigation bar (navbar) to your Django web application, you will begin by creating a new HTML file named navbar.html in the templates/ folder in your project’s root directory. The purpose of the navbar is to provide easy navigation across various pages or features of the application. It typically appears at the top of the page and contains links or buttons to different sections of the app. You can populate the navbar.html file with the following code template:

    ```
    <nav class="bg-[#074173] shadow-lg fixed top-0 left-0 z-40 w-screen">
        <div class="absolute inset-y-0 left-0 flex items-center sm:hidden">
            <!-- Mobile menu button-->
            <button type="button" class="relative inline-flex items-center justify-center rounded-md p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-inset focus:ring-white" aria-controls="mobile-menu" aria-expanded="false">
            <span class="absolute -inset-0.5"></span>
            <span class="sr-only">Open main menu</span>
            <svg class="block h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
            </svg>
            <svg class="hidden h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
            </svg>
            </button>
          </div>       
        </div>
      </div>
    </div>

        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
            <div class="flex items-center">
            <h1 class="text-2xl font-bold text-center text-white">DFootball</h1>
                <div class="flex flex-1 items-center justify-center sm:items-stretch sm:justify-start">
                <div class="hidden sm:ml-6 sm:block">
                    <div class="flex space-x-4">
                    <!-- Current: "bg-gray-900 text-white", Default: "text-gray-300 hover:bg-gray-700 hover:text-white" -->
                    <a href="#" class="rounded-md bg-gray-900 px-3 py-2 text-sm font-medium text-white" aria-current="page">Home</a>
                    <a href="#" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">Categories</a>
                    <a href="#" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">Cart</a>
                    <a href="#" class="rounded-md px-3 py-2 text-sm font-medium text-gray-300 hover:bg-gray-700 hover:text-white">About Store</a>
                    </div>
                  </div>
                </div>        
            </div>
            <div class="hidden md:flex items-center">
            {% if user.is_authenticated %}
            <span class="text-white mr-4">Welcome, {{ user.username }}</span>
                <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                Logout
                </a>
            {% else %}
                <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">
                Login
                </a>
                <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                Register
                </a>
            {% endif %}
            </div>
            <div class="md:hidden flex items-center">
                <button class="mobile-menu-button">
                    <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                        <path d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>
          </div>
        </div>
        <!-- Mobile menu -->
        <div class="mobile-menu hidden md:hidden  px-4 w-full md:max-w-full">
          <div class="pt-2 pb-3 space-y-1 mx-auto">
            {% if user.is_authenticated %}
              <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
              <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                Logout
              </a>
            {% else %}
              <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
                Login
              </a>
              <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">
                Register
              </a>
            {% endif %}
          </div>
        </div>
        <script>
          const btn = document.querySelector("button.mobile-menu-button");
          const menu = document.querySelector(".mobile-menu");
        
          btn.addEventListener("click", () => {
            menu.classList.toggle("hidden");
          });
        </script>
      </nav>
    ```

    This code defines a navigation bar (navbar) for a web application, specifically designed with Tailwind CSS classes for styling and a responsive design. The navbar is fixed at the top of the page and features a blue background (`bg-[#074173]`) with various sections. It starts with a mobile menu button for smaller screens, which can toggle between being visible or hidden. This mobile button uses two SVG icons: one for the menu and one for closing the menu. The main navbar includes the site title ("DFootball") and a set of navigation links ("Home," "Categories," "Cart," "About Store"), which change appearance on hover. These links provide easy access to different sections of the web application. For larger screens, the navbar includes a user authentication section where logged-in users are greeted by their username, and buttons are provided for login, logout, and registration, depending on the user’s authentication status. The navbar is fully responsive, adapting to different screen sizes. The script at the end adds functionality to the mobile menu button, toggling its visibility when clicked.

    Next, we need to include this navigation bar in your existing HTML files. In main.html, create_object_entry.html, and edit_object.html files located in the main/templates/ subdirectory, you should include the navbar using the Django {% include %} tag. The inclusion will ensure that the navbar appears on every page where it is added. Update your HTML files to look like this:

    ```
    {% extends 'base.html' %}
    {% block content %}
    {% include 'navbar.html' %}
    ...
    {% endblock content %}
    ```

5. Configuring Static Files:
    
    We need to add the **WhiteNoise middleware** to `settings.py`. This middleware helps Django manage static files efficiently, especially in production mode when `DEBUG=False`. By placing the line `'whitenoise.middleware.WhiteNoiseMiddleware'` directly under `'django.middleware.security.SecurityMiddleware'`, static files will automatically be served in production without additional configurations.

    Next, in `settings.py`, it is important to set the correct paths for serving static files depending on the environment. The `STATIC_URL` variable is set to `'/static/'` to define the base URL for static content. When in **development mode** (`DEBUG=True`), the `STATICFILES_DIRS` variable should point to the `/static` directory in the project root, allowing Django to serve files during development. In **production mode** (`DEBUG=False`), you need to set `STATIC_ROOT`, which refers to the location where Django will collect static files when running the `collectstatic` command. This setup ensures static files are served properly in both modes. 

    Here is the code snippet for the configuration:
    ```
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'whitenoise.middleware.WhiteNoiseMiddleware', # Add it directly under SecurityMiddleware
        ...
    ]

    STATIC_URL = '/static/'

    if DEBUG:
        STATICFILES_DIRS = [
            BASE_DIR / 'static' # refers to /static root project in development mode
        ]
    else:
        STATIC_ROOT = BASE_DIR / 'static' # refers to /static root project in production mode
    ```

6. Adding Styles to the Application with Tailwind and External CSS
    We can enhance the aesthetics of your application by incorporating Tailwind CSS and a custom CSS file. To begin, create a global.css file in the /static/css directory within your project's root. This file allows you to define your custom classes and styles, providing a personalized touch to your application. Once you've established your styles, you'll need to link both the global.css and the Tailwind CSS script in your base.html file. To do this, modify base.html as follows:

    Create a global.css file in /static/css in the root directory, and link global.css and Tailwind script to base.html and modify it as follows :

    ```
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        {% block meta %} {% endblock meta %}
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="{% static 'css/global.css' %}"/>
    </head>
    <body>
        {% block content %} {% endblock content %}
    </body>
    </html>
    ```
    and modify the global.css as follows :
    ```
    .form-style form input, form textarea, form select {
        width: 100%;
        padding: 0.5rem;
        border: 2px solid #bcbcbc;
        border-radius: 0.375rem;
    }
    .form-style form input:focus, form textarea:focus, form select:focus {
        outline: none;
        border-color: #00ff00;
        box-shadow: 0 0 0 3px #00ff00;
    }
    @keyframes shine {
        0% { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    .animate-shine {
        background: linear-gradient(120deg, rgba(255, 255, 255, 0.3), rgba(255, 255, 255, 0.1) 50%, rgba(255, 255, 255, 0.3));
        background-size: 200% 100%;
        animation: shine 3s infinite;
    }
    ```
    In this implementation, we create a `global.css` file in the `/static/css` directory to define custom styles for our application, enhancing its visual appeal. The `global.css` includes styles for form elements, ensuring that input fields, text areas, and select boxes have a consistent appearance with full width, padding, and a border. Additionally, it specifies focus styles, changing the border color and adding a glowing effect when elements are active, which improves user interaction. The CSS also defines a keyframe animation called `shine`, which creates a shimmering effect by animating a linear gradient background. The `.animate-shine` class utilizes this animation, giving elements a dynamic visual effect that can be applied to any component in the application. To ensure these styles are effective, we link `global.css` and the Tailwind CSS script in the `base.html` file, allowing us to combine the utility-first approach of Tailwind with our custom styling for a cohesive design.

    **after that, modify the login page in login.html into the code as follows :**
    ```
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <div class="min-h-screen flex items-center justify-center w-screen bg-[#FFF6E9] py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
        <div>
        <h2 class="mt-6 text-center text-black text-3xl font-extrabold text-gray-900">
            Login to your account
        </h2>
        </div>
        <form class="mt-8 space-y-6" method="POST" action="">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
            <div>
            <label for="username" class="sr-only">Username</label>
            <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-t-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Username">
            </div>
            <div>
            <label for="password" class="sr-only">Password</label>
            <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 rounded-b-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password">
            </div>
        </div>

        <div>
            <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#41A06F] hover:bg-[#41A06F] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#41A06F]">
            Sign in
            </button>
        </div>
        </form>

        {% if messages %}
        <div class="mt-4">
        {% for message in messages %}
        {% if message.tags == "success" %}
                <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                    <span class="block sm:inline">{{ message }}</span>
                </div>
            {% elif message.tags == "error" %}
                <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                    <span class="block sm:inline">{{ message }}</span>
                </div>
            {% else %}
                <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                    <span class="block sm:inline">{{ message }}</span>
                </div>
            {% endif %}
        {% endfor %}
        </div>
        {% endif %}

        <div class="text-center mt-4">
        <p class="text-sm text-black">
            Don't have an account yet?
            <a href="{% url 'main:register' %}" class="font-medium text-[#074173] hover:text-[#0A5B8C]">      
            Register Now
            </a>
        </p>
        </div>
    </div>
    </div>
    {% endblock content %}
    ```
    The `login.html` file is designed to extend the `base.html` template, ensuring consistency across the Django project. It sets the page title to "Login" within the meta block, and the content block contains the main structure of the login form. Using Tailwind CSS, the layout is styled for a modern and responsive interface. The form is centered both vertically and horizontally using classes such as `min-h-screen`, `flex`, and `justify-center`. The form fields for username and password are styled with utility classes that ensure full width, padding, and border styles, along with focus states to improve user interaction. The submit button is styled with custom colors and hover effects. If there are any messages (success, error, or info), they are displayed in appropriately colored alert boxes. Lastly, there's a link prompting users to register if they don't have an account, styled to stand out with a distinct hover effect.

    **after that, modify the register page in register.html into the code as follows :**
    ```
    {% extends 'base.html' %}

    {% block meta %}
    <title>Register</title>
    {% endblock meta %}

    {% block content %}
    <div class="min-h-screen flex items-center justify-center bg-[#FFF6E9] py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 form-style">
        <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
            Create your account
        </h2>
        </div>
        <form class="mt-8 space-y-6" method="POST">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
            {% for field in form %}
            <div class="{% if not forloop.first %}mt-4{% endif %}">
                <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
                {{ field.label }}
                </label>
                <div class="relative">
                {{ field }}
                <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                    {% if field.errors %}
                    <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                        <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                    {% endif %}
                </div>
                </div>
                {% if field.errors %}
                {% for error in field.errors %}
                    <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                {% endfor %}
                {% endif %}
            </div>
            {% endfor %}
        </div>

        <div>
            <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#41A06F] hover:bg-[#3B8F62] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#41A06F]">
            Register
            </button>
        </div>
        </form>

        {% if messages %}
        <div class="mt-4">
        {% for message in messages %}
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <span class="block sm:inline">{{ message }}</span>
        </div>
        {% endfor %}
        </div>
        {% endif %}

        <div class="text-center mt-4">
        <p class="text-sm text-black">
            Already have an account?
            <a href="{% url 'main:login' %}" class="font-medium text-[#074173] hover:text-[#0A5B8C]">
            Login here
            </a>
        </p>
        </div>
    </div>
    </div>
    {% endblock content %}
    ```
    The `register.html` file extends the `base.html` template to maintain a consistent layout across the web application. It sets the page title to "Register" in the meta block and defines the registration form in the content block. The form is centered on the page with the help of Tailwind CSS classes like `min-h-screen`, `flex`, and `justify-center`. The form itself is styled using utility classes and is wrapped in a div with the class `form-style`, which connects it to the global styles defined earlier. Each form field is dynamically generated using Django's form rendering, with error handling and field labels displayed. Error icons (a red warning symbol) appear if the field contains errors, making it user-friendly and easy to understand. The "Register" button at the bottom is styled with a custom color that turns slightly darker on hover, and it includes a focus ring for accessibility. If there are any messages (such as errors or other notifications), they are displayed in a red alert box. Lastly, the page includes a prompt for users who already have an account, offering a link to the login page styled with a hover effect for enhanced user experience.

    **after that, modify the home page :**
    Create a card_info.html file in the main/templates directory, then add the following HTML code:
    ```
    <div class="bg-[#3b82f6] rounded-xl overflow-hidden border-2 border-[#FFF6E9]">
        <div class="p-4 animate-shine">
          <h5 class="text-lg font-semibold text-[#FFF6E9]">{{ title }}</h5>
          <p class="text-[#FFF6E9]">{{ value }}</p>
        </div>
    </div>
    ```

    and create a card_object.html file in the main/templates directory, then add the following HTML code:
    ```
    <div class="relative break-inside-avoid">
      <!-- Absolute top icons -->
      <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
        <div class="w-[3rem] h-8 bg-gray-200 rounded-md opacity-80 -rotate-90"></div>
        <div class="w-[3rem] h-8 bg-gray-200 rounded-md opacity-80 -rotate-90"></div>
      </div>
      <!-- Main content card -->
      <div class="relative top-5 bg-white shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-indigo-300 transform rotate-1 hover:rotate-0 transition-transform duration-300">
        <!-- Header section -->
        <div class="bg-[#41A06F] text-gray-800 p-4 rounded-t-lg border-b-2 border-[#41A06F]">
          <h3 class="font-bold text-xl mb-2 text-[#FFF6E9]">{{object_entry.name}}</h3>
          <p class="text-gray-600">{{object_entry.time}}</p>
        </div>

      <!-- Body section -->
        <div class="p-4">
          <p class="font-semibold text-lg mb-2">Description</p>
          <p class="text-gray-700 mb-2">
            <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{object_entry.description}}</span>
          </p>

          <!-- Size section -->
          <div class="mt-4">
            <p class="text-gray-700 font-semibold mb-2">Price</p>
            <div class="relative pt-1">
              <div class="flex mb-2 items-center justify-between">
                <div>
                  <span class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-indigo-600 bg-indigo-200">
                    {% if object_entry.price > 10 %}10+{% else %}{{object_entry.price}}{% endif %}
                  </span>
                </div>
              </div>

                <!-- Progress bar -->
                <div class="overflow-hidden h-2 mb-4 text-xs flex rounded bg-indigo-200">
                  <div style="width:{% if object_entry.price > 10 %}100%{% else %}{{ object_entry.price }}0%{% endif %}" class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-indigo-500"></div>
                </div>
              </div>
            </div>
          </div>

          <!-- Action buttons -->
          <div class="absolute top-0 -right-4 flex space-x-1">
            <a href="{% url 'main:edit_object' object_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
              </svg>
            </a>
            <a href="{% url 'main:delete_object' object_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
              </svg>
            </a>
        </div>
      </div>
    </div>
    ```

    **After everything is done, we need to merge card_info.html, card_object.html, and very-sad.png in the main.html template. Modify main.html like this:**
    ```
    {% extends 'base.html' %}
    {% load static %}

    {% block meta %}
    <title>DFootball</title>
    {% endblock meta %}
    {% block content %}
    {% include 'navbar.html' %}
    <div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-[#FFF6E9] flex flex-col">
      <div class="p-2 mb-6 relative">
        <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">
          {% include "card_info.html" with title='NAME APP' value=name_app %}
          {% include "card_info.html" with title='Name' value=name %}
          {% include "card_info.html" with title='Class' value=class %}
        </div>
        <div class="w-full px-6 absolute top-[44px] left-0 z-20 hidden md:flex">
          <div class="w-full min-h-4 bg-[#074173]"></div>
        </div>
        <div class="h-full w-full py-6 absolute top-0 left-0 z-20 md:hidden flex">
          <div class="h-full min-w-4 bg-[#074173] mx-auto"></div>
        </div>
      </div> <!-- Close div for p-2 mb-6 relative -->

      <div class="px-3 mb-4">
        <div class="flex rounded-md items-center bg-[#41A06F] py-2 px-4 w-fit">
          <h1 class="text-white text-center">Last Login: {{last_login}}</h1>
        </div>
      </div>

      <div class="flex justify-end mb-6">
        <a href="{% url 'main:model_object' %}" class="bg-[#41A06F] hover:bg-indigo-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
        Add New Item
        </a>
      </div>

      {% if not object_entries %}
      <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
        <img src="{% static 'image/very-sad.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
        <p class="text-center text-gray-600 mt-4">There is no item in DFootball.</p>
      </div>
      {% else %}
      <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
        {% for object_entry in object_entries %}
          {% include 'card_object.html' with object_entry=object_entry %}
        {% endfor %}
      </div>
      {% endif %}
    </div> <!-- Close div for overflow-x-hidden -->
    {% endblock content %}
    ```

    **after that, style the create_model_object.html as follows:**
    ```
    {% extends 'base.html' %}
    {% load static %}
    {% block meta %}
    <title>Add Item</title>
    {% endblock meta %}

    {% block content %}
    {% include 'navbar.html' %}

    <div class="flex flex-col min-h-screen bg-[#FFF6E9]">
    <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
        <h1 class="text-3xl font-bold text-center mb-8 text-black">Create Object</h1>
    
        <div class="bg-white shadow-md rounded-lg p-6 form-style">
        <form method="POST" class="space-y-6">
            {% csrf_token %}
            {% for field in form %}
            <div class="flex flex-col">
                <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                {{ field.label }}
                </label>
                <div class="w-full">
                {{ field }}
                </div>
                {% if field.help_text %}
                <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                {% endif %}
                {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                {% endfor %}
            </div>
            {% endfor %}
            <div class="flex justify-center mt-6">
            <button type="submit" class="bg-[#41A06F] text-white font-semibold px-6 py-3 rounded-lg hover:bg-[#38A65E] transition duration-300 ease-in-out w-full">
                Create Object
            </button>
            </div>
        </form>
        </div>
    </div>
    </div>

    {% endblock %}
    ```

    **and the last, modify the edit_object into like this :**
    ```
    {% extends 'base.html' %}
    {% load static %}
    {% block meta %}
    <title>Edit Object</title>
    {% endblock meta %}

    {% block content %}
    {% include 'navbar.html' %}
    <div class="flex flex-col min-h-screen bg-[#FFF6E9]">
    <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
        <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Item</h1>
    
        <div class="bg-white rounded-lg p-6 form-style">
        <form method="POST" class="space-y-6">
            {% csrf_token %}
            {% for field in form %}
                <div class="flex flex-col">
                    <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                        {{ field.label }}
                    </label>
                    <div class="w-full">
                        {{ field }}
                    </div>
                    {% if field.help_text %}
                        <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                    {% endif %}
                    {% for error in field.errors %}
                        <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                    {% endfor %}
                </div>
            {% endfor %}
            <div class="flex justify-center mt-6">
                <button type="submit" class="bg-[#41A06F] text-white font-semibold px-6 py-3 rounded-lg hover:bg-[#38A65E] transition duration-300 ease-in-out w-full">
                    Edit Item
                </button>
            </div>
        </form>
    </div>
    </div>
    </div>
    {% endblock %}
    ```

### Assignment 6
**1. Benefits of using JavaScript in developing web applications:**

JavaScript is essential for creating dynamic and interactive web applications, offering a range of benefits. One of the key advantages is that it allows developers to build responsive user interfaces that can update without reloading the page, improving user experience. Features like real-time form validation, content updates, and animations enhance interactivity. JavaScript's support for asynchronous operations (like AJAX) enables seamless communication with the server, allowing data to be fetched or submitted in the background without interrupting the user's experience. Additionally, JavaScript is cross-browser compatible, ensuring that applications function consistently across different platforms. The language can also be used on both the client and server sides (thanks to Node.js), making it a versatile tool for full-stack development, allowing developers to use a single language across the entire web application stack.

**2. Why we need to use `await` when calling `fetch()`:**

When using `fetch()` to make HTTP requests in JavaScript, the function returns a promise that represents the eventual completion (or failure) of the request. Since the operation is asynchronous, it does not return the data immediately. The `await` keyword is used to pause the execution of the surrounding code until the promise resolves, ensuring that the program waits for the data before proceeding. Without `await`, the code following the `fetch()` call will execute immediately, even though the data has not yet been retrieved, which can lead to errors or incomplete data being processed. By using `await`, the function ensures that the HTTP request completes before moving on to the next operation, preventing potential issues caused by the asynchronous nature of `fetch()`.

**3. Why we need to use the `csrf_exempt` decorator on the view used for AJAX POST requests:**

In Django, the CSRF (Cross-Site Request Forgery) protection mechanism is applied to all POST requests to ensure that they are coming from a trusted source, such as within the same site. When using AJAX to send POST requests, the server expects a valid CSRF token to be included in the request headers. If the token is missing, Django will block the request as a security measure. The `csrf_exempt` decorator can be used to bypass this check for specific views where including a CSRF token might not be possible or necessary, such as certain API endpoints. However, this should be done with caution, as disabling CSRF protection entirely for a view can expose the application to potential attacks. A better practice is to include the CSRF token in the AJAX request headers, but `csrf_exempt` can be useful in cases where this is not feasible.

**4. Why sanitization can't be done only in the front-end:**

Relying solely on front-end input sanitization for security is risky because the client-side code can be easily manipulated or bypassed by attackers. Users can modify or disable JavaScript on their browser, or directly send malicious requests to the server, skipping any client-side validation. This makes front-end sanitization insufficient for protecting against malicious input, such as SQL injection or XSS (Cross-Site Scripting). Therefore, while front-end validation can improve user experience by catching errors early, sanitization on the back-end is crucial for ensuring the data that reaches the server is clean and secure. The back-end is the only environment fully controlled by the application and thus must enforce strict data validation and sanitization to protect against potential vulnerabilities.

**5. Explain step by step**
- Sanitization can't be done solely on the front-end because users can manipulate or disable JavaScript, bypassing client-side validation. Malicious input could be sent directly to the server, so back-end sanitization is essential for security.

For AJAX GET requests, modify the data cards to use AJAX for retrieving data. Ensure that only data belonging to the logged-in user is fetched and displayed.

add this code in main.html :
```
async function getProductEntries(){
      return fetch("{% url 'main:show_json' %}").then((res) => res.json())
  }
```

- The `refreshObjectEntries` function dynamically updates the content of an HTML element with the ID `model_object_cards` by fetching and displaying object data asynchronously. First, it clears the element’s existing content and resets its CSS class. Then, it calls the `getObjectEntries()` function to retrieve data, using the `await` keyword to handle the asynchronous request. If no data is available, a message with a sad image is displayed, indicating that no object data is present. If data is found, the function loops through the entries and creates HTML cards for each object. These cards display sanitized object details, such as the name, description, price, and a rating visualized with a progress bar. Each card also includes action buttons for editing and deleting the object, linking to the appropriate URLs. Finally, the updated HTML and class are applied to the `model_object_cards` element.
```
async function refreshObjectEntries() {
    document.getElementById("model_object_cards").innerHTML = "";
    document.getElementById("model_object_cards").className = "";
    const objectEntries = await getObjectEntries();
    let htmlString = "";
    let classNameString = "";

    if (objectEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">No object data on DFootball yet.</p>
            </div>
        `;
    }
    else {
        classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
        objectEntries.forEach((item) => {
            const name = DOMPurify.sanitize(item.fields.name);
            const description = DOMPurify.sanitize(item.fields.description);
            const price = DOMPurify.sanitize(item.fields.price);
            htmlString += `
            <div class="relative break-inside-avoid">
                <div class="absolute top-1 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
                      <img src="{% static 'image/Football.png' %}" alt="Football" class="w-20 h-20 mb-4"/>
                </div>
                <div class="relative top-5 bg-white shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-[#3b82f6] transform rotate-1 hover:rotate-0 transition-transform duration-300">
                    <div class="bg-[#074173] text-white p-4 rounded-t-lg border-b-2 border-[#3b82f6]">
                        <h3 class="font-bold text-xl mb-2">${name}</h3>
                    </div>
                    <div class="p-4">
                      <div class="mb-4">
                          <p class="font-semibold text-lg mb-2">Price:</p>
                          <p class="text-gray-700">Rp. ${price}</p>
                      </div>
                      <div class="mb-4">
                          <p class="font-semibold text-lg mb-2">Description:</p>
                          <p class="text-gray-600">${description}</p>
                      </div>

                      <div class="mt-4">
                          <p class="text-gray-700 font-semibold mb-2">Rating</p>
                          <div class="relative pt-1">
                              <div class="flex mb-2 items-center justify-between">
                                  <div>
                                      <span class="text-xs font-semibold inline-block py-1 px-2 uppercase rounded-full text-blue-600 bg-blue-200">
                                          ${item.fields.rating > 10 ? '10+' : item.fields.rating}
                                      </span>
                                  </div>
                              </div>
                                <div class="overflow-hidden h-2 mb-4 text-xs flex rounded bg-indigo-200">
                                    <div style="width: ${item.fields.rating > 10 ? 100 : item.fields.rating * 10}%;" class="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-[#41A06F]"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="absolute top-0 -right-4 flex space-x-1">
                    <a href="/edit-object/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                        </svg>
                    </a>
                    <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                        </svg>
                    </a>
                </div>
            </div>
              `;
        });
    }
    document.getElementById("model_object_cards").className = classNameString;
    document.getElementById("model_object_cards").innerHTML = htmlString;
```

- Create a button that opens a modal with a form for adding a object entry. And add this code in main.html

```
<button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-[#41A06F] hover:bg-indigo-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
        Add New Item by AJAX
      </button>
```
This code creates a button element designed to trigger the display of a modal (popup) when clicked. The button uses `data-modal-target` and `data-modal-toggle` attributes to specify the modal with the ID `crudModal` as the target. The button's appearance is styled with various Tailwind CSS classes, giving it a green background (`bg-[#41A06F]`), white text, and rounded corners. On hover, the background color transitions to indigo (`hover:bg-indigo-600`), and the button animates with a slight upward movement (`hover:-translate-y-1`) and scaling effect (`hover:scale-105`). These transitions are smooth, with a duration of 300 milliseconds (`transition duration-300 ease-in-out`). The button also calls a JavaScript function `showModal()` when clicked, which is likely responsible for displaying the modal that allows users to add a new item via AJAX.

- Create a new view function to add a new object entry to the database. And add this in views.py
```
@csrf_exempt
@require_POST
def add_model_object_ajax(request):
    name = strip_tags(request.POST.get("name"))
    price = strip_tags(request.POST.get("price"))
    description = strip_tags(request.POST.get("description"))
    rating = strip_tags(request.POST.get("rating"))
    user = request.user

    new_object = ObjectEntry(
        name= name, 
        price=price,
        description=description,
        rating=rating,
        user=user
    )
    new_object.save()

    return HttpResponse(b"CREATED", status=201)
```
The `add_model_object_ajax` view function in Django handles an AJAX POST request to create a new object entry in the database. It bypasses CSRF protection and ensures only POST requests are allowed. The function retrieves and sanitizes user inputs like `name`, `price`, `description`, and `rating`, then associates the logged-in user with the new entry. After saving the new object to the database, it responds with a "CREATED" message and a 201 status code, indicating successful creation.

- Create a path that routes to the new view function you created. And add this in your urls.py
```
from main.views import show_main,..., add_model_object_ajax

path('create-ajax', add_model_object_ajax, name='add_model_object_ajax'),
```
This code snippet adds a new route to the Django application's URL configuration by defining a path that links to the `add_model_object_ajax` view function. By importing the necessary view from the `main.views` module and using the `path` function, it establishes a URL endpoint, `'create-ajax'`, that users can access to trigger the AJAX request for creating a new object entry. The `name='add_model_object_ajax'` parameter provides a unique identifier for this route, allowing it to be referenced easily throughout the application, such as in templates or when constructing URLs programmatically. This integration facilitates seamless communication between the front-end and back-end, enabling the dynamic creation of object entries without needing a full page refresh.

- Connect the form you created inside the modal to the path. And add this in the main.html
```
function addObjectEntry() {
    fetch("{% url 'main:add_model_object_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#objectEntryForm')),
    })
    .then(response => {
        refreshObjectEntries(); // Refresh the entries after submission
        hideModal(); // Hide the modal after submission
    })
    .catch(error => console.error('Error:', error));

    return false; // Prevent default form submission
  }
  document.getElementById("objectEntryForm").addEventListener("submit", (e) => {
    e.preventDefault(); // Prevents default form submission behavior
    addObjectEntry();
  });
```
This code snippet connects a modal form for adding a new object entry to the designated URL path for AJAX submissions. The `addObjectEntry` function utilizes the Fetch API to send a POST request to the URL generated by Django’s `{% url 'main:add_model_object_ajax' %}` template tag. It captures form data using `new FormData(document.querySelector('#objectEntryForm'))` and submits it in the request body. Upon successful submission, it refreshes the displayed object entries with `refreshObjectEntries()` and closes the modal using `hideModal()`. In case of an error, it logs the issue to the console. The code also prevents the default form submission behavior by attaching an event listener that calls `e.preventDefault()`, ensuring the form data is sent via AJAX without refreshing the page, thus enhancing user experience through asynchronous data handling.

- Perform refresh asynchronous on the main page to display the latest item list without reloading the entire main page. And add this into main.html:
```
refreshObjectEntries();
  const modal = document.getElementById('crudModal');
  const modalContent = document.getElementById('crudModalContent');

  function showModal() {
      const modal = document.getElementById('crudModal');
      const modalContent = document.getElementById('crudModalContent');

      modal.classList.remove('hidden'); 
      setTimeout(() => {
        modalContent.classList.remove('opacity-0', 'scale-95');
        modalContent.classList.add('opacity-100', 'scale-100');
      }, 50); 
  }
```
This code snippet is designed to manage the display of a modal dialog in a web application. It begins by invoking the `refreshObjectEntries()` function, which likely updates the content displayed on the page with the latest object entries. The modal's HTML elements are selected using `getElementById`, targeting the modal itself (`crudModal`) and its content (`crudModalContent`). The `showModal` function is defined to display the modal when called. Inside this function, the `hidden` class is removed from the modal element, making it visible. A `setTimeout` function is used to create a brief delay of 50 milliseconds before altering the appearance of the modal's content, allowing for a smoother transition effect. During this timeout, the classes `opacity-0` and `scale-95` are removed from the modal content, while `opacity-100` and `scale-100` are added, creating a fade-in and scale-up effect that enhances the user experience. Overall, this code facilitates a visually appealing and user-friendly modal display mechanism.