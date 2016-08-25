# -*- coding: utf-8 -*-

from django.db import models

class User(models.Model):
    def __unicode__(self):
        return unicode(self.username)

    account = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    priority = models.IntegerField()

class System(models.Model):
    def __unicode__(self):
        return unicode(self.system)

    system = models.CharField(max_length=50)

class Base(models.Model):
    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        verbose_name = '巡检基础表'
        verbose_name_plural = '巡检基础表'

    date = models.DateField()
    system_id = models.ForeignKey(System)
    subsystem = models.CharField(max_length=50)
    supervisor_1 = models.CharField(max_length=50)
    supervisor_2 = models.CharField(max_length=50)
    supervisor_3 = models.CharField(max_length=50)
    respector = models.CharField(max_length=50)
    experiment = models.CharField(max_length=50)
    IP = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    work = models.CharField(max_length=255)
    category = models.CharField(max_length=50)
    stateOrDate = models.CharField(max_length=255)
    More = models.CharField(max_length=255)

class Biz(models.Model):
    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        verbose_name = '业务情况表'
        verbose_name_plural = '业务情况表'

    system_id = models.ForeignKey(System)
    column = models.CharField(max_length=100)
    playStart = models.DateField()
    playFinish = models.DateField()
    numOfNeeds = models.IntegerField()
    allReadyTime = models.DateField()
    state = models.CharField(max_length=255)

class Event(models.Model):
    def __unicode__(self):
        return unicode(self.id)

    class Meta:
        verbose_name = '巡检事件表'
        verbose_name_plural = '巡检事件表'

    system_id = models.ForeignKey(System)
    date = models.DateField()
    event = models.CharField(max_length=255)