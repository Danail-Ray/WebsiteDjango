# your_app/context_processors.py

def is_user_authenticated(request):
    return {'user_authenticated': request.user.is_authenticated}
