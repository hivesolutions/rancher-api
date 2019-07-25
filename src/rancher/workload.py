#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Rancher API
# Copyright (c) 2008-2019 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2019 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import datetime

class WorkloadAPI(object):
    """
    The workload API endpoints used by the Rancher 2.x
    infra-structure.
    """

    def list_workloads(self, project, *args, **kwargs):
        url = self.base_url + "projects/%s/workloads" % project
        contents = self.get(url, **kwargs)
        data = contents["data"]
        return data

    def list_workloads_name(self, project, name):
        url = self.base_url + "projects/%s/workloads?name=%s" % (project, name)
        contents = self.get(url)
        data = contents["data"]
        return data

    def get_workload(self, project, id):
        url = self.base_url + "projects/%s/workloads/%s" % (project, id)
        contents = self.get(url)
        return contents

    def get_workload_safe(self, project, id):
        contents = self.list_workloads_name(project, id)
        if contents: return contents[0]
        return self.get_workload(project, id)

    def update_workload(self, project, id, payload = {}):
        url = self.base_url + "projects/%s/workloads/%s" % (project, id)
        contents = self.put(url, data_j = payload)
        return contents

    def upgrade_workload(self, project, id):
        workload = self.get_workload(project, id)
        current_date = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H-%M-%SZ")
        workload["annotations"]["cattle.io/timestamp"] = current_date
        self.update_workload(project, id, payload = workload)
        return workload
