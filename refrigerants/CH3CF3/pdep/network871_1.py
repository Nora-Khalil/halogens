species(
    label = 'O=C(O)C(=O)OF(2162)',
    structure = adjacencyList("""1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {6,S} {8,S}
3 O u0 p2 c0 {1,S} {7,S}
4 O u0 p2 c0 {6,D}
5 O u0 p2 c0 {7,D}
6 C u0 p0 c0 {2,S} {4,D} {7,S}
7 C u0 p0 c0 {3,S} {5,D} {6,S}
8 H u0 p0 c0 {2,S}
"""),
    E0 = (-606.368,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,990,1113,200,800,900,1000,1100,1200,1300,1400,1500,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (108.025,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.1158,0.047492,-5.09623e-05,2.86285e-08,-6.84805e-12,-72866.4,17.3002], Tmin=(100,'K'), Tmax=(972.682,'K')), NASAPolynomial(coeffs=[8.06182,0.0230399,-1.3254e-05,2.78357e-09,-2.05339e-13,-74023.1,-11.2212], Tmin=(972.682,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-606.368,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(170.447,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-O2d)H) + group(O2sCF) + group(Cds-O2d(Cds-O2d)O2s) + group(Cds-O2d(Cds-O2d)O2s)"""),
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
    label = 'O=C=C(O)OOF(2168)',
    structure = adjacencyList("""1 F u0 p3 c0 {4,S}
2 O u0 p2 c0 {4,S} {6,S}
3 O u0 p2 c0 {6,S} {8,S}
4 O u0 p2 c0 {1,S} {2,S}
5 O u0 p2 c0 {7,D}
6 C u0 p0 c0 {2,S} {3,S} {7,D}
7 C u0 p0 c0 {5,D} {6,D}
8 H u0 p0 c0 {3,S}
"""),
    E0 = (-163.713,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,277,555,632,350,440,435,1725,2120,512.5,787.5,180,180],'cm^-1')),
        HinderedRotor(inertia=(1.27896,'amu*angstrom^2'), symmetry=1, barrier=(29.4057,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(1.27929,'amu*angstrom^2'), symmetry=1, barrier=(29.4134,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(1.2795,'amu*angstrom^2'), symmetry=1, barrier=(29.4182,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (108.025,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[-0.808039,0.0741517,-9.15501e-05,4.72649e-08,-8.59257e-12,-19489.7,27.4806], Tmin=(100,'K'), Tmax=(1657.89,'K')), NASAPolynomial(coeffs=[24.6906,-0.0116384,8.02798e-06,-1.60696e-09,1.08517e-13,-24609.1,-98.3673], Tmin=(1657.89,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-163.713,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(170.447,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-O2s(Cds-Cd)) + group(O2s-(Cds-Cd)H) + group(O2sFO) + missing(O2d-Cdd) + group(Cds-(Cdd-O2d)OsOs) + missing(Cdd-CdO2d)"""),
)

species(
    label = 'O=C=C(OO)OF(2169)',
    structure = adjacencyList("""1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {4,S} {6,S}
3 O u0 p2 c0 {1,S} {6,S}
4 O u0 p2 c0 {2,S} {8,S}
5 O u0 p2 c0 {7,D}
6 C u0 p0 c0 {2,S} {3,S} {7,D}
7 C u0 p0 c0 {5,D} {6,D}
8 H u0 p0 c0 {4,S}
"""),
    E0 = (-101.208,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1310,387.5,850,1000,231,791,350,440,435,1725,2120,512.5,787.5,180],'cm^-1')),
        HinderedRotor(inertia=(1.31943,'amu*angstrom^2'), symmetry=1, barrier=(30.3362,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(1.31712,'amu*angstrom^2'), symmetry=1, barrier=(30.2833,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(1.31807,'amu*angstrom^2'), symmetry=1, barrier=(30.3051,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (108.025,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.234508,0.0669576,-8.28799e-05,4.4569e-08,-8.70845e-12,-12023.2,24.8052], Tmin=(100,'K'), Tmax=(1453.11,'K')), NASAPolynomial(coeffs=[22.1829,-0.00524063,3.80891e-06,-7.8189e-10,5.38204e-14,-17158.2,-85.0055], Tmin=(1453.11,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-101.208,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(170.447,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-O2s(Cds-Cd)) + group(O2sCF) + group(O2s-OsH) + missing(O2d-Cdd) + group(Cds-(Cdd-O2d)OsOs) + missing(Cdd-CdO2d)"""),
)

species(
    label = '[O]C([O])C(=O)OF(2170)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {7,S}
3 O u1 p2 c0 {6,S}
4 O u1 p2 c0 {6,S}
5 O u0 p2 c0 {7,D}
6 C u0 p0 c0 {3,S} {4,S} {7,S} {8,S}
7 C u0 p0 c0 {2,S} {5,D} {6,S}
8 H u0 p0 c0 {6,S}
"""),
    E0 = (-181.523,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([990,1113,1380,1390,370,380,2900,435,180,180,180,943.088,943.162,943.2,943.207,943.22],'cm^-1')),
        HinderedRotor(inertia=(0.0966787,'amu*angstrom^2'), symmetry=1, barrier=(2.22283,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.0966877,'amu*angstrom^2'), symmetry=1, barrier=(2.22304,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (108.025,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.87633,0.051182,-7.83435e-05,6.77705e-08,-2.38782e-11,-21760,23.857], Tmin=(100,'K'), Tmax=(751.478,'K')), NASAPolynomial(coeffs=[7.02624,0.0205541,-1.07894e-05,2.14622e-09,-1.52063e-13,-22443.2,1.08718], Tmin=(751.478,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-181.523,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(174.604,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsH) + group(O2s-CsH) + group(O2sCF) + group(Cs-CsOsOsH) + group(Cds-OdCsOs) + radical(C=OCOJ) + radical(C=OCOJ)"""),
)

species(
    label = '[O]C(=O)C([O])OF(2171)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u1 p2 c0 {6,S}
4 O u1 p2 c0 {7,S}
5 O u0 p2 c0 {7,D}
6 C u0 p0 c0 {2,S} {3,S} {7,S} {8,S}
7 C u0 p0 c0 {4,S} {5,D} {6,S}
8 H u0 p0 c0 {6,S}
"""),
    E0 = (-199.551,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([557,1111,1380,1390,370,380,2900,435,180,180,180,1197.86,1198.05,1198.07,1198.27,1198.44],'cm^-1')),
        HinderedRotor(inertia=(0.276235,'amu*angstrom^2'), symmetry=1, barrier=(6.35119,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.0531497,'amu*angstrom^2'), symmetry=1, barrier=(54.1622,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (108.025,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.9753,0.0516891,-8.8333e-05,8.72398e-08,-3.3798e-11,-23934.6,23.5777], Tmin=(100,'K'), Tmax=(795.905,'K')), NASAPolynomial(coeffs=[4.03295,0.0269986,-1.47568e-05,2.95884e-09,-2.09498e-13,-23807.6,16.9756], Tmin=(795.905,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-199.551,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(174.604,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2sCF) + group(O2s-CsH) + group(O2s-(Cds-O2d)H) + group(Cs-CsOsOsH) + group(Cds-OdCsOs) + radical(C=OCOJ) + radical(CCOJ)"""),
)

species(
    label = '[O]C([O])=C(O)OF(2172)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {6,S} {8,S}
4 O u1 p2 c0 {7,S}
5 O u1 p2 c0 {7,S}
6 C u0 p0 c0 {2,S} {3,S} {7,D}
7 C u0 p0 c0 {4,S} {5,S} {6,D}
8 H u0 p0 c0 {3,S}
"""),
    E0 = (-248.978,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([231,791,3615,1277.5,1000,325,375,415,465,420,450,1700,1750,307.113,307.122,307.154],'cm^-1')),
        HinderedRotor(inertia=(0.256693,'amu*angstrom^2'), symmetry=1, barrier=(17.1814,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.25669,'amu*angstrom^2'), symmetry=1, barrier=(17.1808,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (108.025,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[0.790828,0.073564,-0.000120322,9.24373e-08,-2.714e-11,-29832.4,21.4602], Tmin=(100,'K'), Tmax=(846.246,'K')), NASAPolynomial(coeffs=[14.6872,0.00788236,-3.90492e-06,7.29575e-10,-4.89051e-14,-32184.4,-43.2628], Tmin=(846.246,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-248.978,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(174.604,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2sCF) + group(O2s-(Cds-Cd)H) + group(O2s-(Cds-Cd)H) + group(O2s-(Cds-Cd)H) + group(Cds-CdsCsCs) + group(Cds-CdsCsCs) + radical(C=COJ) + radical(C=COJ)"""),
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
    label = '[O]C(=O)C(=O)O(2173)',
    structure = adjacencyList("""multiplicity 2
1 O u0 p2 c0 {5,S} {7,S}
2 O u0 p2 c0 {5,D}
3 O u1 p2 c0 {6,S}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {1,S} {2,D} {6,S}
6 C u0 p0 c0 {3,S} {4,D} {5,S}
7 H u0 p0 c0 {1,S}
"""),
    E0 = (-479.287,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,200,800,900,1000,1100,1200,1300,1400,1500,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (89.0268,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.37564,0.040515,-5.3068e-05,3.85794e-08,-1.18684e-11,-57590.7,17.2782], Tmin=(100,'K'), Tmax=(775.675,'K')), NASAPolynomial(coeffs=[6.61175,0.0186706,-1.0826e-05,2.2744e-09,-1.6752e-13,-58247.9,-2.08262], Tmin=(775.675,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-479.287,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(149.66,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-O2d)H) + group(O2s-(Cds-O2d)H) + group(Cds-O2d(Cds-O2d)O2s) + group(Cds-O2d(Cds-O2d)O2s) + radical(C=OC=OOJ)"""),
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
    label = 'O=[C]C(=O)OF(2174)',
    structure = adjacencyList("""multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {5,S}
3 O u0 p2 c0 {5,D}
4 O u0 p2 c0 {6,D}
5 C u0 p0 c0 {2,S} {3,D} {6,S}
6 C u1 p0 c0 {4,D} {5,S}
"""),
    E0 = (-188.774,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([990,1113,1855,455,950,437.969,438.638,439.11,439.292,440.997],'cm^-1')),
        HinderedRotor(inertia=(0.31461,'amu*angstrom^2'), symmetry=1, barrier=(43.105,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.314766,'amu*angstrom^2'), symmetry=1, barrier=(43.0762,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (91.0179,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.48528,0.0357768,-3.99738e-05,2.18163e-08,-4.80663e-12,-22651.7,15.8972], Tmin=(100,'K'), Tmax=(1083.58,'K')), NASAPolynomial(coeffs=[8.96519,0.011857,-6.86248e-06,1.44526e-09,-1.06806e-13,-24056.1,-15.885], Tmin=(1083.58,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-188.774,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(124.717,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2sCF) + group(Cds-O2d(Cds-O2d)O2s) + group(Cds-O2d(Cds-O2d)H) + radical(OC=OCJ=O)"""),
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
    label = '[O]C(=O)C(=O)OF(2175)',
    structure = adjacencyList("""multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {6,S}
3 O u0 p2 c0 {6,D}
4 O u1 p2 c0 {7,S}
5 O u0 p2 c0 {7,D}
6 C u0 p0 c0 {2,S} {3,D} {7,S}
7 C u0 p0 c0 {4,S} {5,D} {6,S}
"""),
    E0 = (-344.779,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([990,1113,300,800,800,800,800,800,1600,1600,1600,1600,1600],'cm^-1')),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.156089,'amu*angstrom^2'), symmetry=1, barrier=(3.5888,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (107.017,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.81286,0.053993,-8.42038e-05,7.01827e-08,-2.39876e-11,-41394.1,19.4632], Tmin=(100,'K'), Tmax=(710.135,'K')), NASAPolynomial(coeffs=[7.86586,0.0198995,-1.21919e-05,2.58153e-09,-1.89865e-13,-42253.8,-7.66735], Tmin=(710.135,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-344.779,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(149.66,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2sCF) + group(O2s-(Cds-O2d)H) + group(Cds-O2d(Cds-O2d)O2s) + group(Cds-O2d(Cds-O2d)O2s) + radical(C=OC=OOJ)"""),
)

species(
    label = '[O]F(127)',
    structure = adjacencyList("""multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u1 p2 c0 {1,S}
"""),
    E0 = (102.686,'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(34.9933,'amu')),
        LinearRotor(inertia=(15.6231,'amu*angstrom^2'), symmetry=1),
        HarmonicOscillator(frequencies=([1151.69],'cm^-1')),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (34.9978,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.51779,-0.00115859,7.7708e-06,-9.55983e-09,3.74809e-12,12350.1,5.42233], Tmin=(10,'K'), Tmax=(823.913,'K')), NASAPolynomial(coeffs=[3.16214,0.00226288,-1.54389e-06,4.73852e-10,-5.4015e-14,12351.2,6.72012], Tmin=(823.913,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(102.686,'kJ/mol'), Cp0=(29.1007,'J/(mol*K)'), CpInf=(37.4151,'J/(mol*K)'), label="""[O]F""", comment="""Thermo library: CHOF_G4"""),
)

species(
    label = 'O=[C]C(=O)O(2176)',
    structure = adjacencyList("""multiplicity 2
1 O u0 p2 c0 {4,S} {6,S}
2 O u0 p2 c0 {4,D}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {2,D} {5,S}
5 C u1 p0 c0 {3,D} {4,S}
6 H u0 p0 c0 {1,S}
"""),
    E0 = (-323.282,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([3615,1277.5,1000,1855,455,950,341.575,343.133,964.243,1465.81],'cm^-1')),
        HinderedRotor(inertia=(0.419388,'amu*angstrom^2'), symmetry=1, barrier=(34.6871,'kJ/mol'), semiclassical=False),
        HinderedRotor(inertia=(0.419215,'amu*angstrom^2'), symmetry=1, barrier=(34.5991,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (73.0274,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.74337,0.0260452,-2.26906e-05,9.41168e-09,-1.55069e-12,-38835.4,14.7947], Tmin=(100,'K'), Tmax=(1438.16,'K')), NASAPolynomial(coeffs=[9.12273,0.0083022,-4.18474e-06,8.3322e-10,-5.94748e-14,-40670.3,-18.3001], Tmin=(1438.16,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-323.282,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(124.717,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-O2d)H) + group(Cds-O2d(Cds-O2d)O2s) + group(Cds-O2d(Cds-O2d)H) + radical(OC=OCJ=O)"""),
)

species(
    label = 'O=[C]OF(458)',
    structure = adjacencyList("""multiplicity 2
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u0 p2 c0 {4,D}
4 C u1 p0 c0 {2,S} {3,D}
"""),
    E0 = (-35.6837,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([990,1113,1855,455,950],'cm^-1')),
        HinderedRotor(inertia=(1.77736,'amu*angstrom^2'), symmetry=1, barrier=(40.8651,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (63.0078,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.98172,0.0254564,-4.70449e-05,4.25373e-08,-1.44425e-11,-4258,9.53187], Tmin=(100,'K'), Tmax=(878.476,'K')), NASAPolynomial(coeffs=[5.67747,0.00648674,-3.22257e-06,6.05546e-10,-4.04972e-14,-4473.3,-1.65391], Tmin=(878.476,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-35.6837,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(103.931,'J/(mol*K)'), comment="""Thermo library: CHOF_G4 + radical((O)CJOC)"""),
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
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.92208,0.00762454,3.29884e-06,-1.07135e-08,5.11587e-12,-23028.2,11.2926], Tmin=(200,'K'), Tmax=(1000,'K')), NASAPolynomial(coeffs=[5.39206,0.00411221,-1.48195e-06,2.39875e-10,-1.43903e-14,-23860.7,-2.23529], Tmin=(1000,'K'), Tmax=(6000,'K'))], Tmin=(200,'K'), Tmax=(6000,'K'), E0=(-192.093,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(78.9875,'J/(mol*K)'), label="""HOCO""", comment="""Thermo library: FFCM1(-)"""),
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
    E0 = (-418.724,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (88.4036,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (137.305,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (23.8041,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (46.3149,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (-31.9939,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (-223.929,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS8',
    E0 = (22.0868,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS9',
    E0 = (49.4914,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS10',
    E0 = (-38.1295,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS11',
    E0 = (-45.3107,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['O=C(O)C(=O)OF(2162)'],
    products = ['HF(38)', 'CO2(14)', 'CO2(14)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(0.00285451,'s^-1'), n=4.62568, Ea=(5.17746,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.3917696014098424, var=52.52930589142705, Tref=1000.0, N=14, data_mean=0.0, correlation='Root',), comment="""Estimated from node Root"""),
)

reaction(
    label = 'reaction2',
    reactants = ['O=C=C(O)OOF(2168)'],
    products = ['O=C(O)C(=O)OF(2162)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(4.62709e+20,'s^-1'), n=-1.9758, Ea=(69.6504,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1791595854394145, var=100.97114496904264, Tref=1000.0, N=30, data_mean=0.0, correlation='Root',), comment="""Estimated from node Root"""),
)

reaction(
    label = 'reaction3',
    reactants = ['O=C=C(OO)OF(2169)'],
    products = ['O=C(O)C(=O)OF(2162)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(4.62709e+20,'s^-1'), n=-1.9758, Ea=(56.0464,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.1791595854394145, var=100.97114496904264, Tref=1000.0, N=30, data_mean=0.0, correlation='Root',), comment="""Estimated from node Root"""),
)

reaction(
    label = 'reaction4',
    reactants = ['[O]C([O])C(=O)OF(2170)'],
    products = ['O=C(O)C(=O)OF(2162)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(3.898e+11,'s^-1'), n=0.486, Ea=(22.8614,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [R2radExo;Y_rad;XH_Rrad]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Intra_Disproportionation"""),
)

reaction(
    label = 'reaction5',
    reactants = ['[O]C(=O)C([O])OF(2171)'],
    products = ['O=C(O)C(=O)OF(2162)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(1.4874e+09,'s^-1'), n=1.045, Ea=(63.4002,'kJ/mol'), T0=(1,'K'), comment="""Estimated using an average for rate rule [R3radExo;Y_rad;XH_Rrad]
Euclidian distance = 0
Multiplied by reaction path degeneracy 2.0
family: Intra_Disproportionation"""),
)

reaction(
    label = 'reaction6',
    reactants = ['[O]C([O])=C(O)OF(2172)'],
    products = ['O=C(O)C(=O)OF(2162)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(1.552e+09,'s^-1'), n=0.311, Ea=(34.518,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R4;Y_rad;XH_Rrad_NDe] for rate rule [R4radEndo;Y_rad;XH_Rrad_NDe]
Euclidian distance = 1.0
Multiplied by reaction path degeneracy 2.0
family: Intra_Disproportionation"""),
)

reaction(
    label = 'reaction7',
    reactants = ['F(37)', '[O]C(=O)C(=O)O(2173)'],
    products = ['O=C(O)C(=O)OF(2162)'],
    transitionState = 'TS7',
    kinetics = Arrhenius(A=(3.11128e+07,'m^3/(mol*s)'), n=-5.63145e-08, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.7121440562946592, var=2.9508506800589083, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_3BrCClFINPSSi->C
Multiplied by reaction path degeneracy 2.0"""),
)

reaction(
    label = 'reaction8',
    reactants = ['OH(7)', 'O=[C]C(=O)OF(2174)'],
    products = ['O=C(O)C(=O)OF(2162)'],
    transitionState = 'TS8',
    kinetics = Arrhenius(A=(7.7e+07,'m^3/(mol*s)'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C_Ext-2C-R',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_2R->C_Ext-2C-R"""),
)

reaction(
    label = 'reaction9',
    reactants = ['H(5)', '[O]C(=O)C(=O)OF(2175)'],
    products = ['O=C(O)C(=O)OF(2162)'],
    transitionState = 'TS9',
    kinetics = Arrhenius(A=(4.42074e+06,'m^3/(mol*s)'), n=0.349925, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C',), comment="""Estimated from node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->O_Ext-2O-R_N-3R!H->Cl_3BrCFINOPSSi->C
Multiplied by reaction path degeneracy 2.0"""),
)

reaction(
    label = 'reaction10',
    reactants = ['[O]F(127)', 'O=[C]C(=O)O(2176)'],
    products = ['O=C(O)C(=O)OF(2162)'],
    transitionState = 'TS10',
    kinetics = Arrhenius(A=(7.38316e+06,'m^3/(mol*s)'), n=1.31229e-07, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.016021952005170214, var=0.3543710496450803, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C"""),
)

reaction(
    label = 'reaction11',
    reactants = ['O=[C]OF(458)', 'O=[C]O(457)'],
    products = ['O=C(O)C(=O)OF(2162)'],
    transitionState = 'TS11',
    kinetics = Arrhenius(A=(2.81979e+07,'m^3/(mol*s)'), n=-0.126529, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_2CF->C',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->O_N-1BrCFS-inRing_1BrCFS->C_N-2R->S_N-2BrCF->Br_Ext-1C-R_N-3R!H->F_N-3BrCClINOPSSi->Cl_Ext-1C-R_Ext-3BrCO-R_2CF->C"""),
)

network(
    label = 'PDepNetwork #871',
    isomers = [
        'O=C(O)C(=O)OF(2162)',
    ],
    reactants = [
        ('HF(38)', 'CO2(14)', 'CO2(14)'),
    ],
    bathGas = {
        'N2': 0.5,
        'Ne': 0.5,
    },
)

pressureDependence(
    label = 'PDepNetwork #871',
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

