species(
    label = '[OH+]=[C-]C(F)(F)C=C(F)F(5561)',
    structure = adjacencyList("""1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {8,S}
4  F u0 p3 c0 {8,S}
5  O u0 p1 c+1 {9,D} {11,S}
6  C u0 p0 c0 {1,S} {2,S} {7,S} {9,S}
7  C u0 p0 c0 {6,S} {8,D} {10,S}
8  C u0 p0 c0 {3,S} {4,S} {7,D}
9  C u0 p1 c-1 {5,D} {6,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {5,S}
"""),
    E0 = (-487.052,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2850,1437.5,1250,1305,750,350,3010,987.5,1337.5,450,1655,182,240,577,636,1210,1413,180,180,180,180,180,180,908.402],'cm^-1')),
        HinderedRotor(inertia=(0.168412,'amu*angstrom^2'), symmetry=1, barrier=(3.87213,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.171664,'amu*angstrom^2'), symmetry=1, barrier=(3.9469,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (142.052,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.38111,0.0941465,-0.000180245,1.76006e-07,-6.48342e-11,-58462.6,26.9741], Tmin=(100,'K'), Tmax=(839.908,'K')), NASAPolynomial(coeffs=[5.93475,0.0360585,-2.00004e-05,3.96347e-09,-2.759e-13,-58279.5,7.79347], Tmin=(839.908,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-487.052,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(249.434,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(CsCCFF) + group(Cds-CdsCsH) + group(CdCFF) + group(CsJ2_singlet-CsH)"""),
)

species(
    label = 'CO(13)',
    structure = adjacencyList("""1 O u0 p1 c+1 {2,T}
2 C u0 p1 c-1 {1,T}
"""),
    E0 = (-118.741,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2193.04],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (28.01,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(762.44,'J/mol'), sigma=(3.69,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(1.76,'angstroms^3'), rotrelaxcollnum=4.0, comment="""PrimaryTransportLibrary"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.56838,-0.000852123,2.48917e-06,-1.56331e-09,3.13594e-13,-14284.3,3.57912], Tmin=(100,'K'), Tmax=(1571.64,'K')), NASAPolynomial(coeffs=[2.91307,0.00164657,-6.88611e-07,1.21037e-10,-7.84012e-15,-14180.9,6.71043], Tmin=(1571.64,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-118.741,'kJ/mol'), Cp0=(29.1007,'J/(mol*K)'), CpInf=(37.4151,'J/(mol*K)'), label="""CO""", comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'FC(F)=CC(F)F(344)',
    structure = adjacencyList("""1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {7,S}
4 F u0 p3 c0 {7,S}
5 C u0 p0 c0 {1,S} {2,S} {6,S} {8,S}
6 C u0 p0 c0 {5,S} {7,D} {9,S}
7 C u0 p0 c0 {3,S} {4,S} {6,D}
8 H u0 p0 c0 {5,S}
9 H u0 p0 c0 {6,S}
"""),
    E0 = (-792.994,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([171,205,598,1104,1143,1317,1411,3153,3010,987.5,1337.5,450,1655,182,240,577,636,1210,1413,180],'cm^-1')),
        HinderedRotor(inertia=(0.142102,'amu*angstrom^2'), symmetry=1, barrier=(3.2672,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (114.041,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(2858.21,'J/mol'), sigma=(4.57471,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with Tc=446.45 K, Pc=67.74 bar (from Joback method)"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.74532,0.0233589,0.000133412,-5.9431e-07,7.11464e-10,-95378,11.8568], Tmin=(10,'K'), Tmax=(302.26,'K')), NASAPolynomial(coeffs=[4.97982,0.0307765,-2.12832e-05,6.89182e-09,-8.42907e-13,-95561.1,5.58312], Tmin=(302.26,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-792.994,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(203.705,'J/(mol*K)'), label="""FC(F)DCC(F)F""", comment="""Thermo library: CHOF_G4"""),
)

species(
    label = '[OH+]=[C-]C(F)=CC(F)(F)F(5991)',
    structure = adjacencyList("""1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  F u0 p3 c0 {6,S}
4  F u0 p3 c0 {8,S}
5  O u0 p1 c+1 {9,D} {11,S}
6  C u0 p0 c0 {1,S} {2,S} {3,S} {7,S}
7  C u0 p0 c0 {6,S} {8,D} {10,S}
8  C u0 p0 c0 {4,S} {7,D} {9,S}
9  C u0 p1 c-1 {5,D} {8,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {5,S}
"""),
    E0 = (-519.143,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (142.052,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.685843,0.0822099,-0.000139824,1.29934e-07,-4.75357e-11,-62328.1,26.3409], Tmin=(100,'K'), Tmax=(796.929,'K')), NASAPolynomial(coeffs=[7.42101,0.0329247,-1.79225e-05,3.58364e-09,-2.53102e-13,-62910.1,-1.53951], Tmin=(796.929,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-519.143,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(249.434,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(CsCdFFF) + longDistanceInteraction_noncyclic(Cs(F)3-R-Cds(F)) + group(Cds-CdsCsH) + group(CdCCF) + group(CsJ2_singlet-CsH)"""),
)

species(
    label = 'F[OH+][C-]=C(F)C=C(F)F(5992)',
    structure = adjacencyList("""1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {8,S}
4  F u0 p3 c0 {5,S}
5  O u0 p1 c+1 {4,S} {9,S} {11,S}
6  C u0 p0 c0 {7,S} {8,D} {10,S}
7  C u0 p0 c0 {1,S} {6,S} {9,D}
8  C u0 p0 c0 {2,S} {3,S} {6,D}
9  C u0 p1 c-1 {5,S} {7,D}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {5,S}
"""),
    E0 = (-213.569,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,2995,3025,975,1000,1300,1375,400,500,1630,1680,182,240,577,636,1210,1413,180,180,180,180,4000,4000],'cm^-1')),
        HinderedRotor(inertia=(0.293247,'amu*angstrom^2'), symmetry=1, barrier=(6.74232,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.286863,'amu*angstrom^2'), symmetry=1, barrier=(6.59554,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (142.052,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.931981,0.076438,-0.000133399,1.24099e-07,-4.49148e-11,-25584.6,23.5873], Tmin=(100,'K'), Tmax=(812.088,'K')), NASAPolynomial(coeffs=[7.43027,0.028493,-1.54028e-05,3.06601e-09,-2.15509e-13,-26114.5,-3.175], Tmin=(812.088,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-213.569,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(249.434,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(Cds-Cds(Cds-Cds)H) + group(CdCCF) + group(CdCFF) + group(CsJ2_singlet-CsH)"""),
)

species(
    label = 'FC(F)=[C-][OH+]C=C(F)F(5993)',
    structure = adjacencyList("""1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {8,S}
4  F u0 p3 c0 {8,S}
5  O u0 p1 c+1 {6,S} {9,S} {11,S}
6  C u0 p0 c0 {5,S} {7,D} {10,S}
7  C u0 p0 c0 {1,S} {2,S} {6,D}
8  C u0 p0 c0 {3,S} {4,S} {9,D}
9  C u0 p1 c-1 {5,S} {8,D}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {5,S}
"""),
    E0 = (-399.26,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,3010,987.5,1337.5,450,1655,182,240,577,636,1210,1413,2950,3100,1380,975,1025,1650,180,180,180,180,180],'cm^-1')),
        HinderedRotor(inertia=(0.268716,'amu*angstrom^2'), symmetry=1, barrier=(6.17831,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.268076,'amu*angstrom^2'), symmetry=1, barrier=(6.1636,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (142.052,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.540182,0.0916741,-0.000182661,1.79946e-07,-6.58763e-11,-47910.2,25.7634], Tmin=(100,'K'), Tmax=(856.116,'K')), NASAPolynomial(coeffs=[5.42663,0.0333709,-1.83571e-05,3.60254e-09,-2.48216e-13,-47446.9,10.5403], Tmin=(856.116,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-399.26,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(249.434,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(Cds-CdsCsCs) + group(CdCFF) + group(CdCFF) + group(CsJ2_singlet-CsH)"""),
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
    label = '[OH+]=[C-]C(F)=C=C(F)F(5994)',
    structure = adjacencyList("""1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {6,S}
3 F u0 p3 c0 {6,S}
4 O u0 p1 c+1 {8,D} {9,S}
5 C u0 p0 c0 {1,S} {7,D} {8,S}
6 C u0 p0 c0 {2,S} {3,S} {7,D}
7 C u0 p0 c0 {5,D} {6,D}
8 C u0 p1 c-1 {4,D} {5,S}
9 H u0 p0 c0 {4,S}
"""),
    E0 = (-63.0558,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3010,987.5,1337.5,450,1655,94,120,354,641,825,1294,540,610,2055,180,180,180,180,2185.03,2185.21],'cm^-1')),
        HinderedRotor(inertia=(0.205123,'amu*angstrom^2'), symmetry=1, barrier=(4.71618,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (122.045,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.02859,0.0798776,-0.000162185,1.61778e-07,-5.96063e-11,-7490.81,23.9747], Tmin=(100,'K'), Tmax=(859.706,'K')), NASAPolynomial(coeffs=[4.43098,0.0302736,-1.67087e-05,3.27144e-09,-2.24808e-13,-6827.73,15.3333], Tmin=(859.706,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-63.0558,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(203.705,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(CdCddCF) + group(CdCddFF) + group(Cdd-CdsCds) + group(CsJ2_singlet-CsH)"""),
)

species(
    label = '[OH+]=[C-]C(F)(F)C#CF(5995)',
    structure = adjacencyList("""1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 F u0 p3 c0 {8,S}
4 O u0 p1 c+1 {6,D} {9,S}
5 C u0 p0 c0 {1,S} {2,S} {6,S} {7,S}
6 C u0 p1 c-1 {4,D} {5,S}
7 C u0 p0 c0 {5,S} {8,T}
8 C u0 p0 c0 {3,S} {7,T}
9 H u0 p0 c0 {4,S}
"""),
    E0 = (-28.0455,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2850,1437.5,1250,1305,750,350,2175,525,239,401,1367,180,180,180,180,180,649.149,2294.77],'cm^-1')),
        HinderedRotor(inertia=(1.85682,'amu*angstrom^2'), symmetry=1, barrier=(42.692,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.240584,'amu*angstrom^2'), symmetry=1, barrier=(5.5315,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (122.045,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.871266,0.0856426,-0.000180151,1.81229e-07,-6.66342e-11,-3276.53,23.2943], Tmin=(100,'K'), Tmax=(868.984,'K')), NASAPolynomial(coeffs=[3.9791,0.0313395,-1.7373e-05,3.38201e-09,-2.30662e-13,-2306.49,17.4265], Tmin=(868.984,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-28.0455,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(199.547,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(CsCCFF) + group(CsJ2_singlet-CsH) + group(Ct-CtCs) + group(CtCF)"""),
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
    E0 = (-172.568,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (106.507,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (278.108,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (22.8903,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (155.951,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (274.2,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['[OH+]=[C-]C(F)(F)C=C(F)F(5561)'],
    products = ['CO(13)', 'FC(F)=CC(F)F(344)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(351.483,'s^-1'), n=2.72887, Ea=(13.1321,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13055717705123002, var=19.959654271360805, Tref=1000.0, N=68, data_mean=0.0, correlation='Root',), comment="""Estimated from node Root"""),
)

reaction(
    label = 'reaction2',
    reactants = ['[OH+]=[C-]C(F)(F)C=C(F)F(5561)'],
    products = ['[OH+]=[C-]C(F)=CC(F)(F)F(5991)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(7.45932e+11,'s^-1'), n=0.63878, Ea=(292.207,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='F_Ext-2R!H-R',), comment="""Estimated from node F_Ext-2R!H-R
Multiplied by reaction path degeneracy 2.0"""),
)

reaction(
    label = 'reaction3',
    reactants = ['F[OH+][C-]=C(F)C=C(F)F(5992)'],
    products = ['[OH+]=[C-]C(F)(F)C=C(F)F(5561)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(8.88952e+10,'s^-1'), n=0.725184, Ea=(190.324,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005830439029566195, var=4.831276094152293, Tref=1000.0, N=2, data_mean=0.0, correlation='F',), comment="""Estimated from node F"""),
)

reaction(
    label = 'reaction4',
    reactants = ['FC(F)=[C-][OH+]C=C(F)F(5993)'],
    products = ['[OH+]=[C-]C(F)(F)C=C(F)F(5561)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(9.39365e+11,'s^-1'), n=0.324012, Ea=(120.797,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.014478493324023197, var=15.997960675483611, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R!H-inRing_Ext-4R!H-R',), comment="""Estimated from node Root_N-1R!H-inRing_Ext-4R!H-R"""),
)

reaction(
    label = 'reaction5',
    reactants = ['HF(38)', '[OH+]=[C-]C(F)=C=C(F)F(5994)'],
    products = ['[OH+]=[C-]C(F)(F)C=C(F)F(5561)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(2676.63,'m^3/(mol*s)'), n=0.732206, Ea=(198.768,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.13214706218215122, var=14.38614219007748, Tref=1000.0, N=10, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R',), comment="""Estimated from node HF_Ext-3COCdCddCtO2d-R"""),
)

reaction(
    label = 'reaction6',
    reactants = ['HF(38)', '[OH+]=[C-]C(F)(F)C#CF(5995)'],
    products = ['[OH+]=[C-]C(F)(F)C=C(F)F(5561)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(1.64483e+40,'m^3/(mol*s)'), n=-10.004, Ea=(282.007,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd',), comment="""Estimated from node HF_Ext-3COCdCddCtO2d-R_N-3COCdCddCtO2d->Cd"""),
)

network(
    label = 'PDepNetwork #1656',
    isomers = [
        '[OH+]=[C-]C(F)(F)C=C(F)F(5561)',
    ],
    reactants = [
        ('CO(13)', 'FC(F)=CC(F)F(344)'),
    ],
    bathGas = {
        'N2': 0.5,
        'Ne': 0.5,
    },
)

pressureDependence(
    label = 'PDepNetwork #1656',
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

