#!/usr/bin/python
#dcrespo

fichero=open("/etc/passwd", "r")
lista=fichero.readlines()
dicc = {}

for linea in lista:
	comand=linea.split(":")	
	user=comand[0]
	shell=comand[-1][:-1]
	dicc[user]= shell

try:
	print dicc ["root"]
	print dicc ["imaginario"]
except KeyError:
	print ("username desconocido")
print len(lista)
