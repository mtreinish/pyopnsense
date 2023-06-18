# Copyright 2018 Matthew Treinish
#
# This file is part of pyopnsense
#
# pyopnsense is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyopnsense is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyopnsense. If not, see <http://www.gnu.org/licenses/>.

import fixtures
import testtools


class TestCase(testtools.TestCase):
    def setUp(self):
        super(TestCase, self).setUp()
        stdout = self.useFixture(fixtures.StringStream("stdout")).stream
        self.useFixture(fixtures.MonkeyPatch("sys.stdout", stdout))
        stderr = self.useFixture(fixtures.StringStream("stderr")).stream
        self.useFixture(fixtures.MonkeyPatch("sys.stderr", stderr))
        self.useFixture(fixtures.LoggerFixture(nuke_handlers=False, level=None))
