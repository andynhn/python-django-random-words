from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return render(request, 'random_word_app/index.html')


def randomize(request):
    print("*"*25, "RANDOMIZE METHOD", "*"*25)
    random_word = get_random_string(length=14)
    print(f"Random Word generated is: {random_word}")

    request.session['word'] = random_word
    print(f"Random word stored in session as: {request.session['word']}")

    if 'count' not in request.session:
        request.session['count'] = 1
        print(f"Count stored in session as: {request.session['count']}")
    else:
        request.session['count'] += 1
        print(f"Count incremented by 1. Count is now {request.session['count']}")
    print("*"*25, "END RANDOMIZE METHOD", "*"*25)
    return redirect("/")

def reset(request):
    print("*"*25, "RESET METHOD", "*"*25)
    request.session['count'] = 0
    print("Count has been reset to 0")
    print("Redirecting back to /random_word")
    print("*"*25, "END RANDOMIZE METHOD", "*"*25)
    return redirect('/random_word')