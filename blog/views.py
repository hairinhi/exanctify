from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from .forms import BlogForm

class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"
    paginate_by = 2

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = "blog"

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("index")
    template_name = "blog/blog_create_form.html"

    login_url = '/login'
    
    def form_valid(self,form):
        messages.success(self.request, "Saved.")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, "Failed.")
        return super().form_invalid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = "blog/blog_update_form.html"

    login_url = '/login'

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy("detail", kwargs={"pk":blog_pk})
        return url

    def form_valid(self,form):
        messages.success(self.request, "Updated.")
        return super().form_valid(form)
    
    def form_invalid(self,form):
        messages.error(self.request, "Failed.")
        return super().form_invalid(form)

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy("index")

    login_url = '/login'

    def delete(self, request, *args, **kwags):
        messages.success(self.request, "Deleted.")
        return super().delete(request)

