from mycroft import MycroftSkill, intent_file_handler


class Welcome(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('welcome.intent')
    def handle_welcome(self, message):
        self.speak_dialog('welcome')


def create_skill():
    return Welcome()

