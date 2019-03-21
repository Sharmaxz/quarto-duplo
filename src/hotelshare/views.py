from django.shortcuts import render
from hotelshare.forms import RequestForm, UserForm
from hotelshare.models import Request, User


def index(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            uf.save()
    elif request.method == 'GET':
        uf = UserForm()

    #rs = User.objects.all()

    ctx = {'userForm': uf,

    }

    return render(request, "index.html", ctx)


def list(request):
    req = Request.objects.all()
    ctx = {'request': req, }

    return render(request, "list.html", ctx)

