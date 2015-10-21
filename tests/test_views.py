import pytest
from django.test import RequestFactory
from redis_views.views import RedisView


class TestRedisView:

    def test_that_it_leaves_non_current_index_value_alone(self, rf):
        view = RedisView()
        view.request = rf.get('/', {'index_key': 'abc'})
        assert view.index_key == 'abc'

    def test_it_uses_default_index_key_if_index_key_missing(self, rf):
        view = RedisView()
        view.request = rf.get('/')
        assert view.index_key == 'current'

    def test_it_uses_template_name_of_app_name_and_index_key(self, rf):
        view = RedisView()
        view.app_name = 'foo'
        view.request = rf.get('/')
        assert view.template_name == '{}:{}'.format(view.app_name, view.index_key)
