from mycroft import MycroftSkill, intent_file_handler


class Translator(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('translator.intent')
    def handle_translator(self, message):
        self.speak_dialog('translator')


def create_skill():
    return Translator()

