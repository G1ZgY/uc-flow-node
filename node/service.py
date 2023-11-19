from uc_flow_nodes.service import NodeService

from view.info import InfoView
from view.execute import ExecuteView

class Service(NodeService):
    class Routes(NodeService.Routes):
        Info = InfoView
        Execute = ExecuteView
