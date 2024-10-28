#!/usr/bin/env python3

# Copyright © 2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import Optional

import json

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QStackedWidget,
    QFrame, QComboBox
)
from PySide6.QtCore import (
    Qt, QFileSystemWatcher, Signal, QSize
)
from PySide6.QtGui import (
    QFontDatabase, QIcon
)

from desktop.utils import (
    resolve_path, put_svg
)
from desktop.ui.ui_bip38 import Ui_MainWindow
from desktop.info import __version__ as desktop_ver
from bip38.info import __version__ as library_ver

class Application(QMainWindow):
    _instance: Optional['Application'] = None
    ui: Ui_MainWindow = None
    theme_watcher: QFileSystemWatcher = None
    resized: Signal = Signal(object)

    def __new__(cls, *args, **kwargs) -> 'Application':
        """
        Create a new instance if not already created, implementing the Singleton pattern.
        """
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        """
        Initialize the Application instance if not already initialized.
        """
        if not hasattr(self, 'initialized'):
            super().__init__()
            self.initialize()
            self.initialized = True

    @classmethod
    def instance(cls) -> 'Application':
        """
        Get the singleton instance of the Application.

        :return: The singleton instance of Application.
        """
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    def initialize(self) -> None:
        """
        Perform initialization tasks for the application, such as setting up the UI and loading resources.
        """
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.detached_window = None

        self.setWindowTitle("Bitcoin Improvement Proposal - 0038")
        self.bip38_icon = QIcon(resolve_path("desktop/ui/images/icon/icon.ico"))
        self.setWindowIcon(self.bip38_icon)
        
        put_svg(
            self.ui.bip38LogoHLayout,
            resolve_path("desktop/ui/images/svg/full-logo.svg"),
            84,
            44
        )
        self.ui.bip38LogoHLayout.setContentsMargins(0, 0, 5, 0)

        css_path = resolve_path("desktop/ui/css/theme.css")
        self.theme_watcher = QFileSystemWatcher([css_path])
        self.theme_watcher.fileChanged.connect(lambda: self.load_stylesheet(css_path))
        QFontDatabase.addApplicationFont(resolve_path("desktop/ui/font/HDWallet.ttf"))
        self.load_stylesheet(css_path)

        info = {
            "library": library_ver,
            "desktop": desktop_ver
        }
        self.ui.outputQTextEdit.setPlaceholderText(json.dumps(info, indent=4))

    def load_stylesheet(self, path: str) -> None:
        """
        Load and apply a stylesheet from the specified path.

        :param path: The path to the stylesheet file.
        """
        try:
            with open(path, 'r', encoding='utf-8') as style_file:
                stylesheet = style_file.read()
                self.setStyleSheet(stylesheet)
        except Exception as e:
            print(f"Failed to load stylesheet: {e}")

    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        self.resized.emit(event)