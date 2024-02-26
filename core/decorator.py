from django.shortcuts import redirect,render

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            # If the user is authenticated, execute the original view function
            return view_func(request, *args, **kwargs)
        else:
            # If not authenticated, redirect to the login page
            return redirect('login')  
        
    return wrapper


@login_required
def restricted_page(request):
    return render(request, 'restricted_page.html')



