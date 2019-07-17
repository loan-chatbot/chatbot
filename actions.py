from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetHelp(Action):

    def name(self):
        return "action_get_help"

    
    def run(self, dispatcher, tracker, domain): 
        size = tracker.get_slot('size') 
        field = tracker.get_slot('field')
        order = tracker.get_slot('order') 
        count = tracker.get_slot('count') 
        amount = tracker.get_slot('amount') 
        time = tracker.get_slot('time') 
        time1 = tracker.get_slot('time1') 
        time2 = tracker.get_slot('time2') 
        refrence_time = tracker.get_slot('refrence_time') 
        allreg = tracker.get_slot('allreg') 
        reg1 = tracker.get_slot('reg1') 
        reg2 = tracker.get_slot('reg2') 
        
        
        dispatcher.utter_message(size)
        dispatcher.utter_message(field)
        dispatcher.utter_message(count)
        dispatcher.utter_message(amount)
        dispatcher.utter_message(order)
        dispatcher.utter_message(time)
        dispatcher.utter_message(time1)
        dispatcher.utter_message(time2)
        dispatcher.utter_message(refrence_time)
        dispatcher.utter_message(reg1)
        dispatcher.utter_message(allreg)
        dispatcher.utter_message(reg2)
        

        return []