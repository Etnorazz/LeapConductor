# emacs-mode: -*- python-*-
from MackieControl.consts import *
from MackieControl.MainDisplay import MainDisplay
from MackieControl.ChannelStrip import ChannelStrip
import Live
class MackieControlXT:
    __module__ = __name__
    __doc__ = "Extension for a Mackie Control. \n     Only works hand in hand with a 'main' Mackie Control as master\n  "

    def __init__(self, c_instance):
        self._MackieControlXT__c_instance = c_instance
        self._MackieControlXT__components = []
        self._MackieControlXT__main_display = MainDisplay(self)
        self._MackieControlXT__components.append(self._MackieControlXT__main_display)
        self._MackieControlXT__channel_strips = [ ChannelStrip(self, i) for i in range(NUM_CHANNEL_STRIPS) ]
        for s in self._MackieControlXT__channel_strips:
            self._MackieControlXT__components.append(s)

        self._MackieControlXT__mackie_control_main = None



    def disconnect(self):
        for c in self._MackieControlXT__components:
            c.destroy()




    def connect_script_instances(self, instanciated_scripts):
        pass


    def is_extension(self):
        return True



    def mackie_control_main(self, mackie_control_main):
        return self._MackieControlXT__mackie_control_main



    def set_mackie_control_main(self, mackie_control_main):
        self._MackieControlXT__mackie_control_main = mackie_control_main



    def channel_strips(self):
        return self._MackieControlXT__channel_strips



    def main_display(self):
        return self._MackieControlXT__main_display



    def shift_is_pressed(self):
        return self._MackieControlXT__mackie_control_main.shift_is_pressed()



    def option_is_pressed(self):
        return self._MackieControlXT__mackie_control_main.option_is_pressed()



    def control_is_pressed(self):
        return self._MackieControlXT__mackie_control_main.control_is_pressed()



    def alt_is_pressed(self):
        return self._MackieControlXT__mackie_control_main.alt_is_pressed()



    def application(self):
        return Application.application()



    def song(self):
        return self._MackieControlXT__c_instance.song()



    def handle(self):
        return self._MackieControlXT__c_instance.handle()



    def refresh_state(self):
        for c in self._MackieControlXT__components:
            c.refresh_state()




    def request_rebuild_midi_map(self):
        self._MackieControlXT__c_instance.request_rebuild_midi_map()



    def build_midi_map(self, midi_map_handle):
        for s in self._MackieControlXT__channel_strips:
            s.build_midi_map(midi_map_handle)

        for i in (channel_strip_switch_ids + fader_touch_switch_ids):
            Live.MidiMap.forward_midi_note(self.handle(), midi_map_handle, 0, i)




    def update_display(self):
        for c in self._MackieControlXT__components:
            c.on_update_display_timer()




    def send_midi(self, midi_event_bytes):
        self._MackieControlXT__c_instance.send_midi(midi_event_bytes)



    def receive_midi(self, midi_bytes):
        if (((midi_bytes[0] & 240) == NOTE_ON_STATUS) or ((midi_bytes[0] & 240) == NOTE_OFF_STATUS)):
            channel = (midi_bytes[0] & 15)
            note = midi_bytes[1]
            velocity = midi_bytes[2]
            if (note in range(SID_FIRST, (SID_LAST + 1))):
                if (note in (channel_strip_switch_ids + fader_touch_switch_ids)):
                    for s in self._MackieControlXT__channel_strips:
                        s.handle_channel_strip_switch_ids(note, velocity)

        elif ((midi_bytes[0] & 240) == CC_STATUS):
            channel = (midi_bytes[0] & 15)
            cc_no = midi_bytes[1]
            cc_value = midi_bytes[2]
            if (cc_no in range(FID_PANNING_BASE, (FID_PANNING_BASE + NUM_CHANNEL_STRIPS))):
                for s in self._MackieControlXT__channel_strips:
                    s.handle_vpot_rotation((cc_no - FID_PANNING_BASE), cc_value)




    def can_lock_to_devices(self):
        return False



    def suggest_input_port(self):
        return ''



    def suggest_output_port(self):
        return ''



    def suggest_map_mode(self, cc_no, channel):
        result = Live.MidiMap.MapMode.absolute
        if (cc_no in range(FID_PANNING_BASE, (FID_PANNING_BASE + NUM_CHANNEL_STRIPS))):
            result = Live.MidiMap.MapMode.relative_signed_bit
        return result




# local variables:
# tab-width: 4
