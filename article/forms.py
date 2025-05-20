from django.forms import ModelForm
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "file"]
        widgets = {
              "content": CKEditor5Widget(
                  attrs={"class": "django_ckeditor_5"}, config_name="extends"
              )
          }