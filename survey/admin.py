from django.contrib import admin
from .models import Question, Answer


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    def possible_answers(self, obj):
        ans = ""
        for answer in Answer.objects.filter(parent=obj.pk):
            ans += " " + answer.text + ","
        return ans.strip(",")



    fieldsets = [
        (None, {'fields': ['prereq', 'text']}), ('Date information', {'fields': ['created'], 'classes': ['collapse']}),
    ]
    inlines = [AnswerInline]

    list_display = ['text', 'possible_answers', 'answers']


admin.site.register(Question, QuestionAdmin)
