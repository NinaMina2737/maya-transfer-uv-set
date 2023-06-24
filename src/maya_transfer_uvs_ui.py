#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals

import traceback

import maya.cmds as cmds
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from PySide2 import QtCore, QtWidgets

import maya_transfer_uvs as mtu
reload(mtu)

WINDOW_TITLE = "Transfer UVs"

class TransferUVsUI(MayaQWidgetBaseMixin, QtWidgets.QWidget):
    """
    The UI class for the Set Ground tool.
    """
    def __init__(self):
        """
        Initializes the class.
        """
        super(self.__class__, self).__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.create_widget()
        self.create_layout()

    def create_widget(self):
        """
        """

    def create_layout(self):
        """
        """
        main_layout = QtWidgets.QVBoxLayout()

def execute():
    """
    Executes the UI.

    Raises:
        Exception: An error occurred.
    """
    try:
        # Check if the window already exists
        if cmds.window(WINDOW_TITLE, exists=True):
            cmds.deleteUI(WINDOW_TITLE)

        # Create the window
        window = TransferUVsUI()
        window.show()
    except Exception as e:
        # Print the error message
        cmds.warning("An error occurred: {}".format(str(e)))
        # Print the traceback
        cmds.warning(traceback.format_exc())

if __name__ == "__main__":
    execute()
