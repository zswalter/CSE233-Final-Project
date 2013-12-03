from django.http.response import HttpResponse

def mainview(request):
    return HttpResponse("""
<!DOCTYPE html>
<html>
<head>
    <title>
        Welcome to CSE233Care!
    </title>
</head>
<body>
    <h1>Here is the main page</h1>
    <p>Here is where we'll have some bootstrappy things</p>
</body>
</html>
    """)
