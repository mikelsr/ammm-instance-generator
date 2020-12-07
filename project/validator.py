from ammm_globals import AMMMException


def validate(data):

    dd = data.__dict__

    # Validate that mandatory input parameters were found
    for paramName in ['inputDataFile', 'solutionFile', 'solver']:
        if paramName not in dd:
            raise AMMMException('Parameter/Set(%s) not contained in Configuration' % str(paramName))

    # Validate input data file
    inputDataFile = data.inputDataFile
    if len(inputDataFile) == 0:
        raise AMMMException('Value for inputDataFile is empty')
    if not os.path.exists(inputDataFile):
        raise AMMMException('inputDataFile(%s) does not exist' % inputDataFile)

    # Validate verbose
    verbose = False
    if 'verbose' in data.dd:
        verbose = data.verbose
        if not isinstance(verbose, bool) or (verbose not in [True, False]):
            raise AMMMException('verbose({}) has to be a boolean value'.format(verbose))
    else:
        data.verbose = verbose

    ints = [
        "nTypes"
        "nCities",
        "nLocations",
        "maxCoordX",
        "maxCoordY",
        "maxDCity",
        "minDCity",
        "d_center",
        "maxCityPop",
        "minCityPop",
        "maxCap",
        "minCap",
        "maxCost",
        "minCost"
    ]

    for parameter in ints:
        if not isinstance(getattr(data, parameter), int):
            raise AMMMException('{} has to be an integer value'.format(parameter))

    if data.maxCap < data.maxCityPop:
        raise AMMMException("Maximum capacity must be greater than maximum population")
