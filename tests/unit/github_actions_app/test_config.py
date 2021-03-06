from unittest.mock import Mock, patch

import pytest

from github_actions_app.config import load


def test_load_no_env():
    obj_mock = Mock()
    with patch("github_actions_app.config.settings_loader") as settings_loader_mock:
        load(obj_mock, env=None)
        settings_loader_mock.assert_not_called()


@pytest.mark.parametrize("env", ["TESTING", "TeStInG", "testing"])
def test_load(env):
    obj_mock = Mock()
    with patch("github_actions_app.config.settings_loader") as settings_loader_mock:
        load(obj_mock, env=env)
        settings_loader_mock.assert_called_once_with(
            obj_mock, filename=f"{env.lower()}.yml"
        )
