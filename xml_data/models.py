from django.db import models
import hashlib

md5sum = lambda f:hashlib.md5(file(f, 'r').read()).hexdigest()

# Create your models here.
class Xml(models.Model):
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=255,blank=True)
    url = models.CharField(max_length=255)
    enabled = models.BooleanField(blank=True,default=True)
    template = models.ForeignKey('XmlTemplate')

    def __unicode__(self):
        return self.title


class XmlUpdate(models.Model):
    xml = models.ForeignKey('Xml')
    update_time = models.DateTimeField(auto_now=True)
    md5sum = models.CharField(max_length=32)

    def __unicode__(self):
        return u'%s %s' % (self.xml.title,str(self.update_time))


class XmlTemplate(models.Model):
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=255,blank=True)
    enabled = models.BooleanField(blank=True,default=True)
    template = models.TextField(blank=True)
    
    def __unicode__(self):
        return self.title
    

class DataBase(models.Model):
    title = models.CharField(max_length=100)
    intro = models.CharField(max_length=255,blank=True)
    enabled = models.BooleanField(blank=True,default=True)
    
    def __unicode__(self):
        return title

class DataBaseTemplate(models.Model):
    database = models.ForeignKey('DataBase')
    template = models.ForeignKey('XmlTemplate')

    def __unicode__(self):
        return u'%s %s' % (self.database.title, self.template.title)
