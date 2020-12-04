from os import path

from ammm_globals import AMMMException


class InstanceGenerator:

    def __init__(self, config):
        self.config = config

    def generate(self):
        instancesDirectory = self.config.instancesDirectory
        fileNamePrefix = self.config.fileNamePrefix
        fileNameExtension = self.config.fileNameExtension
        numInstances = self.config.numInstances

        # nTypes
        nTypes = self.config.nTypes

        # posCc,cords...
        numCities = self.config.numCities
        # d_city
        maxDCity = self.config.maxDCity
        minDCity = self.config.minDCity
        # pc
        maxCityPop = self.config.maxCityPop
        minCityPop = self.config.minCityPop

        # posLoct,cords
        numLocations = self.config.numLocations
        # d_center
        d_center = self.config.d_center

        # capt
        maxCap = self.config.maxCap
        minCap = self.config.minCap

        # costt
        maxCost = self.config.maxCost
        minCost = self.config.minCost

        if not path.isdir(instancesDirectory):
            raise AMMMException('Directory(%s) does not exist' % instancesDirectory)

        for i in range(numInstances):
            instancePath = path.join(instancesDirectory, '{}_{}.{}'.format(fileNamePrefix, i, fileNameExtension))
            with open(instancePath, 'w') as fInstance:
                population = [0] * numCities

                pos_cities = [[0, 0]] * numCities

                pos_locations = [[0, 0]] * numLocations

                cap_t = [0] * nTypes

                cost_t = [0] * nTypes
