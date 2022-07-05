from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"), # главному маршруту присвоили имя home
    path('about/', about, name="about"),
    path('post/<int:post_id>/', show_post, name="post"), # post_id прилетает из get_absolute_url
                                     # при открытии страницы  show_post
    path('category/<int:cat_id>/', show_category, name="category")
]