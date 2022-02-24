# gladier-XRF


## Installing

The main core of gladier uses Globus for transfers and FuncX for executions.

### Installing Gladier 

    conda create -n gladier python=3 pip ipython jupyter
    conda activate gladier

    git clone https://github.com/globus-gladier/gladier-xrf
    cd gladier-xrf
    
    pip install -r requirements.txt

    python setup.py develop



## Running

Gladier works on top of several different services and it may be complicated to explain all at once.
We supply different notebooks to introduce each topic. 
