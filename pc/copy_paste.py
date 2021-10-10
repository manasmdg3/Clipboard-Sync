import pyperclip as pc
def getFromClipboard():
    while True:
        pc.waitForNewPaste()
        text2 = pc.paste()
        print(text2+" from copy_paste")
        return text2