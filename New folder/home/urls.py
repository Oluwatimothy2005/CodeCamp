from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('products', views.products,name='products'),
    path('category/<str:id>', views.category, name='category'),
    path('detail/<str:id>/<slug:slug>', views.detail, name='detail'),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('signout', views.signout,name='signout'),
    path('signin', views.signin,name='signin'),
    path('signup', views.signup,name='signup'),
    path('profile', views.profile,name='profile'),
    path('profile_update', views.profile_update,name='profile_update'),
    
]
