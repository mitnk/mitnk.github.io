    sudo apt-get install python-setuptools libxml2-dev build-essential python-dev
    sudo pip install uwsgi

uwsgi.ini example:

    [uwsgi]
    chdir=/home/mitnk/projects/foo
    module = django.core.handlers.wsgi:WSGIHandler()
    env = DJANGO_SETTINGS_MODULE=foo.settings
    master=True
    limit-as=256
    pidfile=/tmp/foo.pid
    vacuum=True
    max-requests=3000
    buffer-size=32768
    daemonize=/home/mitnk/uwsgi/foo.log
    socket=127.0.0.1:38717
    processes=2

这里注意  limit-as 不要太小了。我在一个内存为1G的机器上设了 64 结果 uwsgi 报错（但在另一个vps上设64则没事），调了半天才发现是这个参数的事。下面是报的错：

    spawned uWSGI worker 2 (pid: 22350, cores: 1)
    Traceback (most recent call last):
      File "/usr/lib/python2.6/dist-packages/django/core/handlers/wsgi.py", line 241, in __call__
        response = self.get_response(request)
      File "/usr/lib/python2.6/dist-packages/django/core/handlers/base.py", line 179, in get_response
        response = self.handle_uncaught_exception(request, resolver, sys.exc_info())
      File "/usr/lib/python2.6/dist-packages/django/core/handlers/base.py", line 224, in handle_uncaught_exception
        if resolver.urlconf_module is None:
      File "/usr/lib/python2.6/dist-packages/django/core/urlresolvers.py", line 323, in urlconf_module
        self._urlconf_module = import_module(self.urlconf_name)
      File "/usr/lib/python2.6/dist-packages/django/utils/importlib.py", line 35, in import_module
        __import__(name)
      File "./foo/urls.py", line 3, in <module>
        from django.contrib import admin
      File "/usr/lib/python2.6/dist-packages/django/contrib/admin/__init__.py", line 3, in <module>
        from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
      File "/usr/lib/python2.6/dist-packages/django/contrib/admin/helpers.py", line 2, in <module>
        from django.contrib.admin.util import (flatten_fieldsets, lookup_field,
      File "/usr/lib/python2.6/dist-packages/django/contrib/admin/util.py", line 1, in <module>
        from django.db import models
      File "/usr/lib/python2.6/dist-packages/django/db/__init__.py", line 40, in <module>
        backend = load_backend(connection.settings_dict['ENGINE'])
      File "/usr/lib/python2.6/dist-packages/django/db/__init__.py", line 34, in __getattr__
        return getattr(connections[DEFAULT_DB_ALIAS], item)
      File "/usr/lib/python2.6/dist-packages/django/db/utils.py", line 92, in __getitem__
        backend = load_backend(db['ENGINE'])
      File "/usr/lib/python2.6/dist-packages/django/db/utils.py", line 24, in load_backend
        return import_module('.base', backend_name)
      File "/usr/lib/python2.6/dist-packages/django/utils/importlib.py", line 35, in import_module
        __import__(name)
      File "/usr/lib/python2.6/dist-packages/django/db/backends/postgresql_psycopg2/base.py", line 8, in <module>
        from django.db import utils
    ImportError: cannot import name utils

开始以为是 psycopg2 的问题呢，到最后才发现是 uwsgi 内存设得太小了。

找到这个原因是因为在另一个log日志里有 `libk5crypto.so.3: failed to map segment from shared object: Cannot allocate memory` 的错误信息。以此为关键字找到了 [这篇文章](http://forum.lxcenter.org/index.php?t=msg&goto=94393)，其中的方案是增加内存分配量。虽然他们不是在uwsgi中遇到的问题，但我也试了同样的思路，问题才得以解决。折腾了近一天吧。

记录一点log吧：

    sudo apt-get install memcached python-memcache python-psycopg2
    wget http://nginx.org/download/nginx-1.1.9.tar.gz
    wget ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.30.tar.gz
    ./configure --with-pcre=/home/ocean/pcre-8.30/ --with-openssl=/usr/lib/ssl/
    wget http://zlib.net/zlib-1.2.6.tar.gz
    ./configure 
    make
    sudo make install

    wget http://initd.org/psycopg/tarballs/PSYCOPG-2-4/psycopg2-2.4.5.tar.gz
    tar xfz psycopg2-2.4.5.tar.gz 
    sudo apt-get install libpq-dev python-dev
    sudo pip install --upgrade psycopg2


另外两篇设置 nginx / uwsgi 不错的文章是：

[http://pig-monkey.com/2011/07/19/ubuntu-vps-django/](http://pig-monkey.com/2011/07/19/ubuntu-vps-django/)  
[http://senya.pl/2011/03/sexy-nginx-uwsgi-stack-for-django-with-virtualenv/](http://senya.pl/2011/03/sexy-nginx-uwsgi-stack-for-django-with-virtualenv/)