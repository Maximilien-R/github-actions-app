from unittest.mock import Mock

from github_actions_app.server.handlers import (
    handle_graphiql,
    handle_graphql,
    handle_health_live,
    handle_health_ready,
)
from github_actions_app.server.registries import register_routes


def test_register_routes():
    app_mock = Mock()

    register_routes(app_mock)

    assert app_mock.router.add_get.call_count == 4
    assert app_mock.router.add_post.call_count == 1
    assert app_mock.router.add_get.any_call("/graphql", handle_graphql)
    assert app_mock.router.add_post.any_call("/graphql", handle_graphql)
    assert app_mock.router.add_get.any_call("/graphiql", handle_graphiql)
    assert app_mock.router.add_get.any_call("/health/live", handle_health_live)
    assert app_mock.router.add_get.any_call(
        "/health/ready", handle_health_ready
    )
