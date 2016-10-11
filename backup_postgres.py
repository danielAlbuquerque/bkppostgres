#!/usr/bin/python

import time
import subprocess
import os
from subprocess import call

folder_name = time.strftime("%Y%m%d")
diretorio = os.path.dirname(os.path.abspath(__file__)) +"/"+folder_name

if not os.path.exists(diretorio):
    os.makedirs(diretorio)

print "[",time.strftime('%H:%M:%S'),"]","#> ROTINA DE BACKUP DO DMAST"
print "[",time.strftime('%H:%M:%S'),"]","#> SYSADMIN: daniel.alb.querque@gmail.com(Daniel Albuquerque)"
print "[",time.strftime('%H:%M:%S'),"]","#> DATA: ", time.strftime("%d/%m/%Y")
print "[",time.strftime('%H:%M:%S'),"]","#> DIRETORIO: ", diretorio


proc = subprocess.Popen(["pg_dump -v -F c -h localhost dmast_production -U postgres > "+ diretorio +"/dmast_production_" + folder_name +".dmp"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()

print "[",time.strftime('%H:%M:%S'),"]","#> BACKUP REALIZADO COM SUCESSO"


