from gladier import GladierBaseTool, generate_flow_definition


def xrf_maps(**data):
    import os
    import subprocess
    from subprocess import PIPE

    sample_dir = data['sample_dir']
    xrf_loc = data.get('xrf_loc','/container/XRF-Maps/bin/')

    if not os.path.exists(sample_dir):
        raise NameError(f'{sample_dir} \n Sample dir does not exist!')

    #required to run xrf_maps currently. This location is inside the container for now.
    os.chdir(xrf_loc)
    cmd = f"./xrf_maps --dir {sample_dir} --fit roi,nnls,matrix --queantify-with maps_standardinfo.txt --add-v9layout --generate-avg-h5"
  
    res = subprocess.run(cmd, stdout=PIPE, stderr=PIPE,
                             shell=True, executable='/bin/bash')
    
    with open(os.path.join(sample_dir,'xrf_output.log'), 'w+') as f:
                f.write(res.stdout.decode('utf-8'))

    with open(os.path.join(sample_dir,'xrf_errors.log'), 'w+') as f:
                f.write(res.stderr.decode('utf-8'))
    
    return str(res.stdout)


@generate_flow_definition(modifiers={
    xrf_maps: {'WaitTime': 7200}
})
class XRFMaps(GladierBaseTool):

    required_input = [
        'sample_dir',
        'funcx_endpoint_compute',
    ]

    funcx_functions = [
        xrf_maps
    ]

    flow_input = {
    }
