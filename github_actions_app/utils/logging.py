import logging.config

from github_actions_app.config import config

__all__ = ("configure_logging",)


def configure_logging() -> None:
    """Configure logging using a dictionary from config files."""
    logging.config.dictConfig(config["logging"])
