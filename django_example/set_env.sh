#!/usr/bin/env bash

# Set environment variables for django_example app
# Demostation only, should use other tool for managing Consul key/value store

CONSUL_HOST=http://localhost:8500
curl -X PUT -d 'True' $CONSUL_HOST/v1/kv/web00.django.test/debug
curl -X PUT -d 'django.db.backends.sqlite3' $CONSUL_HOST/v1/kv/web00.django.test/databases/default/engine
curl -X PUT -d 'db.envconsul.sqlite3' $CONSUL_HOST/v1/kv/web00.django.test/databases/default/name
curl -X PUT -d 'django.contrib.admin, env' $CONSUL_HOST/v1/kv/web00.django.test/installed_apps
curl -X PUT -d '.example.com, .example.com.' $CONSUL_HOST/v1/kv/web00.django.test/allowed_hosts
echo -e "\nDone setting variables"
