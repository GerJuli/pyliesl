import pytest
from liesl.cli.lsl_api import get_target_for_lsl_api_cfg
from pathlib import Path


@pytest.mark.parametrize(
    "level, parent", [("system", "/etc"), ("user", "~"), ("local", ".")]
)
def test_get_target_for_lsl_api_cfg(level, parent):
    path = get_target_for_lsl_api_cfg(level)
    expected = str(Path(parent).expanduser().absolute())
    assert expected in str(path)
