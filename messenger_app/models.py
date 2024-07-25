from django.db import models
from django.utils.translation import gettext_lazy as _

class Chat(models.Model):
    users = models.ManyToManyField("custom_user.CustomUser", verbose_name=_(""))
    title = models.CharField(_("Titulo"), max_length=100)

    def __str__(self) -> str:
        return f'ID:{self.pk}, {self.title}'


class Message(models.Model):
    user = models.ForeignKey("custom_user.CustomUser", verbose_name=_(""), on_delete=models.CASCADE)    
    chat = models.ForeignKey("messenger_app.Chat", verbose_name=_(""), on_delete=models.CASCADE)
    content = models.TextField(_("Contenido"))

    created = models.DateTimeField(_("Enviado"), auto_now_add=True)

