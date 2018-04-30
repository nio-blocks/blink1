from unittest.mock import patch

from nio.testing.block_test_case import NIOBlockTestCase
from nio.signal.base import Signal

from ..blink1_block import Blink1


class TestBlink1(NIOBlockTestCase):

    @patch(Blink1.__module__ + '.B1')
    def test_defaults(self, b1):
        blk = Blink1()
        self.configure_block(blk, {})
        b1.assert_called_once_with()
        blk.start()
        blk.process_signals([Signal()])
        blk._blink1.fade_to_color.assert_called_once_with(1000, 'blue')
        blk.stop()
        blk._blink1.close.assert_called_once_with()
        self.assert_num_signals_notified(0)

    @patch(Blink1.__module__ + '.B1')
    def test_expresssion_props(self, b1):
        blk = Blink1()
        self.configure_block(blk,
                             {'color': '{{$color}}',
                              'fade_milliseconds': '{{$ms}}'
                              }
                             )
        b1.assert_called_once_with()
        blk.start()
        blk.process_signals([Signal({'ms': 100, 'color': 'blue'})])
        blk._blink1.fade_to_color.assert_called_once_with(100, 'blue')
        blk.stop()
        blk._blink1.close.assert_called_once_with()
        self.assert_num_signals_notified(0)

    @patch(Blink1.__module__ + '.B1')
    def test_multiple_sigs(self, b1):
        blk = Blink1()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal(), Signal()])
        self.assertEqual(2, blk._blink1.fade_to_color.call_count)
        blk.stop()
        blk._blink1.close.assert_called_once_with()
        self.assert_num_signals_notified(0)
