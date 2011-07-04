from django.shortcuts import render_to_response

def blog_home(request) :
    c = {}
    return render_to_response("blog/list.html", c)
