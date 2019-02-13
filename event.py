# CS6352 project 1
# Zheheng Zhao
# zxz163930

class Event:
    def __init__(self, time = 0.0, kind = 0):
        self.time = time
        self.kind = kind
        self.next = None


class EventList:
    def __init__(self, event_count = 0, head = 0):
        self.event_count = event_count
        self.head = head

    #insert an event into an eventlist sorted by time index
    #time - the time at which the event takes place
    #kind - the kind of event
    def insert(self, time, kind):
        self.event_count += 1
        eptr = Event(time, kind)
        if self.head == 0:
            self.head = eptr
            eptr.next = 0
        elif self.head.time >= eptr.time:
            eptr.next = self.head
            self.head = eptr
        else:
            eindex = self.head
            while eindex.next != 0:
                if eindex.next.time < eptr.time:
                    eindex = eindex.next
                else:
                    break
            eptr.next = eindex.next
            eindex.next = eptr

    #return the event from the head of the eventlist
    def get(self):
        if self.event_count == 0:
            return 0
        else:
            self.event_count -= 1
            eptr = self.head
            self.head = self.head.next
            eptr.next = 0
            return eptr

    #clear all events from the eventlist
    def clear(self):
        while(self.head):
            eptr = self.head
            self.head = self.head.next
            eptr.next = 0
            del eptr
        self.event_count = 0

    #remove and return first event of given kind
    def remove(self, kind):
        if self.event_count == 0 or self.head == 0:
            return 0
        else:
            eptr_prev = 0
            eptr = self.head

            while(eptr):
                if eptr.kind == kind:
                    if eptr_prev == 0:
                        self.head = eptr.next
                        eptr.next = 0
                        return eptr
                    else:
                        eptr_prev.next = eptr.next
                        eptr.next = 0
                        return eptr
                else:
                    eptr_prev = eptr
                    eptr = eptr.next
            return 0