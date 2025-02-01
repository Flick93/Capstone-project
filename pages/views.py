from django.views.generic import TemplateView
from posts.models import Post, Status

class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            published_status = Status.objects.get(name="published")
            context['latest_posts'] = Post.objects.filter(
                status=published_status
            ).order_by('-created_on')[:3]
        except Status.DoesNotExist:
            context['latest_posts'] = []
        return context

class AboutPageView(TemplateView):
    template_name = "pages/about.html"