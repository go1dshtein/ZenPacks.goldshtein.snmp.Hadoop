from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.ZenModel.ZenossSecurity import *
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Service import *

import math
import re


class HadoopMemoryUsage(Service):

    portal_type = meta_type = 'HadoopMemoryUsage'
    ifindex = ''
    title = ''
    template_name = ''

    _properties = Service._properties + (
        {'id': 'template_name', 'type': 'string', 'mode': 'r'},
    )

    _relations = Service._relations + (
        ('os',
         ToOne(ToManyCont,
               'Products.ZenModel.OperatingSystem', 'hadoopmemoryusage')),
    )

    factory_type_information = (
        {
            'id':             'HadoopMemoryUsage',
            'meta_type':      'HadoopMemoryUsage',
            'description':    """Arbitrary device grouping class""",
            'product':        'HadoopMemoryUsage',
            'immediate_view': 'HadoopMemoryUsageDetail',
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

    def monitored(self):
        return self.monitor

    def getRRDTemplates(self):
        return [self.getRRDTemplateByName(self.template_name)]

    def getStatus(self, statClass=None):
        if self.snmpIgnore():
            return -1
        return 0

    def viewName(self):
        return self.id
    name = viewName

    def get_caption(self):
        caption = self.id.strip()
        if caption == 'HadoopHdfsZKFCMemoryUsage':
            return 'ZKFC'
        return caption[0] + re.sub('([A-Z])', r' \1', caption[1:-11])

    def get_cached_value(self, name):
        value = self.cacheRRDValue(name, 0)
        if math.isnan(value):
            return value
        else:
            return long(value)

    def get_jvm_max(self):
        if self.id.strip() == 'HadoopImpalaStateStoreMemoryUsage':
            return 0
        resource = "hadoop%sJvmMax" % self.id.strip()
        return self.get_cached_value(resource)

    def get_jvm_used(self):
        if self.id.strip() == 'HadoopImpalaStateStoreMemoryUsage':
            return 0
        resource = "hadoop%sJvmUsed" % self.id.strip()
        return self.get_cached_value(resource)

    def get_jvm_commited(self):
        if self.id.strip() == 'HadoopImpalaStateStoreMemoryUsage':
            return 0
        resource = "hadoop%sJvmCommited" % self.id.strip()
        return self.get_cached_value(resource)


InitializeClass(HadoopMemoryUsage)
