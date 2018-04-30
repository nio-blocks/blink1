from blink1.blink1 import Blink1 as B1

from nio.properties import (Property, StringProperty, PropertyHolder,
                            VersionProperty)
from nio import TerminatorBlock


class Blink1(TerminatorBlock):

    """ Control a blink(1) dongle. """

    fade_milliseconds = Property(title='Time to fade (ms)',
                                 default='1000')
    color = StringProperty(title='Color', default='blue')
    version = VersionProperty("2.0.0")

    def __init__(self):
        super().__init__()
        self._blink1 = None

    def configure(self, context):
        super().configure(context)
        self.logger.debug('Connecting to Blink1')
        self._blink1 = B1()
        self.logger.debug('Connected to Blink1')

    def stop(self):
        try:
            self._blink1.close()
        except:
            self.logger.exception('Exception while closing Blink1 connection')
        super().stop()

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            try:
                fade_milliseconds = int(self.fade_milliseconds(signal))
                color = str(self.color(signal))
            except:
                self.logger.exception('Failed to evalue fade variables')
                continue
            try:
                self.logger.debug(
                    'Fading to {} over {} milliseconds'.format(
                        color, fade_milliseconds))
                self._blink1.fade_to_color(fade_milliseconds, color)
            except:
                self.logger.exception('Failed to fade Blink1')
