from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
#from __future__ import unicode_literals
import codecs

###DPI
from mydatabase.models import Users
from mydatabase.models import Book
#from db.models import person
#from db.models import case
#from db.models import laptop
#from db.models import external_tools
#from db.models import log
#import codecs




from django.http import HttpResponse 




##############DPI



############

def hello(request):
    mm=[["a","b","c"],["d" , "e" , "f"],["h" , "i" , "k"]]
    return render_to_response('hello.html' )




def sabtenam(request):


    if 'username' in request.GET and request.GET['username']:
        #f = request.GET['firstname']
        #p = request.GET['password']
        #e = request.GET['email']


        username = request.GET['username']
        name = request.GET['name']
        family = request.GET['family']
        password = request.GET['password']
        email = request.GET['email']
        #birthday = request.GET['birthday']
        address = request.GET['address']




        sub = True
        if not (username or name or family or password or email or address):
        #if (not f) and (not p)  and (not e):
            vorood = False

        else :
            eusername = False
            ename= False
            efamily= False
            epassword= False
            eemail= False
            eaddress = False
            #ebirthday=False
            vorood = True
            #mina = Users.objects.filter(name__icontains=f)
            check_user = Users.objects.filter(username__icontains=username)

            str_check = str (check_user)
            if str_check == "[]" :
                tekrari = False
                if len(str(username)) > 15 or len(str(username)) < 4:
                    eusername = True
                elif len (str(name)) > 10 or len(str(name)) < 3 :
                    ename = True
                elif len (str(family)) > 30 or len(str(family)) < 3 :
                    efamily = True
                elif len (str(password)) > 15 or len(str(password)) < 4 :
                    epassword = True
                #elif len (str(address)) > 15 or len(str(name)) < 3 :
                    #ename = True
                elif len(str(address)) == 0 :
                    eaddress = True
                #elif len(str(email)) == 0 :
                elif not(((str(email).find("@") < str(email).find(".") ) and (str(email).find("@")!= -1 ))):
                    eemail = True
                else:
                    new_user=Users(name=name,password= password , email = email , username= username , adress = address , family = family , hesab = 0)
                    new_user.save()
            else :
                tekrari = True
                #ezafe kardan be db

        return render_to_response('sabtenam.html', {'efamily': efamily ,'eaddress': eaddress,'eemail': eemail ,'epassword': epassword ,'eusername' : eusername , 'ename' : ename , 'username' : username , 'password' :password , 'email' : email , 'error': vorood , "tekrari" : tekrari , "sub" : sub})

    else :
        sub = False
        return render_to_response('sabtenam.html', {'error': False , "sub" : sub})

