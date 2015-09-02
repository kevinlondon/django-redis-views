=============================
django-redis-views
=============================

.. image:: https://badge.fury.io/py/django-redis-views.png
    :target: https://badge.fury.io/py/django-redis-views

.. image:: https://travis-ci.org/kevinlondon/django-redis-views.png?branch=master
    :target: https://travis-ci.org/kevinlondon/django-redis-views

Simple Redis-based generic views for serving your Django-backed Ember CLI apps.

Documentation
-------------

The full documentation is at https://django-redis-views.readthedocs.org.

Background
----------

Ember CLI and other single-page javascript apps can be challenging to deploy.

Luke Melia presented a talk called 
`Lightning Fast Deployment of Your Rails-backed JavaScript app <https://www.youtube.com/watch?v=QZVYP3cPcWQ>`_,
which eventually led to the creation of `ember-cli-deploy <https://github.com/ember-cli/ember-cli-deploy>`_.

This project acts as the glue between `ember-cli-deploy` and Django by
providing generic views to serve `Redis <http://redis.io/>`_-backed index pages for single
page javascript applications.


Quickstart
----------

Let's assume we already have an Ember CLI app that we're ready to deploy.
We're using the `ember-deploy-redis
<https://github.com/LevelbossMike/ember-deploy-redis>`_ adapter and we 
ran `ember deploy` to push the `index.html` file into Redis.
In this case, we'll pretend that the
Ember CLI project's name is `ember-cli-my-great-app`.

First, install django-redis-views::

    pip install django-redis-views

In your Django settings file, set the Redis url. For example, you may want
to access Redis on the localhost running on the default port. In which case,
you would add something like this to the your `settings.py` file::

    REDIS_URL = 'redis://localhost:6379/0'

Then, to use it in your Django project, first add a new view to a
`views.py` file::

    from redis_views import RedisView


    class EmberAppIndex(RedisView):
        app_name = 'ember-cli-my-great-app'

And then set it a route for it in your `urls.py` file::

    from django.conf.urls import patterns
    from myapp.views import EmberAppIndex


    urlpatterns = patterns('',
        url(r'^$', EmberIndexView.as_view()),
    )
    
At this point, you should be able to go to your root url and see your index
page!

TODO: Walk through a full example project.

Features
--------

* Serves your single page javascript apps easily through Django views.
* Works out-of-the-box with `ember-cli-deploy
  <https://github.com/ember-cli/ember-cli-deploy>`_ and 
  `ember-deploy-redis <https://github.com/LevelbossMike/ember-deploy-redis>`_.

Cookiecutter Tools Used in Making This Package
----------------------------------------------

*  cookiecutter
*  cookiecutter-djangopackage
