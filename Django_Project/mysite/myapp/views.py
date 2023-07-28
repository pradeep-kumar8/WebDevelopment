from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from mysite.forms import Userform
from myapp.models import Services, Ctu, About
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#signup view in which match password and if user exist show message to user
def Signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass2 != pass1:
            messages.error(request, f"Password didn't matched !")
            return render(request, 'signup.html')
        try:
            user = User.objects.get(username=username)
            messages.error(request, f"User already exist, try another username!")
            return render(request, 'signup.html')
        except User.DoesNotExist:
            myuser = User.objects.create_user(username, email, pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request, f'You are Sign Up Successfully...')
            return redirect('login')
    return render(request, 'signup.html')

#user login view that will provide login page and error message if raise
def Login(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                fname = user.first_name
                messages.success(request, f'You are Login Successfully...')
                return render(request, 'index.html', {'fname': fname})
            else:
                messages.error(request, f'UserName or Password Incorrect !')
                return redirect('login')
        return render(request, 'login.html')
    except Exception as e:
        print("An error occured!", e.args)


#view to user logout if user login
def Logout(request):
    logout(request)
    messages.success(request, f'You are LogOut Successfully...')
    return redirect('login')


# ******************************************************
# ******************************************************

#homepage view if user login then show all pages otherwise not
def HomePage(request):
    data = {
        'title': 'Home Page',
    }
    return render(request, 'index.html', data)


#footer form save view
@login_required(login_url='login')
def ctu(request):
    try:
        data = {}
        if request.method == "POST":
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            dob = request.POST.get('dob')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            file = request.FILES.get('file')
            name = fname + ' ' + lname
            try:
                modeldata = Ctu(Name=name, Dob=dob, Email=email, Phone=phone, File=file)
                modeldata.save()
                m = 'Data Inserted Successfully'
                data = {
                    'msg': m,
                    'title': 'Home Page',
                }
                msg = 'Data Inserted Successfully'
            except Exception as e:
                print('an error occured', e.args)
        return render(request, 'index.html', data)
    except Exception as e:
        print('Error occured!', e.args)


@login_required(login_url='login')
def services(request):
    data = {
        'title': 'Services',
    }
    return render(request, 'services.html', data)

#below view return blog with paginator functionilty
@login_required(login_url='login')
def blog(request):
    # servicesdata=Services.objects.all().order_by('-blog_title')[:3]
    servicesda = Services.objects.all().order_by('-blog_title')
    paginator = Paginator(servicesda, 3)
    page_num = request.GET.get('page')
    servicesdata = paginator.get_page(page_num)
    totalpage = servicesdata.paginator.num_pages

    #below code fetch value from url path
    if request.method == "GET":
        st = request.GET.get('stext')
        if st != None:
            servicesdata = Services.objects.filter(blog_title__icontains=st)
    data = {
        'st': st,
        'servicesdata': servicesdata,
        'last': totalpage,
        'pagelist': [n + 1 for n in range(totalpage)],
        'title': 'Blogs',
    }

    return render(request, 'blog.html', data)

#this below view make about page side form and return if user give value and save it into database
@login_required(login_url='login')
def aboutus(request):
    #this below function return form as html page about-us.html
    fn = Userform()
    data = {'form': fn,
            'title': 'About Us',
            }

    #below code save form value if user give
    if request.method=='POST':
        Name = request.POST['Name']
        Phone = request.POST['Phone']
        Email = request.POST['Email']
        Text = request.POST['Textarea']
        try:
            about=About(Name=Name, Phone=Phone, Email=Email, Textarea=Text)
            about.save()
            messages.success(request, f'Thank you for your Suggestion...')
            return redirect('about')
        except Exception as e:
            print('an error occured', e.args)
            return redirect('about')

    return render(request, 'about-us.html', data)


#this is only catact info page path
@login_required(login_url='login')
def contact(request):
    data = {
        'title': 'Contact',
    }
    return render(request, 'contact.html', data)


#NewsDes create new page where we show only one news
@login_required(login_url='login')
def newsDes(request, id):
    news = Services.objects.get(id=id)
    data = {
        'news': news,
        'title': 'News',
    }
    return render(request, 'newsDes.html', data)


#this below view make a function to add new blog page
@login_required(login_url='login')
def addblog(request):
    if request.method == "POST":
        Heading = request.POST['heading']
        Textarea = request.POST['textarea']
        try:
            blogdata = Services(blog_title=Heading, blog_desc=Textarea)
            blogdata.save()
            return redirect('blogs')
        except Exception as e:
            print('an error occured', e.args)

    return render(request, 'addblog.html')
