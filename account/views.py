from django.shortcuts import render
from django.views import View


class Authentication(View):
    template = 'authentication/auth.html'

    def get(self, request):
        context = {

        }
        return render(request, template_name=self.template, context=context)