
import sys
import imp
import os

from flask import Flask


CONTEXT_CONST = (
    SETTINGS, CONFIG_PATH, CONFIG_PATH_ENV_NAME, FUNC_GET_BLUEPRINT,
) = (
    'settings', 'CONFIG_PATH', 'APPLICATION_CONFIG_PATH', 'get_blueprint',
)


CONFIG_KEYWORDS = (
    C_DEBUG, C_SECRET_KEY, C_ROUTES, C_MIDDLEWARES,
) = (
    'DEBUG', 'SECRET_KEY', 'ROUTES', 'MIDDLEWARES',
)


PROJECT_NAME = 'application'


def get_module(namespace, module_name):

    return __import__(
        name='%s.%s' % (namespace, module_name),
        fromlist=[namespace])


def get_attr_or_default(attr_name, module, default):

    return getattr(
        module, attr_name,
        getattr(default, attr_name))


def override_or_use_default(attr_name, module, default):

    ''' override attribute from 'module' to 'default'
        if source module has no attribute, then use default.
    '''

    setattr(
        default, attr_name,
        get_attr_or_default(attr_name, module, default))


def get_settings(flask_app):

    ''' import and override settings
        returns overrided settings which based on default.
    '''

    settings = get_module(PROJECT_NAME, SETTINGS)

    # get config path from arg '-c', then lookup env. var.
    config_path = flask_app.config.get(
        CONFIG_PATH, os.environ.get(CONFIG_PATH_ENV_NAME))

    # if 'config_path' is exists, then override settings
    if config_path:
        config = imp.load_source(SETTINGS, config_path)

        for key in CONFIG_KEYWORDS:
            # override dynamically
            override_or_use_default(key, config, settings)

    return settings


def initialize():

    ''' initialize flask application.

        it wraps some module to app context and returns app.
        when using uWSGI, you need to use 'initialize()' in callable
    '''

    # expose application instance
    app = Flask(import_name=PROJECT_NAME)

    # import and override settings
    # then set application configs
    settings = get_settings(app)
    for key in CONFIG_KEYWORDS:
        app.config[key] = getattr(settings, key)

    # TODO: initialize additional context
    # mongoengine.MongoEngine(app)

    # adapt middlewares
    for name, middleware in app.config[C_MIDDLEWARES].items():
        parsed_path = middleware.split('.')

        if len(parsed_path[:-1]) > 1:
            namespace = '.'.join(parsed_path[:-2])
            module_name = parsed_path[-2]

        else:
            namespace = parsed_path[-2]
            module_name = ''

        module = get_module(namespace, module_name)
        module_class = getattr(module, parsed_path[-1], None)
        setattr(sys.modules[__name__], name, module_class(app))

    # register blueprints
    for route in app.config[C_ROUTES]:
        module = get_module(PROJECT_NAME, route)
        blueprint = getattr(module, FUNC_GET_BLUEPRINT, None)
        app.register_blueprint(blueprint())

    return app, sys.modules[__name__]


# expose application context
app, sys.modules[__name__] = initialize()
