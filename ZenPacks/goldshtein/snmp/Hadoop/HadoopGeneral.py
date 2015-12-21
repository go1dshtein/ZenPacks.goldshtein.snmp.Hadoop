from Globals import InitializeClass
from AccessControl import ClassSecurityInfo
from Products.ZenModel.ZenossSecurity import *
from Products.ZenRelations.RelSchema import *
from Products.ZenModel.Service import *

import math


class HadoopGeneral(Service):

    portal_type = meta_type = 'HadoopGeneral'
    ifindex = ''
    title = ''
    template_name = ''

    _properties = Service._properties + (
        {'id': 'template_name', 'type': 'string', 'mode': 'r'},
    )

    _relations = Service._relations + (
        ('os', ToOne(ToManyCont,
                     'Products.ZenModel.OperatingSystem', 'hadoopgeneral')),
    )

    factory_type_information = (
        {
            'id':             'HadoopGeneral',
            'meta_type':      'HadoopGeneral',
            'description':    """Arbitrary device grouping class""",
            'product':        'HadoopGeneral',
            'immediate_view': 'HadoopGeneralDetail',
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
        mapping = {
            'HadoopHdfsCapacity':         'HDFS Capacity',
            'HadoopHdfsDatanodes':        'HDFS Datanodes',
            'HadoopHdfsJournalNodeStats': 'HDFS Journal Node Stats',
            'HadoopHdfsDatanodeCapacity': 'HDFS Datanode Capacity',
            'HadoopOozieRunningJobs':     'Oozie Running Jobs',
            'HadoopYarnResourceManager':  'Resource Manager',
            'HadoopImpalaServer':         'Impala Server',
        }
        return mapping.get(self.id.strip(), self.id)

    def get_cached_value(self, name):
        value = self.cacheRRDValue(name, 0)
        if math.isnan(value):
            return value
        else:
            return long(value)


InitializeClass(HadoopGeneral)
