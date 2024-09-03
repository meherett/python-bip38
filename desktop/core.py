#!/usr/bin/env python3

# Copyright © 2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

from typing import Optional

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QStackedWidget,
    QFrame, QComboBox
)
from PySide6.QtCore import (
    Qt, QFileSystemWatcher
)
from PySide6.QtGui import (
    QFontDatabase
)

from desktop.utils import resolve_path
from desktop.ui.ui_bip38 import Ui_MainWindow


class Application(QMainWindow):
    _instance: Optional['Application'] = None
    ui: Ui_MainWindow = None
    theme_watcher: QFileSystemWatcher = None

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

        self.setWindowTitle("BIP38")
        css_path = resolve_path("desktop/ui/css/theme.css")
        self.theme_watcher = QFileSystemWatcher([css_path])
        self.theme_watcher.fileChanged.connect(lambda: self.load_stylesheet(css_path))
        QFontDatabase.addApplicationFont(resolve_path("desktop/ui/font/HD Wallet-Regular.ttf"))
        self.load_stylesheet(css_path)

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