from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
friends={
    "Tanishq":"Jolly & lively",
    "Raunit":"Smart & witty",
    "Katyayan":"Funny & witty",
    "Himanshu":"Smart & determinant",
    "Rohit":"Sweet & Kind",
    "Amrita":"Sweet & Witty",
    "Vanshika":"Passionate & Humble",
    "Ashish":"Smart & Well-spoken",
    "Shivendra":"Sweet & Polite",
    "Aakash":"Hardworking & Persistent",
    "Nikita":"Polite & Down-To-Earth",
    "Paarth":"Genuine & Intelligent",
    "Hardik":"Good-looking & Artistic",
    "Disha":"Sweet & Caring",
    "Tanisha":"Good looking & Confident",
    "Jigyasa":"Smart & Hardworking",
    "Akshat":"Creative & Sweet",
    "Ankita":"Creative and Nice",
    "Aahana":"Hardworking and Confident",
    "Manisha":"Jolly & Caring",
    "Harshvardhan":"Hardworking & Persistent",
    "Deepika":"Sweet & Polite",
}

def friend_char(request,friend):
    try:
        college_friend=friends[friend]
        return HttpResponse(college_friend)
    except:
        return HttpResponseNotFound("Not well known to me")
    
