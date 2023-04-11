from gladier import  GladierBaseClient, generate_flow_definition
from gladier_xrf.tools.xrf_maps import xrf_maps
from gladier_xrf.tools.gather_data import GatherMetaData
@generate_flow_definition
class XRFMapsFlow(GladierBaseClient):    
    globus_group = '0bbe98ef-de8f-11eb-9e93-3db9c47b68ba'
    gladier_tools = [
       'gladier_tools.transfer.Transfer',
        # 'gladier_xrf.tools.XRFMaps',
        GatherMetaData,
       'gladier_tools.publish.Publishv2'
    ]
    
