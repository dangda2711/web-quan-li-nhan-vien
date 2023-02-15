from django.apps import AppConfig

#định nghĩa ra tên của app
class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'
