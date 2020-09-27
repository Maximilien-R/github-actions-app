from aiohttp import web
from tartiflette import Engine

__all__ = ("register_graphql_engine",)

_GRAPHQL_ENGINE: "Engine" = Engine(
    "github_actions_app/graphql/sdl/",
    modules=[
        "github_actions_app.graphql.directives",
        "github_actions_app.graphql.resolvers",
        "github_actions_app.graphql.scalars",
    ],
)


async def register_graphql_engine(app: web.Application) -> None:
    """Create a GraphQL engine and register it into the application.

    :param app: application to which register the GraphQL engine
    :type app: web.Application
    """
    await _GRAPHQL_ENGINE.cook()
    app["graphql_engine"] = _GRAPHQL_ENGINE
