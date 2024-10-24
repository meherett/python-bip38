#!/usr/bin/env python3

# Copyright © 2024, Eyoel Tadesse <eyoel_tadesse@proton.me>
# Distributed under the MIT software license, see the accompanying
# file COPYING or https://opensource.org/license/mit

import os
from PySide6.QtWidgets import QLayout
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtCore import QSize

def clear_layout(layout: QLayout, delete: bool = True) -> None:
    """
    Clear all widgets from a layout.

    :param layout: The layout to clear.
    :param delete: Whether to delete the widgets after removing them from the layout.
    """
    if layout is not None:
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None and delete:
                widget.deleteLater()
            else:
                clear_layout(item.layout())


def resolve_path(path: str) -> str:
    """
    Resolve the absolute path of a given relative path.

    :param path: The relative path to resolve.
    :type path: str
    :return: The absolute path of the given relative path.
    :rtype: str
    """
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../", path))


def put_svg(layout: QLayout, path: str, width: int, height: int) -> QSvgWidget:
    """
    Add an SVG widget to a layout.

    :param layout: The layout to add the SVG widget to.
    :param path: The path to the SVG file.
    :param width: The width of the SVG widget.
    :param height: The height of the SVG widget.
    :return: The SVG widget.
    """
    clear_layout(layout)
    svg = QSvgWidget(path)
    svg.setMinimumSize(QSize(width, height))
    svg.setMaximumSize(QSize(width, height))
    svg.setStyleSheet("background: transparent")
    layout.addWidget(svg)
    return svg
