﻿from django.db import models
from django.utils.translation import gettext_lazy as _

from .base_manager import AsyncBaseManager


class AbstractTelegramUser(models.Model):
    """Абстрактная модель Telegram пользователя"""
    telegram_id = models.BigIntegerField(
        verbose_name=_('Телеграм ID'),
        unique=True,
        db_index=True,
    )
    username = models.CharField(
        _('Имя пользователя'),
        max_length=70,
        unique=True,
        db_index=True,
        null=True,
    )
    
    objects = AsyncBaseManager()
    
    class Meta: 
        abstract = True