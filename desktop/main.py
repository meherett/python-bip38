#!/usr/bin/env python3

# Copyright © 2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

import re
import os
import json
import inspect
import functools
from typing import (
    Optional, Union
)

from PySide6.QtCore import QRegularExpression
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import (
    QTextCharFormat, QTextCursor, QColor,
    QTextFormat, QTextOption, QRegularExpressionValidator
)

from bip38 import (
    cryptocurrencies, BIP38
)
from bip38.exceptions import (
    Error, PassphraseError, WIFError
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
        (re.compile(r'\".*?\"(?=\s*:)'), QColor(101, 97, 156)),  # keys
        (re.compile(r'\".*?\"'), QColor(255, 255, 255)),         # string
        (re.compile(r'\b\d+\b'), QColor(125, 211, 252)),         # numbers
        (re.compile(r'\btrue\b|\bfalse\b|\bnull\b'), QColor(21, 128, 61)),  # boolean/null
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

        self.inputs = {
            "Passphrase": {
                "input": self.ui.passphraseQLineEdit,
                "optional": False, # cant be empty
                "min_length": 1
            },
            "Private Key": {
                "input": self.ui.noECPrivateKeyQLineEdit,
                "validator": self.regex_validator("^[0-9A-Fa-f]{1,64}$"), # hex only
                "optional": False,
                "min_length": 64
            },
            "WIF": {
                "input": self.ui.noECWIFQLineEdit,
                "validator": self.regex_validator("^[0-9A-Za-z]{1,52}$"), # alpha num only
                "optional": False,
                "min_length": 51
            },
            "Owner Salt": {
                "input": self.ui.ecOwnerSaltQLineEdit,
                "validator": self.regex_validator("^[0-9A-Fa-f]{1,16}$"), # hex only
                "optional": False,
                "min_length": 16
            },
            "Seed": {
                "input": self.ui.ecSeedQLineEdit,
                "validator": self.regex_validator("^[0-9A-Fa-f]{1,48}$"), # hex only
                "optional": False,
                "min_length": 48
            },
            "Lot": {
                "input": self.ui.ecLotQLineEdit,
                "optional": True,
                "min_length": 6
            },
            "Sequence": {
                "input": self.ui.ecSequenceQLineEdit,
                "optional": True,
                "min_length": 1
            },
            "Intermediate Passphrase": {
                "input": self.ui.ecIPassphraseQLineEdit,
                "validator": self.regex_validator("^passphrase[0-9A-Za-z]{1,62}$"), # alpha num only with passphrase prefix
                "optional": False,
                "min_length": 72
            },
            "Confirmation Code": {
                "input": self.ui.ecConfirmCodeQLineEdit,
                "validator": self.regex_validator("^cfrm[0-9A-Za-z]{1,71}$"), # alpha num only with passphrase cfrm
                "optional": False,
                "min_length": 75
            },
            "Encrypted WIF": {
                "input": self.ui.decryptWIFQLineEdit,
                "validator": self.regex_validator("^[0-9A-Za-z]{1,58}$"), # alpha num only
                "optional": False,
                "min_length": 58
            }
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

        self.ui.noECWIFTypeQComboBox.addItems(self.wif_types)
        self.ui.noECWIFTypeQComboBox.setCurrentIndex(0)

        self.ui.createEncryptedWIFTypeQComboBox.addItems(self.wif_types)
        self.ui.createEncryptedWIFTypeQComboBox.setCurrentIndex(0)

        # validation stuff

        for key, item in self.inputs.items():
            qt_input = item["input"]
            
            if "validator" in item:
                qt_input.setValidator(item["validator"])
            qt_input.textChanged.connect(functools.partial(self.validate_input, key))

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

    def change_cryptocurrency(self, cryptocurrency: str) -> None:
        cryptocurrency_class: ICryptocurrency = self.cryptocurrencies[cryptocurrency]

        self.ui.networkQComboBox.clear()
        self.ui.networkQComboBox.addItems(
            [network.title() for network in cryptocurrency_class.NETWORKS.keys()]
        )
        self.ui.networkQComboBox.setCurrentIndex(0)

    def change_mode(self, mode: str) -> None:
        is_on_ec = "EC-Multiply" == mode
        self.ui.decryptWIFTypeContainerQFrame.setVisible(is_on_ec)
        self.ui.createEncryptedWIFQPushButton.setVisible(is_on_ec)
        self.ui.modeQStackedWidget.setCurrentWidget(self.modes[mode])
        self.clean_all_required()

    def cryptocurrency(self):
        cryptocurrency_name: str = self.ui.cryptocurrencyQComboBox.currentText()
        cryptocurrency: ICryptocurrency = self.cryptocurrencies[cryptocurrency_name]
        return cryptocurrency

    def netowrk(self):
        return self.ui.networkQComboBox.currentText().lower()


    def bip38(self):
        return BIP38(
            cryptocurrency=self.cryptocurrency(),
            network=self.netowrk()
        )

    def noec_convert_private_key(self):   
        try:
            private_key, = self.validate_and_get("Private Key")
            
            wif: str = private_key_to_wif(
                private_key=private_key,
                cryptocurrency=self.cryptocurrency(),
                network=self.netowrk(),
                wif_type=self.ui.noECWIFTypeQComboBox.currentText()
            )
            self.ui.noECWIFQLineEdit.setText(wif)
        except (Error, BIP38Application.ValidationError) as e:
            self.logerr(e)

    def noec_encrypt(self):
        try:
            wif, passphrase = self.validate_and_get("WIF", "Passphrase")

            encrypted_wif: str = self.bip38().encrypt(
                wif=wif,
                passphrase=passphrase
            )
            self.ui.decryptWIFQLineEdit.setText(encrypted_wif)
            self.log(encrypted_wif)
        except WIFError as we:
            self.set_required(self.ui.noECWIFQLineEdit, True)
            self.logerr(we)
        except (Error, BIP38Application.ValidationError) as e:
            self.logerr(e)

    def ec_generate_ipassphrase(self):
        try:

            passphrase, owner_salt, lot, sequence = self.validate_and_get(
                "Passphrase", "Owner Salt", "Lot", "Sequence"
            )

            lot: Optional[int] = str_to_int(lot)
            sequence: Optional[int] = str_to_int(sequence)

            if (lot and sequence is None) or (lot is None and sequence):
                self.set_required(self.ui.ecLotQLineEdit, True)
                self.set_required(self.ui.ecSequenceQLineEdit, True)
                raise BIP38Application.ValidationError("'Lot' and 'Sequence' must both be set or both left blank.")

            intermediate_passphrase: str = self.bip38().intermediate_code(
                passphrase=passphrase,
                owner_salt=owner_salt,
                lot=lot,
                sequence=sequence
            )
            self.ui.ecIPassphraseQLineEdit.setText(intermediate_passphrase)
            self.log(intermediate_passphrase)
        except (Error, BIP38Application.ValidationError) as e:
            self.logerr(e)

    def ec_confirm_code(self):
        try:
            passphrase, confirmation_code = self.validate_and_get(
                "Passphrase", "Confirmation Code"
            )

            confirmation_code = self.bip38().confirm_code(
                    passphrase=passphrase,
                    confirmation_code=confirmation_code, 
                    detail=True
            )
            self.log(confirmation_code)

        except PassphraseError as pe:
            self.set_required(self.ui.passphraseQLineEdit, True)
            self.logerr(pe) 
        except Error as e:
            self.set_required(self.ui.ecConfirmCodeQLineEdit, True)
            self.logerr(e)
        except BIP38Application.ValidationError as ve:
            self.logerr(ve)

    def create_encrypted_wif(self):
        try:
            seed, intermediate_passphrase = self.validate_and_get(
                "Seed", "Intermediate Passphrase"
            )

            wif_type: str = self.ui.createEncryptedWIFTypeQComboBox.currentText()

            encrypted_wif: str = self.bip38().create_new_encrypted_wif(
                intermediate_passphrase=intermediate_passphrase,
                wif_type=wif_type,
                seed=seed,
            )
            self.ui.decryptWIFQLineEdit.setText(encrypted_wif["encrypted_wif"])
            self.log(encrypted_wif)

        except PassphraseError as pe:
            self.set_required(self.ui.ecIPassphraseQLineEdit, True)
            self.logerr(pe) 
        except (Error, BIP38Application.ValidationError) as e:
            self.logerr(e)

    def decrypt(self):
        try:
            encrypted_wif, passphrase = self.validate_and_get("Encrypted WIF", "Passphrase")
            decrypted_wif: dict = self.bip38().decrypt(
                encrypted_wif=encrypted_wif,
                passphrase=passphrase,
                detail=True
            )
            self.log(decrypted_wif)
        except WIFError as we:
            self.set_required(self.ui.decryptWIFQLineEdit, True)
            self.logerr(we)
        except PassphraseError as pe:
            self.set_required(self.ui.passphraseQLineEdit, True)
            self.logerr(pe) 
        except (Error, BIP38Application.ValidationError) as e:
            self.logerr(e)

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

        default_format = QTextCharFormat()
        default_format.setForeground(BIP38Application.TEXT_COLOR)  

        cursor = self.ui.outputQTextEdit.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText("ERROR", cformat)
        cursor.insertText(f": {err}{end}", default_format)

        self.ui.outputQTextEdit.setTextCursor(cursor)
        self.ui.outputQTextEdit.ensureCursorVisible()

    ## validation related functions 

    class ValidationError(Exception):
        def __init__(self, message):
            super().__init__(message)

    def validate_and_get(self, *args):
        self.clean_all_required() # forget old validations
        
        all_data = ()
        valid_inputs = 0

        for input_key in args:
            input_data = self.inputs[input_key]
            text = input_data["input"].text()

            all_data += (text,)
            valid_inputs += self.validate_input(input_key, text)

        if len(args) != valid_inputs:
            raise BIP38Application.ValidationError("Please Fill All Required Fields!")

        return all_data

    def validate_input(self, input_key, text):
        input_data = self.inputs[input_key]

        qt_input = input_data["input"]
        optional = input_data["optional"]
        min_length = input_data["min_length"]

        is_valid = len(text) >= min_length or (optional and len(text) == 0)
        self.set_required(qt_input, not is_valid)

        return is_valid

    def set_required(self, widget, value=True):
        widget.setProperty("required", value)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()

    def clean_all_required(self):
        for key, item in self.inputs.items():
            self.set_required(item["input"], False)

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

    def regex_validator(self, regex):
        return QRegularExpressionValidator(QRegularExpression(regex))
