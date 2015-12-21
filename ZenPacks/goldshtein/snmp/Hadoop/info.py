from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo
from Products.Zuul.infos.device import DeviceInfo

from ZenPacks.goldshtein.snmp.Hadoop.interfaces import IHadoopGeneralInfo
from ZenPacks.goldshtein.snmp.Hadoop.interfaces import IHadoopMemoryUsageInfo
from ZenPacks.goldshtein.snmp.Hadoop.interfaces import IHadoopOozieJobStatusInfo
from ZenPacks.goldshtein.snmp.Hadoop.interfaces import IHadoopSchedulerQueueInfo

import math


class HadoopGeneralInfo(ComponentInfo):
    implements(IHadoopGeneralInfo)

    @property
    def caption(self):
        return self._object.get_caption()


class HadoopMemoryUsageInfo(ComponentInfo):
    implements(IHadoopMemoryUsageInfo)

    @property
    def caption(self):
        return self._object.get_caption()

    @property
    def jvm_max(self):
        return self._object.get_jvm_max()

    @property
    def jvm_used(self):
        return self._object.get_jvm_used()

    @property
    def jvm_commited(self):
        return self._object.get_jvm_commited()

    @property
    def jvm_max_mb(self):
        value = self._object.get_jvm_max()
        if math.isnan(value):
            return value
        else:
            return value / 1024 / 1024

    @property
    def jvm_used_mb(self):
        value = self._object.get_jvm_used()
        if math.isnan(value):
            return value
        else:
            return value / 1024 / 1024

    @property
    def jvm_commited_mb(self):
        value = self._object.get_jvm_commited()
        if math.isnan(value):
            return value
        else:
            return value / 1024 / 1024


class HadoopSchedulerQueueInfo(ComponentInfo):
    implements(IHadoopSchedulerQueueInfo)

    @property
    def caption(self):
        return self._object.name()

    @property
    def max_cores(self):
        return self._object.get_max_cores()

    @property
    def max_memory(self):
        return self._object.get_max_memory()

    @property
    def max_apps(self):
        return self._object.get_max_apps()

    @property
    def used_memory(self):
        return self._object.get_used_memory()

    @property
    def used_cores(self):
        return self._object.get_used_cores()

    @property
    def fair_cores(self):
        return self._object.get_fair_cores()

    @property
    def fair_memory(self):
        return self._object.get_fair_memory()

    @property
    def steady_fair_cores(self):
        return self._object.get_steady_fair_cores()

    @property
    def steady_fair_memory(self):
        return self._object.get_steady_fair_memory()

    @property
    def active_apps(self):
        return self._object.get_active_apps()

    @property
    def pending_apps(self):
        return self._object.get_pending_apps()


class HadoopOozieJobStatusInfo(ComponentInfo):
    implements(IHadoopOozieJobStatusInfo)

    @property
    def caption(self):
        return self._object.name()

    @property
    def count(self):
        return self._object.get_count()
