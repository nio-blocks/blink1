from blink1.blink1 import Blink1 as B1
from nio.metadata.properties.expression import ExpressionProperty
from nio.metadata.properties.object import ObjectProperty
from nio.metadata.properties.holder import PropertyHolder
from nio.common.block.base import Block
from nio.common.discovery import Discoverable, DiscoverableType


class Color(PropertyHolder):
    red = ExpressionProperty(title='Red', default='0')
    green = ExpressionProperty(title='Green', default='0')
    blue = ExpressionProperty(title='Blue', default='0')


@Discoverable(DiscoverableType.block)
class Blink1(Block):

    """ This is the Example block. Put a brief description here. """

    fade_milliseconds = ExpressionProperty(title='Time to fade (ms)',
                                           default='1000')
    color = ObjectProperty(Color, title='Color', default=Color())

    def __init__(self):
        super().__init__()
        self._blink1 = None

    def configure(self, context):
        super().configure(context)
        self._logger.debug('Connecting to Blink1')
        self._blink1 = B1()
        self._logger.debug('Connected to Blink1')

    def stop(self):
        try:
            self._blink1.close()
        except:
            self._logger.exception('Exception while closing Blink1 connection')
        super().stop()

    def process_signals(self, signals, input_id='default'):
        for signal in signals:
            try:
                fade_milliseconds = int(self.fade_milliseconds(signal))
                red = int(self.color.red(signal))
                green = int(self.color.green(signal))
                blue = int(self.color.blue(signal))
            except:
                self._logger.exception('Failed to evalue fade variables')
                continue
            try:
                self._logger.debug(
                    'Fading to ({}, {}, {}) over {} milliseconds'.format(
                        red, green, blue, fade_milliseconds))
                self._blink1.fade_to_rgb(fade_milliseconds, red, green, blue)
            except:
                self._logger.exception('Failed to fade Blink1')
