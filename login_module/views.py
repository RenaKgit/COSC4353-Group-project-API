from django.contrib.auth import authenticate, login
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful'})
        else:
            return JsonResponse({'message': 'Invalid username or password'}, status=401)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return JsonResponse({'message': 'Username already exists'}, status=400)

        # Validate password strength
        try:
            validate_password(password)
        except ValidationError as e:
            return JsonResponse({'message': list(e.messages)}, status=400)

        # Create and save the user to the database
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        return JsonResponse({'message': 'Registration successful'})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
