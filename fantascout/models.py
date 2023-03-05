from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class FantaTask(models.Model):
    class Type(models.TextChoices):
        ABILITA_MANUALE = 'AM', _('Abilità Manuale')
        PROGRESSIONE_PERSONALE = 'PP', _('Progressione Personale')
        SPIRITO_SERVIZIO = 'SS', _('Spirito di Servizio')
        SPIRITO_PATTUGLIA = 'SP', _('Spirito di Pattuglia')
        GIOCHI = 'AW', _('Vincitore di giochi')
        STILE = 'ST', _('Stile')

    description = models.TextField()
    point = models.SmallIntegerField()
    type = models.CharField(max_length=2, choices=Type.choices)
    repetitive = models.BooleanField()
    personal = models.BooleanField()

class ScoutCompleteTask(models.Model):
    task = models.ForeignKey(FantaTask, on_delete=models.CASCADE)
    scout = models.ForeignKey("scout.Scout", on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    checked = models.BooleanField(default=False)