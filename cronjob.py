#!/usr/local/python/bin/python
# -*- coding: utf-8 -*-

from django.core.management import setup_environ
import data_system.settings 
setup_environ(data_system.settings)
from xml_data.models import Xml, XmlUpdate 
import hashlib
import urllib2
import datetime
from multiprocessing import Process


def check_process(xml):
    resp = urllib2.urlopen(xml[1].encode('utf-8'))
    new_md5sum = hashlib.md5(resp.read()).hexdigest()
    if new_md5sum != xml[2]:
        XmlUpdate(xml=xml[0],update_time=datetime.datetime.now(),md5sum=new_md5sum).save()    


if __name__  == "__main__":
    #读取xml
    xmls = []
    for xml in Xml.objects.filter(enabled=True).all():
        update_info = XmlUpdate.objects.filter(xml=xml.id).order_by('-update_time')
        md5sum = ''
        if update_info:
            md5sum = update_info[0].md5sum
        xmls.append((xml,xml.url,md5sum))
    tasks = []
    for xml in xmls:
        p = Process(target=check_process,args=(xml,))
        p.start()
        tasks.append(p)
    for t in tasks:
        t.join()
