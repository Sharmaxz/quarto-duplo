from django.shortcuts import render
from hotelshare.forms import RequestForm, UserForm
from hotelshare.models import Request, User


def index(request):
    user_id = None
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user_id = user.id
            print(user.__dict__)
        request_form = RequestForm(request.POST)
        if request_form.is_valid():
            request_model = request_form.save()
            print(request_model.__dict__)

    user_form = UserForm()
    request_form = RequestForm()
    #rs = User.objects.all()

    ctx = {'userForm': user_form,
           'requestForm': request_form,
           'id': user_id
            }

    return render(request, "index.html", ctx)


def list(request):
    req = Request.objects.all()
    ctx = {'request': req, }

    return render(request, "list.html", ctx)




