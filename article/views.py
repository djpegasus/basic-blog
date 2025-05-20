from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from .forms import ArticleForm
from .models import Article, Comment

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def articles(request):
    article = Article.objects.all()
    keyword = request.GET.get("keyword")
    if keyword:
        article=Article.objects.filter(title__contains = keyword)
        return render(request, "articles.html", {"article":article})
    return render(request, "articles.html", {"article":article})

@login_required(login_url="users:login")
def addArticle(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Makale Kaydedildi.")
        return redirect ("user:dashboard")
    return render(request, "addarticle.html", {"form":form})

@login_required(login_url="users:login")
def updateArticle(request,id):
    article = get_object_or_404(Article, id=id, author=request.user)
    form = ArticleForm(request.POST or None , request.FILES or None, instance=article)
    if form.is_valid():
        form.save()
        messages.success(request, "Makale Güncellendi.")
        return redirect ("user:dashboard")
    return render(request, "update.html", {"form":form})

@login_required(login_url="users:login")
def deleteArticle(request,id):
    article = Article.objects.filter(id=id).delete()
    messages.success(request, "Makale Başarıyla Silindi.")
    return redirect ("user:dashboard")

def detailArticle(request,id):
    article = get_object_or_404(Article, id=id)
    comment = article.comments.all()
    return render(request, "detail.html", {"article":article, "comment":comment}) 

def addComment(request,id):
    article = get_object_or_404(Article, id=id)
    if request.method=="POST":
        c_author = request.POST.get("c_author")
        c_content = request.POST.get("c_content")
        newComment = Comment(c_author=c_author, c_content=c_content)
        newComment.article = article
        newComment.save()
        return redirect(reverse("article:detail", args=[id]))