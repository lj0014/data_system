from xml_data.models import Xml
from xml_data.models import XmlUpdate
from xml_data.models import XmlTemplate
from xml_data.models import DataBase
from xml_data.models import DataBaseTemplate
from django.contrib import admin

admin.site.register(Xml)
admin.site.register(XmlUpdate)
admin.site.register(XmlTemplate)
admin.site.register(DataBase)
admin.site.register(DataBaseTemplate)
