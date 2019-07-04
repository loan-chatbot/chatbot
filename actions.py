from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetHelp(Action):

    def name(self):
        return "action_get_help"

    
    def run(self, dispatcher, tracker, domain):
        size=field=order=""
        size = tracker.get_slot('size')
        field = tracker.get_slot('field')
        order = tracker.get_slot('order')
        message= "Size:" + size + "\nField: " + field + "\nOrder: " + order

        dispatcher.utter_message(message)

        return []
