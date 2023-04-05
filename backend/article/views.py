from django.shortcuts import render, redirect
from django.views import View

from .models import Article
from .forms import ArticleForm


class UploadImage(View):
    template_name = "article/uploadImage.html"

    def get(self, *args, **kwargs):

        form = ArticleForm()

        context = {
            "form": form
        }

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        form = ArticleForm(self.request.POST, self.request.FILES,)
        if form.is_valid():
            form.save()
            return redirect("/")

        context = {
            "form": ArticleForm()
        }

        return render(self.request, self.template_name, context)


def HomeView(request):
    return render(request, "article/home.html")
