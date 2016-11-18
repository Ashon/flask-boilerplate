# My Flask Boilerplate

## File Structure

``` bash
$ tree src
src/
├── application # project directory
│   ├── hello_view # application like django
│   │   ├── __init__.py
│   │   └── views.py
│   ├── __init__.py
│   └── settings.py
└── manage.py
```


## Develop with boilerplate

### `manage.py`
``` bash
$ cd src
$ ./manage.py

usage: manage.py [-?] {shell,runserver} ...

positional arguments:
  {shell,runserver}
    shell            Runs a Python shell inside Flask application context.
    runserver        Start server with development mode

optional arguments:
  -?, --help         show this help message and exit

```

### run server in dev env
```
$ ./manage.py runserver
```


## Adding a new route(module)

### create new module
``` python
# file: application/awesome_view/__init__.py

from flask import Blueprint
from application.awesome_view.views import AwesomeView


def get_blueprint():
    ''' get_blueprint() should returns flask.Blueprint
    '''

    # Register the urls
    blueprint = Blueprint('awesome_view', __name__)
    blueprint.add_url_rule('/awesome', view_func=AwesomeView.as_view('awesome_view'))

    return blueprint
```

### add module to `ROUTES`

``` python
# file: application/settings.py

...

ROUTES = [
    'awesome_view' # add module name
]
```
