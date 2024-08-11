#!/usr/bin/env python3

# Copyright © 2023-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from pathlib import Path

import json
import pytest
import os


@pytest.fixture(scope="module")
def project_path():
    original_path = os.getcwd()
    os.chdir(original_path + "/tests")
    yield Path(original_path + "/tests")
    os.chdir(original_path)


@pytest.fixture(
    scope="session", name="_"
)
def test_data():
    base_path: str = os.path.dirname(__file__)
    file_path: str = os.path.abspath(os.path.join(base_path, "data/values.json"))
    values = open(file_path, "r", encoding="utf-8")
    return json.loads(values.read())
