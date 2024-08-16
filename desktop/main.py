#!/usr/bin/env python3

# Copyright © 2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from desktop.core import Application


class BIP38Application:
    """
    Main application class for managing the UI and core functionalities.
    """
    def __init__(self) -> None:
        """
        Initialize the MainApplication class.
        """
        super().__init__()

        self.app = Application.instance()
        self.ui = self.app.ui

        self.__init_ui()

    def __init_ui(self) -> None:
        """
        Initialize the UI components and their connections.
        """
        pass