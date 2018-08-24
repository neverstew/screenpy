class TakeNotes:

    def __init__(self, notepad=dict()):
        super(TakeNotes, self).__init__()
        self.notepad = notepad

    @classmethod
    def using(cls, notepad):
        return cls(notepad)

    def note(self, topic, content):
        self.notepad[topic] = content

    def read(self, topic):
        if topic in self.notepad:
            return self.notepad[topic]
        else:
            raise KeyError("{} not in notepad".format(topic))
