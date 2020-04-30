class SMS_store :

    def __init__( self, mess = (True,0,0,"") ) :
        if mess == (True,0,0,"") :
            self.msgs = []
        else:
            self.msgs = [ mess ]

    def __str__( self ):
        S = "------------------------------\n"
        for mess in self.msgs :
           S += "( {0}, {1} :\n {2} )\n\n".format( mess[1], mess[2], mess[3] )    
        S += "------------------------------\n"
        return S

    def message_count( self ) :
        # Returns the number of sms messages in my_inbox
        return len( self.msgs )

    def add_new_arrival( self, from_number, time_arrived, text_of_SMS ) :
        # Makes new SMS tuple, inserts it after other messages
        # in the store. When creating this message, its
        # has_been_viewed status is set False.
        self.msgs.append( ( False, from_number, time_arrived, text_of_SMS ) )

    def get_unread_indexes( self ) :
        # Returns list of indexes of all not-yet-viewed SMS messages
        idx = []
        for k in range( 0, len( self.msgs ) ) :
            if not( self.msgs[k][0] ) :
                idx.append( k )
        return idx

    def delete( self, idx ) :
        # Delete the message at index i
        if idx < 0 or idx >= self.message_count() :
            self.msgs.pop(idx)

    def get_message( self, idx ) :
        # Return (from_number, time_arrived, text_of_sms) for message[i]
        # Also change its state to "has been viewed".
        # If there is no message at position i, return None
        if idx < 0 or idx >= self.message_count() :
            return "None"
        else :
            import copy
            mess = copy.deepcopy( self.msgs[idx] )
            if not( mess[0] ) :
                up_mess = ( True, mess[1], mess[2], mess[3] )
                self.msgs.pop(idx)
                self.msgs.insert( idx, up_mess )
            return ( mess[1], mess[2], mess[3] )

    def clear( self ) :
        # Delete all messages from inbox
        for k in range( 0, len( self.msgs ) ) :
            self.msgs.pop()

mess1 = ( False, 123456789, 12.36, "prova" )

my_inbox = SMS_store()

my_inbox.add_new_arrival( mess1[1], mess1[2], mess1[3] )
my_inbox.add_new_arrival( 987654321, 23.41, "prova due" )
print( my_inbox.message_count() )

print( my_inbox.get_unread_indexes() )

print( my_inbox.get_message( 0 ) )

print( my_inbox.get_unread_indexes() )
my_inbox.clear()