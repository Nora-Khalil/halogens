species(
    label = 'FC=C=C(F)F(5206)',
    structure = adjacencyList("""1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {6,D} {7,S}
5 C u0 p0 c0 {2,S} {3,S} {6,D}
6 C u0 p0 c0 {4,D} {5,D}
7 H u0 p0 c0 {4,S}
"""),
    E0 = (-364.702,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([113,247,382,1207,3490,94,120,354,641,825,1294,540,610,2055,2775.82],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (94.0351,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(2930.43,'J/mol'), sigma=(4.61545,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with Tc=457.73 K, Pc=67.63 bar (from Joback method)"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.78631,0.0191407,1.84311e-05,-5.99612e-08,3.72113e-11,-43861.2,10.8341], Tmin=(10,'K'), Tmax=(620.754,'K')), NASAPolynomial(coeffs=[5.19832,0.0213405,-1.41861e-05,4.38954e-09,-5.1374e-13,-44254.2,2.94178], Tmin=(620.754,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-364.702,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(157.975,'J/(mol*K)'), label="""FCDCDC(F)F""", comment="""Thermo library: CHOF_G4"""),
)

species(
    label = 'F[C]C=C(F)F(290)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 C u0 p0 c0 {5,D} {6,S} {7,S}
5 C u0 p0 c0 {1,S} {2,S} {4,D}
6 C u2 p0 c0 {3,S} {4,S}
7 H u0 p0 c0 {4,S}
"""),
    E0 = (-199.193,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3010,987.5,1337.5,450,1655,182,240,577,636,1210,1413,290.002,290.011,1499.69],'cm^-1')),
        HinderedRotor(inertia=(0.00200412,'amu*angstrom^2'), symmetry=1, barrier=(0.119627,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (94.0351,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(2837.71,'J/mol'), sigma=(4.65594,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with Tc=443.24 K, Pc=63.8 bar (from Joback method)"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.52272,0.0350047,-3.9402e-05,2.35737e-08,-5.77126e-12,-23906.3,16.3068], Tmin=(100,'K'), Tmax=(978.231,'K')), NASAPolynomial(coeffs=[7.71576,0.0137706,-6.84236e-06,1.3845e-09,-1.00585e-13,-24922.3,-8.63235], Tmin=(978.231,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-199.193,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(203.705,'J/(mol*K)'), comment="""Thermo library: CHOF_G4 + radical(CsCCl_triplet)"""),
)

species(
    label = 'F(37)',
    structure = adjacencyList("""multiplicity 2
1 F u1 p3 c0
"""),
    E0 = (72.8916,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (18.9984,'amu'),
    collisionModel = TransportData(shapeIndex=0, epsilon=(665.158,'J/mol'), sigma=(2.75,'angstroms'), dipoleMoment=(0,'De'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""NIST_Fluorine"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.90371,-0.000635296,2.64735e-07,7.69063e-11,-5.45254e-14,8672.27,2.70828], Tmin=(298,'K'), Tmax=(1400,'K')), NASAPolynomial(coeffs=[2.65117,-0.00014013,5.19236e-08,-8.84954e-12,5.9028e-16,8758.29,4.07857], Tmin=(1400,'K'), Tmax=(3000,'K'))], Tmin=(298,'K'), Tmax=(3000,'K'), E0=(72.8916,'kJ/mol'), Cp0=(20.7862,'J/mol/K'), CpInf=(20.7862,'J/mol/K'), label="""F""", comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'C#C[C](F)F(5103)',
    structure = adjacencyList("""multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {6,S}
6 H u0 p0 c0 {5,S}
"""),
    E0 = (-26.8544,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([206,285,386,586,1331,2175,525,750,770,3400,2100],'cm^-1')),
        HinderedRotor(inertia=(1.71463,'amu*angstrom^2'), symmetry=1, barrier=(39.4227,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (75.0367,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.77657,0.0193607,5.56292e-05,-2.69315e-07,2.92795e-10,-3231.84,9.63996], Tmin=(10,'K'), Tmax=(359.491,'K')), NASAPolynomial(coeffs=[5.78028,0.0162647,-1.15608e-05,3.84623e-09,-4.80538e-13,-3499.97,0.297681], Tmin=(359.491,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-26.8544,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(133.032,'J/(mol*K)'), label="""C#C[C](F)F""", comment="""Thermo library: CHOF_G4"""),
)

species(
    label = 'FC#C[CH]F(5082)',
    structure = adjacencyList("""multiplicity 2
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {5,S}
3 C u1 p0 c0 {1,S} {4,S} {6,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {2,S} {4,T}
6 H u0 p0 c0 {3,S}
"""),
    E0 = (45.0609,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([300,424,1135,1289,3214,2175,525,239,401,1367,3931.13],'cm^-1')),
        HinderedRotor(inertia=(0.0154395,'amu*angstrom^2'), symmetry=1, barrier=(18.3074,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (75.0367,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.90024,0.00741053,7.60747e-05,-2.30944e-07,2.00261e-10,5421.02,10.0255], Tmin=(10,'K'), Tmax=(407.55,'K')), NASAPolynomial(coeffs=[4.65259,0.0154555,-1.03221e-05,3.27509e-09,-3.95979e-13,5231.56,5.49913], Tmin=(407.55,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(45.0609,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(124.717,'J/(mol*K)'), label="""FC#C[CH]F""", comment="""Thermo library: CHOF_G4"""),
)

species(
    label = 'H(5)',
    structure = adjacencyList("""multiplicity 2
1 H u1 p0 c0
"""),
    E0 = (211.805,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (1.00797,'amu'),
    collisionModel = TransportData(shapeIndex=0, epsilon=(1205.6,'J/mol'), sigma=(2.05,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""GRI-Mech"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.5,-1.84483e-15,2.71425e-18,-1.30028e-21,1.91033e-25,25474.2,-0.444973], Tmin=(100,'K'), Tmax=(3598.68,'K')), NASAPolynomial(coeffs=[2.5,-2.82485e-12,1.07037e-15,-1.78888e-19,1.11248e-23,25474.2,-0.444973], Tmin=(3598.68,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(211.805,'kJ/mol'), Cp0=(20.7862,'J/(mol*K)'), CpInf=(20.7862,'J/(mol*K)'), label="""H""", comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'F[C]=C=C(F)F(4317)',
    structure = adjacencyList("""multiplicity 2
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 F u0 p3 c0 {6,S}
4 C u0 p0 c0 {1,S} {2,S} {5,D}
5 C u0 p0 c0 {4,D} {6,D}
6 C u1 p0 c0 {3,S} {5,D}
"""),
    E0 = (-151.638,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([94,120,354,641,825,1294,540,610,2055,137,207,812],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (93.0271,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.81697,0.0142144,8.17672e-05,-2.81639e-07,2.55173e-10,-18237.7,11.4722], Tmin=(10,'K'), Tmax=(406.163,'K')), NASAPolynomial(coeffs=[5.51158,0.0188349,-1.39947e-05,4.71475e-09,-5.89764e-13,-18551.1,2.65979], Tmin=(406.163,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-151.638,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(133.032,'J/(mol*K)'), label="""F[C]DCDC(F)F""", comment="""Thermo library: CHOF_G4"""),
)

species(
    label = '[CH]C(F)=C(F)F-2(6375)',
    structure = adjacencyList("""1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {5,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 C u0 p0 c0 {2,S} {3,S} {4,D}
6 C u0 p1 c0 {4,S} {7,S}
7 H u0 p0 c0 {6,S}
"""),
    E0 = (-98.8496,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([405,756,886,1212,182,240,577,636,1210,1413,226.198,226.243,1989,1989.04],'cm^-1')),
        HinderedRotor(inertia=(0.173439,'amu*angstrom^2'), symmetry=1, barrier=(6.29761,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (94.0351,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.94728,0.0507415,-8.81641e-05,8.12829e-08,-2.93903e-11,-11820.4,16.112], Tmin=(100,'K'), Tmax=(796.09,'K')), NASAPolynomial(coeffs=[6.69026,0.0181123,-1.01071e-05,2.03398e-09,-1.43965e-13,-12296.8,-3.93756], Tmin=(796.09,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-98.8496,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(153.818,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(CdCCF) + group(CdCFF) + longDistanceInteraction_noncyclic(Cds(F)2=Cds(F)) + group(CsJ2_singlet-CsH)"""),
)

species(
    label = 'F[C]C=C(F)F-2(6211)',
    structure = adjacencyList("""1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 C u0 p0 c0 {5,D} {6,S} {7,S}
5 C u0 p0 c0 {1,S} {2,S} {4,D}
6 C u0 p1 c0 {3,S} {4,S}
7 H u0 p0 c0 {4,S}
"""),
    E0 = (-223.777,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3010,987.5,1337.5,450,1655,182,240,577,636,1210,1413,315,622,1128],'cm^-1')),
        HinderedRotor(inertia=(0.346675,'amu*angstrom^2'), symmetry=1, barrier=(7.97073,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (94.0351,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.53736,0.0330301,-3.01871e-05,1.357e-08,-2.48101e-12,-26862.3,15.9167], Tmin=(100,'K'), Tmax=(1281.09,'K')), NASAPolynomial(coeffs=[8.95577,0.0129898,-6.72251e-06,1.35932e-09,-9.81616e-14,-28506.9,-16.6384], Tmin=(1281.09,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-223.777,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(153.818,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(Cds-CdsCsH) + group(CdCFF) + group(CJ2_singlet-FC)"""),
)

species(
    label = 'F[C]C(F)=CF(5202)',
    structure = adjacencyList("""1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {6,S}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 C u0 p0 c0 {2,S} {4,D} {7,S}
6 C u0 p1 c0 {3,S} {4,S}
7 H u0 p0 c0 {5,S}
"""),
    E0 = (-200.451,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([405,756,886,1212,194,682,905,1196,1383,3221,315,622,1128,405.868],'cm^-1')),
        HinderedRotor(inertia=(1.20903,'amu*angstrom^2'), symmetry=1, barrier=(27.7979,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (94.0351,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.41902,0.0362497,-3.49255e-05,1.62035e-08,-3.0371e-12,-24053.2,15.2113], Tmin=(100,'K'), Tmax=(1255.66,'K')), NASAPolynomial(coeffs=[9.69591,0.0130687,-7.23371e-06,1.50114e-09,-1.0989e-13,-25880.6,-21.5522], Tmin=(1255.66,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-200.451,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(153.818,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(CdCCF) + longDistanceInteraction_noncyclic(Cds(F)=Cds(F)) + group(CdCFH) + longDistanceInteraction_noncyclic(Cds(F)=Cds(F)) + group(CJ2_singlet-FC)"""),
)

species(
    label = 'N2',
    structure = adjacencyList("""1 N u0 p1 c0 {2,T}
2 N u0 p1 c0 {1,T}
"""),
    E0 = (-8.64289,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (28.0137,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(810.913,'J/mol'), sigma=(3.621,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(1.76,'angstroms^3'), rotrelaxcollnum=4.0, comment="""PrimaryTransportLibrary"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.53101,-0.000123661,-5.02999e-07,2.43531e-09,-1.40881e-12,-1046.98,2.96747], Tmin=(200,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[2.95258,0.0013969,-4.92632e-07,7.8601e-11,-4.60755e-15,-923.949,5.87189], Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(200,'K'), Tmax=(6000,'K'), E0=(-8.64289,'kJ/mol'), Cp0=(29.1007,'J/(mol*K)'), CpInf=(37.4151,'J/(mol*K)'), label="""N2""", comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'Ne',
    structure = adjacencyList("""1 Ne u0 p4 c0
"""),
    E0 = (-6.19738,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (20.1801,'amu'),
    collisionModel = TransportData(shapeIndex=0, epsilon=(1235.53,'J/mol'), sigma=(3.758e-10,'m'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with fixed Lennard Jones Parameters. This is the fallback method! Try improving transport databases!"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,3.35532], Tmin=(200,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[2.5,0,0,0,0,-745.375,3.35532], Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(200,'K'), Tmax=(6000,'K'), E0=(-6.19738,'kJ/mol'), Cp0=(20.7862,'J/(mol*K)'), CpInf=(20.7862,'J/(mol*K)'), label="""Ne""", comment="""Thermo library: primaryThermoLibrary"""),
)

transitionState(
    label = 'TS1',
    E0 = (-111.525,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (110.843,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (182.759,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (124.973,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (75.1133,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (-65.6004,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (10.231,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction21',
    reactants = ['F[C]C=C(F)F(290)'],
    products = ['FC=C=C(F)F(5206)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(1.949e+11,'s^-1'), n=0.486, Ea=(22.8614,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [R2radExo;Y_rad;XH_Rrad]
Euclidian distance = 0
family: Intra_Disproportionation"""),
)

reaction(
    label = 'reaction30',
    reactants = ['F(37)', 'C#C[C](F)F(5103)'],
    products = ['FC=C=C(F)F(5206)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(1.11549e+09,'m^3/(mol*s)'), n=-0.68237, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.29431919638206655, var=1.0853977775937997, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-3BrCO-R_Sp-3BrBrCCOO=1C"""),
)

reaction(
    label = 'reaction31',
    reactants = ['F(37)', 'FC#C[CH]F(5082)'],
    products = ['FC=C=C(F)F(5206)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(1e+06,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_N-2CF->C',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_N-2CF->C
Ea raised from -0.1 to 0.0 kJ/mol."""),
)

reaction(
    label = 'reaction32',
    reactants = ['H(5)', 'F[C]=C=C(F)F(4317)'],
    products = ['FC=C=C(F)F(5206)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(1e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->C',), comment="""Estimated from node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->Br_5CF->C
Ea raised from -2.0 to 0.0 kJ/mol."""),
)

reaction(
    label = 'reaction33',
    reactants = ['[CH]C(F)=C(F)F-2(6375)'],
    products = ['FC=C=C(F)F(5206)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(1.91033e+10,'s^-1'), n=0.827, Ea=(109.157,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCY',), comment="""Estimated from node CCY"""),
)

reaction(
    label = 'reaction34',
    reactants = ['F[C]C=C(F)F-2(6211)'],
    products = ['FC=C=C(F)F(5206)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(3.33334e+12,'s^-1'), n=-1.40567e-07, Ea=(93.3703,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCH_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F',), comment="""Estimated from node CCH_Ext-3C-R_N-4R!H->Br_4CClFINOPSSi->F"""),
)

reaction(
    label = 'reaction35',
    reactants = ['F[C]C(F)=CF(5202)'],
    products = ['FC=C=C(F)F(5206)'],
    transitionState = 'TS7',
    kinetics = Arrhenius(A=(1.91033e+10,'s^-1'), n=0.827, Ea=(145.876,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CCY',), comment="""Estimated from node CCY"""),
)

network(
    label = 'PDepNetwork #2744',
    isomers = [
        'FC=C=C(F)F(5206)',
    ],
    reactants = [
    ],
    bathGas = {
        'N2': 0.5,
        'Ne': 0.5,
    },
)

pressureDependence(
    label = 'PDepNetwork #2744',
    Tmin = (300,'K'),
    Tmax = (2500,'K'),
    Tcount = 8,
    Tlist = ([302.558,324.028,372.925,464.512,632.697,950.724,1545.17,2335.46],'K'),
    Pmin = (0.01,'bar'),
    Pmax = (100,'bar'),
    Pcount = 5,
    Plist = ([0.0125282,0.0667467,1,14.982,79.8202],'bar'),
    maximumGrainSize = (0.5,'kcal/mol'),
    minimumGrainCount = 250,
    method = 'modified strong collision',
    interpolationModel = ('Chebyshev', 6, 4),
    activeKRotor = True,
    activeJRotor = True,
    rmgmode = True,
)

