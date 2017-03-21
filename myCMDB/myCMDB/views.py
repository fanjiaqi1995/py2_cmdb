# coding:utf-8
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


def index(request):
    try:
        cookie_username = request.COOKIES["username"]
        session_username = request.session["username"]
        username = request.COOKIES["username"]

        return render_to_response("index.html, locals")
    except:
        return HttpResponseRedirect("/Enter/login")


def setcookie(request):
    cookies = request.COOKIES
    response = render_to_response("setcookie")
