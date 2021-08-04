from django.contrib.auth.models import User
from django.template.defaultfilters import title
from game.forms import CategoryForm, PageForm, UserForm, UserProfileForm, ChangePassword
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from game.models import Category, Comment, Page, UserProfile, WishList
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from game.plugs import calculator_simple
from game.bing_search import run_query

# weather function
weather = "None" 

def home(request):
    category_list = Category.objects.order_by('-likes')[:5]
    pages = Page.objects.order_by("-views")[:5]

    global weather
    if weather is "None":
        weather = calculator_simple.weather()
    context_dict = {}
    context_dict['boldmessage'] = "Today's weather is " + weather
    context_dict['categories'] = category_list
    context_dict['pages'] = pages

    #visitor_cookie_handler(request)
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
    #visitor_cookie_handler(request)
    #context_dict['visits'] = request.session['visits']
    #if request.session.test_cookie_worked():
    #    print("TEST COOKIE WORKED!")
    #    request.session.delete_test_cookie()
    return render(request, 'game/about.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category).order_by("-likes")

        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'game/category.html', context=context_dict)

def show_page(request, category_name_slug):
    context_dict = {}
    try:
        title = request.GET["game"]
        game = Page.objects.get(category=category_name_slug, title=title)
        id = game.id
        visitor_cookie_handler(request, game)
        context_dict['game'] = game
        try:
            comments = Comment.objects.filter(page=id)
            context_dict['comments'] = comments
        except Comment.DoesNotExist:
            context_dict['comments'] = None
    except Category.DoesNotExist:
        context_dict['game'] = None
    
    return render(request, 'game/Game.html/', context=context_dict)
    

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
    
def likes_page(request):
    username = request.GET["username"]
    title = request.GET["game"]
    try:
        game = Page.objects.get(title=title)
        game.likes += 1
        game.save()
    except Page.DoesNotExist:
        return HttpResponse("errors")
    
    return HttpResponse("success")

def comments(request):
    username = request.GET["username"]
    title = request.GET["game"]
    comment = request.GET["comment"]
    try:
        p = Page.objects.get(title=title)
        comm = Comment()
        comm.page = p
        comm.user=username
        comm.content = comment
        comm.save()
    except Page.DoesNotExist:
        return HttpResponse("errors")
    return HttpResponse("success")

def wishlist(request):
    username = request.GET['username']
    url = request.GET['url']
    title = request.GET['title']
    try:
        
        user = User.objects.get(username=username)
        userpro = UserProfile.objects.get(user=user)
        wishlist = WishList.objects.filter(user=userpro,url=url)
        if not wishlist:
            wishlist = WishList()
            wishlist.user = userpro
            wishlist.url = url
            wishlist.page = title
            wishlist.save()
        else:
            return HttpResponse("have")
    except User.DoesNotExist:
        return HttpResponse("errors")
    return HttpResponse("success")

def delete_comment(request):
    username, title, content = request.GET['content'].split("%%")
    #user = request.GET['user']
    try:
        pages = Page.objects.filter(title=title)
        for i in pages:
            Comment.objects.filter(page=i, content=content).delete()
    except Comment.DoesNotExist:
        return HttpResponse("errors")
    return HttpResponse("success")

def delete_wishlist(request):
    username, url = request.GET['content'].split("%%")
    try:
        print(username)
        print(url)
        
        user = User.objects.get(username=username)
        userpro = UserProfile.objects.get(user=user)
        WishList.objects.filter(user=userpro, url=url).delete()
    except UserProfile.DoesNotExist:
        return HttpResponse("errors")
    return HttpResponse("success")

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
                page.likes = 0
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
        print(request.POST)

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
def change_password(request):

    if request.method == 'POST':
        username = request.user.username
        password = request.POST.get('oldpassword')
        newpassword = request.POST.get('newpassword')
        reppassword = request.POST.get('reppassword')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            print(newpassword,reppassword)
            if newpassword == reppassword:
                user.set_password(newpassword)
                user.save()
                return redirect(reverse('game:account'))
            else:
                context_dict = {'errors': "The twice password is not same"}
                return render(request, 'game/change.html', context=context_dict)
        else:
            context_dict = {'errors':"wrong password"}
            return render(request, 'game/change.html', context=context_dict)
    else:
        print(request.user.username)
        return render(request, 'game/change.html')

@login_required
def account(request):
    print(request.user)
    username = request.user
    context_dict = {}
    try:
        user = User.objects.get(username=username)
        try:
            userpro = UserProfile.objects.get(user=user)
            comment = Comment.objects.filter(user=username)
            wishlist = WishList.objects.filter(user=userpro)
            context_dict['wishlists'] = wishlist
            context_dict['comments'] = comment
            #context_dict['user'] = userpro
        except UserProfile.DoesNotExist:
            context_dict['user'] = None
    except User.DoesNotExist:
        context_dict['user'] = None
    
    return render(request, 'game/account.html', context=context_dict)

@login_required
def user_logout(request):
    logout(request)

    return redirect(reverse('game:home'))

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request, page):

    #visits = int(request.COOKIES.get('visits', '1'))
    visits = page.views
    #visits = int(get_server_side_cookie(request, 'visits', '1'))

    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    #print("last visit time:  ", (datetime.now() - last_visit_time).seconds)

    if (datetime.now() - last_visit_time).seconds > 1:
        visits = visits + 1
        page.views += 1
        page.save()
        #response.set_cookie('last_visit', str(datetime.now()))
        request.session['last_visit'] = str(datetime.now())
    else:
        #response.set_cookie('last_visit', last_visit_cookie)
        request.session['last_visit'] = last_visit_cookie

    #response.set_cookie('visits', visits)
    request.session['visits'] = visits

def search(request):
    result_list = []
    query = ''

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            result_list = run_query(query)
    
    return render(request, 'game/search.html', {'result_list': result_list, 'query': query})