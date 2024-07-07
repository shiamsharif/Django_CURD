from django.views.generic import TemplateView, ListView, DetailView

from .models import Article
# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"