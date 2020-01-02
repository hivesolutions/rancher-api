#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Rancher API
# Copyright (c) 2008-2020 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import base

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

    @appier.route("/clusters", "GET")
    def clusters(self):
        api = self.get_api()
        clusters = api.list_clusters()
        return clusters

    @appier.route("/clusters/<str:id>", "GET")
    def cluster_safe(self, id):
        api = self.get_api()
        cluster = api.get_cluster_safe(id)
        return cluster

    @appier.route("/clusters/<str:cluster>/projects", "GET")
    def projects(self, cluster):
        api = self.get_api()
        cluster = api.get_cluster_safe(cluster)["id"]
        projects = api.list_projects(cluster)
        return projects

    @appier.route("/clusters/<str:cluster>/projects/<str:id>", "GET")
    def project_safe(self, cluster, id):
        api = self.get_api()
        cluster = api.get_cluster_safe(cluster)["id"]
        project = api.get_project_safe(cluster, id)
        return project

    @appier.route("/clusters/<str:cluster>/projects/<str:project>/workloads", "GET")
    def workloads(self, cluster, project):
        api = self.get_api()
        cluster = api.get_cluster_safe(cluster)["id"]
        project = api.get_project_safe(cluster, project)["id"]
        workloads = api.list_workloads(project)
        return workloads

    @appier.route("/clusters/<str:cluster>/projects/<str:project>/workloads/<str:id>", "GET")
    def workload_safe(self, cluster, project, id):
        api = self.get_api()
        cluster = api.get_cluster_safe(cluster)["id"]
        project = api.get_project_safe(cluster, project)["id"]
        workload = api.get_workload_safe(project, id)
        return workload

    @appier.route("/clusters/<str:cluster>/projects/<str:project>/workloads/<str:id>/upgrade", "GET")
    def upgrade_workload(self, cluster, project, id):
        api = self.get_api()
        cluster = api.get_cluster_safe(cluster)["id"]
        project = api.get_project_safe(cluster, project)["id"]
        id = api.get_workload_safe(project, id)["id"]
        workload = api.upgrade_workload(project, id)
        return workload

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

    @appier.route("/services/name/<str:name>", "GET")
    def services_name(self, name):
        api = self.get_api()
        services = api.list_services_name(name)
        return services

    @appier.route("/services/<str:id>", "GET")
    def _service(self, id):
        api = self.get_api()
        service = api.get_service(id)
        return service

    @appier.route("/services/<str:id>/safe", "GET")
    def service_safe(self, id):
        api = self.get_api()
        service = api.get_service_safe(id)
        return service

    @appier.route("/services/<str:id>/upgrade", ("GET", "POST"))
    def upgrade_service(self, id):
        api = self.get_api()
        service = api.upgrade_service(id)
        return service

    @appier.route("/services/<str:id>/finish_upgrade", ("GET", "POST"))
    def finish_upgrade_service(self, id):
        api = self.get_api()
        service = api.finish_upgrade_service(id)
        return service

    @appier.route("/services/<str:id>/rollback", ("GET", "POST"))
    def rollback_service(self, id):
        api = self.get_api()
        service = api.rollback_service(id)
        return service

    @appier.route("/services/<str:id>/restart", ("GET", "POST"))
    def restart_service(self, id):
        api = self.get_api()
        service = api.restart_service(id)
        return service

    def get_api(self):
        api = base.get_api()
        return api

if __name__ == "__main__":
    app = RancherApp()
    app.serve()
else:
    __path__ = []
