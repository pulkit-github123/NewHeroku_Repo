from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import csv

# Add a new username to the file if it is not already existing
@api_view(['GET'])
def saveUsername(request):
    username = request.GET.get('username')
    fil = open('PostmanApp/Users.txt', 'a+')
    status = 'User Not Saved'
    with open('PostmanApp/Users.txt') as myfile:
        if username in myfile.read():
            status = "User Already Exists"
        else:
            fil.write('\n'+username)
            status = "User Saved"
    fil.close()
    return Response(status)


# To check the validity of the username
@api_view(['POST'])
def checkPassword(request):
    password = request.POST.get('password')
    status = 'Invalid password'
    l, u, p, d = 0, 0, 0, 0
    if (len(password) >= 8):
        for letter in password:
            if (letter.islower()):
                l+=1
            if (letter.isupper()):
                u+=1
            if (letter.isdigit()):
                d+=1
            if (letter=="@" or letter=="$" or letter=="_"):
                p+=1
            print(l,u,p,d)
            if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
                print("Valid Password")
                status = "Valid Password"
            else:
                print("Invalid Password")
                status = "Invalid Password"
            return Response(status)


#To check whether username already exists
@api_view(['GET'])
def checkUsername(request):
    username = request.GET.get('username')
    fil = open('PostmanApp/Users.txt', 'r+')
    users = fil.read().splitlines()
    fil.close()
    print(users)
    status = 'Invalid Username'
    if username in users:
        status = 'Valid Username'
    return Response(status)


# Getting the content from Products.csv and storing in a file
@api_view(['GET'])
def viewProducts(request):
    csv_file= open('PostmanApp/Products.csv')
    csv_reader= csv.reader(csv_file, delimiter =',')
    line_cout = 0
    display = []
    for row in csv_reader:
        if line_cout == 0:
            print(f'{row[1]} {row[2]} {row[3]} ')
            display.append(f'{row[1]} {row[2]} {row[3]} ')
            line_cout +=1
        else:
            print(f'{row[1]} \t {row[2]} \t {row[3]} ')
            line_cout +=1
            display.append(f'{row[1]} {row[2]} {row[3]} ')
    return Response(display)


