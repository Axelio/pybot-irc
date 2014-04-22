#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importar algunas librerias necesarias.
import socket  

# Algunas variables básicas utilizadas para configurar el bot        
server = "" # Servidor al que conectar
channel = "#" # Canal al que unirse
botnick = "" # Nick del bot

def ping(): # Esta es nuestra primera función! Responderá a los pings del servidor.
  ircsock.send("PONG :Pong\n")  
  
def sendmsg(chan , msg): # Esta es la función de enviar mensajes, simplemente envía mensajes al canal.
  ircsock.send("PRIVMSG "+ chan +" :"+ msg +"\n") 

def joinchan(chan): # Esta función se utiliza para unirse a canales.
  ircsock.send("JOIN "+ chan +"\n")

def hello(): # Esta función responde a un usuario que escriba "Hello Mybot"
  ircsock.send("PRIVMSG "+ channel +" :Pues, no me llamo todos pero Hola!!\n")
                  
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, 6667)) # Aqui conectamos con el servidor utilizando el puerto 6667
ircsock.send("USER "+ botnick +" "+ botnick +" "+ botnick +" :Este bot es el resultado de un tutorial que se encuentra en http://shellium.org/wiki.\n") # Autentificación de usuario
ircsock.send("NICK "+ botnick +"\n") # aquí es donde verdaderamente asignamos el alias al bot


while 1: # Cuidado con esto! Podría crear un bucle infinito
  ircmsg = ircsock.recv(512) # recibe datos del servidor
  ircmsg = ircmsg.strip('\n\r') # elimina saltos de línea innecesarios
  print(ircmsg) # Aquí mostramos lo que viene del servidor

  if ircmsg.find("hola a todos") != -1: # Si podemos encontrar "Hello Mybot" llamará a la función hello()
    hello()
  if ircmsg.find("PING :") != -1: # si el servidor nos hace ping entonces respondemos
    pongid = ircmsg.split('\r')[0].split(':')[1]
    ircsock.send("PONG :%s\n" % (pongid))
  joinchan(channel) # Entra al canal utilizando la función definida anteriormente
