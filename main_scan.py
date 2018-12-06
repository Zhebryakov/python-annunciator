#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.header import Header
from base64 import encodebytes
import email
import mimetypes
from email import encoders


import sys
import string
import shutil

import pdb

import ctypes
import datetime
import time
from  datetime import timedelta



from tkinter.messagebox import *



host="name sptp-server"
port=21
main_dir = "//server/share"
nameprinyat="spisok.txt"



CurrentDat=datetime.date.fromtimestamp(time.time())
check_year=CurrentDat.strftime("%Y")
check_month=CurrentDat.strftime("%m")
check_day=CurrentDat.strftime("%d")


tekdir=main_dir+"\\"+check_year+"\\"+check_month+"\\"+check_day+"\\"

def MessageAllInc(mess,namefile):                
    fromadr="frommail@domen.ru"
    toadr=["person1@domen.ru","person2@domen.ru"]
    
    toadrs="person1@domen.ru>"
    mail_coding = 'utf-8'
    outs=mess
  
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(namefile,"rb").read() )
    basename = os.path.basename(namefile)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)
    
    message=MIMEMultipart('related')
    message['Subject']=Header("subject mail",mail_coding)
    message['From']=Header(fromadr,mail_coding)
    message['To']=Header(toadrs,mail_coding)

    
    msg=MIMEText(outs.encode(mail_coding),'plain',mail_coding)
    msg.set_charset(mail_coding)
    
    message.attach(msg)
    message.attach(part)

    s=smtplib.SMTP(host)
    s.sendmail(fromadr,toadr,message.as_string())
    s.quit()    


prinyaty=[]
# если директории ещё нет - значит делать нечего
if os.path.isdir(tekdir):
    #ищем файл "spisok.txt"
    print(tekdir)
    if os.path.isfile(tekdir+"\\"+nameprinyat) :
        inpfile=open(tekdir+"\\"+nameprinyat,'rt', encoding='cp1251',errors ='ignore' )
        countstr=0
        NameFile=""
        for stroka in inpfile.readlines():
            countstr=countstr+1
            prinyaty.append(stroka.rstrip())
            print(stroka)
            print(prinyaty)
        inpfile.close()
    else :
        inpfile=open(tekdir+"\\"+nameprinyat,'w+', encoding='cp1251',errors ='ignore' )    
        inpfile.close()
        
    names = os.listdir(tekdir)
    # список файлов и поддиректорий в данной директории        
    for name in names:
        if name==nameprinyat :
            continue
        namefile=tekdir+"\\"+name
        # директории внутри не смотрим
        if os.path.isfile(namefile):
            print (name)
            if name in prinyaty :
                # ничего не делаем
                print("файл уже обработан")
            else :
                prinyaty.append(name)
                inpfile=open(tekdir+"\\"+nameprinyat,'a', encoding='cp1251',errors ='ignore' )
                inpfile.writelines(name+"\n")
                inpfile.close()
                
                MessageAllInc("new file received",namefile)
                




    
