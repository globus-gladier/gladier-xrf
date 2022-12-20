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
            'globus_endpoint_clutch': depl_input['input']['globus_endpoint_source'],
            'globus_endpoint_theta': depl_input['input']['globus_endpoint_proc'],
        }
    }

    xrf_maps_flow = XRFMapsFlow()

    xrf_run_label = 'Raf is testing' #pathlib.Path(hdf_name).name[:62]

    flow_run = xrf_maps_flow.run_flow(flow_input=flow_input, label=xrf_run_label)

    print('run_id : ' + flow_run['action_id'])


