import pyperclip as pc
def getFromClipboard():
    while True:
        pc.waitForNewPaste()
        text2 = pc.paste()
        return text2