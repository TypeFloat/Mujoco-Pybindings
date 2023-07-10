class MjModel:
    # no doc
    def actuator(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        actuator(*args, **kwargs)
        Overloaded function.
        
        1. actuator(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelActuatorViews
        
        2. actuator(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelActuatorViews
        """
        pass

    def body(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        body(*args, **kwargs)
        Overloaded function.
        
        1. body(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelBodyViews
        
        2. body(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelBodyViews
        """
        pass

    def cam(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        cam(*args, **kwargs)
        Overloaded function.
        
        1. cam(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelCameraViews
        
        2. cam(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelCameraViews
        """
        pass

    def camera(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        camera(*args, **kwargs)
        Overloaded function.
        
        1. camera(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelCameraViews
        
        2. camera(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelCameraViews
        """
        pass

    def eq(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        eq(*args, **kwargs)
        Overloaded function.
        
        1. eq(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelEqualityViews
        
        2. eq(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelEqualityViews
        """
        pass

    def equality(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        equality(*args, **kwargs)
        Overloaded function.
        
        1. equality(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelEqualityViews
        
        2. equality(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelEqualityViews
        """
        pass

    def exclude(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        exclude(*args, **kwargs)
        Overloaded function.
        
        1. exclude(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelExcludeViews
        
        2. exclude(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelExcludeViews
        """
        pass

    def from_binary_path(self, filename, assets, Dict=None, p_str=None, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        from_binary_path(filename: str, assets: Optional[Dict[str, bytes]] = None) -> mujoco._structs.MjModel
        
        Loads an MjModel from an MJB file and an optional assets dictionary.
        
        The filename for the MJB can also refer to a key in the assets dictionary.
        This is useful for example when the MJB is not available as a file on disk.
        """
        pass

    def from_xml_path(self, filename, assets, Dict=None, p_str=None, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        from_xml_path(filename: str, assets: Optional[Dict[str, bytes]] = None) -> mujoco._structs.MjModel
        
        Loads an MjModel from an XML file and an optional assets dictionary.
        
        The filename for the XML can also refer to a key in the assets dictionary.
        This is useful for example when the XML is not available as a file on disk.
        """
        pass

    def from_xml_string(self, xml, assets, Dict=None, p_str=None, bytes=None, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        from_xml_string(xml: str, assets: Optional[Dict[str, bytes]] = None) -> mujoco._structs.MjModel
        
        Loads an MjModel from an XML string and an optional assets dictionary.
        """
        pass

    def geom(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        geom(*args, **kwargs)
        Overloaded function.
        
        1. geom(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelGeomViews
        
        2. geom(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelGeomViews
        """
        pass

    def hfield(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        hfield(*args, **kwargs)
        Overloaded function.
        
        1. hfield(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelHfieldViews
        
        2. hfield(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelHfieldViews
        """
        pass

    def jnt(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        jnt(*args, **kwargs)
        Overloaded function.
        
        1. jnt(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelJointViews
        
        2. jnt(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelJointViews
        """
        pass

    def joint(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        joint(*args, **kwargs)
        Overloaded function.
        
        1. joint(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelJointViews
        
        2. joint(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelJointViews
        """
        pass

    def key(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        key(*args, **kwargs)
        Overloaded function.
        
        1. key(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelKeyframeViews
        
        2. key(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelKeyframeViews
        """
        pass

    def keyframe(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        keyframe(*args, **kwargs)
        Overloaded function.
        
        1. keyframe(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelKeyframeViews
        
        2. keyframe(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelKeyframeViews
        """
        pass

    def light(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        light(*args, **kwargs)
        Overloaded function.
        
        1. light(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelLightViews
        
        2. light(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelLightViews
        """
        pass

    def mat(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        mat(*args, **kwargs)
        Overloaded function.
        
        1. mat(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelMaterialViews
        
        2. mat(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelMaterialViews
        """
        pass

    def material(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        material(*args, **kwargs)
        Overloaded function.
        
        1. material(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelMaterialViews
        
        2. material(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelMaterialViews
        """
        pass

    def mesh(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        mesh(*args, **kwargs)
        Overloaded function.
        
        1. mesh(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelMeshViews
        
        2. mesh(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelMeshViews
        """
        pass

    def numeric(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        numeric(*args, **kwargs)
        Overloaded function.
        
        1. numeric(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelNumericViews
        
        2. numeric(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelNumericViews
        """
        pass

    def pair(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        pair(*args, **kwargs)
        Overloaded function.
        
        1. pair(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelPairViews
        
        2. pair(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelPairViews
        """
        pass

    def sensor(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        sensor(*args, **kwargs)
        Overloaded function.
        
        1. sensor(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelSensorViews
        
        2. sensor(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelSensorViews
        """
        pass

    def site(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        site(*args, **kwargs)
        Overloaded function.
        
        1. site(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelSiteViews
        
        2. site(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelSiteViews
        """
        pass

    def skin(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        skin(*args, **kwargs)
        Overloaded function.
        
        1. skin(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelSkinViews
        
        2. skin(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelSkinViews
        """
        pass

    def tendon(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        tendon(*args, **kwargs)
        Overloaded function.
        
        1. tendon(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelTendonViews
        
        2. tendon(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelTendonViews
        """
        pass

    def tex(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        tex(*args, **kwargs)
        Overloaded function.
        
        1. tex(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelTextureViews
        
        2. tex(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelTextureViews
        """
        pass

    def texture(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        texture(*args, **kwargs)
        Overloaded function.
        
        1. texture(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelTextureViews
        
        2. texture(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelTextureViews
        """
        pass

    def tuple(self, *args, **kwargs): # real signature unknown; restored from __doc__
        """
        tuple(*args, **kwargs)
        Overloaded function.
        
        1. tuple(self: mujoco._structs.MjModel, arg0: int) -> mujoco::python::MjModelTupleViews
        
        2. tuple(self: mujoco._structs.MjModel, name: str = '') -> mujoco::python::MjModelTupleViews
        """
        pass

    def __copy__(self): # real signature unknown; restored from __doc__
        """ __copy__(self: mujoco._structs.MjModel) -> mujoco._structs.MjModel """
        pass

    def __deepcopy__(self, arg0): # real signature unknown; restored from __doc__
        """ __deepcopy__(self: mujoco._structs.MjModel, arg0: dict) -> mujoco._structs.MjModel """
        pass

    def __getstate__(self): # real signature unknown; restored from __doc__
        """ __getstate__(self: mujoco._structs.MjModel) -> bytes """
        return b""

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, arg0): # real signature unknown; restored from __doc__
        """ __setstate__(self: mujoco._structs.MjModel, arg0: bytes) -> None """
        pass

    actuator_acc0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_actadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_actlimited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_actnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_actrange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_biasprm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_biastype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_cranklength = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_ctrllimited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_ctrlrange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_dynprm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_dyntype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_forcelimited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_forcerange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_gainprm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_gaintype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_gear = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_length0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_lengthrange = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_plugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_trnid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_trntype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    actuator_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_dofadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_dofnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_geomadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_geomnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_gravcomp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_inertia = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_invweight0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_ipos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_iquat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_jntadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_jntnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_mass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_mocapid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_parentid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_plugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_quat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_rootid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_sameframe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_simple = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_subtreemass = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    body_weldid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cam_bodyid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cam_fovy = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cam_ipd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cam_mat0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cam_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cam_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cam_pos0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cam_poscom0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cam_quat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cam_targetbodyid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    cam_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dof_armature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dof_bodyid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dof_damping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dof_frictionloss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dof_invweight0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dof_jntid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dof_M0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dof_Madr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dof_parentid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dof_simplenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dof_solimp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    dof_solref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eq_active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eq_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eq_obj1id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eq_obj2id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eq_solimp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eq_solref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    eq_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    exclude_signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_bodyid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_conaffinity = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_condim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_contype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_dataid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_fluid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_friction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_gap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_margin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_matid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_priority = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_quat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_rbound = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_rgba = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_sameframe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_solimp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_solmix = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_solref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    geom_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hfield_adr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hfield_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hfield_ncol = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hfield_nrow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    hfield_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_axis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_bodyid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_dofadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_limited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_margin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_qposadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_range = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_solimp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_solref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_stiffness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    jnt_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_act = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_ctrl = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_mpos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_mquat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_qpos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_qvel = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    key_time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_active = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_ambient = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_attenuation = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_bodyid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_castshadow = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_cutoff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_diffuse = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_dir = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_dir0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_directional = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_exponent = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_pos0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_poscom0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_specular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    light_targetbodyid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mat_emission = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mat_reflectance = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mat_rgba = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mat_shininess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mat_specular = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mat_texid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mat_texrepeat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mat_texuniform = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mesh_face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mesh_faceadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mesh_facenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mesh_graph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mesh_graphadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mesh_normal = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mesh_texcoord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mesh_texcoordadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mesh_vert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mesh_vertadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    mesh_vertnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    na = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    names = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    names_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_actuatoradr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_bodyadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_camadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_eqadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_excludeadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_geomadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_hfieldadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_jntadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_keyadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_lightadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_matadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_meshadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_numericadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_pairadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_pluginadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_sensoradr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_siteadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_skinadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_tendonadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_texadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_textadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name_tupleadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nbody = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nbuffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ncam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nconmax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nD = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nemax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    neq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nexclude = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ngeom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nhfield = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nhfielddata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    njmax = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    njnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nkey = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nlight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nM = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmesh = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmeshface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmeshgraph = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmeshtexvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmeshvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nmocap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nnames = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nnames_map = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nnumeric = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nnumericdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    npair = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nplugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    npluginattr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    npluginstate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nq = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nsensor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nsensordata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nsite = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nskin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nskinbone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nskinbonevert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nskinface = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nskintexvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nskinvert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nstack = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ntendon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ntex = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ntexdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ntext = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ntextdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ntuple = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    ntupledata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nu = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numeric_adr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numeric_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    numeric_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nuserdata = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nuser_actuator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nuser_body = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nuser_cam = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nuser_geom = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nuser_jnt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nuser_sensor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nuser_site = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nuser_tendon = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nv = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    nwrap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    opt = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pair_dim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pair_friction = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pair_gap = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pair_geom1 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pair_geom2 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pair_margin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pair_signature = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pair_solimp = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    pair_solref = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    plugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    plugin_attr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    plugin_attradr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    plugin_stateadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    plugin_statenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qpos0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    qpos_spring = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_adr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_cutoff = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_datatype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_dim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_needstage = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_noise = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_objid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_objtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_plugin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_refid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_reftype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sensor_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_bodyid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_matid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_pos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_quat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_rgba = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_sameframe = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    site_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_boneadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_bonebindpos = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_bonebindquat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_bonebodyid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_bonenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_bonevertadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_bonevertid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_bonevertnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_bonevertweight = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_face = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_faceadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_facenum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_inflate = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_matid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_rgba = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_texcoord = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_texcoordadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_vert = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_vertadr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    skin_vertnum = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    stat = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_adr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_damping = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_frictionloss = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_group = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_invweight0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_length0 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_lengthspring = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_limited = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_margin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_matid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_num = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_range = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_rgba = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_solimp_fri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_solimp_lim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_solref_fri = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_solref_lim = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_stiffness = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_user = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tendon_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_adr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_data = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    text_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_adr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_rgb = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tex_width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tuple_adr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tuple_objid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tuple_objprm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tuple_objtype = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    tuple_size = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    vis = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_objid = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_prm = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    wrap_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    _address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



