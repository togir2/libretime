from os import environ
from unittest import mock

from pytest import mark, raises

from libretime_shared.config import BaseConfig, Database


# pylint: disable=too-few-public-methods
class FixtureConfig(BaseConfig):
    api_key: str
    database: Database


FIXTURE_CONFIG_RAW = """
api_key: "f3bf04fc"

# Comment !
database:
    host: "localhost"
    port: 5672

ignored: "ignored"
"""


def test_base_config(tmpdir):
    config_filepath = tmpdir.join("config.yml")
    config_filepath.write(FIXTURE_CONFIG_RAW)

    with mock.patch.dict(
        environ,
        dict(
            LIBRETIME_API="invalid",
            LIBRETIME_API_KEY="f3bf04fc",
            LIBRETIME_DATABASE="invalid",
            LIBRETIME_DATABASE_PORT="8888",
            WRONGPREFIX_API_KEY="invalid",
        ),
    ):
        config = FixtureConfig(filepath=config_filepath)

        assert config.api_key == "f3bf04fc"
        assert config.database.host == "localhost"
        assert config.database.port == 8888


FIXTURE_CONFIG_RAW_MISSING = """
database:
    host: "localhost"
"""

FIXTURE_CONFIG_RAW_INVALID = """
database
    host: "localhost"
"""


@mark.parametrize(
    "raw,exception",
    [
        (FIXTURE_CONFIG_RAW_INVALID, SystemExit),
        (FIXTURE_CONFIG_RAW_MISSING, SystemExit),
    ],
)
def test_load_config_error(tmpdir, raw, exception):
    config_filepath = tmpdir.join("config.yml")
    config_filepath.write(raw)

    with raises(exception):
        with mock.patch.dict(environ, {}):
            FixtureConfig(filepath=config_filepath)