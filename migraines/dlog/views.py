from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from .models import user_login, migraines_log
from django.urls import reverse

from .forms import Create_migraines_log

# Create your views here.

#1
def new_user_view(request):
    if request.method == 'POST': 
        form = forms.CreateUser(request.POST, request.FILES) 
        if form.is_valid():
            newpost = form.save(commit=False) 
            newpost.author = request.user 
            newpost.save()
    else:
        form = forms.CreateUser()
    return render(request, 'dlog/new_user.html', { 'form': form })


#2
# Function to handle user login
def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)

        
        if form.is_valid():
            user_email = form.cleaned_data['user_email']
            user_password = form.cleaned_data['user_password']

                    
            # Check if user_email exists in user_login table
            try:
                user = user_login.objects.get(user_email=user_email)
                # Check if password matches
                if user.user_password == user_password:  # You should use hashed password comparison in production
                    print("Login successful ====")
                    # Simulate login by storing user info in session
                    request.session['user_email'] = user_email
                    #
                    #
                    print("Login successful ====redirect migraines_log")
                    #return redirect(reverse("migraines_log"))      # NOT-WORK.   best option. need to check
                    return redirect('../migraines_log')  #   WORKES- OK/Good option.
                    #return redirect("http://127.0.0.1:8000/dlog/migraines_log/")  # WORKED - total hardcoded. avoid
                else:
                    print("password wromg")
                    messages.error(request, "Invalid password.")
            except user_login.DoesNotExist:
                print("email wromg")
                messages.error(request, "Invalid email.")
    else:
        form = forms.LoginForm()
    
    return render(request, 'dlog/user_login.html', {'form': form})



##3
""" 
def migraines_log_view(request):
    context = {}

    # Get the user's email from the session
    user_email = request.session.get('user_email')

    if user_email:
        # Filter the migraines_log based on the logged-in user's email
        user = user_login.objects.get(user_email=user_email)
        user_migraines_log = migraines_log.objects.filter(user_email=user).order_by('log_date')

        context['all_migraines_log'] = user_migraines_log
        context['title'] = 'Migraines Log'
    else:
        # If no user email in session (user not logged in), show an error or redirect
        messages.error(request, "You need to be logged in to view the migraines log.")
        return redirect('dlog:login_view')

    return render(request, 'dlog/migraines_log.html', context)
 """



def migraines_log_view(request):
    context = {}

    # Get the user's email from the session
    user_email = request.session.get('user_email')

    if user_email:
        # Get the user object based on the email in the session
        user = user_login.objects.get(user_email=user_email)

        # Fetch the user's migraines log entries
        user_migraines_log = migraines_log.objects.filter(user_email=user).order_by('log_date')

        # Add the user's migraine logs to the context
        context['all_migraines_log'] = user_migraines_log
        context['title'] = 'Migraines Log'

        # Handle form submission for adding a new log
        if request.method == 'POST':
            form = Create_migraines_log(request.POST)
            if form.is_valid():
                # Save the new migraines log entry with the current user's email
                new_log = form.save(commit=False)
                new_log.user_email = user  # Set the current user as the owner of the log
                new_log.save()  # Save the new log entry

                # Display success message
                messages.success(request, "migraine log added!")
                return redirect('dlog:migraines_log')  # Redirect to the migraines log page after saving

        else:
            # Display the form for adding a new migraines log
            form = Create_migraines_log()

        context['form'] = form
    else:
        # If no user email in session (user not logged in), show an error or redirect
        messages.error(request, "You need to be logged in to view the migraines log.")
        return redirect('dlog:login_view')

    return render(request, 'dlog/migraines_log.html', context)
