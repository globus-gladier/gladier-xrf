import argparse
import os

from gladier_xrf.flows.flow_xrf import XRFMapsFlow
from gladier_xrf.deployments import deployment_map


def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sample', help='Path to the sample folder file', default='')
    return parser.parse_args()


if __name__ == '__main__':

    args = arg_parse()

    depl = deployment_map.get(args.deployment)
    if not depl:
        raise ValueError(f'Invalid Deployment, deployments available: {list(deployment_map.keys())}')

    depl_input = depl.get_input()

    local_sample_dir = os.path.basename(args.sample)
    dest_sample_dir = ''
 
    flow_input = {
        'input': {
            'local_sample_dir': local_sample_dir, 
            'sample_dir': dest_sample_dir,

            # funcX endpoints
            'funcx_endpoint_non_compute': depl_input['input']['funcx_endpoint_non_compute'],
            'funcx_endpoint_compute': depl_input['input']['funcx_endpoint_compute'],

            # globus endpoints
            'source_globus_endpoint':depl_input['input']['globus_endpoint_source'],
            'destination_globus_endpoint':depl_input['input']['globus_endpoint_proc'],
            'source_globus_path':local_sample_dir,
            'destination_globus_path':dest_sample_dir,

            'publishv2': {
                'dataset': local_sample_dir,
                'index': 'aeda697d-18e2-40d9-a4bf-1d97543bc632',
                'project': 'gladier-xrf',
                'source_collection': depl_input['input']['globus_endpoint_proc'],
                'source_collection_basepath': '/',
                'destination_collection': '18ec5071-db68-496d-b66a-ac3f150f8a07',
                'metadata': {},
                'ingest_enabled': True,
                'transfer_enabled':True,
                'destination':str("/portal/"),
                'visible_to' : ['public']
                }
        }
    }

    xrf_maps_flow = XRFMapsFlow()

    xrf_run_label = 'Raf is testing' #pathlib.Path(hdf_name).name[:62]

    flow_run = xrf_maps_flow.run_flow(flow_input=flow_input, label=xrf_run_label)

    print('run_id : ' + flow_run['action_id'])


