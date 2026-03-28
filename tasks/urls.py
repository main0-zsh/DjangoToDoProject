from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='tasks/index.html',
        extra_context={'title': 'Главная страница'}
    ), name='index'),

    path('create/', TemplateView.as_view(
        template_name='tasks/create_task.html',
        extra_context={'title': 'Создание задачи'}
    ), name='create_task'),

    path('task/<int:task_id>/', TemplateView.as_view(
        template_name='tasks/view_task.html',
        extra_context={'title': 'Просмотр задачи'}
    ), name='view_task'),

    path('edit/<int:task_id>/', TemplateView.as_view(
        template_name='tasks/edit_task.html',
        extra_context={'title': 'Редактирование'}
    ), name='edit_task'),

    path('delete/<int:task_id>/', TemplateView.as_view(
        template_name='tasks/delete_task.html',
        extra_context={'title': 'Удаление задачи'}
    ), name='delete_task'),
    path('user-form/', views.user_form_view, name='user_form')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
