OPAC SSM
========

Static Storage Management for OPAC website

.. image:: https://travis-ci.org/scieloorg/opac_ssm.svg?branch=master
    :target: https://travis-ci.org/scieloorg/opac_ssm

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

.. image:: https://landscape.io/github/scieloorg/opac_ssm/master/landscape.svg?style=flat
   :target: https://landscape.io/github/scieloorg/opac_ssm/master
   :alt: Code Health

.. image:: https://pyup.io/repos/github/scieloorg/opac_ssm/shield.svg
     :target: https://pyup.io/repos/github/scieloorg/opac_ssm/
     :alt: Updates

.. image:: https://pyup.io/repos/github/scieloorg/opac_ssm/python-3-shield.svg
     :target: https://pyup.io/repos/github/scieloorg/opac_ssm/
     :alt: Python 3
     
.. image:: https://images.microbadger.com/badges/image/scieloorg/opac_ssm.svg
     :target: https://microbadger.com/images/scieloorg/opac_ssm
     :alt: Get your own image badge on microbadger.com

.. image:: https://images.microbadger.com/badges/version/scieloorg/opac_ssm.svg
     :target: https://microbadger.com/images/scieloorg/opac_ssm
     :alt: Get your own version badge on microbadger.com

.. image:: https://images.microbadger.com/badges/commit/scieloorg/opac_ssm.svg
     :target: https://microbadger.com/images/scieloorg/opac_ssm
     :alt: Get your own commit badge on microbadger.com

:License: BSD


Configuração: Variáveis de ambiente:
====================================

Docker:
-------

* ``USE_DOCKER`` - se o ambiente é feito com docker, definir como: 'yes'

Database:
---------

* ``POSTGRES_USER`` - usuário postgres (requerido)
* ``POSTGRES_PASSWORD`` - senha do usuário postgres (requerido)


Django:
-------

* ``DJANGO_SETTINGS_MODULE``- caminho do modulo de settings. (default: 'config.settings.production')
* ``DJANGO_DEBUG`` - habilita/deshabilita modo debug da webapp (default: False)
* ``DJANGO_ACCOUNT_ALLOW_REGISTRATION`` - habilita/deshabilita cadastro de usuários (default: True)
* ``DJANGO_ADMIN_URL`` - URL do admin (default: quando acessar /admin gera erro)
* ``DJANGO_SECRET_KEY`` - segredo para segurança (default: gera erro)
* ``DJANGO_ALLOWED_HOSTS`` - host permitidos (default: '*' (aceita tudo, deveria ser somente o host do ssm somente))
* ``FILE_UPLOAD_MAX_MEMORY_SIZE`` - espaço em memoria máximo (em bytes) utilizada n upload de arquivos (default: 2621440 equivale a: 2.5MB)
* ``DJANGO_SECURE_SSL_REDIRECT`` -

Django (email):
---------------

* ``DJANGO_DEFAULT_FROM_EMAIL`` - email padrão no from (default: 'OPAC SSM <noreply@example.com>')
* ``DJANGO_EMAIL_SUBJECT_PREFIX`` - email padrão no from (default: '[OPAC SSM] ')
* ``DJANGO_EMAIL_HOST`` - host do servidor de envio de emails (default: 'mailhog')
* ``DJANGO_EMAIL_PORT`` - porta do servidor de envio de emails (default: 1025)
* ``DJANGO_EMAIL_HOST_USER`` - usuário do servidor de envio de email (default: '')
* ``DJANGO_EMAIL_HOST_PASSWORD`` - senha do usuário do servidor de envio de email (default: '')
* ``DJANGO_EMAIL_USE_TLS`` - True/False dependendo se o servidor de envio de email usa TLS na autenticação (default: False)
* ``DJANGO_EMAIL_USE_SSL`` - True/False dependendo se o servidor de envio de email usa SSL na autenticação (default: False)


Sentry:
-------

* ``DJANGO_SENTRY_DSN`` - DSN do Sentry (default: não reporta nada, obter o DSN de: https://homolog.sentry.scielo.org/sentry/homologopacssmscieloorg/settings/keys/)
* ``DJANGO_SENTRY_LOG_LEVEL`` - (integer) nivel de log do Sentry (default: logging.INFO)  - Mais info: https://docs.python.org/2/library/logging.html#logging-levels


Redis:
------

* ``REDIS_URL`` - URL de conexão para o servidor Redis (default: "redis://127.0.0.1:6379", no entrypoint.sh definido como: "redis://redis:6379")


Haystack:
---------

* ``HAYSTACK_CONNECTIONS_HOST`` - host do servidor de indice (ElasticSearch) (default: '127.0.0.1')
* ``HAYSTACK_CONNECTIONS_PORT`` - porta do servidor de indice (ElasticSearch) (default: '9200')
* ``HAYSTACK_CONNECTIONS_INDEX`` - nome do indice no servidor de indice (ElasticSearch) (default: 'opac_ssm_idx')


Servidor GRPC:
--------------

* ``GRCP_HOST`` - host do servidor gRPC (default: '[::]')
* ``GRCP_PORT`` - porta do servidor gRPC (default: 5000)
* ``GRCP_MAX_WORKERS`` - porta do servidor de indice (ElasticSearch) (default: 4)


GRPC Server
===========

Command to generate GRPC class:

.. code-block:: python

    python -m grpc_tools.protoc -I grpc_ssm --python_out=grpc_ssm --grpc_python_out=grpc_ssm grpc_ssm/opac.proto


