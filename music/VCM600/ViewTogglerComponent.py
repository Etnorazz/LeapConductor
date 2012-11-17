# emacs-mode: -*- python-*-
import Live
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.ButtonElement import ButtonElement
class ViewTogglerComponent(ControlSurfaceComponent):
    __module__ = __name__
    __doc__ = ' Component that can toggle the device chain- and clip view of a number of tracks '

    def __init__(self, num_tracks):
        assert (num_tracks > 0)
        ControlSurfaceComponent.__init__(self)
        self._num_tracks = num_tracks
        self._chain_buttons = None
        self._clip_buttons = None
        self._ignore_track_selection = False
        self.application().view.add_is_view_visible_listener('Detail', self._on_detail_view_changed)
        self.application().view.add_is_view_visible_listener('Detail/Clip', self._on_views_changed)



    def disconnect(self):
        self.application().view.remove_is_view_visible_listener('Detail', self._on_detail_view_changed)
        self.application().view.remove_is_view_visible_listener('Detail/Clip', self._on_views_changed)
        if (self._chain_buttons != None):
            for button in self._chain_buttons:
                button.unregister_value_notification(self._chain_value)

            self._chain_buttons = None
        if (self._clip_buttons != None):
            for button in self._clip_buttons:
                button.unregister_value_notification(self._clip_value)

            self._clip_buttons = None



    def set_buttons(self, chain_buttons, clip_buttons):
        assert ((chain_buttons == None) or (isinstance(chain_buttons, tuple) and (len(chain_buttons) == self._num_tracks)))
        assert ((clip_buttons == None) or (isinstance(clip_buttons, tuple) and (len(clip_buttons) == self._num_tracks)))
        do_update = False
        if (self._chain_buttons != None):
            for button in self._chain_buttons:
                button.unregister_value_notification(self._chain_value)

        self._chain_buttons = chain_buttons
        if (self._chain_buttons != None):
            do_update = True
            for button in self._chain_buttons:
                assert isinstance(button, ButtonElement)
                button.register_value_notification(self._chain_value, identify_sender=True)

        if (self._clip_buttons != None):
            for button in self._clip_buttons:
                button.unregister_value_notification(self._clip_value)

        self._clip_buttons = clip_buttons
        if (self._clip_buttons != None):
            do_update = True
            for button in self._clip_buttons:
                assert isinstance(button, ButtonElement)
                button.register_value_notification(self._clip_value, identify_sender=True)

        self.on_selected_track_changed()
        if do_update:
            self._rebuild_callback()



    def on_selected_track_changed(self):
        self._update_buttons()



    def on_enabled_changed(self):
        self.update()



    def update(self):
        if self.is_enabled():
            self._update_buttons()
        else:
            if (self._chain_buttons != None):
                for button in self._chain_buttons:
                    button.turn_off()

            if (self._clip_buttons != None):
                for button in self._clip_buttons:
                    button.turn_off()




    def _on_detail_view_changed(self):
        self._update_buttons()



    def _on_views_changed(self):
        self._update_buttons()



    def _update_buttons(self):
        for index in range(self._num_tracks):
            if ((len(self.song().tracks) > index) and ((self.song().tracks[index] == self.song().view.selected_track) and self.application().view.is_view_visible('Detail'))):
                if self.application().view.is_view_visible('Detail/DeviceChain'):
                    self._chain_buttons[index].turn_on()
                else:
                    self._chain_buttons[index].turn_off()
                if self.application().view.is_view_visible('Detail/Clip'):
                    self._clip_buttons[index].turn_on()
                else:
                    self._clip_buttons[index].turn_off()
            else:
                if (self._chain_buttons != None):
                    self._chain_buttons[index].turn_off()
                if (self._clip_buttons != None):
                    self._clip_buttons[index].turn_off()




    def _chain_value(self, value, sender):
        assert (sender in self._chain_buttons)
        if ((not sender.is_momentary()) or (value != 0)):
            index = list(self._chain_buttons).index(sender)
            self._ignore_track_selection = True
            if (len(self.song().tracks) > index):
                if (self.song().view.selected_track != self.song().tracks[index]):
                    self.song().view.selected_track = self.song().tracks[index]
                    if ((not self.application().view.is_view_visible('Detail')) or (not self.application().view.is_view_visible('Detail/DeviceChain'))):
                        self.application().view.show_view('Detail')
                        self.application().view.show_view('Detail/DeviceChain')
                elif (self.application().view.is_view_visible('Detail/DeviceChain') and self.application().view.is_view_visible('Detail')):
                    self.application().view.hide_view('Detail')
                else:
                    self.application().view.show_view('Detail')
                    self.application().view.show_view('Detail/DeviceChain')
            self._ignore_track_selection = False



    def _clip_value(self, value, sender):
        assert (sender in self._clip_buttons)
        if ((not sender.is_momentary()) or (value != 0)):
            index = list(self._clip_buttons).index(sender)
            self._ignore_track_selection = True
            if (len(self.song().tracks) > index):
                if (self.song().view.selected_track != self.song().tracks[index]):
                    self.song().view.selected_track = self.song().tracks[index]
                    if ((not self.application().view.is_view_visible('Detail')) or (not self.application().view.is_view_visible('Detail/Clip'))):
                        self.application().view.show_view('Detail')
                        self.application().view.show_view('Detail/Clip')
                elif (self.application().view.is_view_visible('Detail/Clip') and self.application().view.is_view_visible('Detail')):
                    self.application().view.hide_view('Detail')
                else:
                    self.application().view.show_view('Detail')
                    self.application().view.show_view('Detail/Clip')
            self._ignore_track_selection = False




# local variables:
# tab-width: 4
