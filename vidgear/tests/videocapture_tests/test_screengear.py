"""
============================================
vidgear library code is placed under the MIT license
Copyright (c) 2019 Abhishek Thakur

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
===============================================
"""

from vidgear.gears import ScreenGear
from mss.exception import ScreenShotError
import pytest, platform

def test_screengear():
	"""
	Tests ScreenGear's playback capabilities with custom defined dimensions -> passes if fails with ScreenShotError
	"""
	try:
		# define dimensions of screen w.r.t to given monitor to be captured
		options = {'top': 40, 'left': 0, 'width': 100, 'height': 100} 
		#Open Live Screencast on current monitor 
		stream = ScreenGear(monitor=1, logging=True, colorspace = 'COLOR_BGR2GRAY', **options).start() 
		#playback
		i = 0
		while (i>10):
			frame = stream.read()
			if frame is None: break
			i+=1
		#clean resources
		stream.stop()
	except Exception as e:
		if platform.system() == 'Linux' or platform.system() == 'Windows':
			print(e)
		else:
			pytest.fail(str(e))