from waitress import serve

from meuprojeto.wsgi import application
# documentation: https://docs.pylonsproject.org/projects/waitress/en/stable/api.html

if __name__ == '__main__':
    serve(application, host = '10.11.1.128', port='80')