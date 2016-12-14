#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Rancher API
# Copyright (c) 2008-2016 Hive Solutions Lda.
#
# This file is part of Hive Rancher API.
#
# Hive Rancher API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Rancher API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Rancher API. If not, see <http://www.apache.org/licenses/>.

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2016 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

import base

class RancherApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "rancher",
            *args, **kwargs
        )

    @appier.route("/", "GET")
    def index(self):
        return self.stacks()

    @appier.route("/stacks", "GET")
    def stacks(self):
        api = self.get_api()
        stacks = api.list_stacks()
        return stacks

    @appier.route("/services", "GET")
    def services(self):
        api = self.get_api()
        services = api.list_services()
        return services

    def get_api(self):
        api = base.get_api()
        return api

if __name__ == "__main__":
    app = RancherApp()
    app.serve()