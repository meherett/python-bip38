#!/usr/bin/env python3

# Copyright © 2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

import re
import os
import json
import inspect
from typing import (
    Optional, Union
)

from PySide6.QtWidgets import QWidget
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


str_to_int = lambda s: int(s) if s.isdigit() else None

class BIP38Application:
    """
    Main application class for managing the UI and core functionalities.
    """
    TEXT_COLOR: QColor = QColor(255, 255, 255)
    ERROR_COLOR: QColor = QColor(255, 96, 96)
    JSON_PATTERNS = [
        # (re.compile(r'\".*?\"(?=\s*:)'), QColor(0, 191, 165)),  # keys
        (re.compile(r'\".*?\"'), QColor(0, 191, 165)),          # string
        (re.compile(r'\b\d+\b'), QColor(125, 211, 252)),        # numbers
        (re.compile(r'\btrue\b|\bfalse\b|\bnull\b'), QColor(16, 182, 212)),  # boolean/null
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

        self.wif_types = {
            "wif": "uncompressed", 
            "wif-compressed": "compressed"
        }

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

        self.ui.noECWIFTypeQComboBox.addItems(self.wif_types.keys())
        self.ui.noECWIFTypeQComboBox.setCurrentIndex(0)


        self.ui.ecLotQLineEdit.textEdited.connect(
            lambda: self.validate_int(self.ui.ecLotQLineEdit)
        )
        self.ui.ecLotQLineEdit.editingFinished.connect(
            lambda: self.enforce_int_range(self.ui.ecLotQLineEdit, 100000, 999999)
        )

        self.ui.ecSequenceQLineEdit.textEdited.connect(
            lambda: self.validate_int(self.ui.ecSequenceQLineEdit)
        )
        self.ui.ecSequenceQLineEdit.editingFinished.connect(
            lambda: self.enforce_int_range(self.ui.ecSequenceQLineEdit, 0, 4095)
        )
        self.ui.createEncryptedWIFTypeQComboBox.addItems(self.wif_types.keys())
        self.ui.createEncryptedWIFTypeQComboBox.setCurrentIndex(0)

        # button bindings
        self.ui.noECPrivateKeyConvertQPushButton.clicked.connect(self.noec_convert_private_key)
        self.ui.noECEncryptQPushButton.clicked.connect(self.noec_encrypt)

        self.ui.ecOwnerSaltGenerateQPushButton.clicked.connect(
            lambda: self.ui.ecOwnerSaltQLineEdit.setText(
                os.urandom(8).hex()
            )
        )
        self.ui.ecSeedGenerateQPushButton.clicked.connect(
            lambda: self.ui.ecSeedQLineEdit.setText(
                os.urandom(24).hex()
            )
        )

        self.ui.ecIPassphraseGenerateQPushButton.clicked.connect(self.ec_generate_ipassphrase)
        self.ui.ecConfirmCodeVerifyQPushButton.clicked.connect(self.ec_confirm_code)
        self.ui.createEncryptedWIFQPushButton.clicked.connect(self.create_encrypted_wif)

        self.ui.decryptWIFQPushButton.clicked.connect(self.decrypt)

        ## setting default values

        # will update network combo too
        self.ui.cryptocurrencyQComboBox.setCurrentText("Bitcoin")
        self.ui.modeQComboBox.setCurrentIndex(0)

    def validate_int(self, line_edit):
        text = line_edit.text()
        if not text.isdigit():
            line_edit.setText(''.join(filter(str.isdigit, text)))

    def enforce_int_range(self, line_edit, min_value, max_value):
        text = line_edit.text()
        validator = line_edit.validator()

        if text.isdigit():
            value = int(text)
            value = max(min_value, min(value, max_value)) # clamp
            line_edit.setText(str(value))

    def change_cryptocurrency(self, cryptocurrency: str) -> None:
        cryptocurrency_class: ICryptocurrency = self.cryptocurrencies[cryptocurrency]

        self.ui.networkQComboBox.clear()
        self.ui.networkQComboBox.addItems(
            [network.title() for network in cryptocurrency_class.NETWORKS.keys()]
        )
        self.ui.networkQComboBox.setCurrentIndex(0)

    def change_mode(self, mode: str) -> None:
        is_on_ec = "EC-Multiply" == mode
        self.ui.createEncryptedWIFTypeQComboBox.setVisible(is_on_ec)
        self.ui.createEncryptedWIFQPushButton.setVisible(is_on_ec)
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
            self.set_required(self.ui.noECPrivateKeyQLineEdit)
            self.logerr(f"Error: {e}")

    def noec_encrypt(self):
        wif: str = self.ui.noECWIFQLineEdit.text().strip()

        # validate=True will show error if passphrase is not set
        if not (passphrase := self.get_passphrase(validate=True)):
            return None

        bip38: BIP38 = BIP38(
            cryptocurrency=self.get_cryptocurrency(),
            network=self.get_netowrk()
        )

        try:
            encrypted_wif: str = bip38.encrypt(
                wif=wif,
                passphrase=passphrase
            )
            self.ui.decryptWIFQLineEdit.setText(encrypted_wif)
            self.log(encrypted_wif)
        except ValueError as e:
            self.set_required(self.ui.noECWIFQLineEdit)
            self.logerr(f"Error: {e}")

    def ec_generate_ipassphrase(self):
        if not (passphrase := self.get_passphrase(validate=True)):
            return None

        owner_salt: str = self.ui.ecOwnerSaltQLineEdit.text().strip()
        lot: Optional[int] = str_to_int(self.ui.ecLotQLineEdit.text())
        sequence: Optional[int] = str_to_int(self.ui.ecSequenceQLineEdit.text())

        bip38: BIP38 = BIP38(
            cryptocurrency=self.get_cryptocurrency(),
            network=self.get_netowrk()
        )

        try:
            intermediate_passphrase: str = bip38.intermediate_code(
                passphrase=passphrase,
                owner_salt=owner_salt,
                lot=lot,
                sequence=sequence
            )
            self.ui.ecIPassphraseQLineEdit.setText(intermediate_passphrase)
            self.log(intermediate_passphrase)
        except ValueError as e:
            self.logerr(f"Error: {e}")

    def ec_confirm_code(self):
        if not (passphrase := self.get_passphrase(validate=True)):
            return None

        confirmation_code: str = self.ui.ecConfirmCodeQLineEdit.text().strip()
        encrypted_wif: str = self.ui.decryptWIFQLineEdit.text().strip()

        bip38: BIP38 = BIP38(
            cryptocurrency=self.get_cryptocurrency(),
            network=self.get_netowrk()
        )

        try:
            confirmation_code=bip38.confirm_code(
                    passphrase=passphrase,
                    confirmation_code=confirmation_code, 
                    detail=True
            )
            self.log(confirmation_code)
        except ValueError as e:
            self.logerr(f"Error: {e}")


    def create_encrypted_wif(self):
        intermediate_passphrase: str = self.ui.ecIPassphraseQLineEdit.text().strip()
        seed: str = self.ui.ecSeedQLineEdit.text().strip()
        wif_type: str = self.ui.createEncryptedWIFTypeQComboBox.currentText()
        wif_type = self.wif_types[wif_type]

        bip38: BIP38 = BIP38(
            cryptocurrency=self.get_cryptocurrency(),
            network=self.get_netowrk()
        )

        try:
            encrypted_wif: str = bip38.create_new_encrypted_wif(
                intermediate_passphrase=intermediate_passphrase,
                public_key_type=wif_type,
                seed=seed,
            )
            self.ui.decryptWIFQLineEdit.setText(encrypted_wif["encrypted_wif"])
            self.log(encrypted_wif)
        except ValueError as e:
            self.logerr(f"Error: {e}")

    def decrypt(self):
        encrypted_wif: str = self.ui.decryptWIFQLineEdit.text().strip()

        if not (passphrase := self.get_passphrase(validate=True)):
            return None

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
            self.set_required(self.ui.decryptWIFQLineEdit)
            self.logerr(f"Error: {e}")

    def get_cryptocurrency(self):
        cryptocurrency_name: str = self.ui.cryptocurrencyQComboBox.currentText()
        cryptocurrency: ICryptocurrency = self.cryptocurrencies[cryptocurrency_name]
        return cryptocurrency

    def get_netowrk(self):
        return self.ui.networkQComboBox.currentText().lower()

    def get_passphrase(self, validate):
        passphrase: str = self.ui.passphraseQLineEdit.text().strip()
        if validate and not passphrase:
            self.set_required(self.ui.passphraseQLineEdit)
            self.logerr("Error: Passphrase Required")

        return passphrase

    def log(self, data: Optional[Union[str, dict]], end="\n") -> None:
        if isinstance(data, dict):
            data = json.dumps(data, indent=4)

        cursor = self.ui.outputQTextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)

        default_format = QTextCharFormat()
        default_format.setForeground(BIP38Application.TEXT_COLOR)  

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
                    cursor.insertText(line[pos], default_format)
                    pos += 1
            cursor.insertText(end, default_format)

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

    def set_required(self, widget, value=True):
        widget.setProperty("required", value)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()