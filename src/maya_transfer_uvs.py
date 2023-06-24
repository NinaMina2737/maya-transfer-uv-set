#!/usr/bin/env python
# coding=utf-8

from __future__ import absolute_import, division, print_function, unicode_literals
import maya.cmds as cmds
import traceback

def transfer_uvs(base=None):
    # Get the selected objects
    objects = cmds.ls(selection=True)

    # If no base object is specified, use the first selected object
    if base is None:
        base = objects.pop(0)

    # Transfer UVs from the base object to the other selected objects
    for object in objects:
        # Select the base object and the object to transfer UVs to
        cmds.select([base,object])
        # Sample Space: 0=local, 1=world, 2=UV, 3=component
        # Transfer UVs: 0=off, 1=closestPoint, 2=closestComponent, 3=closestCorner, 4=closestBorder, 5=closestPolygon, 6=sharedPolygon, 7=sharedPosition
        # Transfer Colors: 0=off, 1=RGB, 2=RGBA, 3=RGB+Alpha
        cmds.transferAttributes(sampleSpace=4,transferUVs=2,transferColors=2)

def execute(base=None):
    try:
        # Open an undo chunk
        cmds.undoInfo(openChunk=True)
        # Execute the script
        transfer_uvs(base=base)
    except Exception as e:
        # Print the error message
        cmds.warning("An error occurred: {}".format(str(e)))
        # Print the traceback
        cmds.warning(traceback.format_exc())
    finally:
        # Close the undo chunk
        cmds.undoInfo(closeChunk=True)

if __name__ == '__main__':
    # Execute the script
    execute()
