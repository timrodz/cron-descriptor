# Copyright (C) 2017 Adam Schubert <adam.schubert@sg1-game.net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import locale
import tests.TestCase as TestCase
from cron_descriptor import Options, DescriptionTypeEnum, ExpressionDescriptor, CasingTypeEnum


class TestLocale(TestCase.TestCase):
    def test_default(self):
        options = Options()
        options.locale = 'de_DE'
        options.use_24hour_time_format = True
        self.assertEqual(
            "jede Minute",
            ExpressionDescriptor("* * * * *", options).get_description())