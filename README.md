# EnvConsul

Python environment variable wrapper around Consul key/value storage. When instantiated, `EnvConsol` fetches the key value data for a defined service from Consul. These environment variables are retrievable via the path they were stored in Consul. 

For example if we insert a database name for specific services in Consul

```shell
curl -X -d 'db.sqlite3' \
	http://localhost:8500/v1/kv/web00.django.test/databases/default/name
```
EnvConsul can fetch and be queried like so

```python
ENV_CONSUL = envconsul.EnvConsul('web00.django.test')
DATABASE_NAME = ENV_CONSUL.get_str('/databases/default/engine')
```

## Features

- Retrieve Consul key/value environment variables service
- Typed retrieval of environment variables
- EnvConsol object implements a simple ReadOnly/Immutable dict
- Implemented using supported Python's Consul `consulate`
  - [https://github.com/gmr/consulate](https://github.com/gmr/consulate])


## Install

```
pip install python-envconsul
```

## Example Usage

### Initialization

```python
import envconsul
# where service name is 'web00.django.test'
ENV_CONSUL = envconsul.EnvConsul('web00.django.test')

# Or if using remote Consul instance
ENV_CONSUL = envconsul.EnvConsul(
    host='my.consul.host.com',
    port=8500,
    service_name='web00.django.test')
```

### Retrieval of Environment Variables

```
# Taking from django settings file

# http://localhost:8500/v1/kv/web00.django.test/debug = "True"
# Retrun bool type
DEBUG = ENV_CONSUL.get_bool('/debug', True)
...

# http://localhost:8500/v1/kv/web00.django.test/allowed_hosts = "example.com, example.com."
# Return list type
ALLOWED_HOSTS = []
ALLOWED_HOSTS += ENV_CONSUL.get_list('/allowed_hosts', [])
...

# http://localhost:8500/v1/kv/web00.django.test/installed_apps = "django.contrib.admin, env"
# Return tuple type
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
INSTALLED_APPS += ENV_CONSUL.get_tuple('/installed_apps', ['django.contrib.admin',])
...

# http://localhost:8500/v1/kv/web00.django.test/databases/default/engine = "django.db.backends.sqlite3"
# http://localhost:8500/v1/kv/web00.django.test/databases/default/name = "db.sqlite3"
# Dictionary example, where Consul key/value path  '/databases/default/engine'
# maps to the following nested dictionary
DATABASES = {
    'default': {
        'ENGINE': ENV_CONSUL.get_str('/databases/default/engine'),
        'NAME': os.path.join(BASE_DIR, ENV_CONSUL.get_str('/databases/default/name', 'db.sqlite3')),
    }
}
...

# Simple no-default, no type retrieval; not recommend
REDIS_HOST = ENV_CONSUL.get('/redis_host')
```


## For Development

Git clone project

`git clone https://github.com/cevaris/python-envconsul.git`

Build and install project

`pip install -r requirements-dev.txt`

Run tests

`py.test tests/`
