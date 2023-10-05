from django.contrib import admin
<<<<<<< HEAD
from .models import *


admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(User)

=======
from .models import Message, Chat
# Register your models here.


admin.site.register(Message)
admin.site.register(Chat)
>>>>>>> origin/main
