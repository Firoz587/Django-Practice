from django.shortcuts import render
import datetime
def home(request):
    d = {'name':'Firoz','Age':20,'Gender':'Male','v':20,'value':datetime.datetime.now(),'lst': ['Md','Sheikh','Firoz','Islam'],'Courses':[
        {
            'id' : 1,
            'Name' : 'Python',
            'fees' : 10000
        },
        {
            'id' : 2,
            'Name' : 'Django',
            'fees' : 5000
        },
        {
            'id' : 3,
            'Name' : 'C++',
            'fees' : 12000
        },
        {
            'id' : 4,
            'Name' : 'C',
            'fees' : 2000
        },
        {
            'id' : 5,
            'Name' : 'Java',
            'fees' : 15000
        },
    ]}
    return render(request,"home.html",d)