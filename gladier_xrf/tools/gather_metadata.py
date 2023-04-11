from gladier import generate_flow_definition, GladierBaseTool

def gather_metadata(**data):
    GENERAL_METADATA = {
    "creators": [{"creatorName": "BIO Team"}],
    "publicationYear": "2023", 
    "publisher": "Argonne National Lab",
    "resourceType": {
        "resourceType": "Dataset",
        "resourceTypeGeneral": "Dataset"
    },
    "subjects": [{"subject": "SDL"}],
    "exp_type": "Campaign2"

    }
    datal = {} ##add new data here
    
    GENERAL_METADATA.update(datal)
    final_data = data["publishv2"]
    final_data['metadata'] = GENERAL_METADATA
    return final_data

@generate_flow_definition
class GatherMetaData(GladierBaseTool):
    funcx_functions = [gather_metadata]
    required_input = [
        'funcx_endpoint_compute'
    ]