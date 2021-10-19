
from django.http import HttpResponse
from django.shortcuts import render



def homepage(request):
    return render(request, 'Home.html')


def aboutpage(request):
    return render(request, 'About.html')


def contactpage(request):
    return render(request, 'Contact.html')

def productpage(request):
    return render(request, 'Products.html')


def contactus(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    message = request.GET.get('message')
    sendquery(name,email,message)
    return (HttpResponse("<h1> Responses are submitted we will revert to you soon</h1>"))


def user(request):
    return render(request,'passwordmanager.html')

def sendquery(name,email,message):
    import os
    os.chdir('C:\\Users\\ts751413')
    import mysql.connector
    from mysql.connector.constants import ClientFlag
    config = {
                'user': 'root',
                'password': 'tarunsh2908',
                'host': '35.244.28.202',
                'database': 'PasswordManager',
                'client_flags': [ClientFlag.SSL],
                'ssl_ca': 'server-ca.pem',
                'ssl_cert': 'client-cert.pem',
                'ssl_key': 'client-key.pem'

            }
    cnxn = mysql.connector.connect(**config)
    mycursor = cnxn.cursor()
    mycursor.execute(f"INSERT INTO queries (name,emailid,message) VALUES (%s,%s,%s)",(name,email,message))
    cnxn.commit()
    return email
