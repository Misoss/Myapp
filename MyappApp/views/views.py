from django.shortcuts import render
from django.views import View

class Home(View):
    #
    default_template = 'home.html'
    page = {
        "title": "Myapp Home Page"
    }
    #
    def get(self, request):
        #
        context = {
            "page": self.page
        }
        #
        return render(request, self.default_template, context)