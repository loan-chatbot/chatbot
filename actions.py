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
            "call getNPA(type:"+typo+", time_string:"+str(time)+")")

        return []


class ActionGetNPAForeclosed(Action):

    def name(self):
        return "action_get_getNPAForeclosed"

    def run(self, dispatcher, tracker, domain):
        typo = tracker.get_slot('type')
        time = tracker.get_slot('time')
        dispatcher.utter_message(
            "call getNPAForeclosed(type:"+typo+", time_string:"+str(time)+")")

        return []


class ActionGetTimeBasedLoanDisbursed(Action):

    def name(self):
        return "action_get_getTimeBasedLoanDisbursed"

    def run(self, dispatcher, tracker, domain):
        typo = tracker.get_slot('type')
        time = tracker.get_slot('time')
        dispatcher.utter_message(
            "call getTimeBasedLoanDisbursed(type:"+typo+", time_string:"+str(time)+")")

        return []


class ActionGetRegionInfo(Action):

    def name(self):
        return "action_get_getRegionInfo"

    def run(self, dispatcher, tracker, domain):
        typo = tracker.get_slot('type')
        region = tracker.get_slot('region')
        time = tracker.get_slot('time')
        dispatcher.utter_message(
            "call getRegionInfo(type:"+typo+", region:"+region+", time_string:"+str(time)+")")
        return []


class ActionGetSalesPerformance(Action):

    def name(self):
        return "action_get_getSalesPerformance"

    def run(self, dispatcher, tracker, domain):
        typo = tracker.get_slot('type')
        region = tracker.get_slot('region')
        time = tracker.get_slot('time')
        order = tracker.get_slot('order')
        dispatcher.utter_message(
            "call getSalesPerformance(type:"+typo+", region:"+region+", time_string:"+str(time) + ", order:"+order+")")

        return []


class ActionGetMonthlySalesPerformance(Action):

    def name(self):
        return "action_get_getMonthlySalesPerformance"

    def run(self, dispatcher, tracker, domain):
        typo = tracker.get_slot('type')
        time = tracker.get_slot('time')
        person = tracker.get_slot('PERSON')
        dispatcher.utter_message(
            "call getMonthlySalesPerformance(type:"+typo+", time_string:"+str(time) + ", PERSON:"+person+")")

        return []

class ActionGetLiveLoans(Action):

        def name(self):
            return "action_get_getLiveLoans"
    
        def run(self, dispatcher, tracker, domain):
            typo = tracker.get_slot('type')
            time = tracker.get_slot('time')
            ref_time = tracker.get_slot('ref_time')
            dispatcher.utter_message(
                "call getLiveLoans(type:"+typo+", time_string:"+str(time) + ", refrence_time:"+ref_time+")")
    
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
