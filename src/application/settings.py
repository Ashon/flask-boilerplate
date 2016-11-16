
# Application debug handler
DEBUG = True


# CSRF Secret token
SECRET_KEY = 'KeepThisS3cr3t'


# If You want to add middlewares,
# middleware class must have 'init_app(...)' method.
# And add to this list as a string which looks following this...
# 'some.middleware.package.MiddlewareClass'
# we use as 'from some.middleware.package import MiddleWareClass'
MIDDLEWARES = {
    # 'login_manager': 'flask.ext.login.LoginManager',
    # 'csrf': 'flask_wtf.csrf.CsrfProtect',
    # 'mailbox': 'flask_mail.Mail',
}


# ROUTES is a list of module name which has function named 'get_blueprint()'
# returns 'flask.Blueprint'.
ROUTES = [
    'hello_view',
]
