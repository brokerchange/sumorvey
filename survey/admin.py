from django.contrib import admin
from .models import Question, Answer
from .forms import CustomQuestionAdminForm

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    def possible_answers(self, obj):
        ans = ""
        for answer in Answer.objects.filter(parent=obj.pk):
            ans += " " + answer.text + ","
        return ans.strip(",")

    form = CustomQuestionAdminForm

    fieldsets = [
        (None, {'fields': ['prereq', 'text']}), ('Date information', {'fields': ['created'], 'classes': ['collapse']}),
    ]
    inlines = [AnswerInline]

    list_display = ['text', 'possible_answers', 'answers']


admin.site.site_header = 'Su(mo)rvey Admin'
admin.site.site_title = 'Su(mo)rvey Admin'
admin.site.register(Question, QuestionAdmin)
