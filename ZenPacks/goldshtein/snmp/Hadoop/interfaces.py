from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.utils import ZuulMessageFactory as _t


class IHadoopGeneralInfo(IComponentInfo):
    pass


class IHadoopMemoryUsageInfo(IComponentInfo):
    pass


class IHadoopSchedulerQueueInfo(IComponentInfo):
    pass


class IHadoopOozieJobStatusInfo(IComponentInfo):
    pass
