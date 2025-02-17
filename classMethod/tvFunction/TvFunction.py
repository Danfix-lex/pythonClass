class TvFunction:
    def __init__(self):
        self.is_muted = None

    def _init_(self):
        self.is_on = False
        self.volume = 0
        self.channel = 1
        self.is_muted = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False
        self.is_muted = False

    def increase_volume(self):
        if self.is_on and self.volume < 100:
            self.is_muted = False
            self.volume = self.volume + 1

    def decrease_volume(self):
        if self.is_on and self.volume > 0:
            self.is_muted = False
            self.volume = self.volume - 1

    def channel_up(self):
        if self.is_on and self.channel <= 100:
            self.channel = self.channel + 1

    def channel_down(self):
        if self.is_on and self.channel > 1:
            self.channel = self.channel - 1

    def set_channel(self, channel):
        if self.is_on and 1 <= channel <= 100:
            self.channel = channel

    def mute(self):
        if self.is_on:
            self.is_muted = not self.is_muted