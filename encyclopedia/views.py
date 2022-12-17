from django.shortcuts import render
import markdown

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
