from django.shortcuts import render
from .forms import PostForm

# Create your views here.
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('create_post')

        else:
            form = PostForm()
            return render(request, 'post/create_post.html', {'form': form})