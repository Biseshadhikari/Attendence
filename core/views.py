from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from datetime import datetime
import time
from django.db.models import Q
from .forms import *
from .models import *
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User

def signin(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user_obj = User.objects.filter(username=username).first()
            if user_obj is None:
                messages.success(request, 'User not found! Please sign in with the correct username.')
                return redirect('/login')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # Check if 'redirect' parameter exists in GET request, else redirect to home
                redirect_url = request.GET.get('redirect', '/')  # Defaults to 'home' if no redirect is specified
                return redirect(redirect_url)
            else:
                messages.success(request, 'Wrong password.')
                return redirect('/login')

        return render(request, 'core/login.html')
    else:
        return redirect('/')

    


@login_required(login_url='login')
def Home(request):
    date_min = request.GET.get("from")
    date_max = request.GET.get("to")
    users = request.GET.get('user')

    if request.method == "POST":
        value = request.POST.get('btn')
        if value == "Entry":
            t = time.localtime()
            current_time = str(timezone.localtime(timezone.now()))[:10]
            attended_today = Attendance.objects.filter(employee=request.user, entry__startswith=str(current_time))
            attd_no = len(attended_today)

            if attd_no > 0:
                messages.warning(request, "Today's entry already recorded.")
            else:
                entry = str(timezone.localtime(timezone.now()))
                attendance = Attendance(employee=request.user, entry=entry)
                attendance.save()
                messages.success(request, "Today's entry recorded.")
                
            return redirect('home')  # Use the appropriate URL name for the home view
        elif value == "Exit":
            t = time.localtime()
            current_time = str(timezone.localtime(timezone.now()))[:10]
            attended_today = Attendance.objects.filter(employee=request.user, entry__startswith=str(current_time))
            attd_no = len(attended_today)
            attd = len(Attendance.objects.filter(employee=request.user, leave__startswith=str(current_time)))

            if attd > 0:
                messages.warning(request, "Today's exit already recorded.")
            elif attd_no > 0:
                attended = attended_today.first()
                attended.leave = str(timezone.localtime(timezone.now()))
                attended.save()
                messages.success(request, "Today's exit recorded.")
            else:
                messages.warning(request, "Please enter the entry first")

            return redirect('home')  # Use the appropriate URL name for the home view

    else:
        todays_current_data = str(timezone.localtime(timezone.now()))[:10]

        if request.user.is_superuser:
            data = Attendance.objects.all().order_by('-created_at')

            if date_min and date_max:
                data = data.filter(created_at__gte=date_min, created_at__lt=date_max)

            elif date_min:
                data = data.filter(created_at__gte=date_min)

            elif date_max:
                data = data.filter(created_at__lt=date_max)

            # Add the following for the search user field
            if users:
                data = data.filter(employee__username__icontains=users)
        else:
            person = User.objects.get(username=request.user.username)
            data = Attendance.objects.filter(employee=person).order_by('-created_at')
            if date_min and date_max:
                data = Attendance.objects.filter(employee=person,created_at__gte=date_min, created_at__lt=date_max)
            elif date_min:
                data = Attendance.objects.filter(employee=person,created_at__gte=date_min)
            elif date_max:
                data = Attendance.objects.filter(employee=person,created_at__lt=date_max)

        page = request.GET.get('page', 1)
        paginator = Paginator(data, 5)

        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)

        return render(request, 'core/index.html', {'datas': page_obj, 'todays_current_data': todays_current_data})


    


@login_required(login_url = 'login')
def user_logout(request):
    logout(request)

    # messages.success(request,'You are now logged out')
    return redirect('home')


# views.py
from .forms import StudentsForm

def create_student(request):
    if request.user.is_superuser: 
        if request.method == 'POST':
            form = StudentsForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('create_student')  # Redirect to a success page
        else:
            form = StudentsForm()

        return render(request, 'core/student_form.html', {'form': form})
    return redirect('/')

def student_list(request):
    students = Students.objects.all()
    return render(request, 'core/student_detail_view.html', {'students': students})


def update_student(request, pk):
    student = get_object_or_404(Students, pk=pk)

    if request.method == 'POST':
        form = StudentsForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # Redirect to the student list page
    else:
        form = StudentsForm(instance=student)

    return render(request, 'core/student_form.html', {'form': form, 'student': student})



def delete_student(request, pk):
    student = get_object_or_404(Students, pk=pk)

    student.delete()
    return redirect('student_list')  # Redirect to the student list page




def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = CourseForm()

    return render(request, 'core/create_course.html', {'form': form})

def create_mentor(request):
    if request.method == 'POST':
        mentor = request.POST.get('user')
        print(mentor)
        user = User.objects.filter(username = mentor).first()
        
        # print(user)
        if user: 

            mentors = Mentor.objects.filter(user = user).first()
            if mentors:
                messages.success(request,'mentor already created')
                return redirect('create_mentor')
            mentor = Mentor(user = user)
            mentor.save()
            messages.success(request,'mentor created')
            return redirect('create_mentor')

        else: 
            messages.success(request,'user not found')

            return redirect('create_mentor')
        
    

    return render(request, 'core/create_mentor.html',)


from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in after password change
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'core/change_password.html', {'form': form})








def chiya(request): 
    return render(request,'core/chiya.html')



import qrcode
from io import BytesIO
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Attendance

def generate_qr(request):
    """Generate QR dynamically with the current domain."""
    current_domain = request.get_host()  # Get the current domain dynamically
    qr_url = f"http://{current_domain}/scan/"  # Generate URL dynamically
    
    qr = qrcode.make(qr_url)

    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    buffer.seek(0)

    return HttpResponse(buffer.getvalue(), content_type="image/png")

@login_required(login_url='/login/?redirect=/scan')
def scan_qr(request):
    """Handle QR scan and mark attendance."""
    user = request.user
    current_date = timezone.localtime(timezone.now()).date()

    attended_today = Attendance.objects.filter(employee=user, entry__startswith=str(current_date))

    if attended_today.exists():
        attendance = attended_today.first()

        if attendance.leave:
            messages.warning(request, "Your exit has already been recorded today.")
        else:
            attendance.leave = timezone.localtime(timezone.now())
            attendance.save()
            messages.success(request, "Exit recorded successfully.")
    else:
        entry_time = timezone.localtime(timezone.now())
        Attendance.objects.create(employee=user, entry=entry_time)
        messages.success(request, "Entry recorded successfully.")

    return redirect('home')  # Redirect to homepage


