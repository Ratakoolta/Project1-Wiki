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
    html_content = transl_md_html(title)
    if html_content == None:
        return render(request, "encyclopedia/null.html")
    else: 
        return render(request, "encyclopedia/entry.html", {
            "titulo": title,
            "contenido": html_content
        })
