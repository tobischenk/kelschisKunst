from django.views.generic import TemplateView

from core.models import BaseImageBuyer
from showroom.models import ShowroomImage


# Create your views here.
class ShowroomIndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(ShowroomIndexView, self).get_context_data(**kwargs)
        showroom_images = ShowroomImage.objects.filter(public=True)
        print(showroom_images[1].image)
        print(BaseImageBuyer.objects.all())
        context["showroom_images"] = ShowroomImage.objects.filter(public=True)

        return context

