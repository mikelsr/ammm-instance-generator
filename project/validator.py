from ammm_globals import AMMMException


def validate(data):

    # Validate verbose
    verbose = False
    if "verbose" in data.__dict__:
        verbose = data.verbose
        if not isinstance(verbose, bool) or (verbose not in [True, False]):
            raise AMMMException("verbose({}) has to be a boolean value".format(verbose))
    else:
        data.verbose = verbose

    ints = [
        "numInstances",
        "nTypes",
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
        "minCost",
    ]

    for parameter in ints:
        if not isinstance(getattr(data, parameter), int):
            raise AMMMException("{} has to be an integer value".format(parameter))

    if data.maxCap < data.maxCityPop:
        raise AMMMException("Maximum capacity must be greater than maximum population")
