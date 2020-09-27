from unittest.mock import Mock, patch

from github_actions_app.server.factory import create_app
from github_actions_app.server.registries import register_graphql_engine


def test_create_app():
    app_mock = Mock()
    app_mock.on_startup = []

    with patch("github_actions_app.server.factory.web.Application", return_value=app_mock):
        with patch("github_actions_app.server.factory.register_routes") as register_routes_mock:
            assert create_app() == app_mock
            register_routes_mock.assert_called_once_with(app_mock)
            assert register_graphql_engine in app_mock.on_startup
