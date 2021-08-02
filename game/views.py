from typing import Container
from game.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from game.models import Category, Page
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime

def home(request):
    category_list = Category.objects.order_by('-likes')[:5]
    pages = Page.objects.order_by("-views")[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = pages

    visitor_cookie_handler(request)
    #context_dict['visits'] = request.session['visits']
    response = render(request, 'game/home.html', context=context_dict)
    #visitor_cookie_handler(request, response)
    
    #request.session.set_test_cookie()
    #return render(request, 'game/home.html', context=context_dict)
    return response

def about(request):
    print(request.method)
    print(request.user)

    context_dict = {}
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']
    #if request.session.test_cookie_worked():
    #    print("TEST COOKIE WORKED!")
    #    request.session.delete_test_cookie()
    return render(request, 'game/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'game/category.html', context=context_dict)

@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/game/')
        else:
            print(form.errors)
    return render(request, 'game/add_category.html', {'form': form})

@login_required
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    
    if  category is None:
        return redirect('/game/')

    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()

                return redirect(reverse('game:show_category', kwargs={'category_name_slug':category_name_slug}))
        else:
            print(form.errors)

    context_dict = {'form':form, 'category':category}
    return render(request, 'game/add_page.html', context=context_dict)


def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user


            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'game/register.html', context={'user_form':user_form, 'profile_form':profile_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('game:home'))
            else:
                return HttpResponse("Your game account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'game/login.html')

@login_required
def restricted(request):
    return render(request, 'game/restricted.html')

@login_required
def user_logout(request):
    logout(request)

    return redirect(reverse('game:home'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):

    #visits = int(request.COOKIES.get('visits', '1'))
    visits = int(get_server_side_cookie(request, 'visits', '1'))

    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    #print("last visit time:  ", (datetime.now() - last_visit_time).seconds)

    if (datetime.now() - last_visit_time).seconds > 1:
        visits = visits + 1
        #response.set_cookie('last_visit', str(datetime.now()))
        request.session['last_visit'] = str(datetime.now())
    else:
        #response.set_cookie('last_visit', last_visit_cookie)
        request.session['last_visit'] = last_visit_cookie

    #response.set_cookie('visits', visits)
    request.session['visits'] = visits