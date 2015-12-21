(function(){

var ZC = Ext.ns('Zenoss.component');

ZC.registerName(
    'HadoopMemoryUsage',
    _t('Hadoop Memory Usage'),
    _t('Hadoop Memory Usage'));

ZC.HadoopMemoryUsagePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'HadoopMemoryUsage',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'caption'},
                {name: 'jvm_max_mb'},
                {name: 'jvm_used_mb'},
                {name: 'jvm_commited_mb'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'caption',
                dataIndex: 'caption',
                header: _t('Name'),
                sortable: true
            },{
                id: 'jvm_max_mb',
                dataIndex: 'jvm_max_mb',
                header: _t('Max') + ', MB',
                sortable: true
            },{
                id: 'jvm_used_mb',
                dataIndex: 'jvm_used_mb',
                header: _t('Used') + ', MB',
                sortable: true
            },{
                id: 'jvm_commited_mb',
                dataIndex: 'jvm_commited_mb',
                header: _t('Commited') + ', MB',
                sortable: true
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.HadoopMemoryUsagePanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('HadoopMemoryUsagePanel', ZC.HadoopMemoryUsagePanel);

})();


