species(
    label = 'C=C([O])C[C](F)F(3131)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  O u1 p2 c0 {5,S}
4  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {7,D}
6  C u1 p0 c0 {1,S} {2,S} {4,S}
7  C u0 p0 c0 {5,D} {10,S} {11,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
"""),
    E0 = (-302.345,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2850,1437.5,1250,1305,750,350,350,440,435,1725,190,488,555,1236,1407,2950,3100,1380,975,1025,1650,282.601,282.711,4000],'cm^-1')),
        HinderedRotor(inertia=(0.381043,'amu*angstrom^2'), symmetry=1, barrier=(21.6155,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.381395,'amu*angstrom^2'), symmetry=1, barrier=(21.618,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.15653,0.0567821,-5.60201e-05,2.76571e-08,-5.34978e-12,-36256.5,25.5036], Tmin=(100,'K'), Tmax=(1261.68,'K')), NASAPolynomial(coeffs=[14.5385,0.0143566,-5.58118e-06,1.0056e-09,-6.88701e-14,-39633.3,-42.1675], Tmin=(1261.68,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-302.345,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(249.434,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-Cd)H) + group(Cs-(Cds-Cds)CsHH) + group(CsCsFFH) + group(Cds-CdsCsOs) + group(Cds-CdsHH) + radical(C=C(C)OJ) + radical(Csj(Cs-CdHH)(F1s)(F1s))"""),
)

species(
    label = 'CH2CF2(57)',
    structure = adjacencyList("""1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u0 p0 c0 {4,D} {5,S} {6,S}
4 C u0 p0 c0 {1,S} {2,S} {3,D}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
"""),
    E0 = (-361.616,'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(64.0125,'amu')),
        NonlinearRotor(inertia=([45.7027,48.2614,93.9642],'amu*angstrom^2'), symmetry=2),
        HarmonicOscillator(frequencies=([437.293,557.015,653.832,726.079,816.319,956,966.438,1345.56,1413.22,1792.31,3202.97,3303.55],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (64.034,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(2091.09,'J/mol'), sigma=(4.442,'angstroms'), dipoleMoment=(1.4,'De'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""NIST_Fluorine"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.10281,-0.0101072,0.000121983,-2.28108e-07,1.37933e-10,-43490.6,7.77929], Tmin=(10,'K'), Tmax=(534.293,'K')), NASAPolynomial(coeffs=[2.52167,0.0198841,-1.31824e-05,4.13929e-09,-4.93215e-13,-43580.8,11.9914], Tmin=(534.293,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-361.616,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(133.032,'J/(mol*K)'), label="""CDC(F)F""", comment="""Thermo library: CHOF_G4"""),
)

species(
    label = 'CH2CO(28)',
    structure = adjacencyList("""1 O u0 p2 c0 {3,D}
2 C u0 p0 c0 {3,D} {4,S} {5,S}
3 C u0 p0 c0 {1,D} {2,D}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
"""),
    E0 = (-60.8183,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2950,3100,1380,975,1025,1650,2120,512.5,787.5],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (42.0366,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(3625.12,'J/mol'), sigma=(3.97,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=2.0, comment="""GRI-Mech"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.13241,0.0181319,-1.74093e-05,9.35336e-09,-2.01725e-12,-7148.09,13.3808], Tmin=(200,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[5.75871,0.00635124,-2.25955e-06,3.62322e-10,-2.15856e-14,-8085.33,-4.9649], Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(200,'K'), Tmax=(6000,'K'), E0=(-60.8183,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(108.088,'J/(mol*K)'), label="""CH2CO""", comment="""Thermo library: FFCM1(-)"""),
)

species(
    label = '[CH2]C(F)(F)C(=C)[O](3151)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {4,S}
2  F u0 p3 c0 {4,S}
3  O u1 p2 c0 {5,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5  C u0 p0 c0 {3,S} {4,S} {7,D}
6  C u1 p0 c0 {4,S} {8,S} {9,S}
7  C u0 p0 c0 {5,D} {10,S} {11,S}
8  H u0 p0 c0 {6,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
"""),
    E0 = (-288.57,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([248,333,466,604,684,796,1061,1199,350,440,435,1725,3000,3100,440,815,1455,1000,2950,3100,1380,975,1025,1650,180],'cm^-1')),
        HinderedRotor(inertia=(0.358535,'amu*angstrom^2'), symmetry=1, barrier=(8.24343,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.358443,'amu*angstrom^2'), symmetry=1, barrier=(8.24131,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.918896,0.0742729,-0.000117693,1.01863e-07,-3.49487e-11,-34602.3,22.7592], Tmin=(100,'K'), Tmax=(810.938,'K')), NASAPolynomial(coeffs=[8.75264,0.0267506,-1.33616e-05,2.58619e-09,-1.79549e-13,-35580.8,-11.5917], Tmin=(810.938,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-288.57,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(249.434,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-Cd)H) + group(CsCCFF) + longDistanceInteraction_noncyclic(Cs(F)2-CdOs) + group(Cs-CsHHH) + group(Cds-CdsCsOs) + group(Cds-CdsHH) + radical(C=C(C)OJ) + radical(Csj(Cs-F1sF1sCd)(H)(H))"""),
)

species(
    label = 'F[C]F(156)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u2 p0 c0 {1,S} {2,S}
"""),
    E0 = (33.7272,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([700.388,993.445,1307.31],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (50.0074,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.28591,0.0107608,-1.05382e-05,4.89881e-09,-8.86384e-13,4216.69,13.1348], Tmin=(298,'K'), Tmax=(1300,'K')), NASAPolynomial(coeffs=[5.33121,0.00197748,-9.60248e-07,2.10704e-10,-1.5954e-14,3366.49,-2.56367], Tmin=(1300,'K'), Tmax=(3000,'K'))], Tmin=(298,'K'), Tmax=(3000,'K'), E0=(33.7272,'kJ/mol'), Cp0=(33.2579,'J/mol/K'), CpInf=(58.2013,'J/mol/K'), label="""CF2(T)""", comment="""Thermo library: halogens"""),
)

species(
    label = '[CH2]C(=C)[O](6456)',
    structure = adjacencyList("""multiplicity 3
1 O u1 p2 c0 {2,S}
2 C u0 p0 c0 {1,S} {3,S} {4,D}
3 C u1 p0 c0 {2,S} {7,S} {8,S}
4 C u0 p0 c0 {2,D} {5,S} {6,S}
5 H u0 p0 c0 {4,S}
6 H u0 p0 c0 {4,S}
7 H u0 p0 c0 {3,S}
8 H u0 p0 c0 {3,S}
"""),
    E0 = (110.41,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([350,440,435,1725,3000,3100,440,815,1455,1000,2950,3100,1380,975,1025,1650,1477.82],'cm^-1')),
        HinderedRotor(inertia=(0.530916,'amu*angstrom^2'), symmetry=1, barrier=(12.2068,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (56.0632,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.69662,0.0242907,-7.63676e-06,-9.31843e-09,6.21032e-12,13330.3,14.3522], Tmin=(100,'K'), Tmax=(924.136,'K')), NASAPolynomial(coeffs=[8.66414,0.00984176,-2.65664e-06,4.14902e-10,-2.77495e-14,11741.3,-16.5962], Tmin=(924.136,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(110.41,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(224.491,'J/(mol*K)'), comment="""Thermo library: DFT_QCI_thermo + radical(C=C(C)OJ) + radical(C=C(O)CJ)"""),
)

species(
    label = 'O(6)',
    structure = adjacencyList("""multiplicity 3
1 O u2 p2 c0
"""),
    E0 = (243.034,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (15.9994,'amu'),
    collisionModel = TransportData(shapeIndex=0, epsilon=(665.16,'J/mol'), sigma=(2.75,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""GRI-Mech"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.5,-1.84483e-15,2.71425e-18,-1.30028e-21,1.91033e-25,29230.2,5.12616], Tmin=(100,'K'), Tmax=(3598.68,'K')), NASAPolynomial(coeffs=[2.5,-2.82485e-12,1.07037e-15,-1.78888e-19,1.11248e-23,29230.2,5.12616], Tmin=(3598.68,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(243.034,'kJ/mol'), Cp0=(20.7862,'J/(mol*K)'), CpInf=(20.7862,'J/(mol*K)'), label="""O(T)""", comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'C=[C]C[C](F)F(6457)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {4,S}
2  F u0 p3 c0 {4,S}
3  C u0 p0 c0 {4,S} {6,S} {7,S} {8,S}
4  C u1 p0 c0 {1,S} {2,S} {3,S}
5  C u0 p0 c0 {6,D} {9,S} {10,S}
6  C u1 p0 c0 {3,S} {5,D}
7  H u0 p0 c0 {3,S}
8  H u0 p0 c0 {3,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {5,S}
"""),
    E0 = (5.27255,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2850,1437.5,1250,1305,750,350,190,488,555,1236,1407,2950,3100,1380,975,1025,1650,1685,370,180,180],'cm^-1')),
        HinderedRotor(inertia=(0.174506,'amu*angstrom^2'), symmetry=1, barrier=(4.01223,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.173344,'amu*angstrom^2'), symmetry=1, barrier=(3.98551,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (90.0713,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.85087,0.0534165,-8.25249e-05,7.6958e-08,-2.8593e-11,705.562,20.6252], Tmin=(100,'K'), Tmax=(806.814,'K')), NASAPolynomial(coeffs=[4.76329,0.0276677,-1.3627e-05,2.65376e-09,-1.85499e-13,603.709,9.48087], Tmin=(806.814,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(5.27255,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(274.378,'J/(mol*K)'), comment="""Thermo library: CHOF_G4 + radical(Csj(Cs-CdHH)(F1s)(F1s)) + radical(Cds_S)"""),
)

species(
    label = 'C=C1CC(F)(F)O1(6420)',
    structure = adjacencyList("""1  F u0 p3 c0 {5,S}
2  F u0 p3 c0 {5,S}
3  O u0 p2 c0 {5,S} {6,S}
4  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
6  C u0 p0 c0 {3,S} {4,S} {7,D}
7  C u0 p0 c0 {6,D} {10,S} {11,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
"""),
    E0 = (-515.653,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.53707,0.0354003,3.03597e-05,-8.05548e-08,3.83392e-11,-61912.5,14.8276], Tmin=(100,'K'), Tmax=(910.933,'K')), NASAPolynomial(coeffs=[20.2386,0.00275984,2.63086e-06,-6.32818e-10,4.03972e-14,-67372.6,-84.9201], Tmin=(910.933,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-515.653,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(257.749,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-Cd)) + group(Cs-(Cds-Cds)CsHH) + group(CsCFFO) + group(Cds-CdsCsOs) + group(Cds-CdsHH) + ring(2methyleneoxetane)"""),
)

species(
    label = 'C=C(O)C=C(F)F(6458)',
    structure = adjacencyList("""1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  O u0 p2 c0 {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,S} {6,D}
5  C u0 p0 c0 {4,S} {7,D} {8,S}
6  C u0 p0 c0 {4,D} {9,S} {10,S}
7  C u0 p0 c0 {1,S} {2,S} {5,D}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {3,S}
"""),
    E0 = (-512.794,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.324541,0.0667377,-7.19641e-05,3.67101e-08,-7.00298e-12,-61530.5,22.2963], Tmin=(100,'K'), Tmax=(1447.11,'K')), NASAPolynomial(coeffs=[19.493,0.00575937,-4.70618e-07,-4.36233e-11,6.0277e-15,-66241.2,-74.3722], Tmin=(1447.11,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-512.794,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(249.434,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-Cd)H) + group(Cds-Cds(Cds-Cds)O2s) + group(Cds-Cds(Cds-Cds)H) + group(Cds-CdsHH) + group(CdCFF)"""),
)

species(
    label = 'F[C](F)C[C]1CO1(6459)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  O u0 p2 c0 {5,S} {6,S}
4  C u0 p0 c0 {6,S} {7,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {6,S} {10,S} {11,S}
6  C u1 p0 c0 {3,S} {4,S} {5,S}
7  C u1 p0 c0 {1,S} {2,S} {4,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
"""),
    E0 = (-156.906,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.26289,0.0636224,-8.92605e-05,6.94732e-08,-2.07235e-11,-18776,23.0259], Tmin=(100,'K'), Tmax=(984.659,'K')), NASAPolynomial(coeffs=[8.2437,0.0226318,-7.57311e-06,1.13755e-09,-6.54128e-14,-19538.4,-7.4349], Tmin=(984.659,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-156.906,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(249.434,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(Cs-CsCsOsH) + group(Cs-CsCsHH) + group(Cs-CsOsHH) + group(CsCsFFH) + ring(Ethylene_oxide) + radical(C2CsJO) + radical(Csj(Cs-CsHH)(F1s)(F1s))"""),
)

species(
    label = '[O][C]1CC(F)(F)C1(6460)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {4,S}
2  F u0 p3 c0 {4,S}
3  O u1 p2 c0 {7,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
7  C u1 p0 c0 {3,S} {5,S} {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
"""),
    E0 = (-191.678,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.59718,0.0456059,-2.9088e-05,6.47166e-09,2.36973e-13,-22961.1,20.81], Tmin=(100,'K'), Tmax=(1205.81,'K')), NASAPolynomial(coeffs=[12.3753,0.0194,-8.36614e-06,1.58198e-09,-1.10786e-13,-26254.5,-36.0837], Tmin=(1205.81,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-191.678,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(257.749,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsH) + group(Cs-CsCsOsH) + group(Cs-CsCsHH) + group(Cs-CsCsHH) + group(CsCsCsFF) + ring(Cs-Cs-Cs(F)(F)-Cs) + radical(CC(C)OJ) + radical(C2CsJOH)"""),
)

species(
    label = '[CH2]C1([O])CC1(F)F(6461)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  O u1 p2 c0 {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,S} {7,S}
5  C u0 p0 c0 {4,S} {6,S} {8,S} {9,S}
6  C u0 p0 c0 {1,S} {2,S} {4,S} {5,S}
7  C u1 p0 c0 {4,S} {10,S} {11,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
"""),
    E0 = (-113.685,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.17735,0.0583073,-5.65982e-05,2.78111e-08,-5.42308e-12,-13568.3,21.3354], Tmin=(100,'K'), Tmax=(1240.22,'K')), NASAPolynomial(coeffs=[13.7794,0.0176624,-7.4393e-06,1.38617e-09,-9.6376e-14,-16694.2,-42.1754], Tmin=(1240.22,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-113.685,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(253.591,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsH) + group(Cs-CsCsCsOs) + group(Cs-CsCsHH) + group(CsCsCsFF) + group(Cs-CsHHH) + ring(Cs(F)(F)-Cs(C)-Cs) + radical(CC(C)2OJ) + radical(CJC(C)2O)"""),
)

species(
    label = '[CH2][C]=O(4470)',
    structure = adjacencyList("""multiplicity 3
1 O u0 p2 c0 {3,D}
2 C u1 p0 c0 {3,S} {4,S} {5,S}
3 C u1 p0 c0 {1,D} {2,S}
4 H u0 p0 c0 {2,S}
5 H u0 p0 c0 {2,S}
"""),
    E0 = (160.185,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3000,3100,440,815,1455,1000,539.612,539.669],'cm^-1')),
        HinderedRotor(inertia=(0.000578908,'amu*angstrom^2'), symmetry=1, barrier=(0.119627,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (42.0366,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.39563,0.0101365,2.3074e-06,-8.97566e-09,3.68242e-12,19290.3,10.0703], Tmin=(100,'K'), Tmax=(1068.9,'K')), NASAPolynomial(coeffs=[6.35055,0.00638951,-2.69368e-06,5.4221e-10,-4.02476e-14,18240.9,-6.33602], Tmin=(1068.9,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(160.185,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(153.818,'J/(mol*K)'), comment="""Thermo library: FFCM1(-) + radical(CJC=O) + radical(CsCJ=O)"""),
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
    label = 'C=C([O])C=C(F)F(6462)',
    structure = adjacencyList("""multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  O u1 p2 c0 {4,S}
4  C u0 p0 c0 {3,S} {5,S} {6,D}
5  C u0 p0 c0 {4,S} {7,D} {8,S}
6  C u0 p0 c0 {4,D} {9,S} {10,S}
7  C u0 p0 c0 {1,S} {2,S} {5,D}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
"""),
    E0 = (-374.989,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([350,440,435,1725,3010,987.5,1337.5,450,1655,2950,3100,1380,975,1025,1650,182,240,577,636,1210,1413,180,180],'cm^-1')),
        HinderedRotor(inertia=(0.774915,'amu*angstrom^2'), symmetry=1, barrier=(17.8168,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (105.063,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.18196,0.0570639,-5.9972e-05,2.90968e-08,-4.74919e-12,-44994.9,20.7145], Tmin=(100,'K'), Tmax=(971.732,'K')), NASAPolynomial(coeffs=[14.7375,0.0108933,-3.56484e-06,5.95274e-10,-3.99988e-14,-48084,-46.6336], Tmin=(971.732,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-374.989,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(228.648,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-Cd)H) + group(Cds-Cds(Cds-Cds)O2s) + group(Cds-Cds(Cds-Cds)H) + group(Cds-CdsHH) + group(CdCFF) + radical(C=C(C)OJ)"""),
)

species(
    label = '[CH2][C](F)F(163)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {4,S}
2 F u0 p3 c0 {4,S}
3 C u1 p0 c0 {4,S} {5,S} {6,S}
4 C u1 p0 c0 {1,S} {2,S} {3,S}
5 H u0 p0 c0 {3,S}
6 H u0 p0 c0 {3,S}
"""),
    E0 = (-109.048,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3000,3100,440,815,1455,1000,190,488,555,1236,1407],'cm^-1')),
        HinderedRotor(inertia=(0.00258864,'amu*angstrom^2'), symmetry=1, barrier=(7.63529,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (64.034,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.25818,0.018626,-1.56415e-05,8.22322e-09,-2.04586e-12,-13090.7,13.5552], Tmin=(100,'K'), Tmax=(887.641,'K')), NASAPolynomial(coeffs=[4.47008,0.0131648,-6.41281e-06,1.29207e-09,-9.37479e-14,-13305.9,7.85294], Tmin=(887.641,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-109.048,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(178.761,'J/(mol*K)'), comment="""Thermo library: CHOF_G4 + radical(Cs_P) + radical(CsCsF1sF1s)"""),
)

species(
    label = 'CF2(43)',
    structure = adjacencyList("""1 F u0 p3 c0 {3,S}
2 F u0 p3 c0 {3,S}
3 C u0 p1 c0 {1,S} {2,S}
"""),
    E0 = (-203.712,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([192,594,627],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (50.0074,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(897.963,'J/mol'), sigma=(3.977,'angstroms'), dipoleMoment=(0,'De'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""NIST_Fluorine"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.28591,0.0107608,-1.05382e-05,4.89881e-09,-8.86384e-13,-24340.7,13.1348], Tmin=(298,'K'), Tmax=(1300,'K')), NASAPolynomial(coeffs=[5.33121,0.00197748,-9.60248e-07,2.10704e-10,-1.5954e-14,-25190.9,-2.56367], Tmin=(1300,'K'), Tmax=(3000,'K'))], Tmin=(298,'K'), Tmax=(3000,'K'), E0=(-203.712,'kJ/mol'), Cp0=(33.2579,'J/mol/K'), CpInf=(58.2013,'J/mol/K'), label="""CF2""", comment="""Thermo library: halogens"""),
)

species(
    label = '[CH2]C([O])=CC(F)F(6463)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {4,S}
2  F u0 p3 c0 {4,S}
3  O u1 p2 c0 {6,S}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {8,S}
5  C u0 p0 c0 {4,S} {6,D} {9,S}
6  C u0 p0 c0 {3,S} {5,D} {7,S}
7  C u1 p0 c0 {6,S} {10,S} {11,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
"""),
    E0 = (-341.705,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.32175,0.0584807,-6.45611e-05,3.73853e-08,-8.62893e-12,-41000.7,23.5986], Tmin=(100,'K'), Tmax=(1054.03,'K')), NASAPolynomial(coeffs=[11.8523,0.0185181,-7.69086e-06,1.4157e-09,-9.7615e-14,-43220.7,-27.7596], Tmin=(1054.03,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-341.705,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(249.434,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-Cd)H) + group(Cs-(Cds-Cds)HHH) + group(CsCFFH) + group(Cds-CdsCsOs) + group(Cds-CdsCsH) + radical(C=C(C)OJ) + radical(C=C(O)CJ)"""),
)

species(
    label = '[CH2]C(O)=C[C](F)F(6464)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  O u0 p2 c0 {4,S} {11,S}
4  C u0 p0 c0 {3,S} {5,D} {6,S}
5  C u0 p0 c0 {4,D} {7,S} {8,S}
6  C u1 p0 c0 {4,S} {9,S} {10,S}
7  C u1 p0 c0 {1,S} {2,S} {5,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {3,S}
"""),
    E0 = (-320.781,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.800778,0.064274,-6.74613e-05,3.18254e-08,-4.85932e-12,-38460.4,24.1105], Tmin=(100,'K'), Tmax=(977.008,'K')), NASAPolynomial(coeffs=[16.7515,0.0108022,-3.53273e-06,5.99527e-10,-4.1099e-14,-42141.9,-55.3617], Tmin=(977.008,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-320.781,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(245.277,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-Cd)H) + group(Cs-(Cds-Cds)HHH) + group(CsCFFH) + group(Cds-CdsCsOs) + group(Cds-CdsCsH) + radical(C=C(O)CJ) + radical(Csj(Cd-CdH)(F1s)(F1s))"""),
)

species(
    label = '[CH]=C(O)C[C](F)F(6465)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  O u0 p2 c0 {5,S} {10,S}
4  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {3,S} {4,S} {7,D}
6  C u1 p0 c0 {1,S} {2,S} {4,S}
7  C u1 p0 c0 {5,D} {11,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {3,S}
11 H u0 p0 c0 {7,S}
"""),
    E0 = (-193.054,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,2750,2850,1437.5,1250,1305,750,350,350,440,435,1725,190,488,555,1236,1407,3120,650,792.5,1650,231.808],'cm^-1')),
        HinderedRotor(inertia=(0.438369,'amu*angstrom^2'), symmetry=1, barrier=(16.6289,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.435399,'amu*angstrom^2'), symmetry=1, barrier=(16.6245,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.437429,'amu*angstrom^2'), symmetry=1, barrier=(16.6272,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.518087,0.0665983,-7.31889e-05,3.82639e-08,-7.60508e-12,-23085.2,26.6983], Tmin=(100,'K'), Tmax=(1293.44,'K')), NASAPolynomial(coeffs=[18.9407,0.00745745,-2.08849e-06,3.21011e-10,-2.08345e-14,-27669.5,-66.219], Tmin=(1293.44,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-193.054,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(245.277,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-Cd)H) + group(Cs-(Cds-Cds)CsHH) + group(CsCsFFH) + group(Cds-CdsCsOs) + group(Cds-CdsHH) + radical(Csj(Cs-CdHH)(F1s)(F1s)) + radical(Cds_P)"""),
)

species(
    label = '[CH]=C([O])CC(F)F(6466)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {5,S}
2  F u0 p3 c0 {5,S}
3  O u1 p2 c0 {6,S}
4  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {2,S} {4,S} {10,S}
6  C u0 p0 c0 {3,S} {4,S} {7,D}
7  C u1 p0 c0 {6,D} {11,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {7,S}
"""),
    E0 = (-256.52,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2850,1437.5,1250,1305,750,350,235,523,627,1123,1142,1372,1406,3097,350,440,435,1725,3120,650,792.5,1650,291.153,293.831],'cm^-1')),
        HinderedRotor(inertia=(0.184474,'amu*angstrom^2'), symmetry=1, barrier=(11.0692,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.181003,'amu*angstrom^2'), symmetry=1, barrier=(11.0394,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.1113,0.0619673,-6.94013e-05,3.94627e-08,-8.83148e-12,-30746.9,24.1352], Tmin=(100,'K'), Tmax=(1092.16,'K')), NASAPolynomial(coeffs=[13.5529,0.0164011,-6.82073e-06,1.26356e-09,-8.7703e-14,-33464.6,-36.9855], Tmin=(1092.16,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-256.52,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(249.434,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-Cd)H) + group(Cs-(Cds-Cds)CsHH) + group(CsCsFFH) + group(Cds-CdsCsOs) + group(Cds-CdsHH) + radical(C=C(C)OJ) + radical(Cds_P)"""),
)

species(
    label = 'O=[C]CC[C](F)F(6419)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {6,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
6  C u1 p0 c0 {1,S} {2,S} {4,S}
7  C u1 p0 c0 {3,D} {5,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {5,S}
11 H u0 p0 c0 {5,S}
"""),
    E0 = (-276.943,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2783.33,2816.67,2850,1425,1450,1225,1275,1270,1340,700,800,300,400,190,488,555,1236,1407,1855,455,950,180,180],'cm^-1')),
        HinderedRotor(inertia=(0.177406,'amu*angstrom^2'), symmetry=1, barrier=(4.07892,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.177519,'amu*angstrom^2'), symmetry=1, barrier=(4.08151,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.177557,'amu*angstrom^2'), symmetry=1, barrier=(4.08237,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(3294.32,'J/mol'), sigma=(5.47565,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with Tc=514.57 K, Pc=45.53 bar (from Joback method)"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.24568,0.0686936,-0.000113575,1.04519e-07,-3.7389e-11,-33217.1,25.4261], Tmin=(100,'K'), Tmax=(839.079,'K')), NASAPolynomial(coeffs=[6.01458,0.0296698,-1.46922e-05,2.81707e-09,-1.93794e-13,-33444,6.67271], Tmin=(839.079,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-276.943,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(245.277,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(Cs-CsCsHH) + group(Cs-(Cds-O2d)CsHH) + group(CsCsFFH) + group(Cds-OdCsH) + radical(Csj(Cs-CsHH)(F1s)(F1s)) + radical(CCCJ=O)"""),
)

species(
    label = 'CH2(T)(18)',
    structure = adjacencyList("""multiplicity 3
1 C u2 p0 c0 {2,S} {3,S}
2 H u0 p0 c0 {1,S}
3 H u0 p0 c0 {1,S}
"""),
    E0 = (381.37,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1066.91,2790.99,3622.37],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (14.0266,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(1197.29,'J/mol'), sigma=(3.8,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""GRI-Mech"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.01192,-0.00015498,3.26298e-06,-2.40422e-09,5.69498e-13,45867.7,0.5332], Tmin=(100,'K'), Tmax=(1104.56,'K')), NASAPolynomial(coeffs=[3.14983,0.00296674,-9.76055e-07,1.54115e-10,-9.50337e-15,46058.1,4.77807], Tmin=(1104.56,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(381.37,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(58.2013,'J/(mol*K)'), label="""CH2(T)""", comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'O=[C]C[C](F)F(541)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {5,S}
2 F u0 p3 c0 {5,S}
3 O u0 p2 c0 {6,D}
4 C u0 p0 c0 {5,S} {6,S} {7,S} {8,S}
5 C u1 p0 c0 {1,S} {2,S} {4,S}
6 C u1 p0 c0 {3,D} {4,S}
7 H u0 p0 c0 {4,S}
8 H u0 p0 c0 {4,S}
"""),
    E0 = (-243.768,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,2850,1437.5,1250,1305,750,350,190,488,555,1236,1407,1855,455,950,1192.43],'cm^-1')),
        HinderedRotor(inertia=(0.775984,'amu*angstrom^2'), symmetry=1, barrier=(17.8414,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(2.61609,'amu*angstrom^2'), symmetry=1, barrier=(60.1491,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (92.0441,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.83288,0.0293857,-2.14755e-05,7.65592e-09,-1.07841e-12,-29321.8,12.1615], Tmin=(10,'K'), Tmax=(1615.06,'K')), NASAPolynomial(coeffs=[9.89848,0.0143632,-7.52343e-06,1.89685e-09,-1.86956e-13,-31281.1,-20.0092], Tmin=(1615.06,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-243.768,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(182.918,'J/(mol*K)'), label="""OD[C]C[C](F)F""", comment="""Thermo library: 2-BTP_G4"""),
)

species(
    label = 'O=C1CC(F)(F)C1(6433)',
    structure = adjacencyList("""1  F u0 p3 c0 {4,S}
2  F u0 p3 c0 {4,S}
3  O u0 p2 c0 {7,D}
4  C u0 p0 c0 {1,S} {2,S} {5,S} {6,S}
5  C u0 p0 c0 {4,S} {7,S} {8,S} {9,S}
6  C u0 p0 c0 {4,S} {7,S} {10,S} {11,S}
7  C u0 p0 c0 {3,D} {5,S} {6,S}
8  H u0 p0 c0 {5,S}
9  H u0 p0 c0 {5,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {6,S}
"""),
    E0 = (-560.174,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.87788,0.0399471,-1.84114e-05,-6.14877e-10,1.78808e-12,-67291.5,18.051], Tmin=(100,'K'), Tmax=(1249.01,'K')), NASAPolynomial(coeffs=[11.0543,0.0216455,-9.7459e-06,1.86616e-09,-1.30907e-13,-70448.5,-31.7218], Tmin=(1249.01,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-560.174,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(257.749,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(CsCsCsFF) + group(Cs-(Cds-O2d)CsHH) + group(Cs-(Cds-O2d)CsHH) + group(Cds-OdCsCs) + ring(Cyclobutanone)"""),
)

species(
    label = 'CC(=O)C=C(F)F(6467)',
    structure = adjacencyList("""1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  O u0 p2 c0 {5,D}
4  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {3,D} {4,S} {6,S}
6  C u0 p0 c0 {5,S} {7,D} {11,S}
7  C u0 p0 c0 {1,S} {2,S} {6,D}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
"""),
    E0 = (-519.316,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.19476,0.044871,-3.9712e-05,2.25998e-08,-6.23099e-12,-62398.7,19.7734], Tmin=(100,'K'), Tmax=(805.074,'K')), NASAPolynomial(coeffs=[4.71217,0.0323634,-1.64085e-05,3.30289e-09,-2.38786e-13,-62804.1,8.17411], Tmin=(805.074,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-519.316,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(249.434,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(Cs-(Cds-O2d)HHH) + group(Cds-O2d(Cds-Cds)Cs) + group(Cd-Cd(CO)H) + group(CdCFF)"""),
)

species(
    label = '[CH2][C]1CC(F)(F)O1(6468)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {5,S}
2  F u0 p3 c0 {5,S}
3  O u0 p2 c0 {5,S} {6,S}
4  C u0 p0 c0 {5,S} {6,S} {8,S} {9,S}
5  C u0 p0 c0 {1,S} {2,S} {3,S} {4,S}
6  C u1 p0 c0 {3,S} {4,S} {7,S}
7  C u1 p0 c0 {6,S} {10,S} {11,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {7,S}
11 H u0 p0 c0 {7,S}
"""),
    E0 = (-223.947,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.49919,0.0593129,-7.92828e-05,6.3551e-08,-2.12262e-11,-26848.6,21.4486], Tmin=(100,'K'), Tmax=(750.519,'K')), NASAPolynomial(coeffs=[7.27433,0.0273283,-1.29495e-05,2.48941e-09,-1.7378e-13,-27681.5,-4.52961], Tmin=(750.519,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-223.947,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(253.591,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(Cs-CsCsOsH) + group(Cs-CsCsHH) + group(CsCFFO) + group(Cs-CsHHH) + ring(Cs-Cs(F)(F)-O2s-Cs) + radical(C2CsJOCs) + radical(CJC(C)OC)"""),
)

species(
    label = 'CC([O])=C[C](F)F(6469)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {7,S}
3  O u1 p2 c0 {5,S}
4  C u0 p0 c0 {5,S} {8,S} {9,S} {10,S}
5  C u0 p0 c0 {3,S} {4,S} {6,D}
6  C u0 p0 c0 {5,D} {7,S} {11,S}
7  C u1 p0 c0 {1,S} {2,S} {6,S}
8  H u0 p0 c0 {4,S}
9  H u0 p0 c0 {4,S}
10 H u0 p0 c0 {4,S}
11 H u0 p0 c0 {6,S}
"""),
    E0 = (-341.892,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (106.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.47881,0.0564287,-5.97929e-05,3.37465e-08,-7.72515e-12,-41030.1,22.4942], Tmin=(100,'K'), Tmax=(1051.33,'K')), NASAPolynomial(coeffs=[10.7631,0.0211047,-9.39369e-06,1.78734e-09,-1.25429e-13,-42982.3,-22.7617], Tmin=(1051.33,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-341.892,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(249.434,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-Cd)H) + group(Cs-(Cds-Cds)HHH) + group(CsCFFH) + group(Cds-CdsCsOs) + group(Cds-CdsCsH) + radical(C=C(C)OJ) + radical(Csj(Cd-CdH)(F1s)(F1s))"""),
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
    E0 = (-146.666,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (24.4274,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (299.817,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (403.986,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (-138.382,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (-83.2659,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (84.5501,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS8',
    E0 = (-21.4529,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS9',
    E0 = (42.5487,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS10',
    E0 = (-35.2016,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS11',
    E0 = (22.6517,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS12',
    E0 = (-1.9188,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS13',
    E0 = (206.816,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS14',
    E0 = (65.9862,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS15',
    E0 = (-23.4673,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS16',
    E0 = (10.4442,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS17',
    E0 = (154.754,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS18',
    E0 = (-56.5326,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS19',
    E0 = (124.337,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS20',
    E0 = (293.281,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS21',
    E0 = (-138.382,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS22',
    E0 = (-83.2659,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS23',
    E0 = (95.5038,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS24',
    E0 = (-44.4565,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['C=C([O])C[C](F)F(3131)'],
    products = ['CH2CF2(57)', 'CH2CO(28)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(5e+12,'s^-1'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""Exact match found for rate rule [RJJ]
Euclidian distance = 0
family: 1,4_Linear_birad_scission"""),
)

reaction(
    label = 'reaction2',
    reactants = ['[CH2]C(F)(F)C(=C)[O](3151)'],
    products = ['C=C([O])C[C](F)F(3131)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(1.33e+08,'s^-1'), n=1.36, Ea=(157.318,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [cCs(-R!HR!H)CJ;CsJ-HH;C]
Euclidian distance = 0
family: 1,2_shiftC"""),
)

reaction(
    label = 'reaction3',
    reactants = ['F[C]F(156)', '[CH2]C(=C)[O](6456)'],
    products = ['C=C([O])C[C](F)F(3131)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(4.0899e+06,'m^3/(mol*s)'), n=0.382229, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Y_rad;Birad] for rate rule [C_rad/H2/Cd;Birad]
Euclidian distance = 3.0
Multiplied by reaction path degeneracy 2.0
family: Birad_R_Recombination
Ea raised from -1.7 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction4',
    reactants = ['O(6)', 'C=[C]C[C](F)F(6457)'],
    products = ['C=C([O])C[C](F)F(3131)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(1667.73,'m^3/(mol*s)'), n=1.126, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(303.03,'K'), Tmax=(2000,'K'), comment="""Estimated using template [Y_rad;O_birad] for rate rule [Cd_rad/NonDe;O_birad]
Euclidian distance = 3.0
family: Birad_R_Recombination
Ea raised from -8.3 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction5',
    reactants = ['C=C([O])C[C](F)F(3131)'],
    products = ['C=C1CC(F)(F)O1(6420)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(1.62e+12,'s^-1'), n=-0.305, Ea=(8.28432,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R4_SSS;C_rad_out_single;Ypri_rad_out] for rate rule [R4_SSS;C_rad_out_noH;Opri_rad]
Euclidian distance = 1.4142135623730951
family: Birad_recombination"""),
)

reaction(
    label = 'reaction6',
    reactants = ['C=C([O])C[C](F)F(3131)'],
    products = ['C=C(O)C=C(F)F(6458)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(1.4874e+09,'s^-1'), n=1.045, Ea=(63.4002,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [R3radExo;Y_rad;XH_Rrad]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Intra_Disproportionation"""),
)

reaction(
    label = 'reaction7',
    reactants = ['C=C([O])C[C](F)F(3131)'],
    products = ['F[C](F)C[C]1CO1(6459)'],
    transitionState = 'TS7',
    kinetics = Arrhenius(A=(3.473e+12,'s^-1'), n=0.247, Ea=(231.216,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R3_D;doublebond_intra_secNd_2H;radadd_intra] for rate rule [R3_D;doublebond_intra_secNd_2H;radadd_intra_O]
Euclidian distance = 1.0
family: Intra_R_Add_Endocyclic"""),
)

reaction(
    label = 'reaction8',
    reactants = ['C=C([O])C[C](F)F(3131)'],
    products = ['[O][C]1CC(F)(F)C1(6460)'],
    transitionState = 'TS8',
    kinetics = Arrhenius(A=(3.78932e+07,'s^-1'), n=1.19089, Ea=(125.213,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [R4_Cs_HH_D;doublebond_intra;radadd_intra_cs]
Euclidian distance = 0
family: Intra_R_Add_Endocyclic"""),
)

reaction(
    label = 'reaction9',
    reactants = ['C=C([O])C[C](F)F(3131)'],
    products = ['[CH2]C1([O])CC1(F)F(6461)'],
    transitionState = 'TS9',
    kinetics = Arrhenius(A=(1.17979e+10,'s^-1'), n=0.520585, Ea=(189.215,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [R4_S_D;doublebond_intra_2H;radadd_intra_cs]
Euclidian distance = 0
family: Intra_R_Add_Exocyclic"""),
)

reaction(
    label = 'reaction10',
    reactants = ['CH2CF2(57)', '[CH2][C]=O(4470)'],
    products = ['C=C([O])C[C](F)F(3131)'],
    transitionState = 'TS10',
    kinetics = Arrhenius(A=(0.00958,'m^3/(mol*s)'), n=2.41, Ea=(10.5502,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R-inRing_Ext-3R-R_Sp-4R!H=3R_Sp-2R!H=1R!H_2R!H->C_Ext-2C-R_Ext-2C-R_Ext-3R-R',), comment="""Estimated from node Root_N-3R-inRing_Ext-3R-R_Sp-4R!H=3R_Sp-2R!H=1R!H_2R!H->C_Ext-2C-R_Ext-2C-R_Ext-3R-R"""),
)

reaction(
    label = 'reaction11',
    reactants = ['H(5)', 'C=C([O])C=C(F)F(6462)'],
    products = ['C=C([O])C[C](F)F(3131)'],
    transitionState = 'TS11',
    kinetics = Arrhenius(A=(306600,'m^3/(mol*s)'), n=0.481, Ea=(30.1568,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->H_N-2R!H->N_N-1R!H->N_N-2COS->O_N-2CS-inRing_Ext-1COS-R_N-4R!H-inRing_4R!H-u0_Ext-2CS-R_Sp-2CS=1CCOSS_N-5R!H-inRing_Sp-5R!H-2CS_Ext-2CS-R_4R!H->C_Sp-4C-1COS_N-6R!H-inRing_Ext-4C-R_Ext-4C-R',), comment="""Estimated from node Root_3R->H_N-2R!H->N_N-1R!H->N_N-2COS->O_N-2CS-inRing_Ext-1COS-R_N-4R!H-inRing_4R!H-u0_Ext-2CS-R_Sp-2CS=1CCOSS_N-5R!H-inRing_Sp-5R!H-2CS_Ext-2CS-R_4R!H->C_Sp-4C-1COS_N-6R!H-inRing_Ext-4C-R_Ext-4C-R"""),
)

reaction(
    label = 'reaction12',
    reactants = ['[CH2][C](F)F(163)', 'CH2CO(28)'],
    products = ['C=C([O])C[C](F)F(3131)'],
    transitionState = 'TS12',
    kinetics = Arrhenius(A=(9.10216e-08,'m^3/(mol*s)'), n=3.71185, Ea=(12.2683,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.339286171633947, var=3.7349511333863634, Tref=1000.0, N=1489, data_mean=0.0, correlation='Root_N-3R-inRing_Ext-3R-R_Ext-4R!H-R',), comment="""Estimated from node Root_N-3R-inRing_Ext-3R-R_Ext-4R!H-R"""),
)

reaction(
    label = 'reaction13',
    reactants = ['[CH2][C](F)F(163)', '[CH2][C]=O(4470)'],
    products = ['C=C([O])C[C](F)F(3131)'],
    transitionState = 'TS13',
    kinetics = Arrhenius(A=(9.04e+06,'m^3/(mol*s)'), n=2.17087e-08, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C_Ext-2C-R_Ext-2C-R',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C_Ext-2C-R_Ext-2C-R"""),
)

reaction(
    label = 'reaction14',
    reactants = ['CF2(43)', '[CH2]C(=C)[O](6456)'],
    products = ['C=C([O])C[C](F)F(3131)'],
    transitionState = 'TS14',
    kinetics = Arrhenius(A=(0.0195237,'m^3/(mol*s)'), n=2.64543, Ea=(3.60916,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.24524072153041726, var=3.368891203868511, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s',), comment="""Estimated from node Root_N-3R->H_Ext-3BrCClFINOPSSi-R_3BrCClFINOPSSi->C_2Br1sCl1sF1s->F1s
Multiplied by reaction path degeneracy 2.0"""),
)

reaction(
    label = 'reaction15',
    reactants = ['C=C([O])C[C](F)F(3131)'],
    products = ['[CH2]C([O])=CC(F)F(6463)'],
    transitionState = 'TS15',
    kinetics = Arrhenius(A=(11288.6,'s^-1'), n=2.7035, Ea=(123.199,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [R2H_S;C_rad_out_noH;Cs_H_out_H/Cd]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: intra_H_migration"""),
)

reaction(
    label = 'reaction16',
    reactants = ['C=C([O])C[C](F)F(3131)'],
    products = ['[CH2]C(O)=C[C](F)F(6464)'],
    transitionState = 'TS16',
    kinetics = Arrhenius(A=(2.39846e+08,'s^-1'), n=1.46351, Ea=(157.11,'kJ/mol'), T0=(1,'K'), comment="""Estimated using average of templates [R3H_SS;O_rad_out;XH_out] + [R3H_SS_2Cd;Y_rad_out;XH_out] for rate rule [R3H_SS_2Cd;O_rad_out;XH_out]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 2.0
family: intra_H_migration"""),
)

reaction(
    label = 'reaction17',
    reactants = ['[CH]=C(O)C[C](F)F(6465)'],
    products = ['C=C([O])C[C](F)F(3131)'],
    transitionState = 'TS17',
    kinetics = Arrhenius(A=(6718.85,'s^-1'), n=2.58467, Ea=(192.129,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R3H_DS;Cd_rad_out_singleH;XH_out] for rate rule [R3H_DS;Cd_rad_out_singleH;O_H_out]
Euclidian distance = 1.0
family: intra_H_migration"""),
)

reaction(
    label = 'reaction18',
    reactants = ['[CH]=C([O])CC(F)F(6466)'],
    products = ['C=C([O])C[C](F)F(3131)'],
    transitionState = 'TS18',
    kinetics = Arrhenius(A=(37100,'s^-1'), n=2.23, Ea=(44.3086,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R4H_DSS;Cd_rad_out_singleH;Cs_H_out] for rate rule [R4H_DSS;Cd_rad_out_singleH;Cs_H_out_noH]
Euclidian distance = 1.0
family: intra_H_migration"""),
)

reaction(
    label = 'reaction3',
    reactants = ['O=[C]CC[C](F)F(6419)'],
    products = ['C=C([O])C[C](F)F(3131)'],
    transitionState = 'TS19',
    kinetics = Arrhenius(A=(3.53e+06,'s^-1'), n=1.73, Ea=(245.601,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [cCs(-HH)CJ;CJ;C]
Euclidian distance = 0
family: 1,2_shiftC"""),
)

reaction(
    label = 'reaction20',
    reactants = ['CH2(T)(18)', 'O=[C]C[C](F)F(541)'],
    products = ['C=C([O])C[C](F)F(3131)'],
    transitionState = 'TS20',
    kinetics = Arrhenius(A=(2.04495e+06,'m^3/(mol*s)'), n=0.382229, Ea=(0,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Y_rad;Birad] for rate rule [CO_rad/NonDe;Birad]
Euclidian distance = 3.0
family: Birad_R_Recombination
Ea raised from -1.7 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction21',
    reactants = ['C=C([O])C[C](F)F(3131)'],
    products = ['O=C1CC(F)(F)C1(6433)'],
    transitionState = 'TS21',
    kinetics = Arrhenius(A=(1.62e+12,'s^-1'), n=-0.305, Ea=(8.28432,'kJ/mol'), T0=(1,'K'), Tmin=(600,'K'), Tmax=(2000,'K'), comment="""Estimated using template [R4_SSS;C_rad_out_single;Cpri_rad_out_2H] for rate rule [R4_SSS;C_rad_out_noH;Cpri_rad_out_2H]
Euclidian distance = 1.0
family: Birad_recombination"""),
)

reaction(
    label = 'reaction22',
    reactants = ['C=C([O])C[C](F)F(3131)'],
    products = ['CC(=O)C=C(F)F(6467)'],
    transitionState = 'TS22',
    kinetics = Arrhenius(A=(1.4874e+09,'s^-1'), n=1.045, Ea=(63.4002,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [R3radExo;Y_rad;XH_Rrad]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Intra_Disproportionation"""),
)

reaction(
    label = 'reaction23',
    reactants = ['C=C([O])C[C](F)F(3131)'],
    products = ['[CH2][C]1CC(F)(F)O1(6468)'],
    transitionState = 'TS23',
    kinetics = Arrhenius(A=(1.503e+11,'s^-1'), n=0.221, Ea=(242.17,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R4_S_CO;carbonyl_intra;radadd_intra] for rate rule [R4_S_CO;carbonyl_intra;radadd_intra_cs]
Euclidian distance = 1.0
family: Intra_R_Add_Endocyclic"""),
)

reaction(
    label = 'reaction24',
    reactants = ['C=C([O])C[C](F)F(3131)'],
    products = ['CC([O])=C[C](F)F(6469)'],
    transitionState = 'TS24',
    kinetics = Arrhenius(A=(101.408,'s^-1'), n=3.11103, Ea=(102.21,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [R3H_SS;C_rad_out_2H;XH_out]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: intra_H_migration"""),
)

network(
    label = 'PDepNetwork #1801',
    isomers = [
        'C=C([O])C[C](F)F(3131)',
    ],
    reactants = [
        ('CH2CF2(57)', 'CH2CO(28)'),
    ],
    bathGas = {
        'N2': 0.5,
        'Ne': 0.5,
    },
)

pressureDependence(
    label = 'PDepNetwork #1801',
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

