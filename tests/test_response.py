import pytest
from mock import Mock
from django.http import Http404
from redis_views.response import RedisTemplateResponse


class TestRedisTemplateResponse:

    @pytest.fixture
    def response(self):
        response = RedisTemplateResponse(request=None, template='')
        response.connection = Mock()
        return response

    def test_it_resolves_template_to_named_version(self, response):
        response.resolve_template(template=['foo'])
        response.connection.get.assert_called_with('foo')

    def test_it_raises_404_if_no_body(self, response):
        response.connection.get.return_value = None
        with pytest.raises(Http404):
            response.resolve_template([''])

    def test_it_checks_for_another_template_on_current_version(self, response):
        response.resolve_template(['app:current'])
        assert len(response.connection.get.mock_calls) == 2
