from django.views.generic import TemplateView

from core.models import BaseImageBuyer
from core.util import shuffle_queryset
from showroom.models import ShowroomImage


# Create your views here.
class ShowroomIndexView(TemplateView):
    template_name = "showroom.html"

    def get_context_data(self, **kwargs):
        context = super(ShowroomIndexView, self).get_context_data(**kwargs)
        context["showroom_images"] = shuffle_queryset(
            ShowroomImage.objects.filter(public=True)
        )

        return context

