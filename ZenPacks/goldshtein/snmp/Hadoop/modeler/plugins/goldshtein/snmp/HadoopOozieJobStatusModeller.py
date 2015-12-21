from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class HadoopOozieJobStatusModeller(SnmpPlugin):
    mapname = 'HadoopOozieJobStatus'
    compname = 'os'
    relname = 'hadoopooziejobstatus'
    modname = 'ZenPacks.goldshtein.snmp.Hadoop.HadoopOozieJobStatus'

    snmpGetTableMaps = (
        GetTableMap(
            'oozieJobStatus', '1.3.6.1.4.1.777.100.15.3.2.1', {
                '.2': 'oozieJobStatusName',
                }
            ),
        )

    def process(self, device, results, log):
        table = results[1].get('oozieJobStatus', {})

        rm = self.relMap()
        for snmpindex, row in table.items():
            name = row.get('oozieJobStatusName')
            if not name:
                log.warn('skipping oozie job status without name')
                continue

            log.info('oozie job status found: %s', name)
            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                }))

        return rm
