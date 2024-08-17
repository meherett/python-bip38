# -*- coding: utf-8 -*-

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)

from .resources_rc import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(705, 455)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centeralWidgetLayout = QVBoxLayout(self.centralwidget)
        self.centeralWidgetLayout.setSpacing(0)
        self.centeralWidgetLayout.setObjectName(u"centeralWidgetLayout")
        self.centeralWidgetLayout.setContentsMargins(10, 10, 10, 10)
        self.bip38ContainerQFrame = QFrame(self.centralwidget)
        self.bip38ContainerQFrame.setObjectName(u"bip38ContainerQFrame")
        self.bip38ContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.bip38ContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.bip38ContainerQFrame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.cryptoAndNetworkContainerQFrame = QFrame(self.bip38ContainerQFrame)
        self.cryptoAndNetworkContainerQFrame.setObjectName(u"cryptoAndNetworkContainerQFrame")
        self.cryptoAndNetworkContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cryptoAndNetworkContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.cryptoAndNetworkContainerQFrame)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cryptocurrencyContainerQFrame = QFrame(self.cryptoAndNetworkContainerQFrame)
        self.cryptocurrencyContainerQFrame.setObjectName(u"cryptocurrencyContainerQFrame")
        self.cryptocurrencyContainerQFrame.setMaximumSize(QSize(150, 16777215))
        self.cryptocurrencyContainerQFrameVLayout = QVBoxLayout(self.cryptocurrencyContainerQFrame)
        self.cryptocurrencyContainerQFrameVLayout.setSpacing(5)
        self.cryptocurrencyContainerQFrameVLayout.setObjectName(u"cryptocurrencyContainerQFrameVLayout")
        self.cryptocurrencyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.cryptocurrencyLabelContainerQFrame = QFrame(self.cryptocurrencyContainerQFrame)
        self.cryptocurrencyLabelContainerQFrame.setObjectName(u"cryptocurrencyLabelContainerQFrame")
        self.cryptocurrencyLabelContainerQFrameHLayout = QHBoxLayout(self.cryptocurrencyLabelContainerQFrame)
        self.cryptocurrencyLabelContainerQFrameHLayout.setSpacing(15)
        self.cryptocurrencyLabelContainerQFrameHLayout.setObjectName(u"cryptocurrencyLabelContainerQFrameHLayout")
        self.cryptocurrencyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.cryptocurrencyQLabel = QLabel(self.cryptocurrencyLabelContainerQFrame)
        self.cryptocurrencyQLabel.setObjectName(u"cryptocurrencyQLabel")

        self.cryptocurrencyLabelContainerQFrameHLayout.addWidget(self.cryptocurrencyQLabel)

        self.cryptocurrencyLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.cryptocurrencyLabelContainerQFrameHLayout.addItem(self.cryptocurrencyLabelContainerQFrameHSpacer)


        self.cryptocurrencyContainerQFrameVLayout.addWidget(self.cryptocurrencyLabelContainerQFrame)

        self.cryptocurrencyQComboBox = QComboBox(self.cryptocurrencyContainerQFrame)
        self.cryptocurrencyQComboBox.setObjectName(u"cryptocurrencyQComboBox")

        self.cryptocurrencyContainerQFrameVLayout.addWidget(self.cryptocurrencyQComboBox)


        self.horizontalLayout.addWidget(self.cryptocurrencyContainerQFrame)

        self.networkContainerQFrame = QFrame(self.cryptoAndNetworkContainerQFrame)
        self.networkContainerQFrame.setObjectName(u"networkContainerQFrame")
        self.networkContainerQFrame.setMaximumSize(QSize(115, 16777215))
        self.networkContainerQFrameVLayout = QVBoxLayout(self.networkContainerQFrame)
        self.networkContainerQFrameVLayout.setSpacing(5)
        self.networkContainerQFrameVLayout.setObjectName(u"networkContainerQFrameVLayout")
        self.networkContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.networkLabelContainerQFrame = QFrame(self.networkContainerQFrame)
        self.networkLabelContainerQFrame.setObjectName(u"networkLabelContainerQFrame")
        self.networkLabelContainerQFrameHLayout = QHBoxLayout(self.networkLabelContainerQFrame)
        self.networkLabelContainerQFrameHLayout.setSpacing(15)
        self.networkLabelContainerQFrameHLayout.setObjectName(u"networkLabelContainerQFrameHLayout")
        self.networkLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.networkQLabel = QLabel(self.networkLabelContainerQFrame)
        self.networkQLabel.setObjectName(u"networkQLabel")

        self.networkLabelContainerQFrameHLayout.addWidget(self.networkQLabel)

        self.networkLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.networkLabelContainerQFrameHLayout.addItem(self.networkLabelContainerQFrameHSpacer)


        self.networkContainerQFrameVLayout.addWidget(self.networkLabelContainerQFrame)

        self.networkQComboBox = QComboBox(self.networkContainerQFrame)
        self.networkQComboBox.setObjectName(u"networkQComboBox")

        self.networkContainerQFrameVLayout.addWidget(self.networkQComboBox)


        self.horizontalLayout.addWidget(self.networkContainerQFrame)

        self.passphraseContainerQFrame = QFrame(self.cryptoAndNetworkContainerQFrame)
        self.passphraseContainerQFrame.setObjectName(u"passphraseContainerQFrame")
        self.passphraseContainerQFrameVLayout = QVBoxLayout(self.passphraseContainerQFrame)
        self.passphraseContainerQFrameVLayout.setSpacing(5)
        self.passphraseContainerQFrameVLayout.setObjectName(u"passphraseContainerQFrameVLayout")
        self.passphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.passphraseLabelContainerQFrame = QFrame(self.passphraseContainerQFrame)
        self.passphraseLabelContainerQFrame.setObjectName(u"passphraseLabelContainerQFrame")
        self.passphraseLabelContainerQFrameHLayout = QHBoxLayout(self.passphraseLabelContainerQFrame)
        self.passphraseLabelContainerQFrameHLayout.setSpacing(15)
        self.passphraseLabelContainerQFrameHLayout.setObjectName(u"passphraseLabelContainerQFrameHLayout")
        self.passphraseLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.passphraseQLabel = QLabel(self.passphraseLabelContainerQFrame)
        self.passphraseQLabel.setObjectName(u"passphraseQLabel")

        self.passphraseLabelContainerQFrameHLayout.addWidget(self.passphraseQLabel)

        self.passphraseLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.passphraseLabelContainerQFrameHLayout.addItem(self.passphraseLabelContainerQFrameHSpacer)


        self.passphraseContainerQFrameVLayout.addWidget(self.passphraseLabelContainerQFrame)

        self.passphraseQLineEdit = QLineEdit(self.passphraseContainerQFrame)
        self.passphraseQLineEdit.setObjectName(u"passphraseQLineEdit")

        self.passphraseContainerQFrameVLayout.addWidget(self.passphraseQLineEdit)


        self.horizontalLayout.addWidget(self.passphraseContainerQFrame)

        self.modeContainerQFrame = QFrame(self.cryptoAndNetworkContainerQFrame)
        self.modeContainerQFrame.setObjectName(u"modeContainerQFrame")
        self.modeContainerQFrame.setMaximumSize(QSize(145, 16777215))
        self.modeContainerQFrameVLayout = QVBoxLayout(self.modeContainerQFrame)
        self.modeContainerQFrameVLayout.setSpacing(5)
        self.modeContainerQFrameVLayout.setObjectName(u"modeContainerQFrameVLayout")
        self.modeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.modeLabelContainerQFrame = QFrame(self.modeContainerQFrame)
        self.modeLabelContainerQFrame.setObjectName(u"modeLabelContainerQFrame")
        self.modeLabelContainerQFrameHLayout = QHBoxLayout(self.modeLabelContainerQFrame)
        self.modeLabelContainerQFrameHLayout.setSpacing(15)
        self.modeLabelContainerQFrameHLayout.setObjectName(u"modeLabelContainerQFrameHLayout")
        self.modeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.modeQLabel = QLabel(self.modeLabelContainerQFrame)
        self.modeQLabel.setObjectName(u"modeQLabel")

        self.modeLabelContainerQFrameHLayout.addWidget(self.modeQLabel)

        self.modeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.modeLabelContainerQFrameHLayout.addItem(self.modeLabelContainerQFrameHSpacer)


        self.modeContainerQFrameVLayout.addWidget(self.modeLabelContainerQFrame)

        self.modeQComboBox = QComboBox(self.modeContainerQFrame)
        self.modeQComboBox.setObjectName(u"modeQComboBox")

        self.modeContainerQFrameVLayout.addWidget(self.modeQComboBox)


        self.horizontalLayout.addWidget(self.modeContainerQFrame)


        self.verticalLayout.addWidget(self.cryptoAndNetworkContainerQFrame)

        self.modeQStackedWidget = QStackedWidget(self.bip38ContainerQFrame)
        self.modeQStackedWidget.setObjectName(u"modeQStackedWidget")
        self.noECQWidget = QWidget()
        self.noECQWidget.setObjectName(u"noECQWidget")
        self.noECVLayout = QVBoxLayout(self.noECQWidget)
        self.noECVLayout.setSpacing(10)
        self.noECVLayout.setObjectName(u"noECVLayout")
        self.noECVLayout.setContentsMargins(0, 0, 0, 0)
        self.noECPrivateKeyAndWifTypeContainerQFrame = QFrame(self.noECQWidget)
        self.noECPrivateKeyAndWifTypeContainerQFrame.setObjectName(u"noECPrivateKeyAndWifTypeContainerQFrame")
        self.noECPrivateKeyAndWifTypeContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.noECPrivateKeyAndWifTypeContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.noECPrivateKeyAndWifTypeContainerHLayout_2 = QHBoxLayout(self.noECPrivateKeyAndWifTypeContainerQFrame)
        self.noECPrivateKeyAndWifTypeContainerHLayout_2.setSpacing(15)
        self.noECPrivateKeyAndWifTypeContainerHLayout_2.setObjectName(u"noECPrivateKeyAndWifTypeContainerHLayout_2")
        self.noECPrivateKeyAndWifTypeContainerHLayout_2.setContentsMargins(0, 0, 0, 0)
        self.noECPrivateKeyContainerQFrame = QFrame(self.noECPrivateKeyAndWifTypeContainerQFrame)
        self.noECPrivateKeyContainerQFrame.setObjectName(u"noECPrivateKeyContainerQFrame")
        self.noECPrivateKeyContainerQFrameVLayout = QVBoxLayout(self.noECPrivateKeyContainerQFrame)
        self.noECPrivateKeyContainerQFrameVLayout.setSpacing(5)
        self.noECPrivateKeyContainerQFrameVLayout.setObjectName(u"noECPrivateKeyContainerQFrameVLayout")
        self.noECPrivateKeyContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.noECPrivateKeyLabelContainerQFrame = QFrame(self.noECPrivateKeyContainerQFrame)
        self.noECPrivateKeyLabelContainerQFrame.setObjectName(u"noECPrivateKeyLabelContainerQFrame")
        self.noECPrivateKeyLabelContainerQFrameHLayout = QHBoxLayout(self.noECPrivateKeyLabelContainerQFrame)
        self.noECPrivateKeyLabelContainerQFrameHLayout.setSpacing(15)
        self.noECPrivateKeyLabelContainerQFrameHLayout.setObjectName(u"noECPrivateKeyLabelContainerQFrameHLayout")
        self.noECPrivateKeyLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.noECPrivateKeyQLabel = QLabel(self.noECPrivateKeyLabelContainerQFrame)
        self.noECPrivateKeyQLabel.setObjectName(u"noECPrivateKeyQLabel")

        self.noECPrivateKeyLabelContainerQFrameHLayout.addWidget(self.noECPrivateKeyQLabel)

        self.noECPrivateKeyLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.noECPrivateKeyLabelContainerQFrameHLayout.addItem(self.noECPrivateKeyLabelContainerQFrameHSpacer)


        self.noECPrivateKeyContainerQFrameVLayout.addWidget(self.noECPrivateKeyLabelContainerQFrame)

        self.noECPrivateKeyQLineEdit = QLineEdit(self.noECPrivateKeyContainerQFrame)
        self.noECPrivateKeyQLineEdit.setObjectName(u"noECPrivateKeyQLineEdit")

        self.noECPrivateKeyContainerQFrameVLayout.addWidget(self.noECPrivateKeyQLineEdit)


        self.noECPrivateKeyAndWifTypeContainerHLayout_2.addWidget(self.noECPrivateKeyContainerQFrame)

        self.noECWIFTypeContainerQFrame = QFrame(self.noECPrivateKeyAndWifTypeContainerQFrame)
        self.noECWIFTypeContainerQFrame.setObjectName(u"noECWIFTypeContainerQFrame")
        self.noECWIFTypeContainerQFrame.setMaximumSize(QSize(145, 16777215))
        self.noECWIFTypeContainerQFrameVLayout = QVBoxLayout(self.noECWIFTypeContainerQFrame)
        self.noECWIFTypeContainerQFrameVLayout.setSpacing(5)
        self.noECWIFTypeContainerQFrameVLayout.setObjectName(u"noECWIFTypeContainerQFrameVLayout")
        self.noECWIFTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.noECWIFTypeLabelContainerQFrame = QFrame(self.noECWIFTypeContainerQFrame)
        self.noECWIFTypeLabelContainerQFrame.setObjectName(u"noECWIFTypeLabelContainerQFrame")
        self.noECWIFTypeLabelContainerQFrameHLayout = QHBoxLayout(self.noECWIFTypeLabelContainerQFrame)
        self.noECWIFTypeLabelContainerQFrameHLayout.setSpacing(15)
        self.noECWIFTypeLabelContainerQFrameHLayout.setObjectName(u"noECWIFTypeLabelContainerQFrameHLayout")
        self.noECWIFTypeLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.noECWIFTypeQLabel = QLabel(self.noECWIFTypeLabelContainerQFrame)
        self.noECWIFTypeQLabel.setObjectName(u"noECWIFTypeQLabel")

        self.noECWIFTypeLabelContainerQFrameHLayout.addWidget(self.noECWIFTypeQLabel)

        self.noECWIFTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.noECWIFTypeLabelContainerQFrameHLayout.addItem(self.noECWIFTypeLabelContainerQFrameHSpacer)


        self.noECWIFTypeContainerQFrameVLayout.addWidget(self.noECWIFTypeLabelContainerQFrame)

        self.noECWIFTypeQComboBox = QComboBox(self.noECWIFTypeContainerQFrame)
        self.noECWIFTypeQComboBox.setObjectName(u"noECWIFTypeQComboBox")

        self.noECWIFTypeContainerQFrameVLayout.addWidget(self.noECWIFTypeQComboBox)


        self.noECPrivateKeyAndWifTypeContainerHLayout_2.addWidget(self.noECWIFTypeContainerQFrame)

        self.noECCovertButtonContainerQFrame = QFrame(self.noECPrivateKeyAndWifTypeContainerQFrame)
        self.noECCovertButtonContainerQFrame.setObjectName(u"noECCovertButtonContainerQFrame")
        self.noECCovertButtonContainerQFrame.setMaximumSize(QSize(115, 16777215))
        self.noECConvertContainerQFrameVLayout = QVBoxLayout(self.noECCovertButtonContainerQFrame)
        self.noECConvertContainerQFrameVLayout.setSpacing(5)
        self.noECConvertContainerQFrameVLayout.setObjectName(u"noECConvertContainerQFrameVLayout")
        self.noECConvertContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.noECPrivateKeyButtonContainerQFrame = QFrame(self.noECCovertButtonContainerQFrame)
        self.noECPrivateKeyButtonContainerQFrame.setObjectName(u"noECPrivateKeyButtonContainerQFrame")
        self.noECPrivateKeyButtonContainerQFrame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.noECPrivateKeyButtonHLayout = QVBoxLayout(self.noECPrivateKeyButtonContainerQFrame)
        self.noECPrivateKeyButtonHLayout.setSpacing(0)
        self.noECPrivateKeyButtonHLayout.setObjectName(u"noECPrivateKeyButtonHLayout")
        self.noECPrivateKeyButtonHLayout.setContentsMargins(0, 0, 0, 0)
        self.noECPrivateKeyButtonSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.noECPrivateKeyButtonHLayout.addItem(self.noECPrivateKeyButtonSpacer)

        self.noECPrivateKeyConvertQPushButton = QPushButton(self.noECPrivateKeyButtonContainerQFrame)
        self.noECPrivateKeyConvertQPushButton.setObjectName(u"noECPrivateKeyConvertQPushButton")
        self.noECPrivateKeyConvertQPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.noECPrivateKeyButtonHLayout.addWidget(self.noECPrivateKeyConvertQPushButton)


        self.noECConvertContainerQFrameVLayout.addWidget(self.noECPrivateKeyButtonContainerQFrame)


        self.noECPrivateKeyAndWifTypeContainerHLayout_2.addWidget(self.noECCovertButtonContainerQFrame)


        self.noECVLayout.addWidget(self.noECPrivateKeyAndWifTypeContainerQFrame)

        self.noECWIFAndButtonContainerQFrame = QFrame(self.noECQWidget)
        self.noECWIFAndButtonContainerQFrame.setObjectName(u"noECWIFAndButtonContainerQFrame")
        self.noECWIFAndButtonContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.noECWIFAndButtonContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.noECWIFHorizontalLayout = QHBoxLayout(self.noECWIFAndButtonContainerQFrame)
        self.noECWIFHorizontalLayout.setSpacing(15)
        self.noECWIFHorizontalLayout.setObjectName(u"noECWIFHorizontalLayout")
        self.noECWIFHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.noECWIFContainerQFrame = QFrame(self.noECWIFAndButtonContainerQFrame)
        self.noECWIFContainerQFrame.setObjectName(u"noECWIFContainerQFrame")
        self.noECWIFContainerQFrameVLayout = QVBoxLayout(self.noECWIFContainerQFrame)
        self.noECWIFContainerQFrameVLayout.setSpacing(5)
        self.noECWIFContainerQFrameVLayout.setObjectName(u"noECWIFContainerQFrameVLayout")
        self.noECWIFContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.noECWIFwifLableContainerQFrame = QFrame(self.noECWIFContainerQFrame)
        self.noECWIFwifLableContainerQFrame.setObjectName(u"noECWIFwifLableContainerQFrame")
        self.noECWIFLabelContainerQFrameHLayout = QHBoxLayout(self.noECWIFwifLableContainerQFrame)
        self.noECWIFLabelContainerQFrameHLayout.setSpacing(15)
        self.noECWIFLabelContainerQFrameHLayout.setObjectName(u"noECWIFLabelContainerQFrameHLayout")
        self.noECWIFLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.noECWIFQLabel = QLabel(self.noECWIFwifLableContainerQFrame)
        self.noECWIFQLabel.setObjectName(u"noECWIFQLabel")

        self.noECWIFLabelContainerQFrameHLayout.addWidget(self.noECWIFQLabel)

        self.noECWIFLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.noECWIFLabelContainerQFrameHLayout.addItem(self.noECWIFLabelContainerQFrameHSpacer)


        self.noECWIFContainerQFrameVLayout.addWidget(self.noECWIFwifLableContainerQFrame)

        self.noECWIFAndEncyptContainerQFrame = QFrame(self.noECWIFContainerQFrame)
        self.noECWIFAndEncyptContainerQFrame.setObjectName(u"noECWIFAndEncyptContainerQFrame")
        self.noECWIFAndEncyptContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.noECWIFAndEncyptContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.noECWIFContainerVLayout = QHBoxLayout(self.noECWIFAndEncyptContainerQFrame)
        self.noECWIFContainerVLayout.setSpacing(15)
        self.noECWIFContainerVLayout.setObjectName(u"noECWIFContainerVLayout")
        self.noECWIFContainerVLayout.setContentsMargins(0, 0, 0, 0)
        self.noECWIFQLineEdit = QLineEdit(self.noECWIFAndEncyptContainerQFrame)
        self.noECWIFQLineEdit.setObjectName(u"noECWIFQLineEdit")

        self.noECWIFContainerVLayout.addWidget(self.noECWIFQLineEdit)

        self.noECEncryptQPushButton = QPushButton(self.noECWIFAndEncyptContainerQFrame)
        self.noECEncryptQPushButton.setObjectName(u"noECEncryptQPushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noECEncryptQPushButton.sizePolicy().hasHeightForWidth())
        self.noECEncryptQPushButton.setSizePolicy(sizePolicy)
        self.noECEncryptQPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.noECWIFContainerVLayout.addWidget(self.noECEncryptQPushButton)


        self.noECWIFContainerQFrameVLayout.addWidget(self.noECWIFAndEncyptContainerQFrame)


        self.noECWIFHorizontalLayout.addWidget(self.noECWIFContainerQFrame)


        self.noECVLayout.addWidget(self.noECWIFAndButtonContainerQFrame)

        self.modeQStackedWidget.addWidget(self.noECQWidget)
        self.ecQWidget = QWidget()
        self.ecQWidget.setObjectName(u"ecQWidget")
        self.modeQStackedWidget.addWidget(self.ecQWidget)

        self.verticalLayout.addWidget(self.modeQStackedWidget)

        self.decryptWIFAndButtonsContainerQFrame = QFrame(self.bip38ContainerQFrame)
        self.decryptWIFAndButtonsContainerQFrame.setObjectName(u"decryptWIFAndButtonsContainerQFrame")
        self.decryptWIFAndButtonsContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.decryptWIFAndButtonsContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.decryptWIFfHorizontalLayout = QHBoxLayout(self.decryptWIFAndButtonsContainerQFrame)
        self.decryptWIFfHorizontalLayout.setSpacing(15)
        self.decryptWIFfHorizontalLayout.setObjectName(u"decryptWIFfHorizontalLayout")
        self.decryptWIFfHorizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.decryptWIFContainerQFrame = QFrame(self.decryptWIFAndButtonsContainerQFrame)
        self.decryptWIFContainerQFrame.setObjectName(u"decryptWIFContainerQFrame")
        self.decryptWIFContainerQFrameVLayout = QVBoxLayout(self.decryptWIFContainerQFrame)
        self.decryptWIFContainerQFrameVLayout.setSpacing(5)
        self.decryptWIFContainerQFrameVLayout.setObjectName(u"decryptWIFContainerQFrameVLayout")
        self.decryptWIFContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.decryptWIFLableContainerQFrame = QFrame(self.decryptWIFContainerQFrame)
        self.decryptWIFLableContainerQFrame.setObjectName(u"decryptWIFLableContainerQFrame")
        self.decryptWIFLabelContainerQFrameHLayout = QHBoxLayout(self.decryptWIFLableContainerQFrame)
        self.decryptWIFLabelContainerQFrameHLayout.setSpacing(15)
        self.decryptWIFLabelContainerQFrameHLayout.setObjectName(u"decryptWIFLabelContainerQFrameHLayout")
        self.decryptWIFLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.decryptWIFQLabel = QLabel(self.decryptWIFLableContainerQFrame)
        self.decryptWIFQLabel.setObjectName(u"decryptWIFQLabel")

        self.decryptWIFLabelContainerQFrameHLayout.addWidget(self.decryptWIFQLabel)

        self.decryptWIFLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.decryptWIFLabelContainerQFrameHLayout.addItem(self.decryptWIFLabelContainerQFrameHSpacer)


        self.decryptWIFContainerQFrameVLayout.addWidget(self.decryptWIFLableContainerQFrame)

        self.decryptWIFAndButtonContainerQFrame = QFrame(self.decryptWIFContainerQFrame)
        self.decryptWIFAndButtonContainerQFrame.setObjectName(u"decryptWIFAndButtonContainerQFrame")
        self.decryptWIFAndButtonContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.decryptWIFAndButtonContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.decryptWIFHLayout = QHBoxLayout(self.decryptWIFAndButtonContainerQFrame)
        self.decryptWIFHLayout.setSpacing(15)
        self.decryptWIFHLayout.setObjectName(u"decryptWIFHLayout")
        self.decryptWIFHLayout.setContentsMargins(0, 0, 0, 0)
        self.decryptWIFQLineEdit = QLineEdit(self.decryptWIFAndButtonContainerQFrame)
        self.decryptWIFQLineEdit.setObjectName(u"decryptWIFQLineEdit")

        self.decryptWIFHLayout.addWidget(self.decryptWIFQLineEdit)

        self.decryptWIFQPushButton = QPushButton(self.decryptWIFAndButtonContainerQFrame)
        self.decryptWIFQPushButton.setObjectName(u"decryptWIFQPushButton")
        sizePolicy.setHeightForWidth(self.decryptWIFQPushButton.sizePolicy().hasHeightForWidth())
        self.decryptWIFQPushButton.setSizePolicy(sizePolicy)
        self.decryptWIFQPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.decryptWIFHLayout.addWidget(self.decryptWIFQPushButton)


        self.decryptWIFContainerQFrameVLayout.addWidget(self.decryptWIFAndButtonContainerQFrame)


        self.decryptWIFfHorizontalLayout.addWidget(self.decryptWIFContainerQFrame)


        self.verticalLayout.addWidget(self.decryptWIFAndButtonsContainerQFrame)

        self.outputQGroupBox = QGroupBox(self.bip38ContainerQFrame)
        self.outputQGroupBox.setObjectName(u"outputQGroupBox")
        self.outputGroupBoxVLayout = QVBoxLayout(self.outputQGroupBox)
        self.outputGroupBoxVLayout.setSpacing(0)
        self.outputGroupBoxVLayout.setObjectName(u"outputGroupBoxVLayout")
        self.outputGroupBoxVLayout.setContentsMargins(0, 5, 0, 0)
        self.outputQTextEdit = QTextEdit(self.outputQGroupBox)
        self.outputQTextEdit.setObjectName(u"outputQTextEdit")
        self.outputQTextEdit.setReadOnly(True)

        self.outputGroupBoxVLayout.addWidget(self.outputQTextEdit)


        self.verticalLayout.addWidget(self.outputQGroupBox)


        self.centeralWidgetLayout.addWidget(self.bip38ContainerQFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.modeQStackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.cryptocurrencyQLabel.setText(QCoreApplication.translate("MainWindow", u"Cryptocurrency", None))
        self.cryptocurrencyQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.networkQLabel.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.networkQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.passphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Passphrase", None))
        self.modeQLabel.setText(QCoreApplication.translate("MainWindow", u"Mode", None))
        self.modeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.noECPrivateKeyQLabel.setText(QCoreApplication.translate("MainWindow", u"Private Key", None))
        self.noECWIFTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"WIF Type", None))
        self.noECWIFTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.noECPrivateKeyConvertQPushButton.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.noECWIFQLabel.setText(QCoreApplication.translate("MainWindow", u"WIF", None))
        self.noECEncryptQPushButton.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.decryptWIFQLabel.setText(QCoreApplication.translate("MainWindow", u"Encrypted WIF", None))
        self.decryptWIFQPushButton.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.outputQGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.outputQTextEdit.setPlaceholderText("")
    # retranslateUi
