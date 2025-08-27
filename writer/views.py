from django.shortcuts import render, redirect
from django.contrib.auth.decorators  import login_required
from .forms import ArticleForm
from  django.http import HttpResponse
from .models import Article

# Create your views here.

@login_required(login_url="login")
def writer_dashboard(request):
    return render(request, 'writer/writer-dashboard.html')


@login_required(login_url="login")
def Create_article(request):
    form =  ArticleForm()
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article =  form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect("my-article")
        
    context = {"ArticleForm":form}
    
    return render(request, "writer/create-article.html", context)


@login_required(login_url="login")
def my_article(request):
    
    current_user = request.user.id
    article = Article.objects.all().filter(user=current_user)
    
    context = {"All_Article":article}
    
    return render(request, "writer/article.html", context)


@login_required(login_url="login")
def update_article(request, pk):
    try:
        article = Article.objects.get(id=pk, user = request.user)
    except:
        return redirect("my-article")
    
    form = ArticleForm(instance=article)
    
    if request.method == "POST":
        
        form =  ArticleForm(request.POST, instance=article)
        
        if form.is_valid():
            form.save()
            
            return redirect("my-article")
        
    context = {"UpdateArticle":form}
    
    return render(request, "writer/update-article.html")


@login_required(login_url="login")
def delete_article(request, pk):
    try:
        article = Article.objects.get(id=pk, user = request.user)
    except:
        return redirect("my-article")
    
    
    if request.method == "POST":
        article.delete()
        return redirect("my-article")
    
    return render(request, "writer/delete-article.html")