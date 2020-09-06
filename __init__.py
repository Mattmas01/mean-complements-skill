from mycroft import MycroftSkill, intent_file_handler


class MeanComplements(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('complements.mean.intent')
    def handle_complements_mean(self, message):
        self.speak_dialog('complements.mean')


def create_skill():
    return MeanComplements()

