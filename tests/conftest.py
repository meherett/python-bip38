#!/usr/bin/python3

from pathlib import Path

import pytest
import os


@pytest.fixture(scope="module")
def project_path():
    original_path = os.getcwd()
    os.chdir(original_path + "/tests")
    yield Path(original_path + "/tests")
    os.chdir(original_path)
