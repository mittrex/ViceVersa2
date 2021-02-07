from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = str(user_text)[::-1]
    words_count = len(user_text.split())
    return render(request, 'reverse.html', {'usertext':user_text, 'reversedtext':reversed_text, 'count':words_count})