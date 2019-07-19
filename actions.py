from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa.core.events import AllSlotsReset
from rasa.core.events import Restarted

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
        closure=tracker.get_slot('closure')


        message = "\nSize: " + size + "\nField: " + field + "\nOrder: " + order + "\nCount:  " + count + "\nAmount: "+ amount + "\nTime: " + time + "\nTime1: " + time1 + "\nTime2: " + time2 + "\nRefrence time: " + refrence_time +"\nAll Reg: " + allreg + "\nReg1: " + reg1 + "\nReg2: " + reg2 +"\nClosure: " + closure    
        dispatcher.utter_message(message)

        if(size.isalpha()):
            size=size.lower()
        if(field.isalpha()):
            field=field.lower()
        if(order.isalpha()):
            order=order.lower()
        if(count.isalpha()):
            count=count.lower()
        if(amount.isalpha()):
            amount=amount.lower()
        if(time.isalpha()):
            time=time.lower()
        if(time1.isalpha()):
            time1=time1.lower()
        if(time2.isalpha()):
           time2=time2.lower()
        if(refrence_time.isalpha()):
           refrence_time=refrence_time.lower()
        if(allreg.isalpha()):
            allreg=allreg.lower()
        if(reg1.isalpha()):
           reg1=reg1.lower()
        if(reg2.isalpha()):
            reg2=reg2.lower()
        if(closure.isalpha()):
            closure=closure.lower()

                


        if(count!="" and amount!="" and time!=""):
            if(("npa" in amount) or ("npa" in count) or ("npas" in count) or ("npas") in amount):
                if(closure=="foreclosed"):
                    dispatcher.utter_message("call getNPAForeclosed(type:"+count+","+time+")")
                else:
                    dispatcher.utter_message("call getNPA(type:"+amount+","+time+")")
        elif(amount!=""):
            dispatcher.utter_message("call getTimeBasedLoan(type:"+amount+","+time+")")
        else:
            dispatcher.utter_message("call getTimeBasedLoan(type:"+count+","+time+")")


        if(refrence_time!=""):
            if(count!=""):
                dispatcher.utter_message("call getLiveLoans(type:"+count+",refrence_time:"+refrence_time+","+time+")")
            else:
                dispatcher.utter_message("call getLiveLoans(type:"+amount+",refrence_time:"+refrence_time+","+time+")")

        if(time1!="" or time2!=""):
            if(count!=""):
                dispatcher.utter_message("call timeBasedCompareLoans(type:"+count+",refrence_time:"+refrence_time+","+time+")")
            else:
                dispatcher.utter_message("call timeBasedCompareLoans(type:"+amount+",refrence_time:"+refrence_time+","+time+")")
            
        if(field!=""):
            if(allreg!=""):
                dispatcher.utter_message("call getSalesPerformance(order:"+order+",region:"+allreg+","+time+")")
            else:
                 dispatcher.utter_message("call getSalesPerformance(order:"+order+",region 1:"+reg1+",region 2:"+reg2+","+time+")")

        else:
            if(allreg==""):
                dispatcher.utter_message("call getRegionInfo(order:"+order+",region 1:"+reg1+",region 2:"+reg2+","+time+")")
            else:
                 dispatcher.utter_message("call getRegionInfo(order:"+order+",region:"+allreg+","+time+")")
              
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
        