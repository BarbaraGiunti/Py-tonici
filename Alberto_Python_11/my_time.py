#------------------------------------------------
# CLASSES AND MODULES
#------------------------------------------------

class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
            The values of mins and secs may be outside the range 0-59,
            but the resulting MyTime object will be normalized.
        """

        # Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600 # Split in h, m, s
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__( self )
        return "{0}:{1}:{2}".format( self.hours, self.minutes, self.seconds )

    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds() + other.to_seconds())

    def __sub__(self, other):
        return MyTime(0, 0, self.to_seconds() - other.to_seconds())

    def __lt__( self, other ) :
        if self.to_seconds() < other.to_seconds() :
            return True
        return False

    def __gt__( self, other ) :
        if self.to_seconds() > other.to_seconds() :
            return True
        return False

    def __eq__( self, other ) :
        if self.to_seconds() == other.to_seconds() :
            return True
        return False

    def increment( self, secs ):
        tot_secs = secs + self.to_seconds()
        if tot_secs > 0 :
            self = MyTime(0, 0, tot_secs)
        return self = MyTime(0, 0, 0)

    def to_seconds(self):
        """ Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

    def between( self, t1, t2 ) :
        if ( t1 == obj ) or ( t1 < self and self < t2 )
            return True
        return False

#-----------------------------------------------
# FUNCTIONS
#-----------------------------------------------

def add_time(t1, t2):
    secs = t1.to_seconds() + t2.to_seconds()
    return MyTime(0, 0, secs)

#-----------------------------------------------
# SCRIPT
#-----------------------------------------------