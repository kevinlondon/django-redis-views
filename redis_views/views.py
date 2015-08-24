from django.views.generic import TemplateView
from .response import RedisTemplateResponse


class RedisView(TemplateView):

    response_class = RedisTemplateResponse
    content_type = 'text/html'
    default_version = 'current'
    app_name = ''

    @property
    def template_name(self):
        return '{}:{}'.format(self.app_name, self.version)

    @property
    def version(self):
        return self.request.GET.get('version', default=self.default_version)
