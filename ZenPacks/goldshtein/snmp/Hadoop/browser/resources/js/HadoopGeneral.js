(function(){

var ZC = Ext.ns('Zenoss.component');

ZC.registerName(
    'HadoopGeneral',
    _t('Hadoop General'),
    _t('Hadoop General'));

ZC.HadoopGeneralPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'HadoopGeneral',
            autoExpandColumn: 'caption',
            sortInfo: {
                field: 'caption',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'severity'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'caption'},
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

        ZC.HadoopGeneralPanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('HadoopGeneralPanel', ZC.HadoopGeneralPanel);

})();



