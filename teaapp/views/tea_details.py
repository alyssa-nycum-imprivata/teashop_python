import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from .connection import Connection
from teaapp.models import Tea, Packaging, TeaPackaging

def get_tea(tea_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_tea
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            t.name,
            t.flavor
        FROM teaapp_tea t
        WHERE t.id = ?
        """, (tea_id,))

        return db_cursor.fetchone()

def tea_details(request, tea_id):
    if request.method == 'GET':
        tea = get_tea(tea_id)

        packagings = get_packagings(tea_id)

        template = 'tea_details.html'
        context = {
            'tea': tea,
            'packagings': packagings
        }

        return render(request, template, context)

def create_tea(cursor, row):
    _row = sqlite3.Row(cursor, row)

    tea = Tea()
    tea.id = _row['id']
    tea.name = _row['name']
    tea.flavor = _row['flavor']

    return tea

def get_packagings(tea_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_packaging
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            t.id,
            p.id,
            p.name,
            tp.id,
            tp.tea_id,
            tp.packaging_id,
            tp.longevity_in_months
        FROM teaapp_tea t
        JOIN teaapp_teapackaging tp ON t.id = tp.tea_id
        JOIN teaapp_packaging p ON p.id = tp.packaging_id
        WHERE tp.tea_id = ?
        """, (tea_id,))

        packagings = db_cursor.fetchall()

        return packagings

def create_packaging(cursor, row):
    _row = sqlite3.Row(cursor, row)

    packaging = Packaging()
    packaging.id = _row['id']
    packaging.name = _row['name']

    teaPackaging = TeaPackaging()
    teaPackaging.id = _row['id']
    teaPackaging.tea_id = _row['tea_id']
    teaPackaging.packaging_id = _row['packaging_id']
    teaPackaging.longevity_in_months = _row['longevity_in_months']

    return (packaging, teaPackaging)

    


