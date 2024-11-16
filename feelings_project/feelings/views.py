from django.shortcuts import render, redirect, get_object_or_404
from .models import Feeling, Comment

def index(request):
    if request.method == 'POST':
        if 'feeling' in request.POST:
            feeling_text = request.POST.get('feeling')
            if feeling_text:
                Feeling.objects.create(text=feeling_text)
                return redirect('index')
        elif 'comment' in request.POST:
            comment_text = request.POST.get('comment')
            feeling_id = request.POST.get('feeling_id')
            if comment_text and feeling_id:
                feeling = get_object_or_404(Feeling, id=feeling_id)
                Comment.objects.create(feeling=feeling, text=comment_text)
                return redirect('index')

    feelings = Feeling.objects.order_by('-timestamp')  # Most recent first
    return render(request, 'index.html', {'feelings': feelings})
