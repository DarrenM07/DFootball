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
    form = ModelObjectForm(request.POST or None) #is used to create a new MoodEntryForm with the input from the user in request.POST entered into the QueryDict.

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
    2. Create a new function that receives a parameter request with the name show_xml and create a variable in the function itself that stores the result of the query of all data in the MoodEntry.
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
    6. Open the views.py file in the main directory and create a new function that receives a parameter request with the name show_json with a variable in the function itself that stores the result of the query of all data in the MoodEntry.
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
    from main.views import show_main, create_mood_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
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
    In views.py, the login_required decorator is imported from Django's authentication system to restrict access to certain views. By adding the @login_required(login_url='/login') decorator above the show_main function, access to the main page is restricted to authenticated users only. If a user tries to access the main page without being logged in, they will be redirected to the login page. This ensures that only logged-in users can view mood entries, enhancing security and user privacy. After implementing this, running the Django server will redirect unauthenticated users to the login page when attempting to access the main page.

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
        'mood_entries': mood_entries,  
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