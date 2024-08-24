from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Tag, Score


class ScoreInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        for form in self.forms:
            if 'is_main' in form.cleaned_data:
                if form.cleaned_data['is_main']:
                    count += 1
        if count != 1:
            raise ValidationError('Тут всегда ошибка, указан не один тег')
        return super().clean()


class ScoreInline(admin.TabularInline):
    model = Score
    extra = 3
    formset = ScoreInlineFormset

@admin.register(Tag)
class ObjectAdmin(admin.ModelAdmin):
    pass

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScoreInline]
