(function(){

var ZC = Ext.ns('Zenoss.component');

ZC.registerName(
    'HadoopSchedulerQueue',
    _t('Hadoop Scheduler Queue'),
    _t('Hadoop Scheduler Queue'));

ZC.HadoopSchedulerQueuePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'HadoopSchedulerQueue',
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
                {name: 'used_memory'},
                {name: 'used_cores'},
                {name: 'active_apps'},
                {name: 'pending_apps'}
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
                id: 'used_memory',
                dataIndex: 'used_memory',
                header: _t('Memory') + ', MB',
                sortable: true
            },{
                id: 'used_cores',
                dataIndex: 'used_cores',
                header: _t('Cores'),
                sortable: true
            },{
                id: 'active_apps',
                dataIndex: 'active_apps',
                header: _t('Active') + ' ' + _t('Apps'),
                sortable: true
            },{
                id: 'pending_apps',
                dataIndex: 'pending_apps',
                header: _t('Pending') + ' ' + _t('Apps'),
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

        ZC.HadoopSchedulerQueuePanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('HadoopSchedulerQueuePanel', ZC.HadoopSchedulerQueuePanel);

})();
