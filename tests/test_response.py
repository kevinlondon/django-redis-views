import pytest
import mock
import redis
import logging

from django.http import Http404
from redis_views.response import RedisTemplateResponse


class TestRedisTemplateResponse:

    @pytest.fixture
    @mock.patch.object(logging, 'getLogger')
    @mock.patch.object(redis.StrictRedis, 'from_url')
    def response(self, connection_init, get_logger):
        connection_init.return_value = mock.Mock()
        get_logger.return_value = mock.Mock()

        response = RedisTemplateResponse(request=None, template='')

        return response

    def test_it_resolves_template_to_named_version(self, response):
        response.resolve_template(template=['foo'])
        response.connection.get.assert_called_with('foo')

    def test_it_logs_error_and_raises_404_if_no_body(self, response):
        response.connection.get.return_value = None
        with pytest.raises(Http404):
            response.resolve_template([''])

        assert response.logger.error.called

    def test_it_checks_for_another_template_on_current_version(self, response):
        response.resolve_template(['app:current'])
        assert len(response.connection.get.mock_calls) == 2

    def test_it_sets_connection_on_init(self, response):
        assert not hasattr(RedisTemplateResponse, 'connection')
        assert response.connection

    def test_it_pings_connection_on_init(self, response):
        assert response.connection.ping.called

    @mock.patch.object(redis.StrictRedis, 'from_url')
    def test_it_sets_socket_timeout(self, connection_init, settings):
        settings.REDIS_URL = 'foo'
        settings.REDIS_CLIENT_SOCKET_TIMEOUT = 5

        RedisTemplateResponse(request=None, template='')
        connection_init.assert_called_with(
            settings.REDIS_URL,
            socket_timeout=settings.REDIS_CLIENT_SOCKET_TIMEOUT
        )
