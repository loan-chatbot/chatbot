from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa.core.events import AllSlotsReset
from rasa.core.events import Restarted
import re

class ActionGetNPA(Action):

    def name(self):
        return "action_get_getNPA"

    def run(self, dispatcher, tracker, domain):
        typo = tracker.get_slot('type')
        time = tracker.get_slot('time')
        dispatcher.utter_message(
                    "call getNPA(type:"+typo+","+time+")")

        return []

class ActionGetNPAForeclosed(Action):

    def name(self):
        return "action_get_getNPAForeclosed"

    def run(self, dispatcher, tracker, domain):
        typo = tracker.get_slot('type')
        time = tracker.get_slot('time')
        dispatcher.utter_message(
                    "call getNPAForeclosed(type:"+typo+","+time+")")

        return []

class ActionRestarted(Action):
    def name(self):
        return 'action_restarted'

    def run(self, dispatcher, tracker, domain):
        return[Restarted()]

class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'

    def run(self, dispatcher, tracker, domain):
        return[AllSlotsReset()]