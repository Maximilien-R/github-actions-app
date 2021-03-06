from unittest.mock import AsyncMock, Mock, patch

import aiomysql
import pytest

from github_actions_app.server.registries import register_database_pool


@pytest.mark.asyncio
async def test_register_database_pool():
    app_mock = {}

    pool_mock = Mock()
    pool_mock.close = Mock()
    pool_mock.wait_closed = AsyncMock()

    database_credentials_mock = {
        "host": "host",
        "port": 0,
        "user": "user",
        "password": "password",
        "database": "my_app",
    }

    with patch(
        "github_actions_app.server.registries.database.aiomysql.create_pool",
        new_callable=AsyncMock,
        return_value=pool_mock,
    ) as create_pool_mock:
        with patch(
            "github_actions_app.server.registries.database.extract_database_credentials",
            return_value=database_credentials_mock,
        ):
            async for _ in register_database_pool(app_mock):
                pass

        assert app_mock["database_pool"] is pool_mock
        create_pool_mock.assert_awaited_once_with(
            host=database_credentials_mock["host"],
            port=database_credentials_mock["port"],
            user=database_credentials_mock["user"],
            password=database_credentials_mock["password"],
            db=database_credentials_mock["database"],
            cursorclass=aiomysql.DictCursor,
        )
        pool_mock.close.assert_called_once()
        pool_mock.wait_closed.assert_awaited_once()
