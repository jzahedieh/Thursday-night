from django.contrib import admin

from thursday_night.apps.league.models import Event, Player, Session, Result


class EventAdmin(admin.ModelAdmin):
    pass


class SessionAdmin(admin.ModelAdmin):
    pass


class PlayerAdmin(admin.ModelAdmin):
    pass


class ResultAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Player, PlayerAdmin)
admin.site.register(Result, ResultAdmin)
