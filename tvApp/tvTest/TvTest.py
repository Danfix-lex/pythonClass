import unittest
from tvFunction import TvFunction

class TvTest(unittest.TestCase):
    def setUp(self):
        self.tv = TvFunction()

    def test_power_on(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

    def test_power_off(self):
        self.tv.turn_on()
        self.tv.turn_off()
        self.assertFalse(self.tv.is_on)

    def test_increase_volume(self):
        self.tv.turn_on()
        inital_volume = self.tv.volume
        self.tv.increase_volume()
        self.assertEqual(self.tv.volume, inital_volume + 1)

    def test_decrease_volume(self):
        self.tv.turn_on()
        self.tv.volume = 10
        self.tv.decrease_volume()
        self.assertEqual(self.tv.volume,9)

    def test_that_volume_does_not_change_when_off(self):
        inital_volume = self.tv.volume
        self.tv.increase_volume()
        self.assertEqual(self.tv.volume, inital_volume)

    def test_that_channel_can_go_up(self):
        self.tv.turn_on()
        inital_channel = self.tv.channel
        self.tv.channel_up()
        self.assertEqual(self.tv.channel, inital_channel + 1)

    def test_that_channel_can_go_down(self):
        self.tv.turn_on()
        self.tv.channel = 5
        self.tv.channel_down()
        self.assertEqual(self.tv.channel,4)

    def test_that_channel_cannot_change_when_off(self):
        self.tv.turn_off()
        inital_channel = self.tv.channel
        self.tv.channel_up()
        self.assertEqual(self.tv.channel, inital_channel)

    def test_set_channel(self):
        self.tv.turn_on()
        self.tv.set_channel(10)
        self.assertEqual(self.tv.channel, 10)

    def test_that_set_channel_fails_when_off(self):
        self.tv.turn_off()
        inital_channel = self.tv.channel
        self.tv.set_channel(10)
        self.assertEqual(self.tv.channel, inital_channel)

    def test_that_television_can_be_muted(self):
        self.tv.turn_on()
        self.tv.mute()
        self.assertTrue(self.tv.is_muted)

        self.tv.mute()
        self.assertFalse(self.tv.is_muted)

    def test_that_television_can_be_mute_when_off(self):
        self.tv.turn_off()
        self.tv.mute()
        self.assertFalse(self.tv.is_muted)

    def test_unmuted_when_volume_changes(self):
        self.tv.turn_on()
        self.tv.mute()
        self.assertTrue(self.tv.is_muted)

        self.tv.increase_volume()
        self.assertFalse(self.tv.is_muted)

        self.tv.mute()
        self.assertTrue(self.tv.is_muted)

        self.tv.decrease_volume()
        self.assertFalse(self.tv.is_muted)
if __name__ == '__main__':
    unittest.main()