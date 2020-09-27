import uvloop

from github_actions_app.utils import (
    configure_logging,
)

configure_logging()
uvloop.install()
