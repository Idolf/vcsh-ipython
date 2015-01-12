c = get_config()

c.TerminalIPythonApp.display_banner = False
c.TerminalIPythonApp.nosep = True

c.InteractiveShellApp.exec_lines = [
    'from pwn import *',
    'import pwn',
]
c.InteractiveShell.autoindent = True
c.InteractiveShell.colors = 'LightBG'
c.InteractiveShell.confirm_exit = False

c.PrefilterManager.multi_line_specials = True

