import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from .connection import Connection

def get_tea(tea_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT * FROM teaapp_tea t
        WHERE t.id = ?
        """, (tea_id,))

        return db_cursor.fetchone()

def tea_details(request, tea_id):
    if request.method == 'GET':
        tea = get_tea(tea_id)

        template = 'tea_details.html'
        context = {
            'tea': tea
        }

        return render(request, template, context)


