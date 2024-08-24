#!/usr/bin/env python3

# Copyright © 2020-2024, Meheret Tesfaye Batu <meherett.batu@gmail.com>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import (
    Optional, Any
)


class Error(Exception):

    def __init__(
        self, message: str, detail: Optional[str] = None, expected: Any = None, got: Any = None
    ) -> None:
        self._message, self._detail, self._expected, self._got = (
            message, detail, None, f"'{got}'"
        )

        if isinstance(expected, list):
            for expect in expected:
                if self._expected is None:
                    self._expected = f"'{expect}'"
                else:
                    self._expected += f", '{expect}'"
        else:
            self._expected = expected

    def __str__(self):
        if self._expected and self._got and self._detail:
            return f"{self._message}, (expected: {self._expected} | got: {self._got}) {self._detail}"
        elif self._expected and self._got and not self._detail:
            return f"{self._message}, (expected: {self._expected} | got: {self._got})"
        elif self._detail:
            return f"{self._message} {self._detail}"
        else:
            return f"{self._message}"


class CryptocurrencyError(Error):
    pass


class NetworkError(Error):
    pass


class Secp256k1Error(Error):
    pass


class AddressError(Error):
    pass


class WIFError(Error):
    pass


class PassphraseError(Error):
    pass
