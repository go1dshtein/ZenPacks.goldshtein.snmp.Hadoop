import Globals
import os.path

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
from Products.CMFCore.DirectoryView import registerDirectory
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())

from Products.ZenModel.OperatingSystem import OperatingSystem
from Products.ZenModel.ZenPack import ZenPackBase
from Products.ZenRelations.RelSchema import *
from Products.ZenUtils.ZenScriptBase import ZenScriptBase


OperatingSystem._relations += (
    ('hadoopgeneral',
     ToManyCont(ToOne,
                'ZenPacks.goldshtein.snmp.Hadoop.HadoopGeneral', 'os')),
)

OperatingSystem._relations += (
    ('hadoopmemoryusage',
     ToManyCont(ToOne,
                'ZenPacks.goldshtein.snmp.Hadoop.HadoopMemoryUsage', 'os')),
)

OperatingSystem._relations += (
    ('hadoopschedulerqueue',
     ToManyCont(ToOne,
                'ZenPacks.goldshtein.snmp.Hadoop.HadoopSchedulerQueue', 'os')),
)

OperatingSystem._relations += (
    ('hadoopooziejobstatus',
     ToManyCont(ToOne,
                'ZenPacks.goldshtein.snmp.Hadoop.HadoopOozieJobStatus', 'os')),
)


class ZenPack(ZenPackBase):
    """ ZenPack loader
    """
    def install(self, app):
        ZenPackBase.install(self, app)
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()

    def upgrade(self, app):
        ZenPackBase.upgrade(self, app)
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()

    def remove(self, app, junk):
        ZenPackBase.remove(self, app, junk)
        OperatingSystem._relations = tuple(
            [x for x in OperatingSystem._relations if x[0] not in [
                'hadoopgeneral',
                'hadoopmemoryusage',
                'hadoopschedulerqueue',
                'hadoopooziejobstatus']])
        for d in self.dmd.Devices.getSubDevices():
            d.os.buildRelations()
