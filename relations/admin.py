from django.contrib import admin
from .models import Tag, Author, AuthorBiogram, Publication
# Register your models here.


class PublicationInline(admin.TabularInline):
    model = Publication
    fields = ['title', 'year']
    extra = 1  # domyslna ilosc nowych linii w inline

class AuthorBiogramInline(admin.StackedInline):
    model = AuthorBiogram

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name", "last_name"]
    inlines = [AuthorBiogramInline, PublicationInline]

admin.site.register(Tag)
admin.site.register(Author, AuthorAdmin)
admin.site.register(AuthorBiogram)
admin.site.register(Publication)