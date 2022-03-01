from gladier import  generate_flow_definition, utils
from gladier_xrf.flows.base_container_flow import ContainerBaseClient

from gladier_xrf.tools.xrf_maps import xrf_maps


@generate_flow_definition
class XRFMapsFlow(ContainerBaseClient):
    containers = {
            utils.name_generation.get_funcx_function_name(xrf_maps): {
                'container_type': 'singularity',
                'location': '/eagle/APSDataAnalysis/XRF/containers/xrf.simg',
        }
    }
    
    gladier_tools = [
        'gladier_kanzus.tools.XRFMaps',
    ]
    
