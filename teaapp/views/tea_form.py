import sqlite3
from django.shortcuts import render
from .connection import Connection

def tea_form(request):
    if request.method == 'GET':
        template = 'tea_form.html'

        return render(request, template)