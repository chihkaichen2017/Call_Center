## Coding Dojo Assignment: Call Center
import time

class callClass(object):
    id_counter = 0

    def __init__(self,callerName,callerPhoneNumer,reasonForCall):
        self.callerName = callerName
        self.callerPhoneNumer = callerPhoneNumer
        self.reasonForCall = reasonForCall

        self.timeOfCall = time.clock()

        callClass.id_counter +=1 # each callClass instance get unique id in the blueprint
        self.id = callClass.id_counter

    def display(self):
        print "-----------------------------"
        print "id = {}".format(self.id)
        print "Caller Name = {}".format(self.callerName)
        print "Caller Phone Number = {}".format(self.callerPhoneNumer)
        print "Time of Call = {}".format(self.timeOfCall)
        print "Reason for Call = {}".format(self.reasonForCall)

class callCenter(object):
        def __init__(self):
            self.calls = [] # bookkeeping of the calls: a list of objects
            self.queueSize = len(self.calls)

        def add(self,x):
            self.calls.append(x) #update call list
            self.queueSize = len(self.calls)
            return self

        def remove(self): # FCFS no preemptive mechanism
            self.calls.pop(0) # remove a specific index=0 which was in service
            self.queueSize = len(self.calls)
            return self

        def info(self):
            print "---------------------------------------------"
            print "------- Call Center Information -------------"
            print "---------------------------------------------"
            for i in self.calls:
                print i.callerName, i.callerPhoneNumer
                #print "Name = {}, Phone Numer = {}".format(i.callerName,i.callerPhoneNumber)
            return self

        def removeByNumber(self,no):
            found = False
            for j,i in enumerate(self.calls):
                if i.callerPhoneNumer == no:
                    self.calls.pop(j)
                    found = True

            if found == False:
                print "---  There is no call with this phone number in the queue at the call center.  ---"
            else:
                self.queueSize = len(self.calls) # updating queueSize
                print "---  The queue is updated by removing the call with phone number = {}.  ---".format(no)
            return self


call_1 = callClass('John',9999999999,'test')
call_1.display()

call_2 = callClass('Jim',1234567890,'fun')
call_2.display()

call_3 = callClass('Jeffrey',1112223333,'play')
call_3.display()

center = callCenter()
center.add(call_1).info().add(call_2).info().add(call_3).info().remove().info().add(call_1).info().removeByNumber(9999999999).info()
