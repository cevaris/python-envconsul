# Django Example using python-envconsul

Django projects can now reference Consul's key/value store in setting setting.py variables.

## Getting started
  
  
Need to install Consul. Installation guide found here [http://www.consul.io/intro/getting-started/install.html](http://www.consul.io/intro/getting-started/install.html)

```
# Mainly, install consul (Mac OS X) via brew
brew install caskroom/cask/brew-cask
brew cask install consul
```

Create a `/etc/consul.d` directory

```
sudo mkdir /etc/consul.d
```

Copy `django_example/consul_example/web00.django.test.json` to `/etc/consul.d/web00.django.test.json`

```
cat /etc/consul.d/web00.django.test.json
{
    "service":{
	"name": "web00.django.test",
	"tags": ["django"],
	"port": 8000
    }
}
```

Start up consul server. Here is the guide for starting consul [http://www.consul.io/intro/getting-started/agent.html](http://www.consul.io/intro/getting-started/agent.html)

```
consul agent -server -bootstrap-expect 1 -data-dir /tmp/consul -config-dir /etc/consul.d
```

Execute `django_example/consul_example/setup_env.sh` to load example settings.py variables into Consul

```
./django_example/consul_example/setup_env.sh
```

Setup django environment and run server

```
cd django_example
pip install -r requirements.txt
./manage.py runserver

```

Now navigate to [http://127.0.0.1:8000/env/](http://127.0.0.1:8000/env/) in your web browser or use this `curl` command to view Consul backed environment variables

```
echo $(curl http://127.0.0.1:8000/env/ | sed 's/<br\/>/\\n/g')
```
