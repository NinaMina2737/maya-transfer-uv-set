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
        self.base_object_label = QtWidgets.QLabel("Select the base object:")
        self.base_object_line_edit = QtWidgets.QLineEdit()
        self.base_object_line_edit.setReadOnly(True)
        self.base_object_line_edit.setText("None")

        self.base_object_button = QtWidgets.QPushButton("Select Base Object")
        self.base_object_button.clicked.connect(self.select_base_object)

        self.execute_button = QtWidgets.QPushButton("Execute")
        self.execute_button.clicked.connect(self.execute)

    def create_layout(self):
        """
        """
        main_layout = QtWidgets.QVBoxLayout()

        main_layout.addWidget(self.base_object_label)
        main_layout.addWidget(self.base_object_line_edit)
        main_layout.addWidget(self.base_object_button)
        main_layout.addWidget(self.execute_button)

        self.setLayout(main_layout)

    def select_base_object(self):
        """
        """
        # Get the selected objects
        objects = cmds.ls(selection=True)

        # If no base object is specified, use the first selected object
        if len(objects) > 0:
            # Set the base object
            self.base_object_line_edit.setText(objects[0])
        else:
            # Set the base object to None
            self.base_object_line_edit.setText("None")

    def execute(self):
        """
        """
        if self.base_object_line_edit.text() == "None":
            cmds.warning("No base object specified.")
            return

        # Get the base object
        base_object = self.base_object_line_edit.text()

        # Get the selected objects
        objects = cmds.ls(selection=True)

        # Check if any objects are selected
        if len(objects) == 0:
            cmds.warning("No objects selected.")
            return

        # Transfer the UVs
        mtu.transfer_uvs(base_object=base_object, objects=objects)

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
