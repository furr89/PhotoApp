from django.contrib import messages
from django.views.generic import TemplateView, DetailView, FormView

from .models import Post
from .forms import PostForm

# This creates a home page view (a page) which is accessed in ./urls.py which that is then accessed in mysite/urls
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id') # Going to get all posts from the post class. orders by id in reverse (newest first. note the '-' id)
        return context

# Creation of a view for detail.html
class PostDetailView(DetailView):
    template_name = 'detail.html'
    model = Post

class PostFormView(FormView):
    template_name = 'post.html'
    form_class = PostForm
    success_url = "/"

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):

        new_post = Post.objects.create(
            text = form.cleaned_data['text'],
            image = form.cleaned_data['image']
        )

        messages.add_message(self.request, messages.SUCCESS, "Post successfully sent")

        return super().form_valid(form)
