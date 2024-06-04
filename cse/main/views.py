from django.shortcuts import render,HttpResponse,redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
# Create your views here.
@login_required(login_url="/login/")
def landing_page(request):

    
    

    username = request.user.username
    # try:

    #     user_actual_name = user_profile.objects.get( user=request.user)
    #     picture = user_actual_name.profile_picture.url
    #     u1 = user_actual_name.student_details.name

    # # print(user_actual_name)
    #     context = {"message":'Home',"user":u1 , "pic":picture}
    #     return render(request,'landing_page.html',context)

    # except:
    #     return render(request,'landing_page.html')
    context = {"user":username}

    return render(request,'landing_page.html',context)


from django.contrib.auth import authenticate, login,logout


def login_page(request):

    context = {"message":'Login Page'}

    if request.method == "POST":
        data = request.POST
        username = data.get("username1")
        password = data.get("password1")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
        # # Redirect to a success page.
        #     return redirect('/home/')
            next_url = request.GET.get('next') or request.session.get('next_url')
            if next_url:
                # Clear the 'next' parameter from the session
                request.session.pop('next_url', None)
                return redirect(next_url)
            else:
                return redirect('/home/')
        else:
        # Return an 'invalid login' error message.
            return HttpResponse("Invalid Credentials")
    return render(request,'login.html',context)


def logout_page(request):
    logout(request)

    return redirect("/login/")

@login_required(login_url="/login/")
def marks(request):
    username = request.user.username

    context = {'username': username}
    return render(request , 'marks.html',context)

@login_required(login_url="/login/")
def register_student(request):

    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        enrollment = data.get('enrollment')
        roll_no = data.get('roll_no')
        semester = data.get('semester')
        year = data.get('year')
        # print(semester)
        semester_name = Semester.objects.get(semester = semester)
        year_en = Years.objects.get(year = year)
        

        if Students.objects.filter(enrolment_no= enrollment).exists():
            messages.info(request, "This Enrollment Number already exists.")
            return redirect("/register/")

        else:

            student = Students.objects.create(
            name = name,
            enrolment_no =enrollment,
            exam_roll_no = roll_no,
            semester = semester_name,
            year_enrolled = year_en
            )
            return redirect('/register/')


        

        

        

    return render(request,'register_student.html')

@login_required(login_url="/login/")
def register_select(request):
    # if request.method == "POST":
        # action = request.POST.get("action")
        # if action == 'First':

        # return redirect('/register/')
    return render(request,'register_select.html')

# @login_required(login_url="/login/")
# def result_input(request):
#     return render(request,'resultinput.html')




from .decorators import faculty_required

@login_required(login_url="/login/")
@faculty_required
def result_input(request):
    
    return render(request,'resultinput.html')

# @login_required(login_url="/login/")
# def User_profile(request):

#     user_actual_name = user_profile.objects.get( user=request.user)
#     picture = user_actual_name.profile_picture.url
#     Name = user_actual_name.student_details.name
#     Enrolment_no = user_actual_name.student_details.enrolment_no
#     Exam_roll_no = user_actual_name.student_details.exam_roll_no
#     Year_enrolled = user_actual_name.student_details.year_enrolled
#     Sem = user_actual_name.student_details.semester

    

#     context = {"message":"User Profile" , "user":Name , "enrol":Enrolment_no , "exam_roll":Exam_roll_no , "year_enroll":Year_enrolled,"sem":Sem}
#     if request.method == "POST":
#         data = request.POST
#         name = data.get('name')
#         enroll = data.get('enrollment')
#         roll = data.get('roll_no')
#         semester = data.get('semester')
#         year = data.get('year')
#         image = request.FILES['image']

#         print(name)
#         print(enroll)
#         print(roll)
#         print(semester)
#         return redirect("/home/")





#     return render(request,'user_profile.html',context)
