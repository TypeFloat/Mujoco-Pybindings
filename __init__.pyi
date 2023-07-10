from mujoco.pybindings._structs import *
from mujoco.pybindings._enums import *


def mj_name2id(m, type, name): # real signature unknown; restored from __doc__
    """
    mj_name2id(m: mujoco._structs.MjModel, type: int, name: str) -> int
    
    Get id of object with specified name, return -1 if not found; type is mjtObj.
    """
    pass

def mj_step(m, d, nstep=1): # real signature unknown; restored from __doc__
    """
    mj_step(m: mujoco._structs.MjModel, d: mujoco._structs.MjData, nstep: int = 1) -> None
    
    Advance simulation, use control callback to obtain external force and control. Optionally, repeat nstep times.
    """
    pass

def mj_step1(m, d): # real signature unknown; restored from __doc__
    """
    mj_step1(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None
    
    Advance simulation in two steps: before external force and control is set by user.
    """
    pass

def mj_step2(m, d): # real signature unknown; restored from __doc__
    """
    mj_step2(m: mujoco._structs.MjModel, d: mujoco._structs.MjData) -> None
    
    Advance simulation in two steps: after external force and control is set by user.
    """
    pass