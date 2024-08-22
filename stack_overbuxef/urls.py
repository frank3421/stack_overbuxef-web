from django.urls import include,path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login_user, name='login'),
    path('register', views.register_user, name='register_user'),
    path('logout',views.logout_user, name='logout'),
    path('forum', views.forum, name='forum'),
    path('message', views.publish_message, name='message'),
    path('profile', views.profile, name='profile'),
    path('profile/<int:user_id>/', views.profile, name='other_profile'),
    path('admin/', admin.site.urls),
    path('consults/<int:consult_id>/', views.modalAnswers, name='answers'),
    path('makeAnswer/<int:consult_id>/', views.makeModalAnswer, name='makeAnswer'),
    path('deleteComment/<int:consult_id>/', views.deleteComment, name='deleteComment'),
    path('deleteReply/<int:reply_id>/', views.deleteReply, name='deleteReply'),
    path('tags/', views.tags, name='tags'),
    path('delete_tag/<int:tag_id>/', views.deleteTag, name='delete_tag'),
    path('select2/', include("django_select2.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('like/<int:id>/', views.like_consulta, name='like_consulta'),
    path('dislike/<int:id>/', views.dislike_consulta, name='dislike_consulta'),
    path('like1/<int:id>/', views.like_answer, name='like_answer'),
    path('dislike1/<int:id>/', views.dislike_answer, name='dislike_answer'),
    path('votePost/<int:id>/', views.consulta_like_dislike, name='consulta_like_dislike'),
    path('voteAnswer/<int:id>/', views.answer_like_dislike, name='answer_like_dislike')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
