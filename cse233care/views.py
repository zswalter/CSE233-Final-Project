from django.shortcuts import render_to_response

def main_view(request):
    return render_to_response('main_view.html', locals())

def logged_in_view(request):
    return render_to_response('logged_in_view.html', locals())

def log_in(request):
    return render_to_response('log_in.html', locals())  

def register1(request):
    return render_to_response('register1.html', locals())

def register2(request):
    return render_to_response('register2.html', locals())

def register3(request):
    return render_to_response('register3.html', locals())

def claims(request):
    return render_to_response('claims.html', locals())

def contact(request):
    return render_to_response('contact.html', locals())