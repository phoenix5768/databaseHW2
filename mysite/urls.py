from django.urls import path, include
from mysite import views

urlpatterns = [
    path('', views.home, name="home"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('query', views.query, name="query"),
    path('users', views.users, name="users"),
    path('disease', views.disease, name="disease"),
    path('record', views.record, name="record"),

    path('update_country/<cname>', views.update_country, name="update-country"),
    path('delete_country/<cname>', views.delete_country, name="delete-country"),
    path('add_country', views.add_country, name="add-country"),

    path('update_disease/<disease_code>', views.update_disease, name="update-disease"),
    path('delete_disease/<disease_code>', views.delete_disease, name="delete-disease"),
    path('add_disease', views.add_disease, name="add-disease"),

    path('update_diseasetype/<id>', views.update_diseasetype, name="update-diseasetype"),
    path('delete_diseasetype/<id>', views.delete_diseasetype, name="delete-diseasetype"),
    path('add_diseasetype', views.add_diseasetype, name="add-diseasetype"),

    path('update_discover/<cname>/<disease_code>', views.update_discover, name="update-discover"),
    path('delete_discover/<cname>/<disease_code>', views.delete_discover, name="delete-discover"),
    path('add_discover', views.add_discover, name="add-discover"),

    path('update_user/<email>', views.update_user, name="update-user"),
    path('delete_user/<email>', views.delete_user, name="delete-user"),
    path('add_user', views.add_user, name="add-user"),

    path('update_doctor/<email>', views.update_doctor, name="update-doctor"),
    path('delete_doctor/<email>', views.delete_doctor, name="delete-doctor"),
    path('add_doctor', views.add_doctor, name="add-doctor"),

    path('update_specialize/<id>', views.update_specialize, name="update-specialize"),
    path('delete_specialize/<id>', views.delete_specialize, name="delete-specialize"),
    path('add_specialize', views.add_specialize, name="add-specialize"),

    path('update_servant/<email>', views.update_servant, name="update-servant"),
    path('delete_servant/<email>', views.delete_servant, name="delete-servant"),
    path('add_servant', views.add_servant, name="add-servant"),

    path('update_record/<email>/<cname>/<disease_code>', views.update_record, name="update-record"),
    path('delete_record/<email>/<cname>/<disease_code>', views.delete_record, name="delete-record"),
    path('add_record', views.add_record, name="add-record"),
]
