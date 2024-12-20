from django.urls import path
from main.views import show_main, model_object, show_xml, show_json, show_xml_by_id, show_json_by_id, add_model_object_ajax
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_object
from main.views import delete_object
from main.views import create_product_flutter

app_name = 'main'


urlpatterns = [
    path('', show_main, name='show_main'),
    path('model-object', model_object , name='model_object'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-object/<uuid:id>', edit_object, name='edit_object'),
    path('delete/<uuid:id>', delete_object, name='delete_object'), # adjust to the name of the function you created
    path('create-ajax', add_model_object_ajax, name='add_model_object_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]