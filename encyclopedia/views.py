from django.shortcuts import render
import markdown
import random

from . import util

def transl_md_html(title):
    content = util.get_entry(title)
    markdowner = markdown.Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = transl_md_html(title)
    if content == None:
        return render(request, "encyclopedia/null.html")
    else: 
        return render(request, "encyclopedia/entry.html", {
            "titulo": title,
            "contenido": content
        })

def search(request):
    if request.method == "POST":
        busqueda = request.POST['q']
        content = transl_md_html(busqueda)
        if content is not None:
            return render(request, "encyclopedia/entry.html", {
            "titulo": busqueda,
            "contenido": content
            })
        else:
            directorio = util.list_entries()
            resultado = []
            for entry in directorio:
                if busqueda.lower() in entry.lower():
                    resultado.append(entry)
            return render(request, "encyclopedia/busqueda.html", {
                "resultado" : resultado
            })

def add_article(request):
    if request.method == "GET":
        return render(request, "encyclopedia/add.html")
    else:
        title = request.POST['titulo']
        content = request.POST['contenido']
        article_exist = util.get_entry(title)
        if article_exist is not None:
            return render(request, "encyclopedia/exists.html")
        else:
            util.save_entry(title, content)
            content = transl_md_html(title)
        return render(request, "encyclopedia/entry.html", {
            "titulo": title,
            "contenido": content
        })

def edit_article(request):
    if request.method == "POST":
        title = request.POST['article']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
          "titulo": title,
          "articulo": content
        })

def save_edit(request):
    if request.method == "POST":
        title = request.POST['titulo']
        content = request.POST['contenido']
        util.save_entry(title, content)
        content = transl_md_html(title)
        return render(request, "encyclopedia/entry.html", {
            "titulo": title,
            "contenido": content
        })

def randomize(request):
    allArticles = util.list_entries()
    random_entry = random.choice(allArticles)
    content = transl_md_html(random_entry)
    return render(request, "encyclopedia/entry.html", {
            "titulo": random_entry,
            "contenido": content
        })
