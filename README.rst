Requirements
============
CherryPy_

.. _CherryPy: http://www.cherrypy.org/

Installation
============

1. Put ``django_cpserver`` on your ``PYTHONPATH``.
2. Add ``django_cpserver`` to your ``INSTALLED_APPS``.

Usage
=====

Run ``./manage.py runcpserver help`` from within your project directory

Apache and mod_proxy
--------------------
By default runcpserver binds to localhost on port 8088. Another webserver can be used to expose your local CherryPy
instance by proxying requests to the local process. Remember, runcpserver won't serve your static files.


    ProxyPass /static/ !  
    <Location /django>
      ProxyPass http://localhost:8088
      ProxyPassRevese http://localhost:8088
    </Location>


Acknowledgements
================

Idea and code snippets borrowed from `Loic d'Anterroches`__, adapted to run as a management command

__ http://www.xhtml.net/scripts/Django-CherryPy-server-DjangoCerise
