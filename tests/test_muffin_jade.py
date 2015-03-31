import muffin
import pytest


@pytest.fixture(scope='session')
def app(loop):
    app = muffin.Application(
        'jade', loop=loop,

        JADE_TEMPLATE_FOLDER='tests',
        PLUGINS=['muffin_jade'])

    @app.register('/')
    def index(request):
        return app.ps.jade.render('template.jade', **request.GET)

    return app


def test_muffin_jade(app, client):
    response = client.get('/', {'name': 'Jade'})
    assert '<h1>Hello Jade!</h1>' in response.text
