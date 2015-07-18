from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
import datetime

from blog.models import Post, Category
from blog.settings import N_HOME_POSTS

def getc(request):
    c = RequestContext(request)
    c['categories'] = Category.objects.all()

    #sort out months menu (archive)
    stats = {}      # {<date> : n_posts, ... }
    for p in Post.objects.all():
        first_of_month = datetime.date(p.date.year, p.date.month, 1)
        stats[first_of_month] = stats.get(first_of_month, 0) + 1

    months = []
    for d, n in stats.items() :
        months.append({'date' : d, 'n_posts' : n})
    c['months'] = months

    return c


def home(request) :
    c = getc(request)
    c['posts'] = Post.objects.all().order_by("-date")[:N_HOME_POSTS]
    return render_to_response("blog/home.html", c)

def show_month(request, year, month) :
    c = getc(request)
    year = int(year)
    month = int(month)
    try:
        start = datetime.date(year, month, 01)
    # gracefully catch months greater than 13
    except ValueError:
        raise Http404("there are no valid months after 12")

    if month < 12:
        end = datetime.date(year, month+1, 01)
    elif month == 12:
        end = datetime.date(year, month, 01)

    c['posts'] = Post.objects.filter(date__gte=start, date__lt=end).order_by("-date")
    c['month'] = start
    return render_to_response("blog/show_month.html", c)

def show_post(request, year, month, title) :
    c = getc(request)
    c['posts'] = Post.objects.filter(title=title)
    if c['posts']:
        c['post'] = c['posts'][0]
        return render_to_response("blog/show_post.html", c)
    else:
        raise Http404("Not posts matching that title exist")

def show_category(request, category) :
    c = getc(request)
    c['posts'] = Post.objects.filter(categories__name=category).order_by("-date")
    c['category'] = category
    return render_to_response("blog/show_category.html", c)
