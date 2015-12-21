from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_VIEW
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.ZenModel.Service import *

import math


class HadoopOozieJobStatus(Service):
    meta_type = portal_type = 'HadoopOozieJobStatus'
    title = ''

    _relations = Service._relations + (
        ('os', ToOne(
            ToManyCont,
            'Products.ZenModel.OperatingSystem', 'hadoopooziejobstatus',)),
    )

    factory_type_information = (
        {
            'id':              'HadoopOozieJobStatus',
            'meta_type':       'HadoopOozieJobStatus',
            'description':     """HadoopOozieJobStatus""",
            'product':         'HadoopOozieJobStatus',
            'immediate_view':  'HadoopOozieJobStatusDetail',
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
        return 'HadoopOozieJobStatus'

    def get_cached_value(self, name):
        value = self.cacheRRDValue(name, 0)
        if math.isnan(value):
            return value
        else:
            return long(value)

    def get_count(self):
        key = 'hadoopOozieJobstatusCount'
        return self.get_cached_value(key)


InitializeClass(HadoopOozieJobStatus)
