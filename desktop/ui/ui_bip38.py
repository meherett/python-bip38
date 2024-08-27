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
        MainWindow.resize(804, 460)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centeralWidgetLayout = QVBoxLayout(self.centralwidget)
        self.centeralWidgetLayout.setSpacing(0)
        self.centeralWidgetLayout.setObjectName(u"centeralWidgetLayout")
        self.centeralWidgetLayout.setContentsMargins(15, 15, 15, 15)
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
        self.noECPrivateKeyButtonHLayout.setSpacing(5)
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
        self.ecVLayout = QVBoxLayout(self.ecQWidget)
        self.ecVLayout.setSpacing(10)
        self.ecVLayout.setObjectName(u"ecVLayout")
        self.ecVLayout.setContentsMargins(0, 0, 0, 0)
        self.ecSaltMainContainerQFrame = QFrame(self.ecQWidget)
        self.ecSaltMainContainerQFrame.setObjectName(u"ecSaltMainContainerQFrame")
        self.ecSaltMainContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ecSaltMainContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.ecOwnerSaltMainContainerHLayout = QHBoxLayout(self.ecSaltMainContainerQFrame)
        self.ecOwnerSaltMainContainerHLayout.setSpacing(15)
        self.ecOwnerSaltMainContainerHLayout.setObjectName(u"ecOwnerSaltMainContainerHLayout")
        self.ecOwnerSaltMainContainerHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecOwnerSaltContainerQFrame = QFrame(self.ecSaltMainContainerQFrame)
        self.ecOwnerSaltContainerQFrame.setObjectName(u"ecOwnerSaltContainerQFrame")
        self.ecOwnerSaltContainerQFrameVLayout = QVBoxLayout(self.ecOwnerSaltContainerQFrame)
        self.ecOwnerSaltContainerQFrameVLayout.setSpacing(5)
        self.ecOwnerSaltContainerQFrameVLayout.setObjectName(u"ecOwnerSaltContainerQFrameVLayout")
        self.ecOwnerSaltContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.ecOwnerSaltLableContainerQFrame = QFrame(self.ecOwnerSaltContainerQFrame)
        self.ecOwnerSaltLableContainerQFrame.setObjectName(u"ecOwnerSaltLableContainerQFrame")
        self.ecOwnerSaltLableContainerQFrameHLayout = QHBoxLayout(self.ecOwnerSaltLableContainerQFrame)
        self.ecOwnerSaltLableContainerQFrameHLayout.setSpacing(15)
        self.ecOwnerSaltLableContainerQFrameHLayout.setObjectName(u"ecOwnerSaltLableContainerQFrameHLayout")
        self.ecOwnerSaltLableContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecOwnerSaltQLabel = QLabel(self.ecOwnerSaltLableContainerQFrame)
        self.ecOwnerSaltQLabel.setObjectName(u"ecOwnerSaltQLabel")

        self.ecOwnerSaltLableContainerQFrameHLayout.addWidget(self.ecOwnerSaltQLabel)

        self.ecOwnerSaltLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ecOwnerSaltLableContainerQFrameHLayout.addItem(self.ecOwnerSaltLabelContainerQFrameHSpacer)


        self.ecOwnerSaltContainerQFrameVLayout.addWidget(self.ecOwnerSaltLableContainerQFrame)

        self.ecOwnerSaltAndGenerateContainerQFrame = QFrame(self.ecOwnerSaltContainerQFrame)
        self.ecOwnerSaltAndGenerateContainerQFrame.setObjectName(u"ecOwnerSaltAndGenerateContainerQFrame")
        self.ecOwnerSaltAndGenerateContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ecOwnerSaltAndGenerateContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.ecOwnerSaltAndGenerateContainerQFrameHLayout = QHBoxLayout(self.ecOwnerSaltAndGenerateContainerQFrame)
        self.ecOwnerSaltAndGenerateContainerQFrameHLayout.setSpacing(15)
        self.ecOwnerSaltAndGenerateContainerQFrameHLayout.setObjectName(u"ecOwnerSaltAndGenerateContainerQFrameHLayout")
        self.ecOwnerSaltAndGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecOwnerSaltQLineEdit = QLineEdit(self.ecOwnerSaltAndGenerateContainerQFrame)
        self.ecOwnerSaltQLineEdit.setObjectName(u"ecOwnerSaltQLineEdit")

        self.ecOwnerSaltAndGenerateContainerQFrameHLayout.addWidget(self.ecOwnerSaltQLineEdit)

        self.ecOwnerSaltGenerateQPushButton = QPushButton(self.ecOwnerSaltAndGenerateContainerQFrame)
        self.ecOwnerSaltGenerateQPushButton.setObjectName(u"ecOwnerSaltGenerateQPushButton")
        sizePolicy.setHeightForWidth(self.ecOwnerSaltGenerateQPushButton.sizePolicy().hasHeightForWidth())
        self.ecOwnerSaltGenerateQPushButton.setSizePolicy(sizePolicy)
        self.ecOwnerSaltGenerateQPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.ecOwnerSaltAndGenerateContainerQFrameHLayout.addWidget(self.ecOwnerSaltGenerateQPushButton)


        self.ecOwnerSaltContainerQFrameVLayout.addWidget(self.ecOwnerSaltAndGenerateContainerQFrame)


        self.ecOwnerSaltMainContainerHLayout.addWidget(self.ecOwnerSaltContainerQFrame)

        self.ecSeedContainerQFrame = QFrame(self.ecSaltMainContainerQFrame)
        self.ecSeedContainerQFrame.setObjectName(u"ecSeedContainerQFrame")
        self.ecSeedContainerQFrameHLayout = QVBoxLayout(self.ecSeedContainerQFrame)
        self.ecSeedContainerQFrameHLayout.setSpacing(5)
        self.ecSeedContainerQFrameHLayout.setObjectName(u"ecSeedContainerQFrameHLayout")
        self.ecSeedContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecSeedLabelContainerQFrame = QFrame(self.ecSeedContainerQFrame)
        self.ecSeedLabelContainerQFrame.setObjectName(u"ecSeedLabelContainerQFrame")
        self.ecSeedLabelContainerQFrameHLayout = QHBoxLayout(self.ecSeedLabelContainerQFrame)
        self.ecSeedLabelContainerQFrameHLayout.setSpacing(15)
        self.ecSeedLabelContainerQFrameHLayout.setObjectName(u"ecSeedLabelContainerQFrameHLayout")
        self.ecSeedLabelContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecSeedQLabel = QLabel(self.ecSeedLabelContainerQFrame)
        self.ecSeedQLabel.setObjectName(u"ecSeedQLabel")

        self.ecSeedLabelContainerQFrameHLayout.addWidget(self.ecSeedQLabel)

        self.ecSeedLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ecSeedLabelContainerQFrameHLayout.addItem(self.ecSeedLabelContainerQFrameHSpacer)


        self.ecSeedContainerQFrameHLayout.addWidget(self.ecSeedLabelContainerQFrame)

        self.ecSeedAndGenerateContainerQFrame = QFrame(self.ecSeedContainerQFrame)
        self.ecSeedAndGenerateContainerQFrame.setObjectName(u"ecSeedAndGenerateContainerQFrame")
        self.ecSeedAndGenerateContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ecSeedAndGenerateContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.ecSeedAndGenerateContainerQFrameHLayout = QHBoxLayout(self.ecSeedAndGenerateContainerQFrame)
        self.ecSeedAndGenerateContainerQFrameHLayout.setSpacing(15)
        self.ecSeedAndGenerateContainerQFrameHLayout.setObjectName(u"ecSeedAndGenerateContainerQFrameHLayout")
        self.ecSeedAndGenerateContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecSeedQLineEdit = QLineEdit(self.ecSeedAndGenerateContainerQFrame)
        self.ecSeedQLineEdit.setObjectName(u"ecSeedQLineEdit")

        self.ecSeedAndGenerateContainerQFrameHLayout.addWidget(self.ecSeedQLineEdit)

        self.ecSeedGenerateQPushButton = QPushButton(self.ecSeedAndGenerateContainerQFrame)
        self.ecSeedGenerateQPushButton.setObjectName(u"ecSeedGenerateQPushButton")
        sizePolicy.setHeightForWidth(self.ecSeedGenerateQPushButton.sizePolicy().hasHeightForWidth())
        self.ecSeedGenerateQPushButton.setSizePolicy(sizePolicy)
        self.ecSeedGenerateQPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.ecSeedAndGenerateContainerQFrameHLayout.addWidget(self.ecSeedGenerateQPushButton)


        self.ecSeedContainerQFrameHLayout.addWidget(self.ecSeedAndGenerateContainerQFrame)


        self.ecOwnerSaltMainContainerHLayout.addWidget(self.ecSeedContainerQFrame)

        self.ecLotContainerQFrame = QFrame(self.ecSaltMainContainerQFrame)
        self.ecLotContainerQFrame.setObjectName(u"ecLotContainerQFrame")
        self.ecLotContainerQFrame.setMaximumSize(QSize(100, 16777215))
        self.ecLotContainerQFrameVLayout = QVBoxLayout(self.ecLotContainerQFrame)
        self.ecLotContainerQFrameVLayout.setSpacing(5)
        self.ecLotContainerQFrameVLayout.setObjectName(u"ecLotContainerQFrameVLayout")
        self.ecLotContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.ecLotLableContainerQFrame = QFrame(self.ecLotContainerQFrame)
        self.ecLotLableContainerQFrame.setObjectName(u"ecLotLableContainerQFrame")
        self.ecLotLableContainerQFrameHLayout = QHBoxLayout(self.ecLotLableContainerQFrame)
        self.ecLotLableContainerQFrameHLayout.setSpacing(15)
        self.ecLotLableContainerQFrameHLayout.setObjectName(u"ecLotLableContainerQFrameHLayout")
        self.ecLotLableContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecLotQLabel = QLabel(self.ecLotLableContainerQFrame)
        self.ecLotQLabel.setObjectName(u"ecLotQLabel")

        self.ecLotLableContainerQFrameHLayout.addWidget(self.ecLotQLabel)

        self.ecLotLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ecLotLableContainerQFrameHLayout.addItem(self.ecLotLabelContainerQFrameHSpacer)


        self.ecLotContainerQFrameVLayout.addWidget(self.ecLotLableContainerQFrame)

        self.ecLotEditContainerQFrame = QFrame(self.ecLotContainerQFrame)
        self.ecLotEditContainerQFrame.setObjectName(u"ecLotEditContainerQFrame")
        self.ecLotEditContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ecLotEditContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.ecLotEditContainerQFrameHLayout = QHBoxLayout(self.ecLotEditContainerQFrame)
        self.ecLotEditContainerQFrameHLayout.setSpacing(0)
        self.ecLotEditContainerQFrameHLayout.setObjectName(u"ecLotEditContainerQFrameHLayout")
        self.ecLotEditContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecLotQLineEdit = QLineEdit(self.ecLotEditContainerQFrame)
        self.ecLotQLineEdit.setObjectName(u"ecLotQLineEdit")

        self.ecLotEditContainerQFrameHLayout.addWidget(self.ecLotQLineEdit)


        self.ecLotContainerQFrameVLayout.addWidget(self.ecLotEditContainerQFrame)


        self.ecOwnerSaltMainContainerHLayout.addWidget(self.ecLotContainerQFrame)

        self.ecSequenceContainerQFrame = QFrame(self.ecSaltMainContainerQFrame)
        self.ecSequenceContainerQFrame.setObjectName(u"ecSequenceContainerQFrame")
        self.ecSequenceContainerQFrame.setMaximumSize(QSize(100, 16777215))
        self.ecSequenceContainerQFrameVLayout = QVBoxLayout(self.ecSequenceContainerQFrame)
        self.ecSequenceContainerQFrameVLayout.setSpacing(5)
        self.ecSequenceContainerQFrameVLayout.setObjectName(u"ecSequenceContainerQFrameVLayout")
        self.ecSequenceContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.ecSequenceLableContainerQFrame = QFrame(self.ecSequenceContainerQFrame)
        self.ecSequenceLableContainerQFrame.setObjectName(u"ecSequenceLableContainerQFrame")
        self.ecSequenceLableContainerQFrameHLayout = QHBoxLayout(self.ecSequenceLableContainerQFrame)
        self.ecSequenceLableContainerQFrameHLayout.setSpacing(15)
        self.ecSequenceLableContainerQFrameHLayout.setObjectName(u"ecSequenceLableContainerQFrameHLayout")
        self.ecSequenceLableContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecSequenceQLabel = QLabel(self.ecSequenceLableContainerQFrame)
        self.ecSequenceQLabel.setObjectName(u"ecSequenceQLabel")

        self.ecSequenceLableContainerQFrameHLayout.addWidget(self.ecSequenceQLabel)

        self.ecSequenceLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ecSequenceLableContainerQFrameHLayout.addItem(self.ecSequenceLabelContainerQFrameHSpacer)


        self.ecSequenceContainerQFrameVLayout.addWidget(self.ecSequenceLableContainerQFrame)

        self.ecSequenceEditContainerQFrame = QFrame(self.ecSequenceContainerQFrame)
        self.ecSequenceEditContainerQFrame.setObjectName(u"ecSequenceEditContainerQFrame")
        self.ecSequenceEditContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ecSequenceEditContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.ecSequenceEditContainerQFrameHLayout = QHBoxLayout(self.ecSequenceEditContainerQFrame)
        self.ecSequenceEditContainerQFrameHLayout.setSpacing(0)
        self.ecSequenceEditContainerQFrameHLayout.setObjectName(u"ecSequenceEditContainerQFrameHLayout")
        self.ecSequenceEditContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecSequenceQLineEdit = QLineEdit(self.ecSequenceEditContainerQFrame)
        self.ecSequenceQLineEdit.setObjectName(u"ecSequenceQLineEdit")
        self.ecSequenceQLineEdit.setMinimumSize(QSize(0, 0))

        self.ecSequenceEditContainerQFrameHLayout.addWidget(self.ecSequenceQLineEdit)


        self.ecSequenceContainerQFrameVLayout.addWidget(self.ecSequenceEditContainerQFrame)


        self.ecOwnerSaltMainContainerHLayout.addWidget(self.ecSequenceContainerQFrame)


        self.ecVLayout.addWidget(self.ecSaltMainContainerQFrame)

        self.ecIPAndConfirmMainContainerQFrame = QFrame(self.ecQWidget)
        self.ecIPAndConfirmMainContainerQFrame.setObjectName(u"ecIPAndConfirmMainContainerQFrame")
        self.ecIPAndConfirmMainContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ecIPAndConfirmMainContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.ecIntermidatMainContainerQFrameHLayout = QHBoxLayout(self.ecIPAndConfirmMainContainerQFrame)
        self.ecIntermidatMainContainerQFrameHLayout.setSpacing(15)
        self.ecIntermidatMainContainerQFrameHLayout.setObjectName(u"ecIntermidatMainContainerQFrameHLayout")
        self.ecIntermidatMainContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecIPassphraseContainerQFrame = QFrame(self.ecIPAndConfirmMainContainerQFrame)
        self.ecIPassphraseContainerQFrame.setObjectName(u"ecIPassphraseContainerQFrame")
        self.ecIPassphraseContainerQFrameVLayout = QVBoxLayout(self.ecIPassphraseContainerQFrame)
        self.ecIPassphraseContainerQFrameVLayout.setSpacing(5)
        self.ecIPassphraseContainerQFrameVLayout.setObjectName(u"ecIPassphraseContainerQFrameVLayout")
        self.ecIPassphraseContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.ecIPassphraseLableContainerQFrame = QFrame(self.ecIPassphraseContainerQFrame)
        self.ecIPassphraseLableContainerQFrame.setObjectName(u"ecIPassphraseLableContainerQFrame")
        self.ecIPassphraseLableContainerQFrameHLayout = QHBoxLayout(self.ecIPassphraseLableContainerQFrame)
        self.ecIPassphraseLableContainerQFrameHLayout.setSpacing(15)
        self.ecIPassphraseLableContainerQFrameHLayout.setObjectName(u"ecIPassphraseLableContainerQFrameHLayout")
        self.ecIPassphraseLableContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecIPassphraseQLabel = QLabel(self.ecIPassphraseLableContainerQFrame)
        self.ecIPassphraseQLabel.setObjectName(u"ecIPassphraseQLabel")

        self.ecIPassphraseLableContainerQFrameHLayout.addWidget(self.ecIPassphraseQLabel)

        self.ecIPassphraseLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ecIPassphraseLableContainerQFrameHLayout.addItem(self.ecIPassphraseLabelContainerQFrameHSpacer)


        self.ecIPassphraseContainerQFrameVLayout.addWidget(self.ecIPassphraseLableContainerQFrame)

        self.ecIPassphraseAndGenerateContainerQFrameHLayout = QFrame(self.ecIPassphraseContainerQFrame)
        self.ecIPassphraseAndGenerateContainerQFrameHLayout.setObjectName(u"ecIPassphraseAndGenerateContainerQFrameHLayout")
        self.ecIPassphraseAndGenerateContainerQFrameHLayout.setFrameShape(QFrame.Shape.StyledPanel)
        self.ecIPassphraseAndGenerateContainerQFrameHLayout.setFrameShadow(QFrame.Shadow.Raised)
        self.ecIntermediatePassphraseAndGenerateHLayout = QHBoxLayout(self.ecIPassphraseAndGenerateContainerQFrameHLayout)
        self.ecIntermediatePassphraseAndGenerateHLayout.setSpacing(15)
        self.ecIntermediatePassphraseAndGenerateHLayout.setObjectName(u"ecIntermediatePassphraseAndGenerateHLayout")
        self.ecIntermediatePassphraseAndGenerateHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecIPassphraseQLineEdit = QLineEdit(self.ecIPassphraseAndGenerateContainerQFrameHLayout)
        self.ecIPassphraseQLineEdit.setObjectName(u"ecIPassphraseQLineEdit")

        self.ecIntermediatePassphraseAndGenerateHLayout.addWidget(self.ecIPassphraseQLineEdit)

        self.ecIPassphraseGenerateQPushButton = QPushButton(self.ecIPassphraseAndGenerateContainerQFrameHLayout)
        self.ecIPassphraseGenerateQPushButton.setObjectName(u"ecIPassphraseGenerateQPushButton")
        sizePolicy.setHeightForWidth(self.ecIPassphraseGenerateQPushButton.sizePolicy().hasHeightForWidth())
        self.ecIPassphraseGenerateQPushButton.setSizePolicy(sizePolicy)
        self.ecIPassphraseGenerateQPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.ecIntermediatePassphraseAndGenerateHLayout.addWidget(self.ecIPassphraseGenerateQPushButton)


        self.ecIPassphraseContainerQFrameVLayout.addWidget(self.ecIPassphraseAndGenerateContainerQFrameHLayout)


        self.ecIntermidatMainContainerQFrameHLayout.addWidget(self.ecIPassphraseContainerQFrame)

        self.ecConfirmCodeContainerQFrame = QFrame(self.ecIPAndConfirmMainContainerQFrame)
        self.ecConfirmCodeContainerQFrame.setObjectName(u"ecConfirmCodeContainerQFrame")
        self.ecConfirmCodeContainerQFrameVLayout = QVBoxLayout(self.ecConfirmCodeContainerQFrame)
        self.ecConfirmCodeContainerQFrameVLayout.setSpacing(5)
        self.ecConfirmCodeContainerQFrameVLayout.setObjectName(u"ecConfirmCodeContainerQFrameVLayout")
        self.ecConfirmCodeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.ecCodeLableContainerQFrame = QFrame(self.ecConfirmCodeContainerQFrame)
        self.ecCodeLableContainerQFrame.setObjectName(u"ecCodeLableContainerQFrame")
        self.ecCodeLableContainerQFrameHLayout = QHBoxLayout(self.ecCodeLableContainerQFrame)
        self.ecCodeLableContainerQFrameHLayout.setSpacing(15)
        self.ecCodeLableContainerQFrameHLayout.setObjectName(u"ecCodeLableContainerQFrameHLayout")
        self.ecCodeLableContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecConfirmCodeQLabel = QLabel(self.ecCodeLableContainerQFrame)
        self.ecConfirmCodeQLabel.setObjectName(u"ecConfirmCodeQLabel")

        self.ecCodeLableContainerQFrameHLayout.addWidget(self.ecConfirmCodeQLabel)

        self.ecConfirmCodeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.ecCodeLableContainerQFrameHLayout.addItem(self.ecConfirmCodeLabelContainerQFrameHSpacer)


        self.ecConfirmCodeContainerQFrameVLayout.addWidget(self.ecCodeLableContainerQFrame)

        self.ecConfirmCodeAndVerifyContainerQFrame = QFrame(self.ecConfirmCodeContainerQFrame)
        self.ecConfirmCodeAndVerifyContainerQFrame.setObjectName(u"ecConfirmCodeAndVerifyContainerQFrame")
        self.ecConfirmCodeAndVerifyContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ecConfirmCodeAndVerifyContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.ecConfirmCodeAndVerifyContainerQFrameHLayout = QHBoxLayout(self.ecConfirmCodeAndVerifyContainerQFrame)
        self.ecConfirmCodeAndVerifyContainerQFrameHLayout.setSpacing(15)
        self.ecConfirmCodeAndVerifyContainerQFrameHLayout.setObjectName(u"ecConfirmCodeAndVerifyContainerQFrameHLayout")
        self.ecConfirmCodeAndVerifyContainerQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.ecConfirmCodeQLineEdit = QLineEdit(self.ecConfirmCodeAndVerifyContainerQFrame)
        self.ecConfirmCodeQLineEdit.setObjectName(u"ecConfirmCodeQLineEdit")

        self.ecConfirmCodeAndVerifyContainerQFrameHLayout.addWidget(self.ecConfirmCodeQLineEdit)

        self.ecConfirmCodeVerifyQPushButton = QPushButton(self.ecConfirmCodeAndVerifyContainerQFrame)
        self.ecConfirmCodeVerifyQPushButton.setObjectName(u"ecConfirmCodeVerifyQPushButton")
        sizePolicy.setHeightForWidth(self.ecConfirmCodeVerifyQPushButton.sizePolicy().hasHeightForWidth())
        self.ecConfirmCodeVerifyQPushButton.setSizePolicy(sizePolicy)
        self.ecConfirmCodeVerifyQPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.ecConfirmCodeAndVerifyContainerQFrameHLayout.addWidget(self.ecConfirmCodeVerifyQPushButton)


        self.ecConfirmCodeContainerQFrameVLayout.addWidget(self.ecConfirmCodeAndVerifyContainerQFrame)


        self.ecIntermidatMainContainerQFrameHLayout.addWidget(self.ecConfirmCodeContainerQFrame)


        self.ecVLayout.addWidget(self.ecIPAndConfirmMainContainerQFrame)

        self.modeQStackedWidget.addWidget(self.ecQWidget)

        self.verticalLayout.addWidget(self.modeQStackedWidget)

        self.decryptWIFAndButtonsContainerQFrame = QFrame(self.bip38ContainerQFrame)
        self.decryptWIFAndButtonsContainerQFrame.setObjectName(u"decryptWIFAndButtonsContainerQFrame")
        self.decryptWIFAndButtonsQFrameHLayout = QHBoxLayout(self.decryptWIFAndButtonsContainerQFrame)
        self.decryptWIFAndButtonsQFrameHLayout.setSpacing(15)
        self.decryptWIFAndButtonsQFrameHLayout.setObjectName(u"decryptWIFAndButtonsQFrameHLayout")
        self.decryptWIFAndButtonsQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.decryptWIFContainerQFrame = QFrame(self.decryptWIFAndButtonsContainerQFrame)
        self.decryptWIFContainerQFrame.setObjectName(u"decryptWIFContainerQFrame")
        self.decryptWIFContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.decryptWIFContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
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

        self.decryptWIFQLineEdit = QLineEdit(self.decryptWIFContainerQFrame)
        self.decryptWIFQLineEdit.setObjectName(u"decryptWIFQLineEdit")

        self.decryptWIFContainerQFrameVLayout.addWidget(self.decryptWIFQLineEdit)


        self.decryptWIFAndButtonsQFrameHLayout.addWidget(self.decryptWIFContainerQFrame)

        self.decryptWIFTypeContainerQFrame = QFrame(self.decryptWIFAndButtonsContainerQFrame)
        self.decryptWIFTypeContainerQFrame.setObjectName(u"decryptWIFTypeContainerQFrame")
        self.decryptWIFTypeContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.decryptWIFTypeContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.decryptWIFTypeContainerQFrameVLayout = QVBoxLayout(self.decryptWIFTypeContainerQFrame)
        self.decryptWIFTypeContainerQFrameVLayout.setObjectName(u"decryptWIFTypeContainerQFrameVLayout")
        self.decryptWIFTypeContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.wifTypeLableContainerQFrame = QFrame(self.decryptWIFTypeContainerQFrame)
        self.wifTypeLableContainerQFrame.setObjectName(u"wifTypeLableContainerQFrame")
        self.wifTypeLabelContainerQFrameHLayout2 = QHBoxLayout(self.wifTypeLableContainerQFrame)
        self.wifTypeLabelContainerQFrameHLayout2.setSpacing(15)
        self.wifTypeLabelContainerQFrameHLayout2.setObjectName(u"wifTypeLabelContainerQFrameHLayout2")
        self.wifTypeLabelContainerQFrameHLayout2.setContentsMargins(0, 0, 0, 0)
        self.wifTypeQLabel = QLabel(self.wifTypeLableContainerQFrame)
        self.wifTypeQLabel.setObjectName(u"wifTypeQLabel")

        self.wifTypeLabelContainerQFrameHLayout2.addWidget(self.wifTypeQLabel)

        self.wifTypeLabelContainerQFrameHSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.wifTypeLabelContainerQFrameHLayout2.addItem(self.wifTypeLabelContainerQFrameHSpacer)


        self.decryptWIFTypeContainerQFrameVLayout.addWidget(self.wifTypeLableContainerQFrame)

        self.createEncryptedWIFTypeQComboBox = QComboBox(self.decryptWIFTypeContainerQFrame)
        self.createEncryptedWIFTypeQComboBox.setObjectName(u"createEncryptedWIFTypeQComboBox")
        self.createEncryptedWIFTypeQComboBox.setMinimumSize(QSize(145, 0))

        self.decryptWIFTypeContainerQFrameVLayout.addWidget(self.createEncryptedWIFTypeQComboBox)


        self.decryptWIFAndButtonsQFrameHLayout.addWidget(self.decryptWIFTypeContainerQFrame)

        self.decryptWIFButtonsContainerQFrame = QFrame(self.decryptWIFAndButtonsContainerQFrame)
        self.decryptWIFButtonsContainerQFrame.setObjectName(u"decryptWIFButtonsContainerQFrame")
        self.decryptWIFButtonsContainerQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.decryptWIFButtonsContainerQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.decryptWIFButtonsContainerQFrameVLayout = QVBoxLayout(self.decryptWIFButtonsContainerQFrame)
        self.decryptWIFButtonsContainerQFrameVLayout.setSpacing(5)
        self.decryptWIFButtonsContainerQFrameVLayout.setObjectName(u"decryptWIFButtonsContainerQFrameVLayout")
        self.decryptWIFButtonsContainerQFrameVLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 49, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.decryptWIFButtonsContainerQFrameVLayout.addItem(self.verticalSpacer)

        self.decryptWIFButtonsQFrame = QFrame(self.decryptWIFButtonsContainerQFrame)
        self.decryptWIFButtonsQFrame.setObjectName(u"decryptWIFButtonsQFrame")
        self.decryptWIFButtonsQFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.decryptWIFButtonsQFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.decryptWIFButtonsQFrameHLayout = QHBoxLayout(self.decryptWIFButtonsQFrame)
        self.decryptWIFButtonsQFrameHLayout.setSpacing(15)
        self.decryptWIFButtonsQFrameHLayout.setObjectName(u"decryptWIFButtonsQFrameHLayout")
        self.decryptWIFButtonsQFrameHLayout.setContentsMargins(0, 0, 0, 0)
        self.createEncryptedWIFQPushButton = QPushButton(self.decryptWIFButtonsQFrame)
        self.createEncryptedWIFQPushButton.setObjectName(u"createEncryptedWIFQPushButton")
        self.createEncryptedWIFQPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.decryptWIFButtonsQFrameHLayout.addWidget(self.createEncryptedWIFQPushButton)

        self.decryptWIFQPushButton = QPushButton(self.decryptWIFButtonsQFrame)
        self.decryptWIFQPushButton.setObjectName(u"decryptWIFQPushButton")
        sizePolicy.setHeightForWidth(self.decryptWIFQPushButton.sizePolicy().hasHeightForWidth())
        self.decryptWIFQPushButton.setSizePolicy(sizePolicy)
        self.decryptWIFQPushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.decryptWIFButtonsQFrameHLayout.addWidget(self.decryptWIFQPushButton)


        self.decryptWIFButtonsContainerQFrameVLayout.addWidget(self.decryptWIFButtonsQFrame)


        self.decryptWIFAndButtonsQFrameHLayout.addWidget(self.decryptWIFButtonsContainerQFrame)


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

        self.modeQStackedWidget.setCurrentIndex(1)


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
        self.ecOwnerSaltQLabel.setText(QCoreApplication.translate("MainWindow", u"Owner Salt", None))
        self.ecOwnerSaltGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ecSeedQLabel.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
        self.ecSeedGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ecLotQLabel.setText(QCoreApplication.translate("MainWindow", u"Lot", None))
        self.ecLotQLineEdit.setText(QCoreApplication.translate("MainWindow", u"100000", None))
        self.ecSequenceQLabel.setText(QCoreApplication.translate("MainWindow", u"Sequence", None))
        self.ecSequenceQLineEdit.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.ecIPassphraseQLabel.setText(QCoreApplication.translate("MainWindow", u"Intermediate Passphrase", None))
        self.ecIPassphraseGenerateQPushButton.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        self.ecConfirmCodeQLabel.setText(QCoreApplication.translate("MainWindow", u"Confirm Code", None))
        self.ecConfirmCodeVerifyQPushButton.setText(QCoreApplication.translate("MainWindow", u"Verify", None))
        self.decryptWIFQLabel.setText(QCoreApplication.translate("MainWindow", u"Encrypted WIF", None))
        self.wifTypeQLabel.setText(QCoreApplication.translate("MainWindow", u"WIF Type", None))
        self.createEncryptedWIFTypeQComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(Select)", None))
        self.createEncryptedWIFQPushButton.setText(QCoreApplication.translate("MainWindow", u"Create", None))
        self.decryptWIFQPushButton.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.outputQGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.outputQTextEdit.setPlaceholderText("")
    # retranslateUi

