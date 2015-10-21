import logging

from django.template.response import TemplateResponse
from django.template.base import Template
from django.conf import settings
from django.http import Http404

from  redis import StrictRedis


class RedisTemplateResponse(TemplateResponse):

    REDIS_CLIENT_SOCKET_TIMEOUT = 2

    def __init__(self, *args, **kwargs):
        super(RedisTemplateResponse, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(__name__)
        self.connection = StrictRedis.from_url(settings.REDIS_URL,
                                               self.socket_timeout)

        # Ping the server to make sure we have a valid connection.
        # This will raise a ConnectionError if the redis URL is invalid.
        self.connection.ping()

    @property
    def socket_timeout(self):
        try:
            return settings.REDIS_CLIENT_SOCKET_TIMEOUT
        except AttributeError:
            return self.REDIS_CLIENT_SOCKET_TIMEOUT

    def resolve_template(self, template):
        template = template[0]
        if template.endswith('current'):  # then it is a pointer
            template = self.connection.get(template)

        template_body = self.connection.get(template)
        if not template_body:
            error = 'Could not find template with key "{}"'.format(template)
            self.logger.error(error)
            raise Http404()

        return Template(template_body)
