""" Game fix for Divinity: Original Sin 2 - Definitive Edition(435150)
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    """ Changes the proton argument from the launcher to the game
    """

    log('Applying Divinity Original Sin 2  Definitive Edition Game Fixes')

    # Set OS to Windows 10, to fix the save folder creating issue
    util.protontricks('win10')

    # Fix crash on startup issue
    util.replace_command('bin/SupportTool.exe', 'DefEd/bin/EoCApp.exe')
