from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    
    path('addarticle/', views.addArticle, name="addarticle"),
    path('detail/<int:id>', views.detailArticle, name="detail"),
    path('update/<int:id>', views.updateArticle, name="update"),
    path('delete/<int:id>', views.deleteArticle, name="delete"),
    path('comment/<int:id>', views.addComment, name="comment"),

]
