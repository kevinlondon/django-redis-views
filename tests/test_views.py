from mock import patch, Mock
from redis_views.views import RedisView


class TestRedisView:

    def test_that_it_leaves_non_current_version_alone(self, rf):
        view = RedisView()
        view.request = rf.get('/', {'version': 'abc'})
        assert view.version == 'abc'

    def test_it_uses_default_version_if_version_param(self, rf):
        view = RedisView()
        view.request = rf.get('/')
        assert view.version == view.default_version

    def test_it_uses_template_name_of_app_name_and_version(self, rf):
        view = RedisView()
        view.app_name = 'foo'
        view.request = rf.get('/')
        assert view.template_name == '{}:{}'.format(view.app_name, view.version)
