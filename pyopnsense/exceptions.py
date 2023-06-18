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


class APIException(Exception):
    """Representation of the API exception."""

    def __init__(self, status_code=None, resp_body=None, *args, **kwargs):
        """Initialize the API exception."""
        self.resp_body = resp_body
        self.status_code = status_code
        message = kwargs.get("message", resp_body)
        super(APIException, self).__init__(message, *args, **kwargs)
