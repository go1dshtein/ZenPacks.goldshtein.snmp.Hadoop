(function(){

var ZC = Ext.ns('Zenoss.component');

ZC.registerName(
    'HadoopOozieJobStatus',
    _t('Oozie Job Status'),
    _t('Oozie Job Status'));

ZC.HadoopOozieJobStatusPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'HadoopOozieJobStatus',
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
                {name: 'count'}
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
                id: 'count',
                dataIndex: 'count',
                header: _t('Count'),
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

        ZC.HadoopOozieJobStatusPanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('HadoopOozieJobStatusPanel', ZC.HadoopOozieJobStatusPanel);

})();
