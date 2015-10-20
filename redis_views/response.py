import logging

from django.template.response import TemplateResponse
from django.template.base import Template
from django.conf import settings
from django.http import Http404

import redis

logger = logging.getLogger(__name__)


class RedisTemplateResponse(TemplateResponse):

    def __init__(self, *args, **kwargs):
        super(RedisTemplateResponse, self).__init__(*args, **kwargs)
        socket_timeout = 2
        if hasattr(settings, 'REDIS_CLIENT_SOCKET_TIMEOUT'):
            socket_timeout = settings.REDIS_CLIENT_SOCKET_TIMEOUT
        self.connection = redis.StrictRedis.from_url(settings.REDIS_URL,
                                                     socket_timeout=socket_timeout)

        # ping the server to make sure we have a valid connection. This will raise a
        # ConnectionError if the redis URL is invalid.
        self.connection.ping()

    def resolve_template(self, template):
        template = template[0]
        if template.endswith('current'):  # then it is a pointer
            template = self.connection.get(template)

        template_body = self.connection.get(template)
        if not template_body:
            # log an error message if the template key was not found in the DB
            msg = 'Reids Template: Could not find the template key {}'.format(template)
            logger.error(msg)

            raise Http404()

        return Template(template_body)
