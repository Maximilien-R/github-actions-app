from unittest.mock import Mock

import pytest

from github_actions_app.graphql.resolvers import resolve_query_hello


@pytest.mark.asyncio
async def test_resolve_query_hello():
    result = await resolve_query_hello(
        None, {"name": "Maximilien Raulic"}, {}, Mock()
    )
    assert result == "Hello Maximilien Raulic!"
