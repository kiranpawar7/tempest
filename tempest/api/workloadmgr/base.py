# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_log import log as logging

from tempest import config
import tempest.test

CONF = config.CONF
LOG = logging.getLogger(__name__)


class BaseWorkloadmgrTest(tempest.test.BaseTestCase):

    @classmethod
    def setup_clients(cls):
        super(BaseWorkloadmgrTest, cls).setup_clients()

    @classmethod
    def resource_setup(cls):
        super(BaseWorkloadmgrTest, cls).resource_setup()

    @classmethod
    def resource_cleanup(cls):
        super(BaseWorkloadmgrTest, cls).resource_cleanup()
