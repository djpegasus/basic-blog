from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Yazar")
    title = models.CharField(max_length=50, verbose_name="Başlık")
    content = CKEditor5Field("İçerik", config_name="extends")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturma Tarihi")
    file = models.FileField(upload_to="", blank=True, null=True, verbose_name="Dosya Yükle")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ["-created_date"]
    
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name="Makale", related_name="comments")
    c_author = models.CharField(max_length=50, verbose_name="İsim")
    c_content = models.CharField(max_length=50, verbose_name="Yorum")
    c_date = models.DateTimeField(auto_now_add=True, verbose_name="Yorum Tarihi")
    
    def __str__(self):
        return self.c_content
    
    class Meta:
        ordering = ["-c_date"]
    
    