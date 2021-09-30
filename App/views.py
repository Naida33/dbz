from django.shortcuts import render, redirect
from App.models import Item , Basket , Foot ,Chess ,Esport ,Ehlel
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
# Create your views here.


@login_required(login_url='login')
def base(request):
    Item_list = Item.objects.all()
    item_dictionary = {'items': Item_list}
    return render(request, 'App/base.html', context=item_dictionary)

def ehlel(request):
    Ehlel_list = Ehlel.objects.all()
    ehlel_dictionary = {'ehlels': Ehlel_list}
    return render(request, 'App/ehlel.html', context=ehlel_dictionary)


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
           form = CreateUserForm(request.POST)
           if form.is_valid():
               form.save()
               user = form.cleaned_data.get('username')
               messages.success(request, 'Account was created for' + user)
               return redirect('login')

    context = {'form': form}
    return render(request, 'App/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username Or password is isCorrect')
    context = {}
    return render(request, 'App/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')




def sags(request):
    
    Basket_list = Basket.objects.all()
    basket_dictionary = {'baskets': Basket_list}
    return render(request, 'App/sags.html', context=basket_dictionary)

def foot(request):
    Foot_list = Foot.objects.all()
    foot_dictionary = {'foots': Foot_list}
    return render(request, 'App/foot.html', context=foot_dictionary)

def chess(request):
    Chess_list = Chess.objects.all()
    chess_dictionary = {'chesss': Chess_list}
    return render(request, 'App/chess.html', context=chess_dictionary)

def esport(request):
    Esport_list = Esport.objects.all()
    esport_dictionary = {'esports': Esport_list}
    return render(request, 'App/esport.html', context=esport_dictionary)