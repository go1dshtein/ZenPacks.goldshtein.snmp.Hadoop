from Products.DataCollector.plugins.CollectorPlugin import SnmpPlugin
from Products.DataCollector.plugins.CollectorPlugin import GetTableMap, GetMap
from Products.DataCollector.plugins.DataMaps import ObjectMap


class HadoopGeneralModeler(SnmpPlugin):
    maptype = "HadoopGeneral"
    relname = "hadoopgeneral"
    compname = "os"
    modname = 'ZenPacks.goldshtein.snmp.Hadoop.HadoopGeneral'

    deviceProperties = SnmpPlugin.deviceProperties + ('zDeviceTemplates',)
    mibDesc = {
        '.1.3.6.1.4.1.777.100.15.3.1.1.1.1': 'HadoopHdfsCapacity',
        '.1.3.6.1.4.1.777.100.15.3.1.1.4.1': 'HadoopHdfsDatanodes',
        '.1.3.6.1.4.1.777.100.15.3.1.2.1.1': 'HadoopHdfsDatanodeCapacity',
        '.1.3.6.1.4.1.777.100.15.3.1.5.1.1': 'HadoopHdfsJournalNodeStats',
        '.1.3.6.1.4.1.777.100.15.3.2.3.1':   'HadoopOozieRunningJobs',
        '.1.3.6.1.4.1.777.100.15.3.3.1.1.1': 'HadoopYarnResourceManager',
        '.1.3.6.1.4.1.777.100.15.3.6.1.1.1': 'HadoopImpalaServer',
    }
    snmpGetMap = GetMap(mibDesc)

    def process(self, device, results, log):
        getdata, tabledata = results
        rm = self.relMap()

        if len(getdata.keys()) == getdata.values().count(None):
            return

        for each in HadoopGeneralModeler.mibDesc.values():
            if each in getdata and getdata[each] is not None:
                log.info("component found: %s", each)
                om = self.objectMap({'template_name': each})
                om.title = each
                om.id = each
                rm.append(om)
        return rm
