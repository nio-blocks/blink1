from collections import defaultdict
from unittest.mock import MagicMock, patch
from blink1.blink1 import Blink1 as B1
from nio.util.support.block_test_case import NIOBlockTestCase
from nio.common.signal.base import Signal
from ..blink1_block import Blink1


class TestBlink1(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        # This will keep a list of signals notified for each output
        self.last_notified = defaultdict(list)

    def signals_notified(self, signals, output_id='default'):
        self.last_notified[output_id].extend(signals)

    @patch(Blink1.__module__ + '.B1')
    def test_defaults(self, b1):
        blk = Blink1()
        self.configure_block(blk, {})
        b1.assert_called_once_with()
        blk.start()
        blk.process_signals([Signal()])
        blk._blink1.fade_to_rgb.assert_called_once_with(1000, 0, 0, 0)
        blk.stop()
        blk._blink1.close.assert_called_once_with()
        self.assert_num_signals_notified(0)

    @patch(Blink1.__module__ + '.B1')
    def test_expresssion_props(self, b1):
        blk = Blink1()
        self.configure_block(blk,
                             {'color':
                              {'red': '{{100}}',
                               'green': '{{"100"}}',
                               'blue': '{{$blue}}'
                               },
                              'fade_milliseconds': '{{$ms}}'
                              }
                             )
        b1.assert_called_once_with()
        blk.start()
        blk.process_signals([Signal({'ms': 100, 'blue': '100'})])
        blk._blink1.fade_to_rgb.assert_called_once_with(100, 100, 100, 100)
        blk.stop()
        blk._blink1.close.assert_called_once_with()
        self.assert_num_signals_notified(0)

    @patch(Blink1.__module__ + '.B1')
    def test_multiple_sigs(self, b1):
        blk = Blink1()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals([Signal(), Signal()])
        self.assertEqual(2, blk._blink1.fade_to_rgb.call_count)
        blk.stop()
        blk._blink1.close.assert_called_once_with()
        self.assert_num_signals_notified(0)
