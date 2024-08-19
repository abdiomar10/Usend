from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, TaskForm
from .models import Profile, Task
from django.db import IntegrityError

def landing_page(request):
    return render(request, 'UsendApp/Landing_page.html')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            user_type = form.cleaned_data['user_type']

            try:
                profile, created = Profile.objects.get_or_create(user=user)
                profile.user_type = user_type
                profile.save()

                if profile.user_type == 'client':
                    return redirect('client_dashboard')
                elif profile.user_type == 'runner':
                    return redirect('runner_dashboard')

            except IntegrityError:
                messages.error(request, 'A profile with this user already exists.')
                return redirect('signup')
            except Exception as e:
                messages.error(request, f"An error occurred: {str(e)}")
                return redirect('signup')
        else:
            messages.error(request, 'Signup failed. Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'UsendApp/Signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            profile = Profile.objects.get(user=user)
            if profile.user_type == 'client':
                return redirect('client_dashboard')
            elif profile.user_type == 'runner':
                return redirect('runner_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'UsendApp/Login.html', {'form': form})

@login_required
def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('landing_page')

@login_required
def client_dashboard(request):
    tasks = Task.objects.filter(client=request.user)
    return render(request, 'UsendApp/Client_dashboard.html', {'tasks': tasks})

@login_required
def runner_dashboard(request):
    tasks_pending = Task.objects.filter(status='Pending')
    tasks_accepted = Task.objects.filter(runner=request.user, status='In Progress')
    tasks_completed = Task.objects.filter(runner=request.user, status='Completed')

    return render(request, 'UsendApp/Runner_dashboard.html', {
        'tasks_pending': tasks_pending,
        'tasks_accepted': tasks_accepted,
        'tasks_completed': tasks_completed,
    })

@login_required
def post_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.client = request.user
            task.save()
            return redirect('client_dashboard')
    else:
        form = TaskForm()
    return render(request, 'UsendApp/Post_task.html', {'form': form})

@login_required
def set_price(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        proposed_price = request.POST.get('proposed_price')
        task.proposed_price = proposed_price
        task.status = 'Pending Client Approval'
        task.runner = request.user
        task.save()
        return redirect('runner_dashboard')
    return render(request, 'UsendApp/Set_price.html', {'task': task})

@login_required
def accept_task(request, task_id, action):
    task = get_object_or_404(Task, id=task_id)

    if request.user == task.client:
        if action == 'accept':
            task.status = 'In Progress'
            messages.success(request, 'Task accepted. The runner has started the task.')
        elif action == 'decline':
            task.runner = None
            task.proposed_price = None
            task.status = 'Pending'
            messages.info(request, 'Task declined. Please provide new details or wait for a new proposal.')
        task.save()

    return redirect('client_dashboard')

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user == task.runner:
        task.status = 'Completed'
        task.save()
        messages.success(request, 'Errand completed successfully. Please request payment.')

    return redirect('runner_dashboard')

@login_required
def pay_runner(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.user == task.client:
        task.status = 'Paid'
        task.save()
        messages.success(request, 'Payment has been confirmed. Thank you!')

    return redirect('client_dashboard')



def terms_and_conditions(request):
    return render(request, 'UsendApp/Terms_and_conditions.html')

def privacy_policy(request):
    return render(request, 'UsendApp/Privacy_policy.html')

def about(request):
    return render(request, 'UsendApp/About.html')

def contact(request):
    return render(request, 'UsendApp/Contact.html')

def oauth_login(request):
    pass

def oauth_callback(request):
    pass

def password_reset(request):
    pass

def password_reset_done(request):
    pass

def password_reset_confirm(request, uidb64=None, token=None):
    pass

def password_reset_complete(request):
    pass

def csrf_failure(request, reason=""):
    return render(request, 'UsendApp/csrf_failure.html', {'reason': reason})
