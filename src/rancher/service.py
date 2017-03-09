#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Rancher API
# Copyright (c) 2008-2017 Hive Solutions Lda.
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

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2017 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import time

class ServiceApi(object):

    def list_services(self, *args, **kwargs):
        url = self.base_url + "services"
        contents = self.get(
            url,
            **kwargs
        )
        data = contents["data"]
        return data

    def list_services_name(self, name):
        url = self.base_url + "services?name=%s" % name
        contents = self.get(url)
        data = contents["data"]
        return data

    def get_service(self, id):
        url = self.base_url + "services/%s" % id
        contents = self.get(url)
        return contents

    def update_service(self, id, payload = {}):
        url = self.base_url + "services/%s" % id
        contents = self.put(url, data_j = payload)
        data = contents["data"]
        return data

    def upgrade_service(
        self,
        id,
        batch_size = 1,
        interval = 2000,
        full_upgrade = True,
        try_finish = True,
        launch_config = None
    ):
        url = self.base_url + "services/%s?action=upgrade" % id
        if try_finish: self._service_try_finish(id)
        if launch_config == None: launch_config = self._service_launch_config(id)
        contents = self.post(
            url,
            data_j = dict(
                inServiceStrategy = dict(
                    batchSize = batch_size,
                    intervalMillis = interval,
                    fullUpgrade = full_upgrade,
                    launchConfig = launch_config,
                    secondaryLaunchConfigs = []
                )
            )
        )
        data = contents["data"]
        return data

    def finish_upgrade_service(self, id):
        url = self.base_url + "services/%s?action=finishupgrade" % id
        contents = self.post(url)
        data = contents["data"]
        return data

    def rollback_service(self, id):
        url = self.base_url + "services/%s?action=rollback" % id
        contents = self.post(url)
        data = contents["data"]
        return data

    def restart_service(self, id, batch_size = 1, interval = 2000):
        url = self.base_url + "services/%s?action=restart" % id
        contents = self.post(
            url,
            data_j = dict(
                rollingRestartStrategy = dict(
                    batchSize = batch_size,
                    intervalMillis = interval
                )
            )
        )
        data = contents["data"]
        return data

    def _service_try_finish(self, id, timeout = 5.0):
        try: self.finish_upgrade_service(id)
        except: pass
        else: time.sleep(timeout)

    def _service_launch_config(self, id):
        service = self.get_service(id)
        data = service.get("data", {})
        fields = data.get("fields", {})
        launch_config = fields.get("launchConfig", {})
        return launch_config

    def _service_image_uuid(self, id):
        launch_config = self._service_launch_config(id)
        image_uuid = launch_config.get("imageUuid", None)
        return image_uuid
