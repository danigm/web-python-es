import datetime
import feedparser

from django.template import RequestContext
from planet.models import Feed, Entry
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse


def entry_from_feed(entry):
    date = datetime.datetime(*entry.updated_parsed[:7])
    return Entry(author=entry.get('author', ''),
                title=entry.title,
                link=entry.link,
                updated=date,
                html=entry.summary)


def update(request):
    feeds = Feed.objects.all()
    for f in feeds:
        feed_date = f.last_update
        feed = feedparser.parse(f.url)
        entries = feed.entries
        entries.reverse()
        maxdate = None
        for entry in entries:
            date = datetime.datetime(*entry.updated_parsed[:7])
            if feed_date and feed_date < date:
                feed_date = date
                new_entry = entry_from_feed(entry)
                new_entry.save()
            elif not feed_date:
                feed_date = date
                new_entry = entry_from_feed(entry)
                new_entry.save()
        f.last_update = feed_date
        f.save()

    return HttpResponse("ok")


def index(request):
    entries = Entry.objects.all().order_by('-updated')
    return render_to_response("planet/index.html",
              {'entries': entries},
              context_instance=RequestContext(request))
