from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = 'landing/index.html'
    
class ProfileView(TemplateView):
    template_name = 'landing/profile.html'
