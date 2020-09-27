from unittest.mock import patch

from github_actions_app.utils import configure_logging, logging


def test_configure_logging():
    config_mock = {"conf1": "value1"}
    with patch.object(logging, "config", new={"logging": config_mock}):
        with patch(
            "github_actions_app.utils.logging.logging.config.dictConfig"
        ) as dict_config_mock:
            configure_logging()
            dict_config_mock.assert_called_once_with(config_mock)
