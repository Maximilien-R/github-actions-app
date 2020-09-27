from unittest.mock import Mock, patch

from github_actions_app.server import run_app


def test_run_app():
    app_mock = Mock()

    with patch("github_actions_app.server.app.web.run_app") as run_app_mock:
        with patch(
            "github_actions_app.server.app.create_app", return_value=app_mock
        ) as create_app_mock:
            assert run_app() == 0
            create_app_mock.assert_called_once()
        run_app_mock.assert_called_once_with(
            app_mock, host="0.0.0.0", port=8090, handle_signals=True
        )
