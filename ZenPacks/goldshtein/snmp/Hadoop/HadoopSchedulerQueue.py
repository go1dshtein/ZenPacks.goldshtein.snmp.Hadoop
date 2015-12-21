from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

from AccessControl import ClassSecurityInfo
from Globals import InitializeClass
from Products.ZenModel.Service import *

import math


class HadoopSchedulerQueue(Service):
    meta_type = portal_type = 'HadoopSchedulerQueue'
    title = ''

    _relations = Service._relations + (
        ('os', ToOne(
            ToManyCont,
            'Products.ZenModel.OperatingSystem', 'hadoopschedulerqueue',)),
    )

    factory_type_information = (
        {
            'id':              'HadoopSchedulerQueue',
            'meta_type':       'HadoopSchedulerQueue',
            'description':     """HadoopSchedulerQueue""",
            'product':         'HadoopSchedulerQueue',
            'immediate_view':  'HadoopSchedulerQueueDetail',
            'actions': (
                {
                    'id': 'perfConf',
                    'name': 'Template',
                    'action': 'objTemplates',
                    'permissions': (ZEN_VIEW,),
                },
            ),
        },
    )

    security = ClassSecurityInfo()

    def name(self):
        return self.id

    def monitored(self):
        return self.monitor

    def getRRDTemplateName(self):
        return 'HadoopYarnResourceManagerSchedulerQueue'

    def get_cached_value(self, name):
        value = self.cacheRRDValue(name, 0)
        if math.isnan(value):
            return value
        else:
            return long(value)

    def get_max_cores(self):
        key = 'hadoopYarnResourceManagerSchedulerQueueMaxCores'
        return self.get_cached_value(key)

    def get_max_memory(self):
        key = 'hadoopYarnResourceManagerSchedulerQueueMaxMemory'
        return self.get_cached_value(key)

    def get_max_apps(self):
        key = 'hadoopYarnResourceManagerSchedulerQueueMaxApps'
        return self.get_cached_value(key)

    def get_used_memory(self):
        key = 'hadoopYarnResourceManagerSchedulerQueueUsedMemory'
        return self.get_cached_value(key)

    def get_used_cores(self):
        key = 'hadoopYarnResourceManagerSchedulerQueueUsedCores'
        return self.get_cached_value(key)

    def get_fair_cores(self):
        key = 'hadoopYarnResourceManagerSchedulerQueueFairCores'
        return self.get_cached_value(key)

    def get_fair_memory(self):
        key = 'hadoopYarnResourceManagerSchedulerQueueFairMemory'
        return self.get_cached_value(key)

    def get_steady_fair_cores(self):
        key = 'hadoopYarnResourceManagerSchedulerQueueSteadyFairCores'
        return self.get_cached_value(key)

    def get_steady_fair_memory(self):
        key = 'hadoopYarnResourceManagerSchedulerQueueSteadyFairMemory'
        return self.get_cached_value(key)

    def get_active_apps(self):
        key = 'hadoopYarnResourceManagerSchedulerQueueActiveApps'
        return self.get_cached_value(key)

    def get_pending_apps(self):
        key = 'hadoopYarnResourceManagerSchedulerQueuePendingApps'
        return self.get_cached_value(key)


InitializeClass(HadoopSchedulerQueue)
