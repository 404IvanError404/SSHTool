from Gui.Base.BsaeStandardItem import BaseStandardItem


class FileItem(BaseStandardItem):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.setImage("res/image/SFTRWindow/file.png")


class FolderItem(BaseStandardItem):
    def __init__(self, *__args):
        super().__init__(*__args)

        self.setImage("res/image/SFTRWindow/folder.png")
