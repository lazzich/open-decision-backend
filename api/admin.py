from django.contrib import admin
from .models import DecisionTree, Node, PublishedTree
from users.models import CustomUser
# Register your models here.

admin.site.register(DecisionTree)
admin.site.register(Node)
admin.site.register(PublishedTree)
admin.site.register(CustomUser)
