species(
    label = '[CH]=C(F)C([O])=O(5476)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {4,S}
2 O u1 p2 c0 {5,S}
3 O u0 p2 c0 {5,D}
4 C u0 p0 c0 {1,S} {5,S} {6,D}
5 C u0 p0 c0 {2,S} {3,D} {4,S}
6 C u1 p0 c0 {4,D} {7,S}
7 H u0 p0 c0 {6,S}
"""),
    E0 = (32.9204,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([244,384,691,1241,3120,650,792.5,1650,180,180,1552.31,1552.89,1553.88,1555.16],'cm^-1')),
        HinderedRotor(inertia=(0.345386,'amu*angstrom^2'), symmetry=1, barrier=(7.94111,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (88.0371,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.31434,0.0474937,-9.71256e-05,1.02984e-07,-3.99861e-11,4010.04,18.3513], Tmin=(100,'K'), Tmax=(849.54,'K')), NASAPolynomial(coeffs=[1.58229,0.0256792,-1.40057e-05,2.7554e-09,-1.90875e-13,5046,27.1287], Tmin=(849.54,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(32.9204,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(153.818,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-O2d)H) + group(CdCCF) + longDistanceInteraction_noncyclic(Cd(F)-CO) + group(Cds-O2d(Cds-Cds)O2s) + group(Cds-CdsHH) + radical(CCOJ) + radical(Cdj(Cd-F1sCO)(H))"""),
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
    label = 'C2HF(57)',
    structure = adjacencyList("""1 F u0 p3 c0 {3,S}
2 C u0 p0 c0 {3,T} {4,S}
3 C u0 p0 c0 {1,S} {2,T}
4 H u0 p0 c0 {2,S}
"""),
    E0 = (95.331,'kJ/mol'),
    modes = [
        IdealGasTranslation(mass=(44.0062,'amu')),
        LinearRotor(inertia=(51.6236,'amu*angstrom^2'), symmetry=1),
        HarmonicOscillator(frequencies=([429.793,429.793,596.357,596.357,1107.96,2365.05,3506.88],'cm^-1')),
    ],
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (44.0277,'amu'),
    collisionModel = TransportData(shapeIndex=1, epsilon=(1870.76,'J/mol'), sigma=(4.25,'angstroms'), dipoleMoment=(1,'De'), polarizability=(0,'angstroms^3'), rotrelaxcollnum=0.0, comment="""NIST_Fluorine"""),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.4498,0.0030263,3.99146e-05,-8.9615e-08,5.74336e-11,11468.6,5.90915], Tmin=(10,'K'), Tmax=(555.749,'K')), NASAPolynomial(coeffs=[4.23833,0.0086714,-5.87678e-06,1.96876e-09,-2.53031e-13,11206.2,0.995297], Tmin=(555.749,'K'), Tmax=(3000,'K'))], Tmin=(10,'K'), Tmax=(3000,'K'), E0=(95.331,'kJ/mol'), Cp0=(29.1007,'J/(mol*K)'), CpInf=(87.302,'J/(mol*K)'), label="""C#CF""", comment="""Thermo library: CHOF_G4"""),
)

species(
    label = '[CH]=C=C([O])OF(5563)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {2,S}
2 O u0 p2 c0 {1,S} {4,S}
3 O u1 p2 c0 {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,D}
5 C u0 p0 c0 {4,D} {6,D}
6 C u1 p0 c0 {5,D} {7,S}
7 H u0 p0 c0 {6,S}
"""),
    E0 = (270.544,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([231,791,350,440,435,1725,540,610,2055,3120,650,792.5,1650,180],'cm^-1')),
        HinderedRotor(inertia=(1.98854,'amu*angstrom^2'), symmetry=1, barrier=(45.7205,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (88.0371,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[1.66811,0.0558019,-9.53419e-05,7.99914e-08,-2.54552e-11,32618.7,18.7391], Tmin=(100,'K'), Tmax=(899.904,'K')), NASAPolynomial(coeffs=[9.31151,0.0118147,-5.33198e-06,9.46015e-10,-6.08842e-14,31648.4,-15.0772], Tmin=(899.904,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(270.544,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(153.818,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2sCF) + group(O2s-(Cds-Cd)H) + group(Cds-CdsCsCs) + group(Cds-CdsHH) + group(Cdd-CdsCds) + radical(C=COJ) + radical(C=C=CJ)"""),
)

species(
    label = 'O(7)',
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
    label = '[CH]=C(F)[C]=O(5532)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {3,S}
2 O u0 p2 c0 {5,D}
3 C u0 p0 c0 {1,S} {4,D} {5,S}
4 C u1 p0 c0 {3,D} {6,S}
5 C u1 p0 c0 {2,D} {3,S}
6 H u0 p0 c0 {4,S}
"""),
    E0 = (144.404,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([244,384,691,1241,3120,650,792.5,1650,1855,455,950],'cm^-1')),
        HinderedRotor(inertia=(1.1894,'amu*angstrom^2'), symmetry=1, barrier=(27.3466,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (72.0377,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.32805,0.0397957,-6.0778e-05,4.69442e-08,-1.42847e-11,17425.2,14.5804], Tmin=(100,'K'), Tmax=(807.332,'K')), NASAPolynomial(coeffs=[8.36398,0.00989005,-5.21412e-06,1.06136e-09,-7.65328e-14,16450.6,-13.2476], Tmin=(807.332,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(144.404,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(178.761,'J/(mol*K)'), comment="""Thermo library: CHOF_G4 + radical(Cdj(Cd-F1sCO)(H)) + radical(COj(Cd-F1sCd)(O2d))"""),
)

species(
    label = 'O=C1OC=C1F(5552)',
    structure = adjacencyList("""1 F u0 p3 c0 {4,S}
2 O u0 p2 c0 {5,S} {6,S}
3 O u0 p2 c0 {6,D}
4 C u0 p0 c0 {1,S} {5,D} {6,S}
5 C u0 p0 c0 {2,S} {4,D} {7,S}
6 C u0 p0 c0 {2,S} {3,D} {4,S}
7 H u0 p0 c0 {5,S}
"""),
    E0 = (-251.916,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.0371,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.87861,0.0287925,-2.69814e-05,1.42005e-08,-3.37933e-12,-30261.6,13.535], Tmin=(100,'K'), Tmax=(942.426,'K')), NASAPolynomial(coeffs=[5.42763,0.0179736,-9.76161e-06,2.0194e-09,-1.48015e-13,-30742,1.38864], Tmin=(942.426,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-251.916,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(157.975,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-O2d)(Cds-Cd)) + group(CdCCF) + group(Cds-CdsOsH) + group(Cds-O2d(Cds-Cds)O2s) + longDistanceInteraction_cyclic(Cd(F)-CO) + longDistanceInteraction_cyclic(Cd(F)=CdOs) + ring(Cyclobutene)"""),
)

species(
    label = '[CH]C(F)=C1OO1(5564)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {5,S}
2 O u0 p2 c0 {3,S} {4,S}
3 O u0 p2 c0 {2,S} {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,D}
5 C u0 p0 c0 {1,S} {4,D} {6,S}
6 C u2 p0 c0 {5,S} {7,S}
7 H u0 p0 c0 {6,S}
"""),
    E0 = (271.005,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.0371,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.25122,0.0383514,-3.29141e-05,1.47852e-08,-2.75912e-12,32657.4,17.022], Tmin=(100,'K'), Tmax=(1248.89,'K')), NASAPolynomial(coeffs=[8.70267,0.0176885,-8.09656e-06,1.53745e-09,-1.07215e-13,31045.9,-15.5364], Tmin=(1248.89,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(271.005,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(153.818,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-O2s(Cds-Cd)) + group(O2s-O2s(Cds-Cd)) + group(Cs-(Cds-Cds)HHH) + group(CdCsCdF) + group(Cds-CdsCsCs) + ring(O2s-O2s-Cd(Cd-F)) + radical(AllylJ2_triplet)"""),
)

species(
    label = 'O=C1O[CH][C]1F(5565)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {4,S}
2 O u0 p2 c0 {5,S} {6,S}
3 O u0 p2 c0 {6,D}
4 C u1 p0 c0 {1,S} {5,S} {6,S}
5 C u1 p0 c0 {2,S} {4,S} {7,S}
6 C u0 p0 c0 {2,S} {3,D} {4,S}
7 H u0 p0 c0 {5,S}
"""),
    E0 = (-143.374,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.0371,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.89187,0.00941743,5.41897e-05,-8.72395e-08,3.76048e-11,-17190,16.6872], Tmin=(100,'K'), Tmax=(899.863,'K')), NASAPolynomial(coeffs=[13.7299,0.000650841,3.10989e-06,-7.27921e-10,4.89196e-14,-20736.1,-43.3223], Tmin=(899.863,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-143.374,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(157.975,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-Cs(Cds-O2d)) + group(CsCCFH) + group(Cs-CsOsHH) + group(Cds-OdCsOs) + ring(Beta-Propiolactone) + radical(CsCOCsF1s) + radical(CCsJOC(O))"""),
)

species(
    label = '[O]C1([O])C=C1F(5559)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {6,S}
2 O u1 p2 c0 {4,S}
3 O u1 p2 c0 {4,S}
4 C u0 p0 c0 {2,S} {3,S} {5,S} {6,S}
5 C u0 p0 c0 {4,S} {6,D} {7,S}
6 C u0 p0 c0 {1,S} {4,S} {5,D}
7 H u0 p0 c0 {5,S}
"""),
    E0 = (175.079,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.0371,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[4.41074,0.0196062,-8.26852e-06,7.39521e-10,6.02244e-14,21012.7,9.53173], Tmin=(100,'K'), Tmax=(2747.09,'K')), NASAPolynomial(coeffs=[32.3109,-0.0100102,1.89196e-06,-2.67468e-10,1.91103e-14,1529.95,-160.825], Tmin=(2747.09,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(175.079,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(157.975,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-CsH) + group(O2s-CsH) + group(Cs-CsCsOsOs) + group(Cds-CdsCsH) + group(CdCsCdF) + ring(Cd-Cd(F)-Cs(O2)) + radical(CC(C)(O)OJ) + radical(CC(C)(O)OJ)"""),
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
    label = 'C#CC([O])=O(3710)',
    structure = adjacencyList("""multiplicity 2
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u0 p0 c0 {1,S} {2,D} {4,S}
4 C u0 p0 c0 {3,S} {5,T}
5 C u0 p0 c0 {4,T} {6,S}
6 H u0 p0 c0 {5,S}
"""),
    E0 = (87.8995,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([2175,525,750,770,3400,2100,575.088,575.088,575.092,575.095,575.097],'cm^-1')),
        HinderedRotor(inertia=(0.000509706,'amu*angstrom^2'), symmetry=1, barrier=(0.119627,'kJ/mol'), semiclassical=False),
    ],
    spinMultiplicity = 2,
    opticalIsomers = 1,
    molecularWeight = (69.0387,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.42277,0.0164452,1.21293e-05,-6.88169e-08,6.82251e-11,10588.7,10.6549], Tmin=(100,'K'), Tmax=(386.364,'K')), NASAPolynomial(coeffs=[3.92521,0.0164858,-8.38134e-06,1.69264e-09,-1.22499e-13,10510.7,8.2023], Tmin=(386.364,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(87.8995,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(157.975,'J/(mol*K)'), comment="""Thermo library: 2-BTP_G4 + radical(CCOJ)"""),
)

species(
    label = '[O][C]=O(3667)',
    structure = adjacencyList("""multiplicity 3
1 O u1 p2 c0 {3,S}
2 O u0 p2 c0 {3,D}
3 C u1 p0 c0 {1,S} {2,D}
"""),
    E0 = (31.5354,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([1855,455,950],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (44.0094,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.75939,0.00186753,1.03202e-05,-1.52373e-08,5.80537e-12,3804.5,8.40407], Tmin=(100,'K'), Tmax=(1021.26,'K')), NASAPolynomial(coeffs=[6.36178,0.000422737,-4.06602e-07,1.525e-10,-1.51974e-14,2816.75,-6.43921], Tmin=(1021.26,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(31.5354,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(103.931,'J/(mol*K)'), comment="""Thermo library: DFT_QCI_thermo + radical(OJC=O) + radical((O)CJOH)"""),
)

species(
    label = '[CH]=[C]F(488)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {3,S}
2 C u1 p0 c0 {3,D} {4,S}
3 C u1 p0 c0 {1,S} {2,D}
4 H u0 p0 c0 {2,S}
"""),
    E0 = (350.447,'kJ/mol'),
    modes = [
        HarmonicOscillator(frequencies=([167,640,1190,1142.58,1502.03,3807.5],'cm^-1')),
    ],
    spinMultiplicity = 3,
    opticalIsomers = 1,
    molecularWeight = (44.0277,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[3.55591,0.0076799,-5.30098e-07,-4.54651e-09,2.16658e-12,42166.8,9.46363], Tmin=(100,'K'), Tmax=(1043.42,'K')), NASAPolynomial(coeffs=[5.86818,0.00351556,-1.29996e-06,2.62251e-10,-1.98915e-14,41428.4,-3.016], Tmin=(1043.42,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(350.447,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(133.032,'J/(mol*K)'), comment="""Thermo library: CHOF_G4 + radical(Cds_P) + radical(CdCdF1s)"""),
)

species(
    label = '[O]C([O])=C=CF(5562)',
    structure = adjacencyList("""multiplicity 3
1 F u0 p3 c0 {5,S}
2 O u1 p2 c0 {4,S}
3 O u1 p2 c0 {4,S}
4 C u0 p0 c0 {2,S} {3,S} {6,D}
5 C u0 p0 c0 {1,S} {6,D} {7,S}
6 C u0 p0 c0 {4,D} {5,D}
7 H u0 p0 c0 {5,S}
"""),
    E0 = (-74.0333,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
    molecularWeight = (88.0371,'amu'),
    energyTransferModel = SingleExponentialDown(alpha0=(3.5886,'kJ/mol'), T0=(300,'K'), n=0.85),
    thermo = NASA(polynomials=[NASAPolynomial(coeffs=[2.12091,0.0423278,-5.18789e-05,3.17196e-08,-7.649e-12,-8837.27,16.9448], Tmin=(100,'K'), Tmax=(1012.34,'K')), NASAPolynomial(coeffs=[10.0763,0.0108951,-5.30581e-06,1.05025e-09,-7.53367e-14,-10448,-21.5332], Tmin=(1012.34,'K'), Tmax=(5000,'K'))], Tmin=(100,'K'), Tmax=(5000,'K'), E0=(-74.0333,'kJ/mol'), Cp0=(33.2579,'J/(mol*K)'), CpInf=(157.975,'J/(mol*K)'), comment="""Thermo group additivity estimation: group(O2s-(Cds-Cd)H) + group(O2s-(Cds-Cd)H) + group(Cds-CdsCsCs) + group(CdCddFH) + group(Cdd-CdsCds) + radical(C=COJ) + radical(C=COJ)"""),
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
    E0 = (-35.1145,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS2',
    E0 = (404.898,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS3',
    E0 = (319.403,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS4',
    E0 = (-26.8302,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS5',
    E0 = (202.97,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS6',
    E0 = (102.941,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS7',
    E0 = (107.044,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS8',
    E0 = (175.559,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS9',
    E0 = (91.3214,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS10',
    E0 = (24.0973,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS11',
    E0 = (313.947,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

transitionState(
    label = 'TS12',
    E0 = (98.2788,'kJ/mol'),
    spinMultiplicity = 1,
    opticalIsomers = 1,
)

reaction(
    label = 'reaction1',
    reactants = ['[CH]=C(F)C([O])=O(5476)'],
    products = ['CO2(14)', 'C2HF(57)'],
    transitionState = 'TS1',
    kinetics = Arrhenius(A=(5e+12,'s^-1'), n=0, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(1500,'K'), comment="""Exact match found for rate rule [RJJ]
Euclidian distance = 0
family: 1,4_Linear_birad_scission"""),
)

reaction(
    label = 'reaction2',
    reactants = ['[CH]=C=C([O])OF(5563)'],
    products = ['[CH]=C(F)C([O])=O(5476)'],
    transitionState = 'TS2',
    kinetics = Arrhenius(A=(8.88952e+10,'s^-1'), n=0.725184, Ea=(202.389,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.005830439029566195, var=4.831276094152293, Tref=1000.0, N=2, data_mean=0.0, correlation='F',), comment="""Estimated from node F"""),
)

reaction(
    label = 'reaction3',
    reactants = ['O(7)', '[CH]=C(F)[C]=O(5532)'],
    products = ['[CH]=C(F)C([O])=O(5476)'],
    transitionState = 'TS3',
    kinetics = Arrhenius(A=(1667.73,'m^3/(mol*s)'), n=1.126, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(303.03,'K'), Tmax=(2000,'K'), comment="""Estimated using template [Y_rad;O_birad] for rate rule [CO_rad/OneDe;O_birad]
Euclidian distance = 3.0
family: Birad_R_Recombination
Ea raised from -8.3 to 0 kJ/mol."""),
)

reaction(
    label = 'reaction4',
    reactants = ['[CH]=C(F)C([O])=O(5476)'],
    products = ['O=C1OC=C1F(5552)'],
    transitionState = 'TS4',
    kinetics = Arrhenius(A=(3.24e+12,'s^-1'), n=-0.305, Ea=(8.28432,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R4;Y_rad_out;Ypri_rad_out] for rate rule [R4;CdsingleH_rad_out;Opri_rad]
Euclidian distance = 2.23606797749979
Multiplied by reaction path degeneracy 2.0
family: Birad_recombination"""),
)

reaction(
    label = 'reaction5',
    reactants = ['[CH]=C(F)C([O])=O(5476)'],
    products = ['[CH]C(F)=C1OO1(5564)'],
    transitionState = 'TS5',
    kinetics = Arrhenius(A=(1.55936e+11,'s^-1'), n=0.551275, Ea=(238.085,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R3_linear;multiplebond_intra;radadd_intra] for rate rule [R3_CO;carbonyl_intra_De;radadd_intra_O]
Euclidian distance = 2.449489742783178
family: Intra_R_Add_Endocyclic
Ea raised from 238.1 to 238.1 kJ/mol to match endothermicity of reaction."""),
)

reaction(
    label = 'reaction6',
    reactants = ['[CH]=C(F)C([O])=O(5476)'],
    products = ['O=C1O[CH][C]1F(5565)'],
    transitionState = 'TS6',
    kinetics = Arrhenius(A=(3.906e+11,'s^-1'), n=0.387, Ea=(138.055,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R4_D;multiplebond_intra;radadd_intra_cdsingleH] for rate rule [R4_D_CO;carbonyl_intra;radadd_intra_cdsingleH]
Euclidian distance = 1.4142135623730951
Multiplied by reaction path degeneracy 2.0
family: Intra_R_Add_Endocyclic"""),
)

reaction(
    label = 'reaction7',
    reactants = ['[CH]=C(F)C([O])=O(5476)'],
    products = ['[O]C1([O])C=C1F(5559)'],
    transitionState = 'TS7',
    kinetics = Arrhenius(A=(9.36651e+10,'s^-1'), n=0.5685, Ea=(142.158,'kJ/mol'), T0=(1,'K'), comment="""Estimated using template [R4_D;multiplebond_intra;radadd_intra_cdsingleH] for rate rule [R4_D_CO;carbonylbond_intra;radadd_intra_cdsingleH]
Euclidian distance = 1.4142135623730951
family: Intra_R_Add_Exocyclic
Ea raised from 141.3 to 142.2 kJ/mol to match endothermicity of reaction."""),
)

reaction(
    label = 'reaction8',
    reactants = ['F(37)', 'C#CC([O])=O(3710)'],
    products = ['[CH]=C(F)C([O])=O(5476)'],
    transitionState = 'TS8',
    kinetics = Arrhenius(A=(1.575e+07,'m^3/(mol*s)'), n=3.11585e-09, Ea=(82.8031,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R-inRing_N-3R->C_N-1R!H->N_N-2R!H->O_N-3BrClFNOS->Cl_N-2CNS->N_N-3BrFNOS->N_3BrFOS->F',), comment="""Estimated from node Root_N-3R-inRing_N-3R->C_N-1R!H->N_N-2R!H->O_N-3BrClFNOS->Cl_N-2CNS->N_N-3BrFNOS->N_3BrFOS->F"""),
)

reaction(
    label = 'reaction9',
    reactants = ['[O][C]=O(3667)', 'C2HF(57)'],
    products = ['[CH]=C(F)C([O])=O(5476)'],
    transitionState = 'TS9',
    kinetics = Arrhenius(A=(4.19389,'m^3/(mol*s)'), n=1.76036, Ea=(32.49,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.10151511122778119, var=2.139043046412222, Tref=1000.0, N=264, data_mean=0.0, correlation='Root_N-3R-inRing_Ext-3R-R_Sp-4R!H=3R',), comment="""Estimated from node Root_N-3R-inRing_Ext-3R-R_Sp-4R!H=3R"""),
)

reaction(
    label = 'reaction10',
    reactants = ['CO2(14)', '[CH]=[C]F(488)'],
    products = ['[CH]=C(F)C([O])=O(5476)'],
    transitionState = 'TS10',
    kinetics = Arrhenius(A=(520000,'m^3/(mol*s)'), n=-1.07934e-11, Ea=(144.823,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R-inRing_Ext-3R-R_Sp-4R!H=3R_Sp-2R!H=1R!H_N-2R!H->C',), comment="""Estimated from node Root_N-3R-inRing_Ext-3R-R_Sp-4R!H=3R_Sp-2R!H=1R!H_N-2R!H->C"""),
)

reaction(
    label = 'reaction11',
    reactants = ['[O][C]=O(3667)', '[CH]=[C]F(488)'],
    products = ['[CH]=C(F)C([O])=O(5476)'],
    transitionState = 'TS11',
    kinetics = Arrhenius(A=(7.38316e+06,'m^3/(mol*s)'), n=1.31229e-07, Ea=(0,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=-0.016021952005170214, var=0.3543710496450803, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C',), comment="""Estimated from node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->O_Ext-1O-R_N-3R!H->O_Ext-2R-R_2R->C"""),
)

reaction(
    label = 'reaction12',
    reactants = ['[CH]=C(F)C([O])=O(5476)'],
    products = ['[O]C([O])=C=CF(5562)'],
    transitionState = 'TS12',
    kinetics = Arrhenius(A=(1.00763e+12,'s^-1'), n=0.18834, Ea=(133.393,'kJ/mol'), T0=(1,'K'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='R2F_Ext-1R!H-R_4R!H->C',), comment="""Estimated from node R2F_Ext-1R!H-R_4R!H->C"""),
)

network(
    label = 'PDepNetwork #1541',
    isomers = [
        '[CH]=C(F)C([O])=O(5476)',
    ],
    reactants = [
        ('CO2(14)', 'C2HF(57)'),
    ],
    bathGas = {
        'N2': 0.5,
        'Ne': 0.5,
    },
)

pressureDependence(
    label = 'PDepNetwork #1541',
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

