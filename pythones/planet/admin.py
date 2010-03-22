from django.contrib import admin

from planet.models import Entry, Feed


class FeedAdmin(admin.ModelAdmin):
    pass


class EntryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Feed, FeedAdmin)
admin.site.register(Entry, EntryAdmin)
