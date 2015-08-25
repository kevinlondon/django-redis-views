from django.template.response import TemplateResponse
from django.template.base import Template
from django.conf import settings
from django.http import Http404

import redis


class RedisTemplateResponse(TemplateResponse):

    def __init__(self, *args, **kwargs):
        super(RedisTemplateResponse, self).__init__(*args, **kwargs)
        self.connection = redis.StrictRedis.from_url(settings.REDIS_URL)

    def resolve_template(self, template):
        template = template[0]
        if template.endswith('current'):  # then it is a pointer
            template = self.connection.get(template)

        template_body = self.connection.get(template)
        if not template_body:
            raise Http404()

        return Template(template_body)
