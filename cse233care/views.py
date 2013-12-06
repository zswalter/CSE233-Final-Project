from django.shortcuts import render_to_response

def main_view(request):
    return render_to_response('main_view.html', locals())

def logged_in_view(request):
    return render_to_response('logged_in_view.html', locals())

def register(request):
    return render_to_response('register.html', locals())
