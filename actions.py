from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa.core.events import AllSlotsReset
from rasa.core.events import Restarted
import re

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
        person=tracker.get_slot('PERSON')


        message = "\nSize: " + size + "\nField: " + field + "\nOrder: " + order + "\nCount:  " + count + "\nAmount: "+ amount + "\nTime: " + time + "\nTime1: " + time1 + "\nTime2: " + time2 + "\nRefrence time: " + refrence_time +"\nAll Reg: " + allreg + "\nReg1: " + reg1 + "\nReg2: " + reg2 +"\nClosure: " + closure +"\nPerson:" + person  
        dispatcher.utter_message(message)

        pattern= re.compile(r'\s+')
        amount=re.sub(pattern,'',amount)
        count=re.sub(pattern,'',count)
        time=re.sub(pattern,'',time)
        time1=re.sub(pattern,'',time1)
        time2=re.sub(pattern,'',time2)
        field=re.sub(pattern,'',field)

        if((size.isalpha()) == True):
            size=size.lower()
        if((field.isalpha()) == True):
            field=field.lower()
        if((order.isalpha()) == True):
           order=order.lower()
        if((count.isalpha()) == True):
           count= count.lower()
        if((amount.isalpha()) == True):
           amount=amount.lower()
        if((time.isalpha()) == True):
           time= time.lower()
        if((time1.isalpha()) == True):
           time1= time1.lower()
        if((time2.isalpha()) == True):
          time2= time2.lower()
        if((refrence_time.isalpha()) == True):
          refrence_time= refrence_time.lower()
        if((allreg.isalpha()) == True):
           allreg= allreg.lower()
        if((reg1.isalpha()) == True):
          reg1=reg1.lower()
        if((reg2.isalpha()) == True):
            reg2=reg2.lower()
        if((closure.isalpha()) == True):
           closure= closure.lower()
        if((person.isalpha()) == True):
           person= person.lower()
        

                


        if(count!="" or amount!="" and time!=""):
            if(("npa" in amount) or ("npa" in count) or ("npas" in count) or ("npas") in amount):
                if(closure=="foreclosed"):
                    dispatcher.utter_message("call getNPAForeclosed(type:"+count+","+time+")")
                else:
                    dispatcher.utter_message("call getNPA(type:"+amount+","+time+")")
            elif(amount!="" and time!="" and refrence_time=="" and time1=="" and time2=="" and field==""):
                dispatcher.utter_message("call getTimeBasedLoanDisbursed(type:"+amount+","+time+")")
            elif(count!="" and time!="" and refrence_time=="" and time1=="" and time2=="" and field==""):
                dispatcher.utter_message("call getTimeBasedLoanDisbursed(type:"+count+","+time+")")


        if(refrence_time!=""):
            if(count!=""):
                dispatcher.utter_message("call getLiveLoans(type:"+count+",refrence_time:"+refrence_time+","+time+")")
            elif(amount!=""):
                dispatcher.utter_message("call getLiveLoans(type:"+amount+",refrence_time:"+refrence_time+","+time+")")

        if(time1!="" or time2!=""):
            if(count!=""):
                dispatcher.utter_message("call timeBasedCompareLoans(type:"+count+",refrence_time:"+refrence_time+","+time+")")
            elif(amount!=""):
                dispatcher.utter_message("call timeBasedCompareLoans(type:"+amount+",refrence_time:"+refrence_time+","+time+")")
            
        if(field!=""):
            if(allreg!=""):
                dispatcher.utter_message("call getSalesPerformance(order:"+order+",region:"+allreg+","+time+")")
            elif(reg1!="" or reg2!=""):
                dispatcher.utter_message("call getSalesPerformance(order:"+order+",region 1:"+reg1+",region 2:"+reg2+","+time+")")

        else:
            if(reg1!="" or reg2!=""):
                dispatcher.utter_message("call getRegionInfo(order:"+order+",region 1:"+reg1+",region 2:"+reg2+","+time+")")
            elif(allreg!=""):
                dispatcher.utter_message("call getRegionInfo(order:"+order+",region:"+allreg+","+time+")")

        if("month" in time and "performance" in count and person!=""):
            dispatcher.utter_message("call getMonthlySalesPerformance(Type:"+count+","+field+":"+ person+","+time+")")
              
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
        