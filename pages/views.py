from django.views.generic import TemplateView


class HomePagesView(TemplateView):
    template_name = 'home.html'


class AboutPagesView(TemplateView):
    template_name = 'about.html'