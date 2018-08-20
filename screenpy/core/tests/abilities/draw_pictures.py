class DrawPictures:

    def __init__(self, tool='pencil'):
        super(DrawPictures, self).__init__()
        self.tool = tool

    @classmethod
    def using(cls, tool):
        return cls(tool)

    def draw(self, title):
        return "{} drawn with {}".format(title, self.tool)
