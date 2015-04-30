"""
Iso-butanol pyrolysis. Reactor conditions taken from Merchant et al. Combust. Flame 160, 1907-1929 (2013).
"""

# Data sources
database(
    thermoLibraries = ['primaryThermoLibrary', 'GRI-Mech3.0'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = ['training'], 
    kineticsFamilies = 'default',
    kineticsEstimator = 'rate rules',
)

# Constraints on generated species
generatedSpeciesConstraints(
    allowed = ['seed mechanisms','reaction libraries', 'input species'],
    maximumRadicalElectrons = 2,
)

# List of species
species(
    label='iBut',
    reactive=True,
    structure=SMILES("CC(C)CO"),
)
species(
    label='iButyl-A',
    reactive=True,
    structure=SMILES("[CH2]C(C)CO"),
)
species(
    label='prop-2-yl',
    reactive=True,
    structure=SMILES("C[CH]C"),
)
species(
    label='N2',
    reactive=False,
    structure=InChI("InChI=1/N2/c1-2"),
)

# Reaction systems
simpleReactor(
    temperature=(900,'K'),
    pressure=(1.5,'atm'),
    initialMoleFractions={
        "iBut": 1,
        "iButyl-A": 0,
        "prop-2-yl": 0,
    },
    terminationConversion={
        'iBut': 0.99,
    },
)

simpleReactor(
    temperature=(1200,'K'),
    pressure=(1.5,'atm'),
    initialMoleFractions={
        "iBut": 1,
        "iButyl-A": 0,
        "prop-2-yl": 0,
    },
    terminationConversion={
        'iBut': 0.99,
    },
)

simpleReactor(
    temperature=(900,'K'),
    pressure=(1.5,'atm'),
    initialMoleFractions={
        "iBut": 0.1571, # This should be a mass fraction of 1/3 isobutane, 2/3 nitrogen
        "N2": 0.8429,
        "iButyl-A": 0,
        "prop-2-yl": 0,
    },
    terminationConversion={
        'iBut': 0.99,
    },
)

simpleReactor(
    temperature=(1200,'K'),
    pressure=(1.5,'atm'),
    initialMoleFractions={
        "iBut": 0.1571, # This should be a mass fraction of 1/3 isobutane, 2/3 nitrogen
        "N2": 0.8429,
        "iButyl-A": 0,
        "prop-2-yl": 0,
    },
    terminationConversion={
        'iBut': 0.99,
    },
)

simulator(
    atol=1e-16,
    rtol=1e-8,
)

model(
    toleranceKeepInEdge=0.0,
    toleranceMoveToCore=0.5,
    toleranceInterruptSimulation=0.5,
    maximumEdgeSpecies=100000
)

#quantumMechanics(
#    software='mopac',
#    method='pm3',
#    # fileStore='QMfiles', # relative to where you run it from. Defaults to inside the output folder if not defined.
#    scratchDirectory = None, # not currently used
#    onlyCyclics = True,
#    maxRadicalNumber = 0,
#    )
#
#pressureDependence(
#    method='modified strong collision',
#    maximumGrainSize=(0.5,'kcal/mol'),
#    minimumNumberOfGrains=250,
#    temperatures=(300,2000,'K',8),
#    pressures=(0.01,100,'bar',5),
#    interpolation=('Chebyshev', 6, 4),
#)

options(
    units='si',
    saveRestartPeriod=(1,'day'),
    drawMolecules=False,
    generatePlots=False,
)

