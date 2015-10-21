.. :changelog:

History
-------

0.2.1 (2015-10-20)

* Added a socket timeout and server pinging when connecting to the server to raise a
  ConnectionError if there are any connection issues.

* Added error logging of missing template keys.

0.2.0 (2015-09-21)

* Changed the GET parameter value from `version` to `index_key` to match
  the convention established by ember-cli-deploy.

0.1.0 (2015-08-22)
++++++++++++++++++

* First release on PyPI.
