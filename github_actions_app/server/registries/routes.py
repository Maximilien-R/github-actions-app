from aiohttp import web

from github_actions_app.server.handlers import (
    handle_graphiql,
    handle_graphql,
    handle_health_live,
    handle_health_ready,
)

__all__ = ("register_routes",)


def register_routes(app: web.Application) -> None:
    """Register routes into the application.

    :param app: application to which register the routes
    :type app: web.Application
    """
    app.router.add_get("/graphql", handle_graphql)
    app.router.add_post("/graphql", handle_graphql)
    app.router.add_get("/graphiql", handle_graphiql)
    app.router.add_get("/health/live", handle_health_live)
    app.router.add_get("/health/ready", handle_health_ready)
