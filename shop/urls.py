from django.urls import path
from shop import views
urlpatterns=[
    path('',views.home,name='home'),
    path('search/',views.searching,name='search'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.prodetails,name='details'),




]