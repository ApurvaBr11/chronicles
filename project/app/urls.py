from django.urls import path,include,re_path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('', hom , name='home'),
    path('register/', register , name='register'),
    path('create/', create_post , name='create'),
    path('login/', login_view , name='login'),
    path('logout/', logout_view, name='logout'),
    path('viewmyposts/', viewmyposts, name='viewmyposts'),
    path('view/<int:id>', view, name='view'),
    path('viewUser/<int:id>', viewUser, name='viewUser'),
    path('viewcategorie/<int:id>', viewcategorie, name='viewcategorie'),
    path('delete/<int:id>', delete, name='delete'),
    path('edit/<int:id>', edit, name='edit'),
    path('deletecomment/<int:id>', deletecomment, name='deletecomment'),
    path("search/",searchNews, name="search"),
    re_path('^', include('django.contrib.auth.urls')),
    path('like/<int:student_id>/', like_student, name='like_student'),
    path('follow/<int:user_id>/', toggle_follow, name='toggle_follow'),
    path('select_categories/', select_categories, name='select_categories'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
