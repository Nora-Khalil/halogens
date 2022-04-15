species(
    label = 'F[CH]OC1(F)[CH]C2(F)OOC12(1025)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {9,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {11,S}
4  O u0 p2 c0 {8,S} {11,S}
5  O u0 p2 c0 {6,S} {7,S}
6  O u0 p2 c0 {5,S} {9,S}
7  C u0 p0 c0 {5,S} {8,S} {9,S} {12,S}
8  C u0 p0 c0 {2,S} {4,S} {7,S} {10,S}
9  C u0 p0 c0 {1,S} {6,S} {7,S} {10,S}
10 C u1 p0 c0 {8,S} {9,S} {13,S}
11 C u1 p0 c0 {3,S} {4,S} {14,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {10,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-365.337,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,3150,900,1100,289,343,342,428,440,590,571,737,593,785,1204,1386,580,1155,1237,1373,3147,300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.538736,0.0851446,-8.07804e-05,3.78705e-08,-7.39938e-12,-43822.9,24.7478], Tmin=(100,'K'), Tmax=(1178.52,'K')), NASAPolynomial(coeffs=[14.1657,0.0388935,-2.1913e-05,4.57039e-09,-3.35421e-13,-47034.9,-43.2329], Tmin=(1178.52,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-365.337,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(324.264,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsCs) + group(CsCCFO) + group(Cs-CsCsOsH) + group(CsCCFO) + group(Cs-CsCsHH) + group(CsFHHO) + polycyclic(s2_4_4_ane) + radical(CCJCOOH) + radical(Csj(F1s)(O2s-Cs)(H))"""),
)

species(
    label = 'CHFO(47)',
    structure = adjacencyList("""1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 H u0 p0 c0 {3,S}
"""),
    E0 = (-394.294,'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(48.0011,'amu')),
        NonlinearRotor(inertia=([5.46358,42.889,48.3526],'amu*angstrom^2'), symmetry=1),
        HarmonicOscillator(frequencies=([674.139,1050.3,1121.98,1395.32,1906.92,3070.52],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (48.0164,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(2914.22,'J/mol'), sigma=(4.906,'angstroms'), dipoleMoment=(0,'De'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""NIST_Fluorine"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.05425,-0.00375329,3.18277e-05,-4.07297e-08,1.68956e-11,-47423,6.56837], Tmin=(10,'K'), Tmax=(745.315,'K')), NASAPolynomial(coeffs=[2.27714,0.0104751,-6.24845e-06,1.77292e-09,-1.93455e-13,-47288.4,13.7455], Tmin=(745.315,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(-394.294,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(83.1447,'J/(mol*K)'), label="""ODCF""", comment="""Thermo library: CHOF_G4"""),
)

species(
    label = 'FC1=CC2(F)OOC12(939)',
    structure = adjacencyList("""1  F u0 p3 c0 {5,S}
2  F u0 p3 c0 {8,S}
3  O u0 p2 c0 {4,S} {5,S}
4  O u0 p2 c0 {3,S} {6,S}
5  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
6  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
7  C u0 p0 c0 {5,S} {8,D} {10,S}
8  C u0 p0 c0 {2,S} {6,S} {7,D}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
"""),
    E0 = (-248.602,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1380,1390,370,380,2900,435,2750,3150,900,1100,323,467,575,827,1418,554.088,554.758,554.772,556.279,557.402,557.685,557.797,557.853,558.993],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (120.054,'amu'),
    collisionModel = TransportData(shapeIndex=2, epsilon=(3642.96,'J/mol'), sigma=(5.89185,'angstroms'), dipoleMoment=(0,'C*m'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0, comment="""Epsilon & sigma estimated with Tc=569.02 K, Pc=40.41 bar (from Joback method)"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.37506,0.0476133,-2.48124e-05,-2.36521e-09,3.49964e-12,-29797.1,16.5191], Tmin=(100,'K'), Tmax=(1189.18,'K')), NASAPolynomial(coeffs=[15.9615,0.016946,-9.33454e-06,1.96667e-09,-1.45909e-13,-34567,-61.8484], Tmin=(1189.18,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-248.602,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(232.805,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-OsCs) + group(O2s-OsCs) + group(CsCCFO) + group(Cs-(Cds-Cds)CsOsH) + group(Cds-CdsCsH) + group(CdCsCdF) + polycyclic(s2_4_4_ene_1)"""),
)

species(
    label = 'F[CH]OC12[CH]C(F)(OO1)C2F(1358)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {9,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {11,S}
4  O u0 p2 c0 {7,S} {11,S}
5  O u0 p2 c0 {6,S} {7,S}
6  O u0 p2 c0 {5,S} {9,S}
7  C u0 p0 c0 {4,S} {5,S} {8,S} {10,S}
8  C u0 p0 c0 {2,S} {7,S} {9,S} {12,S}
9  C u0 p0 c0 {1,S} {6,S} {8,S} {10,S}
10 C u1 p0 c0 {7,S} {9,S} {13,S}
11 C u1 p0 c0 {3,S} {4,S} {14,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {10,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-387.229,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[-0.582784,0.0792447,-3.4639e-05,-2.81473e-08,1.96703e-11,-46388.6,29.9425], Tmin=(100,'K'), Tmax=(994.085,'K')), NASAPolynomial(coeffs=[28.6181,0.0105315,-4.56967e-06,1.05504e-09,-8.91147e-14,-54604.8,-122.886], Tmin=(994.085,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-387.229,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(324.264,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsCs) + group(Cs-CsCsOsOs) + group(CsCCFO) + group(CsCsCsFH) + group(Cs-CsCsHH) + group(CsFHHO) + polycyclic(s3_4_5_ane) + radical(CCJCOOH) + radical(Csj(F1s)(O2s-Cs)(H)) + longDistanceInteraction_cyclic(Cs(F)-Cs(F)) + longDistanceInteraction_cyclic(Cs(F)-Cs(F)) + longDistanceInteraction_cyclic(Cs(F)-Cs(F)) + longDistanceInteraction_cyclic(Cs(F)-Cs(F))"""),
)

species(
    label = 'F[CH]OC1(F)[CH]C2(OO2)C1F(1359)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {9,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {11,S}
4  O u0 p2 c0 {8,S} {11,S}
5  O u0 p2 c0 {6,S} {7,S}
6  O u0 p2 c0 {5,S} {7,S}
7  C u0 p0 c0 {5,S} {6,S} {9,S} {10,S}
8  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
9  C u0 p0 c0 {1,S} {7,S} {8,S} {12,S}
10 C u1 p0 c0 {7,S} {8,S} {13,S}
11 C u1 p0 c0 {3,S} {4,S} {14,S}
12 H u0 p0 c0 {9,S}
13 H u0 p0 c0 {10,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-357.931,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([316,385,515,654,689,1295,250,417,511,1155,1315,1456,3119,2950,1000,580,1155,1237,1373,3147,300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[-1.09794,0.100421,-0.000106588,5.28602e-08,-1.00693e-11,-42855.8,32.1945], Tmin=(100,'K'), Tmax=(1291.1,'K')), NASAPolynomial(coeffs=[26.6033,0.0145986,-6.88079e-06,1.37566e-09,-1.00164e-13,-50008.8,-108.525], Tmin=(1291.1,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-357.931,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(324.264,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsCs) + group(Cs-CsCsOsOs) + group(CsCCFO) + group(CsCsCsFH) + group(Cs-CsCsHH) + group(CsFHHO) + polycyclic(s1_3_4_ane) + radical(CCJCOOH) + radical(Csj(F1s)(O2s-Cs)(H)) + longDistanceInteraction_cyclic(Cs(F)-Cs(F)) + longDistanceInteraction_cyclic(Cs(F)-Cs(F))"""),
)

species(
    label = 'F[CH]O[C](F)C1C2OOC21F(1360)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {9,S}
2  F u0 p3 c0 {10,S}
3  F u0 p3 c0 {11,S}
4  O u0 p2 c0 {5,S} {8,S}
5  O u0 p2 c0 {4,S} {9,S}
6  O u0 p2 c0 {10,S} {11,S}
7  C u0 p0 c0 {8,S} {9,S} {10,S} {12,S}
8  C u0 p0 c0 {4,S} {7,S} {9,S} {13,S}
9  C u0 p0 c0 {1,S} {5,S} {7,S} {8,S}
10 C u1 p0 c0 {2,S} {6,S} {7,S}
11 C u1 p0 c0 {3,S} {6,S} {14,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {8,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-357.355,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,3150,900,1100,333,384,448,608,1254,1480,395,473,707,1436,580,1155,1237,1373,3147,300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.337818,0.0897249,-9.71522e-05,5.44395e-08,-1.27225e-11,-42855.6,26.7695], Tmin=(100,'K'), Tmax=(1007.19,'K')), NASAPolynomial(coeffs=[13.0881,0.0390876,-2.1738e-05,4.52197e-09,-3.32151e-13,-45424,-34.8343], Tmin=(1007.19,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-357.355,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(320.107,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsCs) + group(Cs-CsCsCsH) + group(Cs-CsCsOsH) + group(CsCCFO) + group(CsCFHO) + group(CsFHHO) + polycyclic(s2_3_4_ane) + radical(CsCsF1sO2s) + radical(Csj(F1s)(O2s-Cs)(H))"""),
)

species(
    label = 'F[CH]OC1(F)C2OO[C](F)C21(1361)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {10,S}
3  F u0 p3 c0 {11,S}
4  O u0 p2 c0 {8,S} {11,S}
5  O u0 p2 c0 {6,S} {9,S}
6  O u0 p2 c0 {5,S} {10,S}
7  C u0 p0 c0 {8,S} {9,S} {10,S} {12,S}
8  C u0 p0 c0 {1,S} {4,S} {7,S} {9,S}
9  C u0 p0 c0 {5,S} {7,S} {8,S} {13,S}
10 C u1 p0 c0 {2,S} {6,S} {7,S}
11 C u1 p0 c0 {3,S} {4,S} {14,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-435.796,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.631259,0.0827478,-7.89874e-05,3.8092e-08,-7.71076e-12,-52300.1,25.2225], Tmin=(100,'K'), Tmax=(1138.58,'K')), NASAPolynomial(coeffs=[13.0411,0.0391503,-2.15508e-05,4.46146e-09,-3.26444e-13,-55126,-36.2582], Tmin=(1138.58,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-435.796,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(324.264,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsCs) + group(Cs-CsCsCsH) + group(CsCCFO) + group(Cs-CsCsOsH) + group(CsCFHO) + group(CsFHHO) + polycyclic(s2_3_5_ane) + radical(CsCsF1sO2s) + radical(Csj(F1s)(O2s-Cs)(H))"""),
)

species(
    label = '[CH]F(137)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {2,S}
2 C u2 p0 c0 {1,S} {3,S}
3 H u0 p0 c0 {2,S}
"""),
    E0 = (214.928,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([787.277,1376.72,4000],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (32.017,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.93333,-0.000263365,8.89188e-06,-1.03032e-08,3.5081e-12,25853.7,4.33729], Tmin=(100,'K'), Tmax=(1056.12,'K')), NASAPolynomial(coeffs=[4.72426,0.00164132,-7.73117e-07,1.90988e-10,-1.59926e-14,25413.4,-0.815515], Tmin=(1056.12,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(214.928,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(108.088,'J/(mol*K)'), comment="""Thermo library: CHOF_G4 + radical(CH2_triplet)"""),
)

species(
    label = '[O]C1(F)[CH]C2(F)OOC12(1362)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {8,S}
3  O u0 p2 c0 {4,S} {6,S}
4  O u0 p2 c0 {3,S} {7,S}
5  O u1 p2 c0 {8,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {10,S}
7  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
8  C u0 p0 c0 {2,S} {5,S} {6,S} {9,S}
9  C u1 p0 c0 {7,S} {8,S} {11,S}
10 H u0 p0 c0 {6,S}
11 H u0 p0 c0 {9,S}
"""),
    E0 = (-136.48,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,3150,900,1100,289,343,342,428,440,590,571,737,593,785,1204,1386,723.828,723.828,723.828,723.828,723.828,723.828,723.828,723.829,723.829,723.829,723.829],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (136.054,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.29392,0.059948,-4.83686e-05,1.77366e-08,-2.58791e-12,-16318.6,19.9696], Tmin=(100,'K'), Tmax=(1580.87,'K')), NASAPolynomial(coeffs=[16.3264,0.0219114,-1.22772e-05,2.51626e-09,-1.80913e-13,-21071.3,-59.4377], Tmin=(1580.87,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-136.48,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(257.749,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-OsCs) + group(O2s-OsCs) + group(O2s-CsH) + group(Cs-CsCsOsH) + group(CsCCFO) + group(CsCCFO) + group(Cs-CsCsHH) + polycyclic(s2_4_4_ane) + radical(O2sj(Cs-F1sCsCs)) + radical(CCJCOOH)"""),
)

species(
    label = 'FC1OC2(F)C3OOC3(F)C12(1027)',
    structure = adjacencyList("""1  F u0 p3 c0 {9,S}
2  F u0 p3 c0 {8,S}
3  F u0 p3 c0 {11,S}
4  O u0 p2 c0 {8,S} {11,S}
5  O u0 p2 c0 {6,S} {9,S}
6  O u0 p2 c0 {5,S} {10,S}
7  C u0 p0 c0 {8,S} {9,S} {11,S} {12,S}
8  C u0 p0 c0 {2,S} {4,S} {7,S} {10,S}
9  C u0 p0 c0 {1,S} {5,S} {7,S} {10,S}
10 C u0 p0 c0 {6,S} {8,S} {9,S} {13,S}
11 C u0 p0 c0 {3,S} {4,S} {7,S} {14,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {10,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-619.5,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[-0.00660412,0.0764497,-5.4265e-05,1.56245e-08,-1.50766e-12,-74354.7,18.1848], Tmin=(100,'K'), Tmax=(1558.46,'K')), NASAPolynomial(coeffs=[25.9369,0.0214984,-1.25749e-05,2.58161e-09,-1.83947e-13,-83854.2,-123.022], Tmin=(1558.46,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-619.5,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(332.579,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsCs) + group(Cs-CsCsCsH) + group(CsCCFO) + group(CsCCFO) + group(Cs-CsCsOsH) + group(CsCFHO) + polycyclic(s2_4_4_ane) + polycyclic(s2_4_4_ane) - ring(Cyclobutane)"""),
)

species(
    label = 'F[CH]OC1(F)[CH]OOC(F)=C1(1363)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {10,S}
3  F u0 p3 c0 {11,S}
4  O u0 p2 c0 {7,S} {11,S}
5  O u0 p2 c0 {6,S} {9,S}
6  O u0 p2 c0 {5,S} {10,S}
7  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
8  C u0 p0 c0 {7,S} {10,D} {12,S}
9  C u1 p0 c0 {5,S} {7,S} {13,S}
10 C u0 p0 c0 {2,S} {6,S} {8,D}
11 C u1 p0 c0 {3,S} {4,S} {14,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-448.904,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1380,1390,370,380,2900,435,2750,3150,900,1100,326,540,652,719,1357,580,1155,1237,1373,3147,300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[-0.184988,0.100388,-0.000150964,1.28869e-07,-4.45019e-11,-53848,28.3581], Tmin=(100,'K'), Tmax=(784.622,'K')), NASAPolynomial(coeffs=[9.87536,0.0405592,-2.02569e-05,3.93822e-09,-2.7511e-13,-55163.8,-16.0617], Tmin=(784.622,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-448.904,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(324.264,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-O2s(Cds-Cd)) + group(CsCCFO) + group(Cs-CsOsHH) + group(CsFHHO) + group(Cds-CdsCsH) + group(CdCFO) + ring(34dihydro12dioxin) + radical(CCsJOOC) + radical(Csj(F1s)(O2s-Cs)(H))"""),
)

species(
    label = 'F[CH]OC(F)=CC1(F)[CH]OO1(1364)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {10,S}
3  F u0 p3 c0 {11,S}
4  O u0 p2 c0 {6,S} {7,S}
5  O u0 p2 c0 {10,S} {11,S}
6  O u0 p2 c0 {4,S} {9,S}
7  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
8  C u0 p0 c0 {7,S} {10,D} {12,S}
9  C u1 p0 c0 {6,S} {7,S} {13,S}
10 C u0 p0 c0 {2,S} {5,S} {8,D}
11 C u1 p0 c0 {3,S} {5,S} {14,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-394.718,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1380,1390,370,380,2900,435,3010,987.5,1337.5,450,1655,2950,1000,326,540,652,719,1357,580,1155,1237,1373,3147,180,180,180,180,737.594,1477.03,1600,1800,3000,3200],'cm^-1')),
        HinderedRotor(inertia=(0.151065,'amu*angstrom^2'), symmetry=1, barrier=(3.47329,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.151065,'amu*angstrom^2'), symmetry=1, barrier=(3.47329,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.151065,'amu*angstrom^2'), symmetry=1, barrier=(3.47329,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[-0.150089,0.0983249,-0.000127743,8.68086e-08,-2.38146e-11,-47330.3,32.6616], Tmin=(100,'K'), Tmax=(884.209,'K')), NASAPolynomial(coeffs=[14.2541,0.0331629,-1.71998e-05,3.46232e-09,-2.49356e-13,-49877.5,-35.0578], Tmin=(884.209,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-394.718,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(320.107,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-Cd)) + group(O2s-OsCs) + group(O2s-OsCs) + group(CsCCFO) + group(Cs-CsOsHH) + group(CsFHHO) + group(Cds-CdsCsH) + group(CdCFO) + ring(Cs-Cs(F)-O2s-O2s) + radical(CCsJOO) + radical(Csj(F1s)(O2s-Cd)(H))"""),
)

species(
    label = '[O]OC1C(F)=CC1(F)O[CH]F(1365)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {9,S}
3  F u0 p3 c0 {11,S}
4  O u0 p2 c0 {7,S} {11,S}
5  O u0 p2 c0 {6,S} {8,S}
6  O u1 p2 c0 {5,S}
7  C u0 p0 c0 {1,S} {4,S} {8,S} {10,S}
8  C u0 p0 c0 {5,S} {7,S} {9,S} {12,S}
9  C u0 p0 c0 {2,S} {8,S} {10,D}
10 C u0 p0 c0 {7,S} {9,D} {13,S}
11 C u1 p0 c0 {3,S} {4,S} {14,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {10,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-433.932,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([492.5,1135,1000,1380,1390,370,380,2900,435,2750,3150,900,1100,323,467,575,827,1418,580,1155,1237,1373,3147,180,180,180,180,749.931,1465.56,1600,1800,3000,3200],'cm^-1')),
        HinderedRotor(inertia=(0.151834,'amu*angstrom^2'), symmetry=1, barrier=(3.49095,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.151834,'amu*angstrom^2'), symmetry=1, barrier=(3.49095,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.151834,'amu*angstrom^2'), symmetry=1, barrier=(3.49095,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[-0.0498198,0.0954785,-0.000118147,7.58058e-08,-1.96534e-11,-52049.5,32.0221], Tmin=(100,'K'), Tmax=(932.609,'K')), NASAPolynomial(coeffs=[14.6316,0.0325098,-1.68691e-05,3.40893e-09,-2.46477e-13,-54788,-37.783], Tmin=(932.609,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-433.932,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(320.107,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsH) + group(CsCCFO) + group(Cs-(Cds-Cds)CsOsH) + group(CsFHHO) + group(CdCsCdF) + group(Cds-CdsCsH) + ring(Cs(F)-Cs-Cd-Cd) + radical(ROOJ) + radical(Csj(F1s)(O2s-Cs)(H))"""),
)

species(
    label = 'F[C]1[CH]C2(F)OOC12(943)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {5,S}
2  F u0 p3 c0 {8,S}
3  O u0 p2 c0 {4,S} {5,S}
4  O u0 p2 c0 {3,S} {6,S}
5  C u0 p0 c0 {1,S} {3,S} {6,S} {7,S}
6  C u0 p0 c0 {4,S} {5,S} {8,S} {9,S}
7  C u1 p0 c0 {5,S} {8,S} {10,S}
8  C u1 p0 c0 {2,S} {6,S} {7,S}
9  H u0 p0 c0 {6,S}
10 H u0 p0 c0 {7,S}
"""),
    E0 = (24.0771,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([316,385,515,654,689,1295,2750,3150,900,1100,212,367,445,1450,792.943,792.943,792.943,792.943,792.943,792.943,792.943,792.943,792.943,792.943],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (120.054,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.01799,0.0472587,-3.27286e-05,9.66919e-09,-1.11055e-12,2962.68,18.0674], Tmin=(100,'K'), Tmax=(1964.11,'K')), NASAPolynomial(coeffs=[16.3603,0.01805,-1.04219e-05,2.0978e-09,-1.46838e-13,-2671.35,-60.8079], Tmin=(1964.11,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(24.0771,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(232.805,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-OsCs) + group(O2s-OsCs) + group(CsCCFO) + group(Cs-CsCsOsH) + group(Cs-CsCsHH) + group(CsCsCsFH) + polycyclic(s2_4_4_ane) + radical(CCJCOOH) + radical(CsCsCsF1s)"""),
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
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.90371,-0.000635296,2.64735e-07,7.69063e-11,-5.45254e-14,8672.27,2.70828], Tmin=(298,'K'), Tmax=(1400,'K')), NASAPolynomial(coeffs=[2.65117,-0.00014013,5.19236e-08,-8.84954e-12,5.9028e-16,8758.29,4.07857], Tmin=(1400,'K'), Tmax=(3000,'K'))], Tmin=(298,'K'), Tmax=(3000,'K'), E0=(72.8916,'kJ/mol'), Cp0=(20.7862,'J/mol/K'), CpInf=(20.7862,'J/mol/K'), label="""F""", comment="""Thermo library: primaryThermoLibrary"""),
)

species(
    label = 'F[CH]OC1=CC2(F)OOC12(1366)',
    structure = adjacencyList("""multiplicity 2
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {10,S}
3  O u0 p2 c0 {4,S} {6,S}
4  O u0 p2 c0 {3,S} {7,S}
5  O u0 p2 c0 {8,S} {10,S}
6  C u0 p0 c0 {3,S} {7,S} {8,S} {11,S}
7  C u0 p0 c0 {1,S} {4,S} {6,S} {9,S}
8  C u0 p0 c0 {5,S} {6,S} {9,D}
9  C u0 p0 c0 {7,S} {8,D} {12,S}
10 C u1 p0 c0 {2,S} {5,S} {13,S}
11 H u0 p0 c0 {6,S}
12 H u0 p0 c0 {9,S}
13 H u0 p0 c0 {10,S}
"""),
    E0 = (-252.63,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2750,3150,900,1100,1380,1390,370,380,2900,435,580,1155,1237,1373,3147,300,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (149.072,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[-0.165025,0.0773932,-6.06457e-05,1.51547e-08,7.9582e-13,-30222.4,25.987], Tmin=(100,'K'), Tmax=(1125.81,'K')), NASAPolynomial(coeffs=[23.3817,0.0159767,-8.45471e-06,1.79998e-09,-1.36043e-13,-36933.9,-96.6636], Tmin=(1125.81,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-252.63,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(299.321,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-Cd)) + group(O2s-OsCs) + group(O2s-OsCs) + group(Cs-(Cds-Cds)CsOsH) + group(CsCCFO) + group(CsFHHO) + group(Cds-CdsCsOs) + group(Cds-CdsCsH) + polycyclic(s2_4_4_ene_1) + radical(Csj(F1s)(O2s-Cd)(H))"""),
)

species(
    label = '[O][CH]F(388)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {3,S}
2 O u1 p2 c0 {3,S}
3 C u1 p0 c0 {1,S} {2,S} {4,S}
4 H u0 p0 c0 {3,S}
"""),
    E0 = (-19.6796,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([580,1155,1237,1373,3147,180],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (48.0164,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.53592,0.00799825,-5.22271e-07,-4.56612e-09,2.08752e-12,-2348.33,9.31392], Tmin=(100,'K'), Tmax=(1079.18,'K')), NASAPolynomial(coeffs=[5.97187,0.0038822,-1.62979e-06,3.36437e-10,-2.54188e-14,-3160.18,-3.94923], Tmin=(1079.18,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-19.6796,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(128.874,'J/(mol*K)'), comment="""Thermo library: CHOF_G4 + radical(CsOJ) + radical(CsF1sHO2s)"""),
)

species(
    label = 'F[CH]OC1(F)C=C2OOC21(1367)',
    structure = adjacencyList("""multiplicity 2
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {10,S}
3  O u0 p2 c0 {6,S} {10,S}
4  O u0 p2 c0 {5,S} {7,S}
5  O u0 p2 c0 {4,S} {8,S}
6  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
7  C u0 p0 c0 {4,S} {6,S} {8,S} {11,S}
8  C u0 p0 c0 {5,S} {7,S} {9,D}
9  C u0 p0 c0 {6,S} {8,D} {12,S}
10 C u1 p0 c0 {2,S} {3,S} {13,S}
11 H u0 p0 c0 {7,S}
12 H u0 p0 c0 {9,S}
13 H u0 p0 c0 {10,S}
"""),
    E0 = (-181.879,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1380,1390,370,380,2900,435,2750,3150,900,1100,580,1155,1237,1373,3147,300,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (149.072,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.14777,0.0691409,-5.9443e-05,2.45653e-08,-4.19516e-12,-21778.2,23.196], Tmin=(100,'K'), Tmax=(1330.64,'K')), NASAPolynomial(coeffs=[13.4681,0.0321053,-1.76939e-05,3.64857e-09,-2.65346e-13,-25057,-39.7617], Tmin=(1330.64,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-181.879,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(299.321,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-O2s(Cds-Cd)) + group(CsCCFO) + group(Cs-(Cds-Cds)CsOsH) + group(CsFHHO) + group(Cds-CdsCsOs) + group(Cds-CdsCsH) + Estimated bicyclic component: polycyclic(s2_4_4_ane) - ring(12dioxetane) - ring(Cyclobutane) + ring(12dioxetane) + ring(Cyclobutene) + radical(Csj(F1s)(O2s-Cs)(H))"""),
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
    label = 'F[CH]OC1=CC2(F)OO[C]12(1368)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {10,S}
3  O u0 p2 c0 {5,S} {6,S}
4  O u0 p2 c0 {8,S} {10,S}
5  O u0 p2 c0 {3,S} {7,S}
6  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
7  C u1 p0 c0 {5,S} {6,S} {8,S}
8  C u0 p0 c0 {4,S} {7,S} {9,D}
9  C u0 p0 c0 {6,S} {8,D} {11,S}
10 C u1 p0 c0 {2,S} {4,S} {12,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {10,S}
"""),
    E0 = (-66.0062,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1380,1390,370,380,2900,435,2950,1000,580,1155,1237,1373,3147,300,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (148.064,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.386197,0.0757345,-7.12335e-05,3.09692e-08,-5.28805e-12,-7805.83,24.8007], Tmin=(100,'K'), Tmax=(1399.79,'K')), NASAPolynomial(coeffs=[20.041,0.0195698,-1.10486e-05,2.30561e-09,-1.68829e-13,-13308.4,-76.633], Tmin=(1399.79,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-66.0062,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(274.378,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-Cd)) + group(O2s-OsCs) + group(O2s-OsCs) + group(Cs-(Cds-Cds)CsOsH) + group(CsCCFO) + group(CsFHHO) + group(Cds-CdsCsOs) + group(Cds-CdsCsH) + polycyclic(s2_4_4_ene_1) + radical(C2CsJOO) + radical(Csj(F1s)(O2s-Cd)(H))"""),
)

species(
    label = 'F[CH]OC1(F)[CH]C2=C1OO2(1369)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {6,S}
2  F u0 p3 c0 {10,S}
3  O u0 p2 c0 {6,S} {10,S}
4  O u0 p2 c0 {5,S} {7,S}
5  O u0 p2 c0 {4,S} {8,S}
6  C u0 p0 c0 {1,S} {3,S} {7,S} {9,S}
7  C u0 p0 c0 {4,S} {6,S} {8,D}
8  C u0 p0 c0 {5,S} {7,D} {9,S}
9  C u1 p0 c0 {6,S} {8,S} {11,S}
10 C u1 p0 c0 {2,S} {3,S} {12,S}
11 H u0 p0 c0 {9,S}
12 H u0 p0 c0 {10,S}
"""),
    E0 = (53.8547,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1380,1390,370,380,2900,435,2950,1000,580,1155,1237,1373,3147,300,800,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (148.064,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.863618,0.0693012,-5.89293e-05,2.30719e-08,-3.60404e-12,6589.13,23.289], Tmin=(100,'K'), Tmax=(1488.7,'K')), NASAPolynomial(coeffs=[17.5589,0.0244426,-1.37301e-05,2.83095e-09,-2.04928e-13,1618.29,-63.8989], Tmin=(1488.7,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(53.8547,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(274.378,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-O2s(Cds-Cd)) + group(O2s-O2s(Cds-Cd)) + group(CsCCFO) + group(Cs-(Cds-Cds)CsHH) + group(CsFHHO) + group(Cds-CdsCsOs) + group(Cds-CdsCsOs) + polycyclic(s2_4_4_ene_m) + radical(C=CCJCO) + radical(Csj(F1s)(O2s-Cs)(H))"""),
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
    label = 'F[CH]OC1(F)CC2(F)OO[C]12(1370)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {11,S}
4  O u0 p2 c0 {7,S} {11,S}
5  O u0 p2 c0 {6,S} {8,S}
6  O u0 p2 c0 {5,S} {10,S}
7  C u0 p0 c0 {2,S} {4,S} {9,S} {10,S}
8  C u0 p0 c0 {1,S} {5,S} {9,S} {10,S}
9  C u0 p0 c0 {7,S} {8,S} {12,S} {13,S}
10 C u1 p0 c0 {6,S} {7,S} {8,S}
11 C u1 p0 c0 {3,S} {4,S} {14,S}
12 H u0 p0 c0 {9,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-379.128,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.615207,0.086236,-9.0091e-05,5.12989e-08,-1.2764e-11,-45486.6,22.9991], Tmin=(100,'K'), Tmax=(925.478,'K')), NASAPolynomial(coeffs=[9.67851,0.0470638,-2.66017e-05,5.56484e-09,-4.09934e-13,-47164.1,-20.0242], Tmin=(925.478,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-379.128,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(324.264,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsCs) + group(CsCCFO) + group(Cs-CsCsOsH) + group(CsCCFO) + group(Cs-CsCsHH) + group(CsFHHO) + polycyclic(s2_4_4_ane) + radical(C2CsJOO) + radical(Csj(F1s)(O2s-Cs)(H))"""),
)

species(
    label = 'FCOC1(F)[CH]C2(F)OO[C]12(1371)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {7,S}
3  F u0 p3 c0 {9,S}
4  O u0 p2 c0 {7,S} {9,S}
5  O u0 p2 c0 {6,S} {8,S}
6  O u0 p2 c0 {5,S} {10,S}
7  C u0 p0 c0 {2,S} {4,S} {10,S} {11,S}
8  C u0 p0 c0 {1,S} {5,S} {10,S} {11,S}
9  C u0 p0 c0 {3,S} {4,S} {12,S} {13,S}
10 C u1 p0 c0 {6,S} {7,S} {8,S}
11 C u1 p0 c0 {7,S} {8,S} {14,S}
12 H u0 p0 c0 {9,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-377.403,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.859032,0.0813312,-7.68624e-05,3.82192e-08,-8.34399e-12,-45288.2,24.1623], Tmin=(100,'K'), Tmax=(1030.59,'K')), NASAPolynomial(coeffs=[9.81668,0.0465642,-2.62599e-05,5.4856e-09,-4.03488e-13,-47134.6,-19.3231], Tmin=(1030.59,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-377.403,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(324.264,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsCs) + group(CsCCFO) + group(Cs-CsCsOsH) + group(CsCCFO) + group(Cs-CsCsHH) + group(CsFHHO) + polycyclic(s2_4_4_ane) + radical(C2CsJOO) + radical(CCJCOOH)"""),
)

species(
    label = 'F[CH]O[C]1C(F)C2(F)OOC12(1372)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {9,S}
3  F u0 p3 c0 {11,S}
4  O u0 p2 c0 {5,S} {7,S}
5  O u0 p2 c0 {4,S} {8,S}
6  O u0 p2 c0 {10,S} {11,S}
7  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
8  C u0 p0 c0 {5,S} {7,S} {10,S} {12,S}
9  C u0 p0 c0 {2,S} {7,S} {10,S} {13,S}
10 C u1 p0 c0 {6,S} {8,S} {9,S}
11 C u1 p0 c0 {3,S} {6,S} {14,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-328.437,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([333,384,448,608,1254,1480,2950,1000,259,529,569,1128,1321,1390,3140,580,1155,1237,1373,3147,300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.059612,0.0967494,-0.000129785,9.94553e-08,-3.21585e-11,-39369.1,26.937], Tmin=(100,'K'), Tmax=(742.157,'K')), NASAPolynomial(coeffs=[9.70123,0.0447812,-2.47446e-05,5.09413e-09,-3.70702e-13,-40800.1,-16.7026], Tmin=(742.157,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-328.437,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(324.264,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsCs) + group(Cs-CsCsOsH) + group(Cs-CsCsOsH) + group(CsCCFO) + group(CsCsCsFH) + group(CsFHHO) + polycyclic(s2_4_4_ane) + radical(C2CsJOCs) + radical(Csj(F1s)(O2s-Cs)(H)) + longDistanceInteraction_cyclic(Cs(F)-Cs(F)) + longDistanceInteraction_cyclic(Cs(F)-Cs(F))"""),
)

species(
    label = 'FC(F)O[C]1[CH]C2(F)OOC12(1373)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {8,S}
2  F u0 p3 c0 {9,S}
3  F u0 p3 c0 {9,S}
4  O u0 p2 c0 {9,S} {10,S}
5  O u0 p2 c0 {6,S} {7,S}
6  O u0 p2 c0 {5,S} {8,S}
7  C u0 p0 c0 {5,S} {8,S} {10,S} {12,S}
8  C u0 p0 c0 {1,S} {6,S} {7,S} {11,S}
9  C u0 p0 c0 {2,S} {3,S} {4,S} {13,S}
10 C u1 p0 c0 {4,S} {7,S} {11,S}
11 C u1 p0 c0 {8,S} {10,S} {14,S}
12 H u0 p0 c0 {7,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-371.913,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.333944,0.0906775,-0.000112781,8.07597e-08,-2.4796e-11,-44607.7,28.4493], Tmin=(100,'K'), Tmax=(773.933,'K')), NASAPolynomial(coeffs=[9.09461,0.0453988,-2.50236e-05,5.16567e-09,-3.77191e-13,-45963.7,-11.5708], Tmin=(773.933,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-371.913,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(324.264,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsCs) + group(Cs-CsCsOsH) + group(Cs-CsCsOsH) + group(CsCCFO) + group(Cs-CsCsHH) + group(CsFFHO) + polycyclic(s2_4_4_ane) + radical(C2CsJOCs) + radical(CCJCOOH)"""),
)

species(
    label = 'F[CH]OC1(F)C(F)[C]2OOC21(1374)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {9,S}
3  F u0 p3 c0 {11,S}
4  O u0 p2 c0 {7,S} {11,S}
5  O u0 p2 c0 {6,S} {8,S}
6  O u0 p2 c0 {5,S} {10,S}
7  C u0 p0 c0 {1,S} {4,S} {8,S} {9,S}
8  C u0 p0 c0 {5,S} {7,S} {10,S} {12,S}
9  C u0 p0 c0 {2,S} {7,S} {10,S} {13,S}
10 C u1 p0 c0 {6,S} {8,S} {9,S}
11 C u1 p0 c0 {3,S} {4,S} {14,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-322.517,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([333,384,448,608,1254,1480,2950,1000,259,529,569,1128,1321,1390,3140,580,1155,1237,1373,3147,300,800,800,800,800,800,800,1600,1600,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.593341,0.0855046,-9.24876e-05,5.57725e-08,-1.4633e-11,-38676.1,25.1921], Tmin=(100,'K'), Tmax=(886.544,'K')), NASAPolynomial(coeffs=[9.39521,0.0457917,-2.5295e-05,5.24502e-09,-3.84606e-13,-40236.8,-16.2119], Tmin=(886.544,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-322.517,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(324.264,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsCs) + group(CsCCFO) + group(Cs-CsCsOsH) + group(Cs-CsCsOsH) + group(CsCsCsFH) + group(CsFHHO) + polycyclic(s2_4_4_ane) + radical(C2CsJOO) + radical(Csj(F1s)(O2s-Cs)(H)) + longDistanceInteraction_cyclic(Cs(F)-Cs(F)) + longDistanceInteraction_cyclic(Cs(F)-Cs(F))"""),
)

species(
    label = 'FC(F)OC1(F)[CH][C]2OOC21(1375)',
    structure = adjacencyList("""multiplicity 3
1  F u0 p3 c0 {7,S}
2  F u0 p3 c0 {9,S}
3  F u0 p3 c0 {9,S}
4  O u0 p2 c0 {7,S} {9,S}
5  O u0 p2 c0 {6,S} {8,S}
6  O u0 p2 c0 {5,S} {10,S}
7  C u0 p0 c0 {1,S} {4,S} {8,S} {11,S}
8  C u0 p0 c0 {5,S} {7,S} {10,S} {12,S}
9  C u0 p0 c0 {2,S} {3,S} {4,S} {13,S}
10 C u1 p0 c0 {6,S} {8,S} {11,S}
11 C u1 p0 c0 {7,S} {10,S} {14,S}
12 H u0 p0 c0 {8,S}
13 H u0 p0 c0 {9,S}
14 H u0 p0 c0 {11,S}
"""),
    E0 = (-365.993,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (168.071,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.876034,0.0795473,-7.68982e-05,4.03683e-08,-9.33548e-12,-43915.3,26.6605], Tmin=(100,'K'), Tmax=(981.896,'K')), NASAPolynomial(coeffs=[9.19936,0.04564,-2.50993e-05,5.19885e-09,-3.80974e-13,-45549.9,-13.3427], Tmin=(981.896,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-365.993,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(324.264,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsCs) + group(O2s-OsCs) + group(O2s-OsCs) + group(CsCCFO) + group(Cs-CsCsOsH) + group(Cs-CsCsOsH) + group(Cs-CsCsHH) + group(CsFFHO) + polycyclic(s2_4_4_ane) + radical(C2CsJOO) + radical(CCJCOOH)"""),
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
    E0 = (-144.918,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (154.082,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (161.487,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (22.9981,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (12.4,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (298.866,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (-136.634,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS8',
    E0 = (-97.6288,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS9',
    E0 = (-48.0828,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS10',
    E0 = (-144.918,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS11',
    E0 = (-57.5044,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS12',
    E0 = (104.07,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS13',
    E0 = (-27.0729,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS14',
    E0 = (155.51,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS15',
    E0 = (224.816,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS16',
    E0 = (127.069,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS17',
    E0 = (192.825,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS18',
    E0 = (222.694,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS19',
    E0 = (3.82257,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS20',
    E0 = (-36.7619,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS21',
    E0 = (62.0996,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS22',
    E0 = (79.3818,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS23',
    E0 = (65.6657,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS24',
    E0 = (52.4632,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    products = ['CHFO(47)', 'FC1=CC2(F)OOC12(939)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(5e+12,'s^-1'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""Exact match found for rate rule [RJJ]
Euclidian distance = 0
family: 1,4_Linear_birad_scission"""),
)

reaction(
    label = 'reaction2',
    reactants = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    products = ['F[CH]OC12[CH]C(F)(OO1)C2F(1358)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(1e+13,'s^-1'), n=0, Ea=(299,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""Exact match found for rate rule [OF]
Euclidian distance = 0
family: 1,2_XY_interchange"""),
)

reaction(
    label = 'reaction3',
    reactants = ['F[CH]OC1(F)[CH]C2(OO2)C1F(1359)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(2e+13,'s^-1'), n=0, Ea=(299,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""Exact match found for rate rule [OF]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: 1,2_XY_interchange"""),
)

reaction(
    label = 'reaction4',
    reactants = ['F[CH]O[C](F)C1C2OOC21F(1360)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(6.55606e+10,'s^-1'), n=0.64, Ea=(159.935,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [cCs(-HC)CJ;CsJ;C]
Euclidian distance = 0
family: 1,2_shiftC"""),
)

reaction(
    label = 'reaction5',
    reactants = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    products = ['F[CH]OC1(F)C2OO[C](F)C21(1361)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(1.33e+08,'s^-1'), n=1.36, Ea=(157.318,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [cCs(-R!HR!H)CJ;CsJ;C] for rate rule [cCs(-R!HR!H)CJ;CsJ-CsH;C]
Euclidian distance = 1.0
family: 1,2_shiftC"""),
)

reaction(
    label = 'reaction6',
    reactants = ['[CH]F(137)', '[O]C1(F)[CH]C2(F)OOC12(1362)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(43772.1,'m^3/(mol*s)'), n=0.920148, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(303.03,'K'), Tmax=(2000,'K'), comment="""Estimated using an average for rate rule [O_rad/NonDe;Birad]
Euclidian distance = 0
family: Birad_R_Recombination
Ea raised from -3.0 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction7',
    reactants = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    products = ['FC1OC2(F)C3OOC3(F)C12(1027)'],
    transitionState = 'TS7',
    kinetics = Arrhenius(A=(1.62e+12,'s^-1'), n=-0.305, Ea=(8.28432,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R4_SSS;C_rad_out_single;Cpri_rad_out_single] for rate rule [R4_SSS;C_rad_out_1H;Cpri_rad_out_H/NonDeC]
Euclidian distance = 2.23606797749979
family: Birad_recombination"""),
)

reaction(
    label = 'reaction8',
    reactants = ['F[CH]OC1(F)[CH]OOC(F)=C1(1363)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS8',
    kinetics = Arrhenius(A=(5.4227e+18,'s^-1'), n=-0.859165, Ea=(130.857,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [Rn0cx_gamma;doublebond_intra_pri;radadd_intra_csHNd] for rate rule [Rn0c6_gamma;doublebond_intra_pri;radadd_intra_csHO]
Euclidian distance = 1.4142135623730951
family: Intra_R_Add_Endocyclic"""),
)

reaction(
    label = 'reaction9',
    reactants = ['F[CH]OC(F)=CC1(F)[CH]OO1(1364)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS9',
    kinetics = Arrhenius(A=(1.23261e+08,'s^-1'), n=1.06333, Ea=(126.217,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R4_Cs_RR_D;doublebond_intra_pri;radadd_intra_csHNd] for rate rule [R4_Cs_RR_D;doublebond_intra_pri;radadd_intra_csHO]
Euclidian distance = 1.0
family: Intra_R_Add_Endocyclic"""),
)

reaction(
    label = 'reaction10',
    reactants = ['[O]OC1C(F)=CC1(F)O[CH]F(1365)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS10',
    kinetics = Arrhenius(A=(5.83633e+10,'s^-1'), n=0.345735, Ea=(68.5957,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R6_cyclic;doublebond_intra_pri;radadd_intra] for rate rule [Rn2c4_alpha_long;doublebond_intra_pri;radadd_intra_O]
Euclidian distance = 1.4142135623730951
family: Intra_R_Add_Endocyclic
Ea raised from 68.2 to 68.6 kJ/mol to match endothermicity of reaction."""),
)

reaction(
    label = 'reaction11',
    reactants = ['CHFO(47)', 'F[C]1[CH]C2(F)OOC12(943)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS11',
    kinetics = Arrhenius(A=(2.66944e+13,'m^3/(mol*s)'), n=-2.06969, Ea=(92.2945,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.21909771748945858, var=15.050572460742625, Tref=1000.0, N=2985, data_mean=0.0, correlation='Root',), comment="""Estimated from node Root"""),
)

reaction(
    label = 'reaction12',
    reactants = ['F(37)', 'F[CH]OC1=CC2(F)OOC12(1366)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS12',
    kinetics = Arrhenius(A=(1.575e+07,'m^3/(mol*s)'), n=3.11585e-09, Ea=(63.3897,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R-inRing_N-3R->C_N-1R!H->N_N-2R!H->O_N-3BrClFNOS->Cl_N-2CNS->N_N-3BrFNOS->N_3BrFOS->F',), comment="""Estimated from node Root_N-3R-inRing_N-3R->C_N-1R!H->N_N-2R!H->O_N-3BrClFNOS->Cl_N-2CNS->N_N-3BrFNOS->N_3BrFOS->F"""),
)

reaction(
    label = 'reaction13',
    reactants = ['[O][CH]F(388)', 'FC1=CC2(F)OOC12(939)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS13',
    kinetics = Arrhenius(A=(9.10216e-08,'m^3/(mol*s)'), n=3.71185, Ea=(20.7906,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.339286171633947, var=3.7349511333863634, Tref=1000.0, N=1489, data_mean=0.0, correlation='Root_N-3R-inRing_Ext-3R-R_Ext-4R!H-R',), comment="""Estimated from node Root_N-3R-inRing_Ext-3R-R_Ext-4R!H-R"""),
)

reaction(
    label = 'reaction14',
    reactants = ['F(37)', 'F[CH]OC1(F)C=C2OOC21(1367)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS14',
    kinetics = Arrhenius(A=(1.575e+07,'m^3/(mol*s)'), n=3.11585e-09, Ea=(44.0787,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R-inRing_N-3R->C_N-1R!H->N_N-2R!H->O_N-3BrClFNOS->Cl_N-2CNS->N_N-3BrFNOS->N_3BrFOS->F',), comment="""Estimated from node Root_N-3R-inRing_N-3R->C_N-1R!H->N_N-2R!H->O_N-3BrClFNOS->Cl_N-2CNS->N_N-3BrFNOS->N_3BrFOS->F"""),
)

reaction(
    label = 'reaction15',
    reactants = ['[O][CH]F(388)', 'F[C]1[CH]C2(F)OOC12(943)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS15',
    kinetics = Arrhenius(A=(9.04e+06,'m^3/(mol*s)'), n=2.17087e-08, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C_Ext-2C-R_Ext-2C-R',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C_Ext-2C-R_Ext-2C-R"""),
)

reaction(
    label = 'reaction16',
    reactants = ['HF(38)', 'F[CH]OC1=CC2(F)OO[C]12(1368)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS16',
    kinetics = Arrhenius(A=(281.116,'m^3/(mol*s)'), n=1.03051, Ea=(253.77,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17160344105964337, var=17.74244203879562, Tref=1000.0, N=7, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""Estimated from node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R"""),
)

reaction(
    label = 'reaction17',
    reactants = ['HF(38)', 'F[CH]OC1(F)[CH]C2=C1OO2(1369)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS17',
    kinetics = Arrhenius(A=(281.116,'m^3/(mol*s)'), n=1.03051, Ea=(199.665,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.17160344105964337, var=17.74244203879562, Tref=1000.0, N=7, data_mean=0.0, correlation='HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R',), comment="""Estimated from node HF_Ext-3COCdCddCtO2d-R_Ext-4COCdCddCtO2d-R"""),
)

reaction(
    label = 'reaction18',
    reactants = ['CHF(40)', '[O]C1(F)[CH]C2(F)OOC12(1362)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS18',
    kinetics = Arrhenius(A=(128827,'m^3/(mol*s)'), n=0.469398, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.009898522871762284, var=0.3372166703721302, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-3R->H_Ext-3BrCClFINOPSSi-R',), comment="""Estimated from node Root_N-3R->H_Ext-3BrCClFINOPSSi-R"""),
)

reaction(
    label = 'reaction19',
    reactants = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    products = ['F[CH]OC1(F)CC2(F)OO[C]12(1370)'],
    transitionState = 'TS19',
    kinetics = Arrhenius(A=(1.05815e+09,'s^-1'), n=0.95, Ea=(148.741,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R3H_SS_Cs;C_rad_out_H/NonDeC;Cs_H_out] for rate rule [R3H_SS_Cs;C_rad_out_H/NonDeC;Cs_H_out_OOH/Cs]
Euclidian distance = 2.0
family: intra_H_migration"""),
)

reaction(
    label = 'reaction20',
    reactants = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    products = ['FCOC1(F)[CH]C2(F)OO[C]12(1371)'],
    transitionState = 'TS20',
    kinetics = Arrhenius(A=(2.19773e+08,'s^-1'), n=1.45, Ea=(108.157,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R4H_SSS_OCs;Y_rad_out;Cs_H_out_OOH/Cs] for rate rule [R4H_SSS_OCs;C_rad_out_1H;Cs_H_out_OOH/Cs]
Euclidian distance = 2.0
family: intra_H_migration"""),
)

reaction(
    label = 'reaction21',
    reactants = ['F[CH]O[C]1C(F)C2(F)OOC12(1372)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS21',
    kinetics = Arrhenius(A=(5.38157e+14,'s^-1'), n=-0.447076, Ea=(170.118,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08474952276158404, var=26.08378321593064, Tref=1000.0, N=4, data_mean=0.0, correlation='R2F_Ext-1R!H-R',), comment="""Estimated from node R2F_Ext-1R!H-R"""),
)

reaction(
    label = 'reaction22',
    reactants = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    products = ['FC(F)O[C]1[CH]C2(F)OOC12(1373)'],
    transitionState = 'TS22',
    kinetics = Arrhenius(A=(0.00930803,'s^-1'), n=4.16824, Ea=(224.3,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R3F',), comment="""Estimated from node R3F"""),
)

reaction(
    label = 'reaction23',
    reactants = ['F[CH]OC1(F)C(F)[C]2OOC21(1374)'],
    products = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    transitionState = 'TS23',
    kinetics = Arrhenius(A=(5.38157e+14,'s^-1'), n=-0.447076, Ea=(167.765,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.08474952276158404, var=26.08378321593064, Tref=1000.0, N=4, data_mean=0.0, correlation='R2F_Ext-1R!H-R',), comment="""Estimated from node R2F_Ext-1R!H-R"""),
)

reaction(
    label = 'reaction24',
    reactants = ['F[CH]OC1(F)[CH]C2(F)OOC12(1025)'],
    products = ['FC(F)OC1(F)[CH][C]2OOC21(1375)'],
    transitionState = 'TS24',
    kinetics = Arrhenius(A=(1.64853e+07,'s^-1'), n=1.15307, Ea=(197.382,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R5nF',), comment="""Estimated from node R5nF"""),
)

network(
    label = 'PDepNetwork #227',
    isomers = [
        'F[CH]OC1(F)[CH]C2(F)OOC12(1025)',
    ],
    reactants = [
        ('CHFO(47)', 'FC1=CC2(F)OOC12(939)'),
    ],
    bathGas = {
        'N2': 0.5,
        'Ne': 0.5,
    },
)

pressureDependence(
    label = 'PDepNetwork #227',
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

