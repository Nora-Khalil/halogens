species(
    label = 'CC(F)OC(=O)O(13389)',
    structure = adjacencyList("""1  F u0 p3 c0 {5,S}
2  O u0 p2 c0 {5,S} {7,S}
3  O u0 p2 c0 {7,S} {12,S}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {1,S} {2,S} {6,S} {8,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {3,S} {4,D}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
"""),
    E0 = (-870.71,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,261,493,600,1152,1365,1422,3097,2750,2800,2850,1350,1500,750,1050,1375,1000,200,800,960,1120,1280,1440,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (108.068,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.23763,0.0487317,-1.58386e-05,-1.68035e-08,9.91533e-12,-104612,22.5394], Tmin=(100,'K'), Tmax=(1043.05,'K')), NASAPolynomial(coeffs=[15.9852,0.0177017,-7.9231e-06,1.59976e-09,-1.19132e-13,-109077,-55.8869], Tmin=(1043.05,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-870.71,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(266.063,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-O2d)) + group(O2s-(Cds-O2d)H) + group(CsCFHO) + group(Cs-CsHHH) + group(Cds-OdOsOs)"""),
)

species(
    label = 'HF(38)',
    structure = adjacencyList("""1 F u0 p3 c0 {2,S}
2 H u0 p0 c0 {1,S}
"""),
    E0 = (-281.113,'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(20.0062,'amu')),
        LinearRotor(inertia=(0.809097,'amu*angstrom^2'), symmetry=1),
        HarmonicOscillator(frequencies=([4113.43],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (20.0064,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(2743.78,'J/mol'), sigma=(3.148,'angstroms'), dipoleMoment=(1.92,'De'), polarizability=(2.46,'angstroms^3'), rotrelaxcollnum=1.0, comment="""NIST_Fluorine"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.43657,0.000486021,-1.2524e-06,1.36475e-09,-4.09574e-13,-33800.1,1.20682], Tmin=(298,'K'), Tmax=(1250,'K')), NASAPolynomial(coeffs=[2.7813,0.00103959,-2.41735e-07,2.68416e-11,-1.09766e-15,-33504.2,5.0197], Tmin=(1250,'K'), Tmax=(3000,'K'))], Tmin=(298,'K'), Tmax=(3000,'K'), E0=(-281.113,'kJ/mol'), Cp0=(29.1007,'J/mol/K'), CpInf=(37.4151,'J/mol/K'), label="""HF""", comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'CO2(14)',
    structure = adjacencyList("""1 O u0 p2 c0 {3,D}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,D} {2,D}
"""),
    E0 = (-403.138,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([664.558,664.681,1368.23,2264.78],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (44.0094,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(1622.99,'J/mol'), sigma=(3.941,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""PrimaryTransportLibrary"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.35681,0.00898413,-7.12206e-06,2.4573e-09,-1.42885e-13,-48372,9.9009], Tmin=(200,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[4.63651,0.00274146,-9.95898e-07,1.60387e-10,-9.16199e-15,-49024.9,-1.9349], Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(200,'K'), Tmax=(6000,'K'), E0=(-403.138,'kJ/mol'), Cp0=(29.1007,'J/(mol*K)'), CpInf=(62.3585,'J/(mol*K)'), label="""CO2""", comment="""Thermo library: FFCM1(-)"""),
)

species(
    label = 'CH3CHO(36)',
    structure = adjacencyList("""1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p0 c0 {1,D} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
"""),
    E0 = (-178.765,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2800,2850,1350,1500,750,1050,1375,1000,180,1305.65,1305.66,1305.67,3976.84],'cm^-1')),
        HinderedRotor(inertia=(0.136163,'amu*angstrom^2'), symmetry=1, barrier=(3.13064,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (44.0526,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(3625.12,'J/mol'), sigma=(3.97,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=2.0, comment="""GRI-Mech"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.72946,-0.00319329,4.75349e-05,-5.74586e-08,2.19311e-11,-21572.9,4.10302], Tmin=(200,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[5.40411,0.0117231,-4.22631e-06,6.83725e-10,-4.09849e-14,-22593.1,-3.48079], Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(200,'K'), Tmax=(6000,'K'), E0=(-178.765,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(153.818,'J/(mol*K)'), label="""CH3CHO""", comment="""Thermo library: FFCM1(-)"""),
)

species(
    label = 'O=C(O)O(2059)',
    structure = adjacencyList("""1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {4,S} {6,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {1,S}
6 H u0 p0 c0 {2,S}
"""),
    E0 = (-625.106,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3580,3650,1210,1345,900,1100,421.686,423.663,424.543,424.784],'cm^-1')),
        HinderedRotor(inertia=(0.00093875,'amu*angstrom^2'), symmetry=1, barrier=(0.119627,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.344145,'amu*angstrom^2'), symmetry=1, barrier=(43.4791,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (62.0248,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.98124,0.0114379,2.77981e-05,-4.94746e-08,2.0802e-11,-75136.3,10.9454], Tmin=(100,'K'), Tmax=(956.736,'K')), NASAPolynomial(coeffs=[11.8951,0.00171649,-1.48201e-07,9.26559e-11,-1.38667e-14,-78102.6,-38.253], Tmin=(956.736,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-625.106,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(124.717,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-O2d)H) + group(O2s-(Cds-O2d)H) + group(Cds-OdOsOs)"""),
)

species(
    label = 'C[C]F(325)',
    structure = adjacencyList("""1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u0 p1 c0 {1,S} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
"""),
    E0 = (80.9091,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2800,2850,1350,1500,750,1050,1375,1000,180,1049.2],'cm^-1')),
        HinderedRotor(inertia=(0.0264144,'amu*angstrom^2'), symmetry=1, barrier=(3.87782,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (46.0436,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.50526,0.00692148,1.56045e-05,-2.26115e-08,8.49098e-12,9752.45,9.13904], Tmin=(100,'K'), Tmax=(981.304,'K')), NASAPolynomial(coeffs=[5.2739,0.00958149,-3.54759e-06,6.48822e-10,-4.59773e-14,8930.14,-1.78146], Tmin=(981.304,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(80.9091,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(128.874,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(Cs-CsHHH) + group(CJ2_singlet-FCs)"""),
)

species(
    label = 'CHF(40)',
    structure = adjacencyList("""1 F u0 p3 c0 {2,S}
2 C u0 p1 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
"""),
    E0 = (138.756,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1169.21,1416.41,2978.06],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (32.017,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.34484,0.00235461,1.93983e-06,-2.65251e-09,7.91169e-13,16766.1,7.05286], Tmin=(298,'K'), Tmax=(1300,'K')), NASAPolynomial(coeffs=[4.48366,0.00174964,-5.0479e-07,1.08953e-10,-9.87898e-15,16210.2,0.289222], Tmin=(1300,'K'), Tmax=(3000,'K'))], Tmin=(298,'K'), Tmax=(3000,'K'), E0=(138.756,'kJ/mol'), Cp0=(33.2579,'J/mol/K'), CpInf=(58.2013,'J/mol/K'), label="""CHF""", comment="""Thermo library: halogens"""),
)

species(
    label = 'COC(=O)O(13462)',
    structure = adjacencyList("""1 O u0 p2 c0 {4,S} {5,S}
2 O u0 p2 c0 {5,S} {9,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {6,S} {7,S} {8,S}
5 C u0 p0 c0 {1,S} {2,S} {3,D}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
9 H u0 p0 c0 {2,S}
"""),
    E0 = (-607.453,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,2750,2800,2850,1350,1500,750,1050,1375,1000,180,180,912.596,912.617,912.661,912.876],'cm^-1')),
        HinderedRotor(inertia=(0.0494564,'amu*angstrom^2'), symmetry=1, barrier=(29.2351,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(1.27155,'amu*angstrom^2'), symmetry=1, barrier=(29.2354,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.0422353,'amu*angstrom^2'), symmetry=1, barrier=(2.49892,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (76.0514,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.52455,0.0229971,1.35731e-05,-3.37413e-08,1.40675e-11,-72998.3,15.9174], Tmin=(100,'K'), Tmax=(1007.63,'K')), NASAPolynomial(coeffs=[10.626,0.0133539,-5.59225e-06,1.1168e-09,-8.36467e-14,-75774.1,-28.9014], Tmin=(1007.63,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-607.453,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(195.39,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-O2d)) + group(O2s-(Cds-O2d)H) + group(Cs-OsHHH) + group(Cds-OdOsOs)"""),
)

species(
    label = 'CH2(S)(25)',
    structure = adjacencyList("""1 C u0 p1 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
"""),
    E0 = (419.091,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1369.93,2896.01,2896.03],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (14.0266,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1197.29,'J/mol'), sigma=(3.8,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""GRI-Mech"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.10264,-0.00144069,5.4507e-06,-3.58003e-09,7.56195e-13,50400.6,-0.411767], Tmin=(100,'K'), Tmax=(1442.35,'K')), NASAPolynomial(coeffs=[2.62647,0.00394764,-1.49925e-06,2.5454e-10,-1.62957e-14,50691.8,6.78382], Tmin=(1442.35,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(419.091,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(58.2013,'J/(mol*K)'), label="""CH2(S)""", comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'O=C(O)OCF(1971)',
    structure = adjacencyList("""1 F u0 p3 c0 {5,S}
2 O u0 p2 c0 {5,S} {6,S}
3 O u0 p2 c0 {6,S} {9,S}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
6 C u0 p0 c0 {2,S} {3,S} {4,D}
7 H u0 p0 c0 {5,S}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {3,S}
"""),
    E0 = (-821.795,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,548,1085,1183,1302,1466,1520,3060,3119,200,800,960,1120,1280,1440,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (94.0418,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(3747.08,'J/mol'), sigma=(5.60211,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with Tc=585.29 K, Pc=48.36 bar (from Joback method)"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.11895,0.0318523,-3.12024e-06,-2.05953e-08,1.01156e-11,-98763.1,18.9786], Tmin=(100,'K'), Tmax=(1027.4,'K')), NASAPolynomial(coeffs=[12.6679,0.0121109,-5.43846e-06,1.11579e-09,-8.43601e-14,-102056,-37.6776], Tmin=(1027.4,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-821.795,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(195.39,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-O2d)) + group(O2s-(Cds-O2d)H) + group(CsFHHO) + group(Cds-OdOsOs)"""),
)

species(
    label = 'CC(F)OC([O])[O](13463)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {5,S}
2  O u0 p2 c0 {5,S} {7,S}
3  O u1 p2 c0 {7,S}
4  O u1 p2 c0 {7,S}
5  C u0 p0 c0 {1,S} {2,S} {6,S} {8,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {3,S} {4,S} {12,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {7,S}
"""),
    E0 = (-388.419,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([261,493,600,1152,1365,1422,3097,2750,2800,2850,1350,1500,750,1050,1375,1000,1380,1390,370,380,2900,435,180,1496.53,1496.78,1496.87,1497.55],'cm^-1')),
        HinderedRotor(inertia=(0.131132,'amu*angstrom^2'), symmetry=1, barrier=(3.01499,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.131116,'amu*angstrom^2'), symmetry=1, barrier=(3.01462,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.131324,'amu*angstrom^2'), symmetry=1, barrier=(3.01939,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (108.068,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.02037,0.0684689,-0.000157244,1.9851e-07,-8.64915e-11,-46669.1,22.3795], Tmin=(100,'K'), Tmax=(834.036,'K')), NASAPolynomial(coeffs=[-12.0558,0.0692354,-3.85868e-05,7.71773e-09,-5.4196e-13,-41999.7,101.651], Tmin=(834.036,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-388.419,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(270.22,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-CsH) + group(O2s-CsH) + group(CsCFHO) + group(Cs-OsOsOsH) + group(Cs-CsHHH) + radical(OCOJ) + radical(OCOJ)"""),
)

species(
    label = 'C[C](F)OC([O])O(13464)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {7,S}
2  O u0 p2 c0 {5,S} {7,S}
3  O u0 p2 c0 {5,S} {12,S}
4  O u1 p2 c0 {5,S}
5  C u0 p0 c0 {2,S} {3,S} {4,S} {8,S}
6  C u0 p0 c0 {7,S} {9,S} {10,S} {11,S}
7  C u1 p0 c0 {1,S} {2,S} {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {3,S}
"""),
    E0 = (-421.292,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,1380,1390,370,380,2900,435,2750,2800,2850,1350,1500,750,1050,1375,1000,395,473,707,1436,180,180,1856.47,1857.68],'cm^-1')),
        HinderedRotor(inertia=(0.153944,'amu*angstrom^2'), symmetry=1, barrier=(3.53948,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.15355,'amu*angstrom^2'), symmetry=1, barrier=(3.53041,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.154301,'amu*angstrom^2'), symmetry=1, barrier=(3.54769,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.154304,'amu*angstrom^2'), symmetry=1, barrier=(3.54774,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (108.068,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.41644,0.0770127,-0.000161835,1.82689e-07,-7.43417e-11,-50596.3,25.8848], Tmin=(100,'K'), Tmax=(841.159,'K')), NASAPolynomial(coeffs=[-4.36617,0.0536333,-2.9416e-05,5.83157e-09,-4.06818e-13,-47823.6,63.4814], Tmin=(841.159,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-421.292,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(266.063,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-CsH) + group(O2s-CsH) + group(CsCFHO) + group(Cs-OsOsOsH) + group(Cs-CsHHH) + radical(OCOJ) + radical(Csj(Cs-HHH)(F1s)(O2s-Cs))"""),
)

species(
    label = 'C[C](F)O[C](O)O(13465)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {6,S}
2  O u0 p2 c0 {6,S} {7,S}
3  O u0 p2 c0 {7,S} {12,S}
4  O u0 p2 c0 {7,S} {11,S}
5  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C u1 p0 c0 {1,S} {2,S} {5,S}
7  C u1 p0 c0 {2,S} {3,S} {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
"""),
    E0 = (-443.444,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3580,3650,1210,1345,900,1100,2750,2800,2850,1350,1500,750,1050,1375,1000,395,473,707,1436,360,370,350,200,800,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (108.068,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.903149,0.0805004,-0.000147279,1.44452e-07,-5.38048e-11,-53234.4,27.2511], Tmin=(100,'K'), Tmax=(837.786,'K')), NASAPolynomial(coeffs=[4.50177,0.0361289,-1.91525e-05,3.75697e-09,-2.60945e-13,-52883.2,16.2216], Tmin=(837.786,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-443.444,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(261.906,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-CsH) + group(O2s-CsH) + group(CsCFHO) + group(Cs-OsOsOsH) + group(Cs-CsHHH) + radical(Csj(Cs-HHH)(F1s)(O2s-Cs)) + radical(Cs_P)"""),
)

species(
    label = '[CH2]C(F)OC([O])O(13466)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {5,S}
2  O u0 p2 c0 {5,S} {6,S}
3  O u0 p2 c0 {6,S} {12,S}
4  O u1 p2 c0 {6,S}
5  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
6  C u0 p0 c0 {2,S} {3,S} {4,S} {9,S}
7  C u1 p0 c0 {5,S} {10,S} {11,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {3,S}
"""),
    E0 = (-403.117,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,487,638,688,1119,1325,1387,3149,1380,1390,370,380,2900,435,3000,3100,440,815,1455,1000,180,1336.5,1337.01,1337.13],'cm^-1')),
        HinderedRotor(inertia=(0.222804,'amu*angstrom^2'), symmetry=1, barrier=(5.1227,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.222779,'amu*angstrom^2'), symmetry=1, barrier=(5.12212,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.222688,'amu*angstrom^2'), symmetry=1, barrier=(5.12004,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.222486,'amu*angstrom^2'), symmetry=1, barrier=(5.11539,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (108.068,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.34519,0.0770684,-0.000157029,1.74723e-07,-7.0863e-11,-48406.3,26.7233], Tmin=(100,'K'), Tmax=(835.965,'K')), NASAPolynomial(coeffs=[-3.13358,0.0519744,-2.85212e-05,5.66692e-09,-3.96335e-13,-46031.8,57.2515], Tmin=(835.965,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-403.117,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(266.063,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-CsH) + group(O2s-CsH) + group(CsCFHO) + group(Cs-OsOsOsH) + group(Cs-CsHHH) + radical(OCOJ) + radical(Csj(Cs-F1sO2sH)(H)(H))"""),
)

species(
    label = '[CH2]C(F)O[C](O)O(13467)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {5,S}
2  O u0 p2 c0 {5,S} {6,S}
3  O u0 p2 c0 {6,S} {12,S}
4  O u0 p2 c0 {6,S} {11,S}
5  C u0 p0 c0 {1,S} {2,S} {7,S} {8,S}
6  C u1 p0 c0 {2,S} {3,S} {4,S}
7  C u1 p0 c0 {5,S} {9,S} {10,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {7,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {4,S}
12 H u0 p0 c0 {3,S}
"""),
    E0 = (-425.268,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3580,3650,1210,1345,900,1100,487,638,688,1119,1325,1387,3149,360,370,350,3000,3100,440,815,1455,1000,200,800,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (108.068,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.836284,0.0805005,-0.000142258,1.36182e-07,-5.01849e-11,-51044.6,28.0741], Tmin=(100,'K'), Tmax=(827.537,'K')), NASAPolynomial(coeffs=[5.72111,0.0344937,-1.82718e-05,3.59574e-09,-2.50751e-13,-51086.2,10.0656], Tmin=(827.537,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-425.268,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(261.906,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-CsH) + group(O2s-CsH) + group(CsCFHO) + group(Cs-OsOsOsH) + group(Cs-CsHHH) + radical(Cs_P) + radical(Csj(Cs-F1sO2sH)(H)(H))"""),
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
    label = 'C[CH]OC(=O)O(13468)',
    structure = adjacencyList("""multiplicity 2
1  O u0 p2 c0 {5,S} {6,S}
2  O u0 p2 c0 {6,S} {11,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {5,S} {7,S} {8,S} {9,S}
5  C u1 p0 c0 {1,S} {4,S} {10,S}
6  C u0 p0 c0 {1,S} {2,S} {3,D}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {2,S}
"""),
    E0 = (-451.074,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,2750,2800,2850,1350,1500,750,1050,1375,1000,3025,407.5,1350,352.5,200,800,960,1120,1280,1440,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (89.07,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.29494,0.0499374,-3.09184e-05,-1.04238e-09,5.06366e-12,-54145.9,21.6345], Tmin=(100,'K'), Tmax=(1018.52,'K')), NASAPolynomial(coeffs=[15.6998,0.012939,-5.25672e-06,1.02944e-09,-7.62671e-14,-58095.5,-53.1092], Tmin=(1018.52,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-451.074,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(241.12,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-O2d)) + group(O2s-(Cds-O2d)H) + group(Cs-CsOsHH) + group(Cs-CsHHH) + group(Cds-OdOsOs) + radical(CCsJOC(O))"""),
)

species(
    label = '[O]C(=O)O(1570)',
    structure = adjacencyList("""multiplicity 2
1 O u0 p2 c0 {4,S} {5,S}
2 O u1 p2 c0 {4,S}
3 O u0 p2 c0 {4,D}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {1,S}
"""),
    E0 = (-383.185,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,680.736,680.742,680.767,680.776,680.779],'cm^-1')),
        HinderedRotor(inertia=(0.00544604,'amu*angstrom^2'), symmetry=1, barrier=(1.79086,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (61.0168,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(3594.87,'J/mol'), sigma=(5.42485,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with Tc=561.51 K, Pc=51.09 bar (from Joback method)"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.97086,0.00159581,4.23066e-05,-7.29624e-08,3.78807e-11,-46086.4,8.41125], Tmin=(10,'K'), Tmax=(620.938,'K')), NASAPolynomial(coeffs=[2.60714,0.0173834,-1.27477e-05,4.30843e-09,-5.42128e-13,-46052.1,13.2535], Tmin=(620.938,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-383.185,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(108.088,'J/(mol*K)'), label="""[O]C(DO)O""", comment="""Thermo library: 2-BTP_G4"""),
)

species(
    label = 'CH3-CHF(63)',
    structure = adjacencyList("""multiplicity 2
1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,S} {4,S} {5,S} {6,S}
3 C u1 p0 c0 {1,S} {2,S} {7,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {2,S}
7 H u0 p0 c0 {3,S}
"""),
    E0 = (-89.9142,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2800,2850,1350,1500,750,1050,1375,1000,334,575,1197,1424,3202],'cm^-1')),
        HinderedRotor(inertia=(0.0832224,'amu*angstrom^2'), symmetry=1, barrier=(1.91345,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (47.0516,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.9096,0.00783843,1.54328e-05,-2.14834e-08,7.90131e-12,-10814.1,7.80299], Tmin=(10,'K'), Tmax=(888.916,'K')), NASAPolynomial(coeffs=[2.27498,0.019093,-1.0138e-05,2.62844e-09,-2.67692e-13,-10677.5,14.6301], Tmin=(888.916,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-89.9142,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(153.818,'J/(mol*K)'), label="""C[CH]F""", comment="""Thermo library: CHOF_G4"""),
)

species(
    label = 'O=[C]O(457)',
    structure = adjacencyList("""multiplicity 2
1 O u0 p2 c0 {3,S} {4,S}
2 O u0 p2 c0 {3,D}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {1,S}
"""),
    E0 = (-192.093,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1855,455,950,1244.76,1684.94],'cm^-1')),
        HinderedRotor(inertia=(0.00103939,'amu*angstrom^2'), symmetry=1, barrier=(0.119627,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (45.0174,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(4140.61,'J/mol'), sigma=(3.59,'angstroms'), dipoleMoment=(0,'De'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=2.0, comment="""NOx2018"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.92208,0.00762454,3.29884e-06,-1.07135e-08,5.11587e-12,-23028.2,11.2926], Tmin=(200,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[5.39206,0.00411221,-1.48195e-06,2.39875e-10,-1.43903e-14,-23860.7,-2.23529], Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(200,'K'), Tmax=(6000,'K'), E0=(-192.093,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(78.9875,'J/(mol*K)'), label="""HOCO""", comment="""Thermo library: FFCM1(-)"""),
)

species(
    label = 'CC([O])F(1765)',
    structure = adjacencyList("""multiplicity 2
1 F u0 p3 c0 {4,S}
2 O u1 p2 c0 {4,S}
3 C u0 p0 c0 {4,S} {5,S} {6,S} {7,S}
4 C u0 p0 c0 {1,S} {2,S} {3,S} {8,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {4,S}
"""),
    E0 = (-267.374,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2800,2850,1350,1500,750,1050,1375,1000,391,562,707,872,1109,1210,1289,3137],'cm^-1')),
        HinderedRotor(inertia=(0.387883,'amu*angstrom^2'), symmetry=1, barrier=(8.9182,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (63.051,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.9549,0.00279172,8.05062e-05,-1.57947e-07,9.71892e-11,-32155.4,9.14749], Tmin=(10,'K'), Tmax=(506.502,'K')), NASAPolynomial(coeffs=[2.07974,0.0266043,-1.66792e-05,5.06677e-09,-5.94452e-13,-32081,15.7784], Tmin=(506.502,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-267.374,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(178.761,'J/(mol*K)'), label="""CC([O])F""", comment="""Thermo library: CHOF_G4"""),
)

species(
    label = 'OH(7)',
    structure = adjacencyList("""multiplicity 2
1 O u1 p2 c0 {2,S}
2 H u0 p0 c0 {1,S}
"""),
    E0 = (28.3945,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3668.68],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (17.0074,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(665.16,'J/mol'), sigma=(2.75,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""GRI-Mech"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.51457,2.92733e-05,-5.3215e-07,1.01947e-09,-3.85939e-13,3414.25,2.10435], Tmin=(100,'K'), Tmax=(1145.76,'K')), NASAPolynomial(coeffs=[3.07194,0.00060402,-1.39807e-08,-2.13441e-11,2.48061e-15,3579.39,4.57802], Tmin=(1145.76,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(28.3945,'kJ/mol'), Cp0=(29.1007,'J/(mol*K)'), CpInf=(37.4151,'J/(mol*K)'), label="""OH(D)""", comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'CC(F)O[C]=O(13469)',
    structure = adjacencyList("""multiplicity 2
1  F u0 p3 c0 {4,S}
2  O u0 p2 c0 {4,S} {6,S}
3  O u0 p2 c0 {6,D}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {7,S}
5  C u0 p0 c0 {4,S} {8,S} {9,S} {10,S}
6  C u1 p0 c0 {2,S} {3,D}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
"""),
    E0 = (-436.879,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([261,493,600,1152,1365,1422,3097,2750,2800,2850,1350,1500,750,1050,1375,1000,1855,455,950,232.82,232.974],'cm^-1')),
        HinderedRotor(inertia=(1.05792,'amu*angstrom^2'), symmetry=1, barrier=(40.6594,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.0535867,'amu*angstrom^2'), symmetry=1, barrier=(40.656,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.707538,'amu*angstrom^2'), symmetry=1, barrier=(27.1709,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (91.061,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.86781,0.0419398,-3.00533e-05,1.03141e-08,-1.41164e-12,-52463.6,17.991], Tmin=(100,'K'), Tmax=(1700.36,'K')), NASAPolynomial(coeffs=[12.9132,0.0159562,-7.13153e-06,1.32716e-09,-9.03086e-14,-56219.9,-41.1602], Tmin=(1700.36,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-436.879,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(220.334,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-O2d)) + group(CsCFHO) + group(Cs-CsHHH) + group(Cds-OdOsH) + radical((O)CJOC)"""),
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
    label = 'CC(F)OC([O])=O(13470)',
    structure = adjacencyList("""multiplicity 2
1  F u0 p3 c0 {5,S}
2  O u0 p2 c0 {5,S} {7,S}
3  O u1 p2 c0 {7,S}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {1,S} {2,S} {6,S} {8,S}
6  C u0 p0 c0 {5,S} {9,S} {10,S} {11,S}
7  C u0 p0 c0 {2,S} {3,S} {4,D}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
"""),
    E0 = (-626.962,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([261,493,600,1152,1365,1422,3097,2750,2800,2850,1350,1500,750,1050,1375,1000,200,800,933.333,1066.67,1200,1333.33,1466.67,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (107.06,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.50764,0.0466938,-2.89905e-05,4.28415e-09,1.28267e-12,-75309.6,22.0519], Tmin=(100,'K'), Tmax=(1165.91,'K')), NASAPolynomial(coeffs=[13.497,0.0180594,-8.23096e-06,1.60842e-09,-1.15125e-13,-78954.8,-41.2732], Tmin=(1165.91,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-626.962,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(245.277,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-O2d)) + group(O2s-(Cds-O2d)H) + group(CsCFHO) + group(Cs-CsHHH) + group(Cds-OdOsOs) + radical(OC=OOJ)"""),
)

species(
    label = 'CH3(19)',
    structure = adjacencyList("""multiplicity 2
1 C u1 p0 c0 {2,S} {3,S} {4,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
4 H u0 p0 c0 {1,S}
"""),
    E0 = (136.188,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([604.263,1333.71,1492.19,2836.77,2836.77,3806.92],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (15.0346,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1197.29,'J/mol'), sigma=(3.8,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""GRI-Mech"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.65718,0.0021266,5.45839e-06,-6.6181e-09,2.46571e-12,16422.7,1.67354], Tmin=(200,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[2.97812,0.00579785,-1.97558e-06,3.07298e-10,-1.79174e-14,16509.5,4.72248], Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(200,'K'), Tmax=(6000,'K'), E0=(136.188,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(83.1447,'J/(mol*K)'), label="""CH3""", comment="""Thermo library: FFCM1(-)"""),
)

species(
    label = 'O=C(O)O[CH]F(2066)',
    structure = adjacencyList("""multiplicity 2
1 F u0 p3 c0 {6,S}
2 O u0 p2 c0 {5,S} {6,S}
3 O u0 p2 c0 {5,S} {8,S}
4 O u0 p2 c0 {5,D}
5 C u0 p0 c0 {2,S} {3,S} {4,D}
6 C u1 p0 c0 {1,S} {2,S} {7,S}
7 H u0 p0 c0 {6,S}
8 H u0 p0 c0 {3,S}
"""),
    E0 = (-616.383,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,580,1155,1237,1373,3147,200,800,960,1120,1280,1440,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (93.0338,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.91185,0.0384544,-2.67174e-05,2.36132e-09,2.66988e-12,-74052.1,19.363], Tmin=(100,'K'), Tmax=(1047.83,'K')), NASAPolynomial(coeffs=[13.5971,0.00813892,-3.77922e-06,7.84164e-10,-5.95255e-14,-77285.5,-41.3012], Tmin=(1047.83,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-616.383,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(170.447,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-O2d)) + group(O2s-(Cds-O2d)H) + group(CsFHHO) + group(Cds-OdOsOs) + radical(Csj(F1s)(O2s-CO)(H))"""),
)

species(
    label = 'C[C](F)OC(=O)O(13471)',
    structure = adjacencyList("""multiplicity 2
1  F u0 p3 c0 {6,S}
2  O u0 p2 c0 {6,S} {7,S}
3  O u0 p2 c0 {7,S} {11,S}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {6,S} {8,S} {9,S} {10,S}
6  C u1 p0 c0 {1,S} {2,S} {5,S}
7  C u0 p0 c0 {2,S} {3,S} {4,D}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {3,S}
"""),
    E0 = (-676.156,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,2750,2800,2850,1350,1500,750,1050,1375,1000,395,473,707,1436,200,800,960,1120,1280,1440,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (107.06,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.28681,0.0550476,-4.81761e-05,2.03504e-08,-3.40662e-12,-81221.5,23.1675], Tmin=(100,'K'), Tmax=(1424.66,'K')), NASAPolynomial(coeffs=[14.8621,0.0169323,-8.04519e-06,1.57116e-09,-1.11239e-13,-85089.5,-47.1304], Tmin=(1424.66,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-676.156,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(241.12,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-O2d)) + group(O2s-(Cds-O2d)H) + group(CsCFHO) + group(Cs-CsHHH) + group(Cds-OdOsOs) + radical(CsCsF1sO2s)"""),
)

species(
    label = '[CH2]C(F)OC(=O)O(13472)',
    structure = adjacencyList("""multiplicity 2
1  F u0 p3 c0 {5,S}
2  O u0 p2 c0 {5,S} {7,S}
3  O u0 p2 c0 {7,S} {11,S}
4  O u0 p2 c0 {7,D}
5  C u0 p0 c0 {1,S} {2,S} {6,S} {8,S}
6  C u1 p0 c0 {5,S} {9,S} {10,S}
7  C u0 p0 c0 {2,S} {3,S} {4,D}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {3,S}
"""),
    E0 = (-658.01,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,487,638,688,1119,1325,1387,3149,3000,3100,440,815,1455,1000,200,800,960,1120,1280,1440,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (107.06,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.08098,0.0549155,-4.1637e-05,1.09659e-08,1.96961e-13,-79027.4,24.8022], Tmin=(100,'K'), Tmax=(1127.68,'K')), NASAPolynomial(coeffs=[16.2539,0.0149793,-6.98292e-06,1.39661e-09,-1.0196e-13,-83332.2,-54.1358], Tmin=(1127.68,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-658.01,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(241.12,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-O2d)) + group(O2s-(Cds-O2d)H) + group(CsCFHO) + group(Cs-CsHHH) + group(Cds-OdOsOs) + radical(Csj(Cs-F1sO2sH)(H)(H))"""),
)

species(
    label = 'CH2CHF(56)',
    structure = adjacencyList("""1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,S} {2,D} {6,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
6 H u0 p0 c0 {3,S}
"""),
    E0 = (-153.05,'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(46.0219,'amu')),
        NonlinearRotor(inertia=([7.59478,47.6085,55.2033],'amu*angstrom^2'), symmetry=1),
        HarmonicOscillator(frequencies=([482.184,740.114,880.476,949.569,983.363,1189.2,1343.65,1421.6,1725.69,3171.53,3191.61,3269.97],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (46.0436,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.09164,-0.0073724,7.45741e-05,-1.12982e-07,5.61696e-11,-18407.3,6.78145], Tmin=(10,'K'), Tmax=(619.705,'K')), NASAPolynomial(coeffs=[1.44203,0.0189088,-1.12569e-05,3.25441e-09,-3.64262e-13,-18255.1,16.8744], Tmin=(619.705,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-153.05,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(133.032,'J/(mol*K)'), label="""CDCF""", comment="""Thermo library: CHOF_G4"""),
)

species(
    label = 'C=COC(=O)O(2672)',
    structure = adjacencyList("""1  O u0 p2 c0 {4,S} {5,S}
2  O u0 p2 c0 {5,S} {10,S}
3  O u0 p2 c0 {5,D}
4  C u0 p0 c0 {1,S} {6,D} {7,S}
5  C u0 p0 c0 {1,S} {2,S} {3,D}
6  C u0 p0 c0 {4,D} {8,S} {9,S}
7  H u0 p0 c0 {4,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {2,S}
"""),
    E0 = (-531.583,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,3010,987.5,1337.5,450,1655,2950,3100,1380,975,1025,1650,200,800,960,1120,1280,1440,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.062,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(3904.09,'J/mol'), sigma=(5.82319,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with Tc=609.81 K, Pc=44.86 bar (from Joback method)"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.4433,0.041636,-3.00299e-06,-3.74019e-08,2.00431e-11,-63829.3,19.2274], Tmin=(100,'K'), Tmax=(956.19,'K')), NASAPolynomial(coeffs=[18.8941,0.00442633,-7.78836e-07,1.94166e-10,-2.16617e-14,-68802.8,-72.7369], Tmin=(956.19,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-531.583,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(220.334,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-O2d)(Cds-Cd)) + group(O2s-(Cds-O2d)H) + group(Cds-CdsOsH) + group(Cds-OdOsOs) + group(Cds-CdsHH)"""),
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
    E0 = (-443.564,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (-194.276,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (-51.6415,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (-100.837,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (-63.6901,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (-56.0244,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (-133.208,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS8',
    E0 = (-76.2759,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS9',
    E0 = (-88.8827,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS10',
    E0 = (-76.3147,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS11',
    E0 = (-171.232,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS12',
    E0 = (-157.599,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS13',
    E0 = (-106.617,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS14',
    E0 = (-113.29,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS15',
    E0 = (-178.328,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS16',
    E0 = (-162.484,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS17',
    E0 = (-144.338,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS18',
    E0 = (-363.127,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS19',
    E0 = (-303.19,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['CC(F)OC(=O)O(13389)'],
    products = ['HF(38)', 'CO2(14)', 'CH3CHO(36)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(5.65824e+14,'s^-1'), n=-0.436116, Ea=(125.279,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.9927400314419011, var=19.60363129417426, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C',), comment="""Estimated from node Root_N-1R!H->C_5Br1sCl1sF1sH->F1s_Ext-2C-R_N-7R!H->C"""),
)

reaction(
    label = 'reaction2',
    reactants = ['O=C(O)O(2059)', 'C[C]F(325)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(3.5279e-12,'m^3/(mol*s)'), n=5.02686, Ea=(48.0541,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='OH_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1sI1s->F1s',), comment="""Estimated from node OH_N-2Br1sCl1sF1sHI1s->H_2Br1sCl1sF1sI1s->F1s
Multiplied by reaction path degeneracy 2.0"""),
)

reaction(
    label = 'reaction3',
    reactants = ['CHF(40)', 'COC(=O)O(13462)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(2.12553e-07,'m^3/(mol*s)'), n=3.34134, Ea=(115.189,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='CO_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s',), comment="""Estimated from node CO_2Br1sCl1sF1sHI1s->F1s_N-3Br1sCCl1sF1sHI1s->F1s"""),
)

reaction(
    label = 'reaction4',
    reactants = ['CH2(S)(25)', 'O=C(O)OCF(1971)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(3.34162e+07,'m^3/(mol*s)'), n=-0.25099, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.05783420702249951, var=0.11014630093021238, Tref=1000.0, N=12, data_mean=0.0, correlation='CH_Ext-4CbCdCsCt-R',), comment="""Estimated from node CH_Ext-4CbCdCsCt-R
Multiplied by reaction path degeneracy 2.0"""),
)

reaction(
    label = 'reaction5',
    reactants = ['CC(F)OC([O])[O](13463)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(3.898e+11,'s^-1'), n=0.486, Ea=(22.8614,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [R2radExo;Y_rad;XH_Rrad]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Intra_Disproportionation"""),
)

reaction(
    label = 'reaction6',
    reactants = ['C[C](F)OC([O])O(13464)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(7.437e+08,'s^-1'), n=1.045, Ea=(63.4002,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [R3radExo;Y_rad_NDe;XH_Rrad]
Euclidian distance = 0
family: Intra_Disproportionation"""),
)

reaction(
    label = 'reaction7',
    reactants = ['C[C](F)O[C](O)O(13465)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS7',
    kinetics = Arrhenius(A=(1.552e+09,'s^-1'), n=0.311, Ea=(8.368,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""Estimated using template [R4;Y_rad_NDe;XH_Rrad_NDe] for rate rule [R4radEndo;Y_rad_NDe;XH_Rrad_NDe]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 2.0
family: Intra_Disproportionation"""),
)

reaction(
    label = 'reaction8',
    reactants = ['[CH2]C(F)OC([O])O(13466)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS8',
    kinetics = Arrhenius(A=(5.14222e+08,'s^-1'), n=0.311, Ea=(24.9733,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R4;Y_rad;XH_Rrad] for rate rule [R4radExo;Y_rad;XH_Rrad]
Euclidian distance = 1.0
family: Intra_Disproportionation"""),
)

reaction(
    label = 'reaction9',
    reactants = ['[CH2]C(F)O[C](O)O(13467)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS9',
    kinetics = Arrhenius(A=(6.42e+09,'s^-1'), n=0.137, Ea=(34.518,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R5;Y_rad;XH_Rrad_NDe] for rate rule [R5radEndo;Y_rad;XH_Rrad_NDe]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 2.0
family: Intra_Disproportionation"""),
)

reaction(
    label = 'reaction10',
    reactants = ['F(37)', 'C[CH]OC(=O)O(13468)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS10',
    kinetics = Arrhenius(A=(1.52887e+10,'m^3/(mol*s)'), n=-0.421056, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.030895812897821735, var=3.1393582276389975, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_Ext-5R!H-R"""),
)

reaction(
    label = 'reaction11',
    reactants = ['[O]C(=O)O(1570)', 'CH3-CHF(63)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS11',
    kinetics = Arrhenius(A=(1.47663e+07,'m^3/(mol*s)'), n=1.31229e-07, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.016021952005170214, var=0.3543710496450803, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C
Multiplied by reaction path degeneracy 2.0"""),
)

reaction(
    label = 'reaction12',
    reactants = ['O=[C]O(457)', 'CC([O])F(1765)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS12',
    kinetics = Arrhenius(A=(7.38316e+06,'m^3/(mol*s)'), n=1.31229e-07, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.016021952005170214, var=0.3543710496450803, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C"""),
)

reaction(
    label = 'reaction13',
    reactants = ['OH(7)', 'CC(F)O[C]=O(13469)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS13',
    kinetics = Arrhenius(A=(7.7e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C_Ext-2C-R',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C_Ext-2C-R"""),
)

reaction(
    label = 'reaction14',
    reactants = ['H(5)', 'CC(F)OC([O])=O(13470)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS14',
    kinetics = Arrhenius(A=(4.42074e+06,'m^3/(mol*s)'), n=0.349925, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C',), comment="""Estimated from node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C
Multiplied by reaction path degeneracy 2.0"""),
)

reaction(
    label = 'reaction15',
    reactants = ['CH3(19)', 'O=C(O)O[CH]F(2066)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS15',
    kinetics = Arrhenius(A=(1.35279e+19,'m^3/(mol*s)'), n=-4.67047, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=1.1952341712979282, var=4.188869180028304, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_3R!H->F_2CF->C_Ext-1C-R
Ea raised from -5.6 to 0.0 kJ/mol."""),
)

reaction(
    label = 'reaction16',
    reactants = ['H(5)', 'C[C](F)OC(=O)O(13471)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS16',
    kinetics = Arrhenius(A=(1.90705e+22,'m^3/(mol*s)'), n=-6.09098, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R',), comment="""Estimated from node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->C_Sp-4C-2C_Ext-2C-R
Ea raised from -0.4 to 0.0 kJ/mol."""),
)

reaction(
    label = 'reaction17',
    reactants = ['H(5)', '[CH2]C(F)OC(=O)O(13472)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS17',
    kinetics = Arrhenius(A=(6.84097e+21,'m^3/(mol*s)'), n=-5.92191, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.3347815616900648, var=90.07385025150133, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R',), comment="""Estimated from node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->O_N-2CHN->N_2CH->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->C_N-3C-inRing_Ext-3C-R_N-4R!H->C_Sp-3C-2C_Ext-3C-R
Ea raised from -3.7 to 0.0 kJ/mol."""),
)

reaction(
    label = 'reaction18',
    reactants = ['CC(F)OC(=O)O(13389)'],
    products = ['O=C(O)O(2059)', 'CH2CHF(56)'],
    transitionState = 'TS18',
    kinetics = Arrhenius(A=(4.18134e+10,'s^-1'), n=0.636142, Ea=(205.716,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0820842374791673, var=3.1024987137828046, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O',), comment="""Estimated from node Root_N-1R!H->C_N-5R!H->N_Ext-2R!H-R_1BrClFINOPSSi->O
Multiplied by reaction path degeneracy 3.0"""),
)

reaction(
    label = 'reaction19',
    reactants = ['HF(38)', 'C=COC(=O)O(2672)'],
    products = ['CC(F)OC(=O)O(13389)'],
    transitionState = 'TS19',
    kinetics = Arrhenius(A=(25.0352,'m^3/(mol*s)'), n=1.25316, Ea=(207.639,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->F',), comment="""Estimated from node HF_N-3COCdCddCtO2d->Ct_3CdO2d->Cd_Ext-4COCdCddCtO2d-R_N-5R!H->F"""),
)

network(
    label = 'PDepNetwork #3623',
    isomers = [
        'CC(F)OC(=O)O(13389)',
    ],
    reactants = [
        ('HF(38)', 'CO2(14)', 'CH3CHO(36)'),
    ],
    bathGas = {
        'N2': 0.5,
        'Ne': 0.5,
    },
)

pressureDependence(
    label = 'PDepNetwork #3623',
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

