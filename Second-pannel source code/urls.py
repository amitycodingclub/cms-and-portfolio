from django.urls import path
from . import views
import accounts.views
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('create/',views.create,name='create'),
    path('update/',views.job,name='job'),
    path('home/',jobs.views.home,name='home'),
    path('',views.allblogs,name='allblogs'),
    path('<int:blog_id>/',views.detail,name="detail"),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
] 