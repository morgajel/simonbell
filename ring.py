#!/usr/bin/env python3

import os
from aiy.voice.audio import play_wav

RING_SOUND = os.path.dirname(os.path.abspath(__file__)) + "/bell.wav"
play_wav(RING_SOUND)
# TODO have google assistant say something.

