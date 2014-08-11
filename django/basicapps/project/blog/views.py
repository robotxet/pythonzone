from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from models import *


class PostListView(ListView):
    model = Post
    paginate_by = 20


class CategoryListView(ListView):
    model = Category
