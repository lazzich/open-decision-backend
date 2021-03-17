from django.contrib import admin
from .models import DecisionTree, Node, PublishedTree
# Register your models here.

admin.site.register(DecisionTree)
admin.site.register(Node)
admin.site.register(PublishedTree)
