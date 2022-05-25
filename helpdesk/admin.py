from django.contrib import admin
from .models import Topicos, Procedimento

# Register your models here.
class TopicosAdmin(admin.ModelAdmin):
    list_display = ('titulo',)

class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('get_topico', 'passo_a_passo',)

    def get_topico(self, obj):
            return obj.topicos.titulo

admin.site.register(Topicos, TopicosAdmin)
admin.site.register(Procedimento, ProcedimentoAdmin)