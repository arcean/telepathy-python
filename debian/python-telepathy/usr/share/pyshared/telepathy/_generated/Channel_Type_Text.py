# -*- coding: utf-8 -*-
# Generated from the Telepathy spec
""" Copyright © 2005-2009 Collabora Limited 
 Copyright © 2005-2009 Nokia Corporation 
 Copyright © 2006 INdT 

    This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
  
"""

import dbus.service


class ChannelTypeText(dbus.service.Interface):
    """\
      A channel type for sending and receiving messages in plain text,
        with no formatting. In future specifications, channels for sending
        and receiving messages that can be reduced to plain text (i.e.
        formatted text) should also have this type.

      When a message is received, an identifier is assigned and a
        Received signal emitted, and the message
        placed in a pending queue which can be inspected with
        ListPendingMessages. A client which has
        handled the message by showing it to the user (or equivalent) should
        acknowledge the receipt using the
        AcknowledgePendingMessages method,
        and the message will then be removed from the pending queue. Numeric
        identifiers for received messages may be reused over the lifetime of
        the channel.

      Each message has an associated 'type' value, which should be one
        of the values allowed by
        Channel_Text_Message_Type.

      Each message also has a flags value, which is a bitwise OR of the
        flags given in Channel_Text_Message_Flags.

      Sending messages can be requested using the
        Send method, which will return
        successfully and emit the Sent signal
        when the message has been delivered to the server, or return an error
        with no signal emission if there is a failure. If a message is sent but
        delivery of the message later fails, this is indicated with the
        SendError signal.

      On protocols where additional contacts cannot be invited into
        a one-to-one chat, or where a one-to-one chat is just a series of
        individual personal messages rather than being represented by some
        object on the server (i.e. most protocols), one-to-one chats should be
        represented by a Text channel with Handle_Type
        CONTACT.

      Named chat rooms whose identity can be saved and used again later
        (IRC channels, Jabber MUCs) are expected to be represented by Text
        channels with Handle_Type ROOM and the Group
        interface; they should usually also have the Properties interface.

      Unnamed, transient chat rooms defined only by their members (e.g. on
        MSN) are expected to be represented by Text channels with handle type
        0, handle 0, the Group
        interface, and optionally the Properties interface.

      On protocols where a conversation with a user is actually just
        a nameless chat room starting with exactly two members, to which
        more members can be invited, calling
        RequestChannel
        with type Text
        and handle type CONTACT should continue to succeed, but may return
        a channel with handle type 0, handle 0, the group interface,
        and the local and remote contacts in its members.

      If a channel of type Text is closed while it has pending messages,
        the connection manager MUST allow this, but SHOULD open a new,
        identical channel to deliver those messages, signalling it as a new
        channel with the
        NewChannel
        signal (with the suppress_handler parameter set to FALSE).

      If messages were sent on the old channel but the
        Sentsignal has not yet been emitted
        for those messages, the new channel SHOULD emit Sent for those
        messages when appropriate - it behaves like a continuation of the
        old channel.

      
        In effect, this turns this situation, in which a client
          is likely to lose messages:

        
          UI window is closed
          message arrives
          text channel emits Received
          UI calls Close on text channel before it has seen the
            Received signal
          text channel emits Closed and closes
        

        into something nearly equivalent to this situation, which is
          fine:

        
          UI window is closed
          UI calls Close on text channel
          text channel emits Closed and closes
          message arrives
          new text channel is created, connection emits NewChannel
          (the same or a different) UI handles it
        

        suppress_handler must be set to FALSE so the replacement channel
          will be handled by something.
      

      As a result, Text channels SHOULD implement Channel.Interface.Destroyable.

      
        This "respawning" behaviour becomes problematic if there is no
          suitable handler for Text channels, or if a particular message
          repeatedly crashes the Text channel handler; a channel dispatcher
          can't just Close() the channel in these situations, because
          it will come back.

        In these situations, the channel dispatcher needs a last-resort
          way to destroy the channel and stop it respawning. It could either
          acknowledge the messages itself, or use the Destroyable interface;
          the Destroyable interface has the advantage that it's not
          channel-type-dependent, so the channel dispatcher only has to
          understand one extra interface, however many channel types
          eventually need a distinction between Close and Destroy.
      

    """

    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Text', in_signature='au', out_signature='')
    def AcknowledgePendingMessages(self, IDs):
        """
        Inform the channel that you have handled messages by displaying them to
        the user (or equivalent), so they can be removed from the pending queue.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Text', in_signature='', out_signature='au')
    def GetMessageTypes(self):
        """
        Return an array indicating which types of message may be sent on this
        channel.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Text', in_signature='b', out_signature='a(uuuuus)')
    def ListPendingMessages(self, Clear):
        """
        List the messages currently in the pending queue, and optionally
        remove then all.
      
        """
        raise NotImplementedError
  
    @dbus.service.method('org.freedesktop.Telepathy.Channel.Type.Text', in_signature='us', out_signature='')
    def Send(self, Type, Text):
        """
        Request that a message be sent on this channel. When the message has
          been submitted for delivery, this method will return and the
          Sent signal will be emitted. If the
          message cannot be submitted for delivery, the method returns an error
          and no signal is emitted.

        This method SHOULD return before the Sent signal is
          emitted.

        
          When a Text channel implements the Messages
            interface, that "SHOULD" becomes a "MUST".
        
      
        """
        raise NotImplementedError
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Text', signature='')
    def LostMessage(self):
        """
        This signal is emitted to indicate that an incoming message was
        not able to be stored and forwarded by the connection manager
        due to lack of memory.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Text', signature='uuuuus')
    def Received(self, ID, Timestamp, Sender, Type, Flags, Text):
        """
        Signals that a message with the given id, timestamp, sender, type
        and text has been received on this channel. Applications that catch
        this signal and reliably inform the user of the message should
        acknowledge that they have dealt with the message with the
        AcknowledgePendingMessages method.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Text', signature='uuus')
    def SendError(self, Error, Timestamp, Type, Text):
        """
        Signals that an outgoing message has failed to send. The error
          will be one of the values from ChannelTextSendError.

        This signal should only be emitted for messages for which
          Sent has already been emitted and
          Send has already returned success.
      
        """
        pass
  
    @dbus.service.signal('org.freedesktop.Telepathy.Channel.Type.Text', signature='uus')
    def Sent(self, Timestamp, Type, Text):
        """
        Signals that a message has been submitted for sending.
      
        """
        pass
  