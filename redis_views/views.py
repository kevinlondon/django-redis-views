from django.views.generic import TemplateView
from .response import RedisTemplateResponse


class RedisView(TemplateView):

    response_class = RedisTemplateResponse
    content_type = 'text/html'
    app_name = ''

    @property
    def template_name(self):
        return '{}:{}'.format(self.app_name, self.index_key)

    @property
    def index_key(self):
        """The index_key property is the hash associated with the commit.

        By specifying an index_key value as a GET parameter, you can
        request a different revision than the one that is currently
        set as active. This allows you to preview versions before they
        are live for all users or to compare the current version to one
        had been previously deployed.

        For example, you could request a URL this way::

            /my-app?index_key=abcdefg1234

        It will then request `<app_name>:abcdefg1234` instead of the
        default, which would be `<app_name>:current`.
        """
        return self.request.GET.get('index_key', default='current')
