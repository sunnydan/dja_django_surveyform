from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, "index.html")

def process(request):
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['favoritelanguage'] = request.POST['favoritelanguage']
        request.session['comment'] = request.POST['comment']
        return  redirect("/surveys/result")
    else:
        return redirect("/surveys/")

def result(request):
    return render(request, "result.html")