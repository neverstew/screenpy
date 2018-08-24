from ..abilities.draw_pictures import DrawPictures


class DrawPicture:

    def __init__(self, title):
        self.title = title

    @classmethod
    def titled(cls, title):
        return cls(title)

    def perform_as(self, actor):
        return actor.ability_to(DrawPictures).draw(self.title)
