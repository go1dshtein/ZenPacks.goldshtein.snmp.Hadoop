from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class HadoopSchedulerQueueModeller(SnmpPlugin):
    mapname = 'HadoopSchedulerQueue'
    compname = 'os'
    relname = 'hadoopschedulerqueue'
    modname = 'ZenPacks.goldshtein.snmp.Hadoop.HadoopSchedulerQueue'

    snmpGetTableMaps = (
        GetTableMap(
            'schedulerQueueTable', '1.3.6.1.4.1.777.100.15.3.3.1.7', {
                '.2': 'schedulerQueueName',
                }
            ),
        )

    def process(self, device, results, log):
        table = results[1].get('schedulerQueueTable', {})

        rm = self.relMap()
        for snmpindex, row in table.items():
            name = row.get('schedulerQueueName')
            if not name:
                log.warn('skipping scheduler queue with no name')
                continue

            log.info('yarn resource manager scheduler queue found: %s', name)
            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                }))

        return rm
