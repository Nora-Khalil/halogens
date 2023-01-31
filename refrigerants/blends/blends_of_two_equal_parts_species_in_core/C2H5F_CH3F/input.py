 

thermolibs = [
'primaryThermoLibrary',
'FFCM1(-)',
'halogens',
'CHOF_G4',
'CHOCl_G4',
'CHOBr_G4',
'CHOFCl_G4',
'CHOFBr_G4',
'CHOFClBr_G4',
'DFT_QCI_thermo',
'Fluorine',
'2-BTP_G4',
'thermo_DFT_CCSDTF12_BAC',
'SulfurHaynes'
]

thermolibs_Creg = [
'primaryThermoLibrary',
'FFCM1(-)',
'DFT_QCI_thermo',
]



database(
thermoLibraries = thermolibs,
reactionLibraries = ['FFCM1(-)','halogens_pdep'],
seedMechanisms = ['FFCM1(-)'],
kineticsDepositories = ['training'],
kineticsFamilies = ['default','halogens','Disproportionation-Y'],
frequenciesLibraries = ['halogens_G4'],
kineticsEstimator = 'rate rules',
)


    
species(
    label = 'N2',
    reactive = False,
    structure = SMILES('N#N')
)
    
    
    


species(
    label = 'C2H5F',
    reactive = True,
    structure = SMILES('CCF')
)      
        
        

species(
    label = 'O2',
    reactive = True,
    structure = SMILES('[O][O]')
)      
        
        

species(
    label = 'H2O',
    reactive = True,
    structure = SMILES('O')
)      
        
        

species(
    label = 'CH4',
    reactive = True,
    structure = SMILES('C')
)      
        
        

species(
    label = 'OH',
    reactive = True,
    structure = SMILES('[OH]')
)      
        
        

species(
    label = 'H',
    reactive = True,
    structure = SMILES('[H]')
)      
        
        

species(
    label = 'O',
    reactive = True,
    structure = SMILES('[O]')
)      
        
        

species(
    label = 'H2',
    reactive = True,
    structure = SMILES('[H][H]')
)      
        
        

species(
    label = 'HO2',
    reactive = True,
    structure = SMILES('[O]O')
)      
        
        

species(
    label = 'Ar',
    reactive = True,
    structure = SMILES('[Ar]')
)      
        
        

species(
    label = 'H2O2',
    reactive = True,
    structure = SMILES('OO')
)      
        
        

species(
    label = 'He',
    reactive = True,
    structure = SMILES('[He]')
)      
        
        

species(
    label = 'CO',
    reactive = True,
    structure = SMILES('[C-]#[O+]')
)      
        
        

species(
    label = 'CO2',
    reactive = True,
    structure = SMILES('O=C=O')
)      
        
        

species(
    label = 'HCO',
    reactive = True,
    structure = SMILES('[CH]=O')
)      
        
        

species(
    label = 'CH',
    reactive = True,
    structure = SMILES('[CH]')
)      
        
        

species(
    label = 'CH2(T)',
    reactive = True,
    structure = SMILES('[CH2]')
)      
        
        

species(
    label = 'CH3',
    reactive = True,
    structure = SMILES('[CH3]')
)      
        
        

species(
    label = 'CH2O',
    reactive = True,
    structure = SMILES('C=O')
)      
        
        

species(
    label = 'HCCO',
    reactive = True,
    structure = SMILES('C#C[O]')
)      
        
        

species(
    label = 'C2H',
    reactive = True,
    structure = SMILES('[C]#C')
)      
        
        

species(
    label = 'C2H2',
    reactive = True,
    structure = SMILES('C#C')
)      
        
        

species(
    label = 'H2CC',
    reactive = True,
    structure = SMILES('[C]=C')
)      
        
        

species(
    label = 'CH3O',
    reactive = True,
    structure = SMILES('C[O]')
)      
        
        

species(
    label = 'CH2CO',
    reactive = True,
    structure = SMILES('C=C=O')
)      
        
        

species(
    label = 'C2H3',
    reactive = True,
    structure = SMILES('[CH]=C')
)      
        
        

species(
    label = 'C2H4',
    reactive = True,
    structure = SMILES('C=C')
)      
        
        

species(
    label = 'C2H6',
    reactive = True,
    structure = SMILES('CC')
)      
        
        

species(
    label = 'C2H5',
    reactive = True,
    structure = SMILES('C[CH2]')
)      
        
        

species(
    label = 'CH2OH',
    reactive = True,
    structure = SMILES('[CH2]O')
)      
        
        

species(
    label = 'CH3CO',
    reactive = True,
    structure = SMILES('C[C]=O')
)      
        
        

species(
    label = 'F',
    reactive = True,
    structure = SMILES('[F]')
)      
        
        

species(
    label = 'HF',
    reactive = True,
    structure = SMILES('F')
)      
        
        

species(
    label = 'CH3F',
    reactive = True,
    structure = SMILES('CF')
)      
        
        

species(
    label = 'CHF',
    reactive = True,
    structure = SMILES('[CH]F')
)      
        
        

species(
    label = 'CH2F2',
    reactive = True,
    structure = SMILES('FCF')
)      
        
        

species(
    label = 'CH2F',
    reactive = True,
    structure = SMILES('[CH2]F')
)      
        
        

species(
    label = 'CHFO',
    reactive = True,
    structure = SMILES('O=CF')
)      
        
        

species(
    label = 'CF',
    reactive = True,
    structure = SMILES('[C]F')
)      
        
        

species(
    label = 'CFO',
    reactive = True,
    structure = SMILES('O=[C]F')
)      
        
        

species(
    label = 'CH2CHF',
    reactive = True,
    structure = SMILES('C=CF')
)      
        
        

species(
    label = 'CH2CF2',
    reactive = True,
    structure = SMILES('C=C(F)F')
)      
        
        

species(
    label = 'C2HF',
    reactive = True,
    structure = SMILES('C#CF')
)      
        
        

species(
    label = 'CHFCHF[Z]',
    reactive = True,
    structure = SMILES('FC=CF')
)      
        
        

species(
    label = 'CH2F-CH2',
    reactive = True,
    structure = SMILES('[CH2]CF')
)      
        
        

species(
    label = 'CH3-CHF',
    reactive = True,
    structure = SMILES('C[CH]F')
)      
        
        

species(
    label = 'CHF2-CH2',
    reactive = True,
    structure = SMILES('[CH2]C(F)F')
)      
        
        

species(
    label = 'CH3-CF2',
    reactive = True,
    structure = SMILES('C[C](F)F')
)      
        
        

species(
    label = 'CH2F-CHF',
    reactive = True,
    structure = SMILES('F[CH]CF')
)      
        
        

species(
    label = 'CH2CF',
    reactive = True,
    structure = SMILES('C=[C]F')
)      
        
        

species(
    label = 'CHFCH[Z]',
    reactive = True,
    structure = SMILES('[CH]=CF')
)      
        
        

species(
    label = 'CHFCF[Z]',
    reactive = True,
    structure = SMILES('F[C]=CF')
)      
        
        

species(
    label = 'CF2CH',
    reactive = True,
    structure = SMILES('[CH]=C(F)F')
)      
        
        

species(
    label = 'CH2CFO',
    reactive = True,
    structure = SMILES('[CH2]C(=O)F')
)      
        
        

species(
    label = 'CHF2',
    reactive = True,
    structure = SMILES('F[CH]F')
)      
        
        

species(
    label = 'C[C]F',
    reactive = True,
    structure = SMILES('C[C]F')
)      
        
        

species(
    label = '[CH]C',
    reactive = True,
    structure = SMILES('[CH]C')
)      
        
        

species(
    label = '[O]C=O',
    reactive = True,
    structure = SMILES('[O]C=O')
)      
        
        

species(
    label = 'CO[O]',
    reactive = True,
    structure = SMILES('CO[O]')
)      
        
        

species(
    label = 'CC[O]',
    reactive = True,
    structure = SMILES('CC[O]')
)      
        
        

species(
    label = 'O=CO',
    reactive = True,
    structure = SMILES('O=CO')
)      
        
        

species(
    label = 'O=[C]O',
    reactive = True,
    structure = SMILES('O=[C]O')
)      
        
        

species(
    label = 'CC(F)O[O]',
    reactive = True,
    structure = SMILES('CC(F)O[O]')
)      
        
        

species(
    label = '[CH]CF',
    reactive = True,
    structure = SMILES('[CH]CF')
)      
        
        

species(
    label = 'CC(=O)F',
    reactive = True,
    structure = SMILES('CC(=O)F')
)      
        
        

species(
    label = 'OC[CH]F',
    reactive = True,
    structure = SMILES('OC[CH]F')
)      
        
        

species(
    label = 'F[C]CF',
    reactive = True,
    structure = SMILES('F[C]CF')
)      
        
        

species(
    label = '[CH2]C([O])F',
    reactive = True,
    structure = SMILES('[CH2]C([O])F')
)      
        
        

species(
    label = '[CH2]CC',
    reactive = True,
    structure = SMILES('[CH2]CC')
)      
        
        

species(
    label = '[O]C[O]',
    reactive = True,
    structure = SMILES('[O]C[O]')
)      
        
        

species(
    label = '[CH]=CC=C',
    reactive = True,
    structure = SMILES('[CH]=CC=C')
)      
        
        

species(
    label = 'C#CC[CH2]',
    reactive = True,
    structure = SMILES('C#CC[CH2]')
)      
        
        

species(
    label = '[CH]=C[O]',
    reactive = True,
    structure = SMILES('[CH]=C[O]')
)      
        
        

species(
    label = '[CH]=CC#C',
    reactive = True,
    structure = SMILES('[CH]=CC#C')
)      
        
        

species(
    label = 'F[C]1CO1',
    reactive = True,
    structure = SMILES('F[C]1CO1')
)      
        
        

species(
    label = '[O]OCC(=O)F',
    reactive = True,
    structure = SMILES('[O]OCC(=O)F')
)      
        
        

species(
    label = 'C=[C]O',
    reactive = True,
    structure = SMILES('C=[C]O')
)      
        
        

species(
    label = 'FC1CO1',
    reactive = True,
    structure = SMILES('FC1CO1')
)      
        
        

species(
    label = 'O=C=CF',
    reactive = True,
    structure = SMILES('O=C=CF')
)      
        
        

species(
    label = 'O=C[CH]F',
    reactive = True,
    structure = SMILES('O=C[CH]F')
)      
        
        

species(
    label = '[O]OC(F)C=O',
    reactive = True,
    structure = SMILES('[O]OC(F)C=O')
)      
        
        

species(
    label = 'C1=CO1',
    reactive = True,
    structure = SMILES('C1=CO1')
)      
        
        

species(
    label = '[O]C1OOC1F',
    reactive = True,
    structure = SMILES('[O]C1OOC1F')
)      
        
        

species(
    label = '[CH]=CCF',
    reactive = True,
    structure = SMILES('[CH]=CCF')
)      
        
        

species(
    label = 'O=C(O)F',
    reactive = True,
    structure = SMILES('O=C(O)F')
)      
        
        

species(
    label = 'CC[CH]F',
    reactive = True,
    structure = SMILES('CC[CH]F')
)      
        
        

species(
    label = '[CH]=CC',
    reactive = True,
    structure = SMILES('[CH]=CC')
)      
        
        

species(
    label = 'C=[C]C',
    reactive = True,
    structure = SMILES('C=[C]C')
)      
        
        

species(
    label = '[CH2]C=C',
    reactive = True,
    structure = SMILES('[CH2]C=C')
)      
        
        

species(
    label = '[CH2]C(=C)F',
    reactive = True,
    structure = SMILES('[CH2]C(=C)F')
)      
        
        

species(
    label = 'C=C[CH]F',
    reactive = True,
    structure = SMILES('C=C[CH]F')
)      
        
        

species(
    label = '[O]OC(F)F',
    reactive = True,
    structure = SMILES('[O]OC(F)F')
)      
        
        

species(
    label = 'C#C[CH]F',
    reactive = True,
    structure = SMILES('C#C[CH]F')
)      
        
        

species(
    label = '[CH]C(F)F-2',
    reactive = True,
    structure = SMILES('[CH]C(F)F')
)      
        
        

species(
    label = 'CC(F)(F)O[O]',
    reactive = True,
    structure = SMILES('CC(F)(F)O[O]')
)      
        
        

species(
    label = 'C#CC',
    reactive = True,
    structure = SMILES('C#CC')
)      
        
        

species(
    label = '[O]C(=O)O',
    reactive = True,
    structure = SMILES('[O]C(=O)O')
)      
        
        

species(
    label = '[O]C(=O)F',
    reactive = True,
    structure = SMILES('[O]C(=O)F')
)      
        
        

species(
    label = '[O][C]=O',
    reactive = True,
    structure = SMILES('[O][C]=O')
)      
        
        

species(
    label = 'O=C(O)O',
    reactive = True,
    structure = SMILES('O=C(O)O')
)      
        
        

species(
    label = '[C]#CF',
    reactive = True,
    structure = SMILES('[C]#CF')
)      
        
        

species(
    label = '[C]=CF-2',
    reactive = True,
    structure = SMILES('[C]=CF')
)      
        
        

species(
    label = 'C#CCF',
    reactive = True,
    structure = SMILES('C#CCF')
)      
        
        

species(
    label = '[CH]=C=C',
    reactive = True,
    structure = SMILES('[CH]=C=C')
)      
        
        

species(
    label = 'C[C]=CF',
    reactive = True,
    structure = SMILES('C[C]=CF')
)      
        
        

species(
    label = 'C#CC=C',
    reactive = True,
    structure = SMILES('C#CC=C')
)      
        
        

species(
    label = 'C=[C]C=C',
    reactive = True,
    structure = SMILES('C=[C]C=C')
)      
        
        

species(
    label = 'C=[C]CF',
    reactive = True,
    structure = SMILES('C=[C]CF')
)      
        
        

species(
    label = 'FC1[CH]C1',
    reactive = True,
    structure = SMILES('FC1[CH]C1')
)      
        
        

species(
    label = 'C=C=CF',
    reactive = True,
    structure = SMILES('C=C=CF')
)      
        
        

species(
    label = 'C=C[C]F-2',
    reactive = True,
    structure = SMILES('C=C[C]F')
)      
        
        

species(
    label = 'FC1C=C1',
    reactive = True,
    structure = SMILES('FC1C=C1')
)      
        
        

species(
    label = 'F[C]1[CH]C1',
    reactive = True,
    structure = SMILES('F[C]1[CH]C1')
)      
        
        

species(
    label = 'FC1[C]C1',
    reactive = True,
    structure = SMILES('FC1[C]C1')
)      
        
        

species(
    label = 'C1OO1',
    reactive = True,
    structure = SMILES('C1OO1')
)      
        
        

species(
    label = 'FC1=CC1',
    reactive = True,
    structure = SMILES('FC1=CC1')
)      
        
        

species(
    label = '[CH2]C#CF',
    reactive = True,
    structure = SMILES('[CH2]C#CF')
)      
        
        

species(
    label = '[C]=CC-2',
    reactive = True,
    structure = SMILES('[C]=CC')
)      
        
        

species(
    label = '[CH]=CC#CC',
    reactive = True,
    structure = SMILES('[CH]=CC#CC')
)      
        
        

species(
    label = 'C#CC=[C]C',
    reactive = True,
    structure = SMILES('C#CC=[C]C')
)      
        
        

species(
    label = 'C=C=C',
    reactive = True,
    structure = SMILES('C=C=C')
)      
        
        

species(
    label = '[C]1=CC1',
    reactive = True,
    structure = SMILES('[C]1=CC1')
)      
        
        

species(
    label = 'C#CC([CH2])=C',
    reactive = True,
    structure = SMILES('C#CC([CH2])=C')
)      
        
        

species(
    label = '[CH]=C=C[C]=C',
    reactive = True,
    structure = SMILES('[CH]=C=C[C]=C')
)      
        
        

species(
    label = 'C=CC([O])=CF',
    reactive = True,
    structure = SMILES('C=CC([O])=CF')
)      
        
        

species(
    label = 'C#CC=C[CH2]',
    reactive = True,
    structure = SMILES('C#CC=C[CH2]')
)      
        
        

species(
    label = '[CH]=C=CC#C',
    reactive = True,
    structure = SMILES('[CH]=C=CC#C')
)      
        
        

species(
    label = 'C#C[CH]C',
    reactive = True,
    structure = SMILES('C#C[CH]C')
)      
        
        

species(
    label = 'F[C]1CC1',
    reactive = True,
    structure = SMILES('F[C]1CC1')
)      
        
        

species(
    label = 'C=[C]C=CC',
    reactive = True,
    structure = SMILES('C=[C]C=CC')
)      
        
        

species(
    label = 'C=CC(F)O[O]',
    reactive = True,
    structure = SMILES('C=CC(F)O[O]')
)      
        
        

species(
    label = '[O]OCC=CF',
    reactive = True,
    structure = SMILES('[O]OCC=CF')
)      
        
        

species(
    label = '[C]=CCF-2',
    reactive = True,
    structure = SMILES('[C]=CCF')
)      
        
        

species(
    label = 'FC1[CH]COO1',
    reactive = True,
    structure = SMILES('FC1[CH]COO1')
)      
        
        

species(
    label = 'FC=CCCC=CF',
    reactive = True,
    structure = SMILES('FC=CCCC=CF')
)      
        
        

species(
    label = '[CH]=C=C1[CH]C1',
    reactive = True,
    structure = SMILES('[CH]=C=C1[CH]C1')
)      
        
        

species(
    label = 'C=CCC(F)C=C',
    reactive = True,
    structure = SMILES('C=CCC(F)C=C')
)      
        
        

species(
    label = 'C=CCCC=CF',
    reactive = True,
    structure = SMILES('C=CCCC=CF')
)      
        
        

species(
    label = 'C#C[CH]CC',
    reactive = True,
    structure = SMILES('C#C[CH]CC')
)      
        
        

species(
    label = 'C#CC=C=C',
    reactive = True,
    structure = SMILES('C#CC=C=C')
)      
        
        

species(
    label = 'C=C[C]=CF',
    reactive = True,
    structure = SMILES('C=C[C]=CF')
)      
        
        

species(
    label = 'C#C[C]=C',
    reactive = True,
    structure = SMILES('C#C[C]=C')
)      
        
        

species(
    label = 'C#C[C]C',
    reactive = True,
    structure = SMILES('C#C[C]C')
)      
        
        

species(
    label = '[C]=CC=C-2',
    reactive = True,
    structure = SMILES('[C]=CC=C')
)      
        
        

species(
    label = '[CH2]C#CC=C',
    reactive = True,
    structure = SMILES('[CH2]C#CC=C')
)      
        
        

species(
    label = 'C=C1[CH]C1',
    reactive = True,
    structure = SMILES('C=C1[CH]C1')
)      
        
        

species(
    label = '[C]1=CCC1',
    reactive = True,
    structure = SMILES('[C]1=CCC1')
)      
        
        

species(
    label = '[CH]=C1CC1',
    reactive = True,
    structure = SMILES('[CH]=C1CC1')
)      
        
        

species(
    label = '[C]1=CCC=C1',
    reactive = True,
    structure = SMILES('[C]1=CCC=C1')
)      
        
        

species(
    label = '[O]C1(F)OO1',
    reactive = True,
    structure = SMILES('[O]C1(F)OO1')
)      
        
        

species(
    label = 'F[CH]C1=CC1',
    reactive = True,
    structure = SMILES('F[CH]C1=CC1')
)      
        
        

species(
    label = 'FC1[C]=CC1',
    reactive = True,
    structure = SMILES('FC1[C]=CC1')
)      
        
        

species(
    label = 'C1=C[CH]C=1',
    reactive = True,
    structure = SMILES('C1=C[CH]C=1')
)      
        
        

# species(
#     label = 'C#C[C]C=C',
#     reactive = True,
#     structure = SMILES('C#C[C]C=C')
# )      
        
        

species(
    label = 'C=C1[C]=CC1',
    reactive = True,
    structure = SMILES('C=C1[C]=CC1')
)      
        
        

species(
    label = 'C#CC#C',
    reactive = True,
    structure = SMILES('C#CC#C')
)      
        
        

species(
    label = '[C]#CC#C',
    reactive = True,
    structure = SMILES('[C]#CC#C')
)      
        
        

species(
    label = '[C]=CC#C',
    reactive = True,
    structure = SMILES('[C]=CC#C')
)      
        
        

species(
    label = '[CH]=C=C=CC',
    reactive = True,
    structure = SMILES('[CH]=C=C=CC')
)      
        
        

species(
    label = '[CH]=C=C=C[CH2]',
    reactive = True,
    structure = SMILES('[CH]=C=C=C[CH2]')
)      
        
        

species(
    label = 'C=[C]C#CC',
    reactive = True,
    structure = SMILES('C=[C]C#CC')
)      
        
        

species(
    label = 'C#CC#CC',
    reactive = True,
    structure = SMILES('C#CC#CC')
)      
        
        

species(
    label = 'C=CC1=[C]C1',
    reactive = True,
    structure = SMILES('C=CC1=[C]C1')
)      
        
        

species(
    label = 'C=C=C1[CH]C1',
    reactive = True,
    structure = SMILES('C=C=C1[CH]C1')
)      
        
        

species(
    label = 'C=C=C=C=C',
    reactive = True,
    structure = SMILES('C=C=C=C=C')
)      
        
        

species(
    label = 'C#C[C]1CC1',
    reactive = True,
    structure = SMILES('C#C[C]1CC1')
)      
        
        

species(
    label = 'C#CC1=CC1',
    reactive = True,
    structure = SMILES('C#CC1=CC1')
)      
        
        

species(
    label = '[O]OC(F)CO',
    reactive = True,
    structure = SMILES('[O]OC(F)CO')
)      
        
        

species(
    label = 'C#CC#C[CH2]',
    reactive = True,
    structure = SMILES('C#CC#C[CH2]')
)      
        
        

species(
    label = '[C]=CC#CC-2',
    reactive = True,
    structure = SMILES('[C]=CC#CC')
)      
        
        

species(
    label = 'C=C1[C]=C1C',
    reactive = True,
    structure = SMILES('C=C1[C]=C1C')
)      
        
        

species(
    label = 'FC1[CH]CC[CH]C1',
    reactive = True,
    structure = SMILES('FC1[CH]CC[CH]C1')
)      
        
        

species(
    label = '[C]1=CC=C=C1',
    reactive = True,
    structure = SMILES('[C]1=CC=C=C1')
)      
        
        

species(
    label = '[CH]=C1[CH]C1=C',
    reactive = True,
    structure = SMILES('[CH]=C1[CH]C1=C')
)      
        
        

species(
    label = 'C#CC1[C]C1',
    reactive = True,
    structure = SMILES('C#CC1[C]C1')
)      
        
        

species(
    label = 'C#CC1C=C1',
    reactive = True,
    structure = SMILES('C#CC1C=C1')
)      
        
        

species(
    label = '[C]1=CC2CC12',
    reactive = True,
    structure = SMILES('[C]1=CC2CC12')
)      
        
        

species(
    label = '[C]=CC=C=C',
    reactive = True,
    structure = SMILES('[C]=CC=C=C')
)      
        
        

species(
    label = 'O=C1OC1=O',
    reactive = True,
    structure = SMILES('O=C1OC1=O')
)      
        
        

species(
    label = 'C(T)',
    reactive = True,
    structure = SMILES('[C]')
)      
        
        

species(
    label = 'CH3OH',
    reactive = True,
    structure = SMILES('CO')
)      
        
        

species(
    label = 'CH2CHO',
    reactive = True,
    structure = SMILES('[CH2]C=O')
)      
        
        

species(
    label = 'CH3CHO',
    reactive = True,
    structure = SMILES('CC=O')
)      
        
        

species(
    label = 'CHF3',
    reactive = True,
    structure = SMILES('FC(F)F')
)      
        
        

species(
    label = 'CF2',
    reactive = True,
    structure = SMILES('F[C]F')
)      
        
        

species(
    label = 'CF3',
    reactive = True,
    structure = SMILES('F[C](F)F')
)      
        
        

species(
    label = 'CF3O',
    reactive = True,
    structure = SMILES('[O]C(F)(F)F')
)      
        
        

species(
    label = 'CF2O',
    reactive = True,
    structure = SMILES('O=C(F)F')
)      
        
        

species(
    label = '[O]OF',
    reactive = True,
    structure = SMILES('[O]OF')
)      
        
        

species(
    label = 'O=O',
    reactive = True,
    structure = SMILES('O=O')
)      
        
        

species(
    label = '[O]CF',
    reactive = True,
    structure = SMILES('[O]CF')
)      
        
        

species(
    label = 'OF',
    reactive = True,
    structure = SMILES('OF')
)      
        
        

species(
    label = '[O]OCF',
    reactive = True,
    structure = SMILES('[O]OCF')
)      
        
        

species(
    label = '[O]C([O])F',
    reactive = True,
    structure = SMILES('[O]C([O])F')
)      
        
        

species(
    label = 'FC1OO1',
    reactive = True,
    structure = SMILES('FC1OO1')
)      
        
        

species(
    label = '[O]C(F)F',
    reactive = True,
    structure = SMILES('[O]C(F)F')
)      
        
        

species(
    label = '[O]C(O)(F)F',
    reactive = True,
    structure = SMILES('[O]C(O)(F)F')
)      
        
        

species(
    label = '[O]OC(=O)F',
    reactive = True,
    structure = SMILES('[O]OC(=O)F')
)      
        
        

species(
    label = 'O[C](F)F',
    reactive = True,
    structure = SMILES('O[C](F)F')
)      
        
        

species(
    label = 'OC(F)(F)F',
    reactive = True,
    structure = SMILES('OC(F)(F)F')
)      
        
        

species(
    label = '[O]OC(F)(F)F',
    reactive = True,
    structure = SMILES('[O]OC(F)(F)F')
)      
        
        
    
simulator(
    atol = 1e-16,
    rtol = 1e-08,
    sens_atol = 1e-06,
    sens_rtol = 0.0001,
)


generatedSpeciesConstraints(
    allowed=['input species','seed mechanisms','reaction libraries'],
    maximumCarbonAtoms=8,
    maximumOxygenAtoms=6,
    #maximumHeavyAtoms=24,
    maximumRadicalElectrons=2,
    maximumSingletCarbenes=1,
    maximumCarbeneRadicals=0,
    allowSingletO2 = True,
)

options(
    units = "si",
    generateSeedEachIteration = True,
    generateOutputHTML = True,
    generatePlots = True,
    saveSimulationProfiles = True,
    saveEdgeSpecies = False,
    keepIrreversible = True,
    verboseComments = False,
)
    
    
simpleReactor(
        temperature=[(1000,'K'),(2000,'K')],
        pressure= [(1.0,'bar'),(10.0,'bar')],
        nSims=10,
        initialMoleFractions={
        "CH2F2": 0.5,
        "CH3F": 0.5,
        "O2": 1,
        "N2": 3.76,
        },
        # terminationConversion={
        # 'halogen': 0.999,
        # },
        #terminationRateRatio=1e-4,
        #terminationTime=(10,'s'),
        terminationTime=(1,'s'),
        #sensitivity=['halogen','OH'],
        #sensitivityThreshold=0.001,
        )
        
model(
    toleranceMoveToCore = 0.1,
    toleranceInterruptSimulation = 0.1,
    maximumEdgeSpecies = 3e5,
    filterReactions = True,
    filterThreshold = 5e8,
    minCoreSizeForPrune = 50,
    minSpeciesExistIterationsForPrune = 4,
)

pressureDependence(
    method='modified strong collision',
    maximumGrainSize=(0.5,'kcal/mol'),
    minimumNumberOfGrains=250,
    temperatures=(300,2500,'K',8),
    pressures=(0.01,100,'bar',5),
    interpolation=('Chebyshev', 6, 4),
    maximumAtoms=16,
)

    
    
    