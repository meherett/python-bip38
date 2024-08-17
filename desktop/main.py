#!/usr/bin/env python3

# Copyright © 2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

import re
import json
import inspect
from typing import (
    Optional, Union
)

from PySide6.QtGui import (
    QTextCharFormat, QTextCursor, QColor,
    QTextFormat, QTextOption
)

from bip38 import (
    cryptocurrencies, BIP38
)
from bip38.cryptocurrencies import ICryptocurrency
from bip38.wif import private_key_to_wif

from desktop.core import Application


class BIP38Application:
    """
    Main application class for managing the UI and core functionalities.
    """
    ERROR_COLOR: QColor = QColor(255, 96, 96)
    JSON_PATTERNS = [
        (re.compile(r'\".*?\"(?=\s*:)'), QColor(0, 191, 165)),  # keys
        (re.compile(r'\".*?\"'), QColor(0, 191, 165)),          # string values
        (re.compile(r'\b\d+\b'), QColor(125, 211, 252)),        # numbers
        (re.compile(r'\btrue\b|\bfalse\b|\bnull\b'), QColor(16, 182, 212)),  # booleans/null
        (re.compile(r'[{}[\],:]'), QColor(255, 255, 255))                    # punctuation
    ]

    def __init__(self) -> None:
        """
        Initialize the MainApplication class.
        """
        super().__init__()

        self.app: Application = Application.instance()
        self.ui = self.app.ui

        # bip38 cryptocurrencies {name: class} dict
        self.cryptocurrencies: dict = {
            name: cls for name, cls in inspect.getmembers(cryptocurrencies, inspect.isclass)
            if issubclass(cls, ICryptocurrency)
        }
        del self.cryptocurrencies["ICryptocurrency"] # Remove Interface class from the dict

        self.modes: dict = {
            "No EC-Multiply": self.ui.noECQWidget,
            "EC-Multiply": self.ui.ecQWidget,
        }

        self.wif_types = ["wif", "wif-compressed"]

        self.__init_ui()

    def __init_ui(self) -> None:
        """
        Initialize the UI components and their connections.
        """

        self.ui.outputQTextEdit.setWordWrapMode(QTextOption.NoWrap)

        ## populate and bindings
        self.ui.cryptocurrencyQComboBox.addItems(
            sorted(self.cryptocurrencies.keys(), key=str.casefold)
        )
        self.ui.cryptocurrencyQComboBox.currentTextChanged.connect(self.change_cryptocurrency)

        self.ui.modeQComboBox.addItems(
            self.modes.keys()
        )
        self.ui.modeQComboBox.currentTextChanged.connect(self.change_mode)

        self.ui.noECWIFTypeQComboBox.addItems(self.wif_types)
        self.ui.noECWIFTypeQComboBox.setCurrentIndex(0)

        # button bindings
        self.ui.noECPrivateKeyConvertQPushButton.clicked.connect(self.noec_convert_private_key)
        self.ui.noECEncryptQPushButton.clicked.connect(self.noec_encrypt)
        self.ui.decryptWIFQPushButton.clicked.connect(self.decrypt)
        ## setting defualt values

        # will update network combo too
        self.ui.cryptocurrencyQComboBox.setCurrentText("Bitcoin")
        self.ui.modeQComboBox.setCurrentIndex(0)

    def change_cryptocurrency(self, cryptocurrency: str) -> None:
        cryptocurrency_class: ICryptocurrency = self.cryptocurrencies[cryptocurrency]

        self.ui.networkQComboBox.clear()
        self.ui.networkQComboBox.addItems(
            [network.title() for network in cryptocurrency_class.NETWORKS.keys()]
        )
        self.ui.networkQComboBox.setCurrentIndex(0)

    def change_mode(self, mode: str) -> None:
        self.ui.modeQStackedWidget.setCurrentWidget(self.modes[mode])

    def noec_convert_private_key(self):
        private_key: str = self.ui.noECPrivateKeyQLineEdit.text().strip()
        wif_type: str = self.ui.noECWIFTypeQComboBox.currentText()
   
        try:
            wif: str = private_key_to_wif(
                private_key=private_key,
                cryptocurrency=self.get_cryptocurrency(),
                network=self.get_netowrk(),
                wif_type=wif_type
            )
            self.ui.noECWIFQLineEdit.setText(wif)
        except ValueError as e:
            self.logerr(f"Error: Invalid Private Key")

    def noec_encrypt(self):
        wif: str = self.ui.noECWIFQLineEdit.text().strip()
        passphrase: str = self.ui.passphraseQLineEdit.text().strip()

        bip38: BIP38 = BIP38(
            cryptocurrency=self.get_cryptocurrency(),
            network=self.get_netowrk()
        )

        try:
            encrypted_wif: str = bip38.encrypt(
                wif=wif,
                passphrase=passphrase
            )
            self.log(encrypted_wif)
        except ValueError as e:
            self.logerr(f"Error: Invalid WIF")

    def decrypt(self):
        encrypted_wif: str = self.ui.decryptWIFQLineEdit.text().strip()
        passphrase: str = self.ui.passphraseQLineEdit.text().strip()

        bip38: BIP38 = BIP38(
            cryptocurrency=self.get_cryptocurrency(),
            network=self.get_netowrk()
        )

        try:
            decrypted_wif: dict = bip38.decrypt(
                encrypted_wif=encrypted_wif,
                passphrase=passphrase,
                detail=True
            )
            self.log(decrypted_wif)
        except ValueError as e:
            self.logerr(f"Error: Invalid Encrypted WIF")

    def get_cryptocurrency(self):
        cryptocurrency_name: str = self.ui.cryptocurrencyQComboBox.currentText()
        cryptocurrency: ICryptocurrency = self.cryptocurrencies[cryptocurrency_name]
        return cryptocurrency

    def get_netowrk(self):
        return self.ui.networkQComboBox.currentText().lower()


    def log(self, data: Optional[Union[str, dict]], end="\n") -> None:
        if isinstance(data, dict):
            data = json.dumps(data, indent=4)

        cursor = self.ui.outputQTextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)

        # Apply highlighting
        for line in data.splitlines():
            pos = 0
            while pos < len(line):
                match_found = False
                for pattern, color in BIP38Application.JSON_PATTERNS:
                    match = pattern.match(line, pos)
                    if match:
                        cformat = QTextCharFormat()
                        cformat.setForeground(color)
                        cursor.insertText(match.group(), cformat)
                        pos = match.end()
                        match_found = True
                        break
                if not match_found:
                    cursor.insertText(line[pos])
                    pos += 1
            cursor.insertText(end)

        self.ui.outputQTextEdit.setTextCursor(cursor)
        self.ui.outputQTextEdit.ensureCursorVisible()

    def logerr(self, err: str , end: str="\n") -> None:
        cformat = QTextCharFormat()
        cformat.setForeground(BIP38Application.ERROR_COLOR)

        cursor = self.ui.outputQTextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(err + end, cformat)

        self.ui.outputQTextEdit.setTextCursor(cursor)
        self.ui.outputQTextEdit.ensureCursorVisible()