from aiohttp import web

from github_actions_app.server.registries import (
    register_database_pool,
    register_graphql_engine,
    register_routes,
)

__all__ = ("create_app",)


def create_app() -> web.Application:
    """Create and setup the application to run.

    :return: the application instance to run
    :rtype: web.Application
    """
    app = web.Application()
    app.on_startup.append(register_graphql_engine)
    app.cleanup_ctx.append(register_database_pool)
    register_routes(app)
    return app
