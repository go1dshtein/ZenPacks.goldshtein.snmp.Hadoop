from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin
from Products.DataCollector.plugins.CollectorPlugin import GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap


class HadoopMemoryUsageModeler(SnmpPlugin):
    maptype = 'HadoopMemoryUsage'
    relname = 'hadoopmemoryusage'
    compname = 'os'
    modname = 'ZenPacks.goldshtein.snmp.Hadoop.HadoopMemoryUsage'

    deviceProperties = SnmpPlugin.deviceProperties + ('zDeviceTemplates',)
    mibDesc = {
        '.1.3.6.1.4.1.777.100.15.3.1.1.6.1': 'HadoopHdfsNamenodeMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.1.2.6.1': 'HadoopHdfsDatanodeMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.1.3.6.1': 'HadoopHdfsSecondaryNamenodeMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.1.4.6.1': 'HadoopHdfsZKFCMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.1.5.6.1': 'HadoopHdfsJournalNodeMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.2.6.1':   'HadoopOozieMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.3.1.6.1': 'HadoopYarnResourceManagerMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.3.2.6.1': 'HadoopYarnNodeManagerMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.3.3.6.1': 'HadoopYarnHistoryServerMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.4.1.6.1': 'HadoopHiveMetastoreMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.4.2.6.1': 'HadoopHiveServerMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.5.6.1':   'HadoopZookeeperMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.6.1.2.1': 'HadoopImpalaServerMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.6.2.2.1': 'HadoopImpalaStateStoreMemoryUsage',
        '.1.3.6.1.4.1.777.100.15.3.6.3.2.1': 'HadoopImpalaCatalogMemoryUsage',
    }
    snmpGetMap = GetMap(mibDesc)

    def process(self, device, results, log):
        getdata, tabledata = results
        rm = self.relMap()

        if len(getdata.keys()) == getdata.values().count(None):
            return

        for each in HadoopMemoryUsageModeler.mibDesc.values():
            if each in getdata and getdata[each] is not None:
                log.info('component found: %s', each)
                om = self.objectMap({'template_name': each})
                om.title = each
                om.id = each
                rm.append(om)
        return rm
