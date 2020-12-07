from math import sqrt
from os import makedirs, path
from random import uniform

from ammm_globals import AMMMException


def _uniform_int(floor, ceil):
    return int(uniform(floor, ceil))


def _gen_coordinates(n, min_dist, max_x, max_y):
    """
    Generate coordinates while respecting minimum distances between them.
    :param n: number of coordinates to generate
    :param min_dist: minimum distance between coordinates
    :param max_x: max x coordinate
    :param max_y: max y coordinate
    :return:
    """
    coords = []
    for _ in range(n):
        coord = [_uniform_int(0, max_x), _uniform_int(0, max_y)]
        while not _coord_is_valid(coord, coords, min_dist):
            coord = [_uniform_int(0, max_x), _uniform_int(0, max_y)]
        coords.append(coord)
    return coords


def _coord_is_valid(coord, prev_cords, min_dist):
    """
    Validate that a coordinate is not too close to other existing coordinates.
    :param coord: new coordinate
    :param prev_cords: existing coordinate
    :param min_dist: minimum distance between new and existing coordinates
    :return: False if the new coord is too close to any existing coord, True otherwise
    """
    for other_coord in prev_cords:
        if sqrt(abs(coord[0] - other_coord[0]) ** 2 \
                + abs(coord[1] - other_coord[1]) ** 2) < min_dist:
            return False
    return True


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

        # coords
        maxCoordX = self.config.maxCoordX
        maxCoordY = self.config.maxCoordY

        # posCc,cords...
        nCities = self.config.nCities

        # d_city
        maxDCity = self.config.maxDCity
        minDCity = self.config.minDCity

        # pc
        maxCityPop = self.config.maxCityPop
        minCityPop = self.config.minCityPop

        # posLoct,cords
        nLocations = self.config.nLocations
        # d_center
        d_center = self.config.d_center

        # capt
        maxCap = self.config.maxCap
        minCap = self.config.minCap

        # costt
        maxCost = self.config.maxCost
        minCost = self.config.minCost

        if not path.isdir(instancesDirectory):
            makedirs(instancesDirectory)
            # raise AMMMException('Directory(%s) does not exist' % instancesDirectory)

        for i in range(numInstances):
            population = [_uniform_int(minCityPop, maxCityPop) for _ in range(nCities)]
            # sort coordinate arrays for readability
            pos_cities = sorted(_gen_coordinates(nCities, 1, maxCoordX, maxCoordY))
            pos_locations = sorted(_gen_coordinates(nLocations, d_center, maxCoordX, maxCoordY))
            d_cities = [_uniform_int(minDCity, maxDCity) for _ in range(nTypes)]
            cap_t = [_uniform_int(minCap, maxCap) for _ in range(nTypes)]
            cost_t = [_uniform_int(minCost, maxCost) for _ in range(nTypes)]

            instancePath = path.join(instancesDirectory,
                                     '{}_{}.{}'.format(fileNamePrefix, i, fileNameExtension))
            lines = [
                'nLocations\t= {};'.format(nLocations),
                'nCities\t\t= {};'.format(nCities),
                'nTypes\t\t= {};'.format(nTypes),
                '',
                'p\t\t= [ {} ];'.format(' '.join(map(str, population))),
                'posCities\t= [ {} ];'.format(' '.join('[{} {}]'.format(x, y) for x, y in pos_cities)),
                'posLocations\t= [ {} ];'.format(' '.join('[{} {}]'.format(x, y) for x, y in pos_locations)),
                '',
                'd_city\t= [{}];'.format(' '.join(map(str, d_cities))),
                'cap\t= [{}];'.format(' '.join(map(str, cap_t))),
                'cost\t= [{}];'.format(' '.join(map(str, cost_t))),
                '',
                'd_center = {};'.format(d_center)
            ]
            with open(instancePath, 'w') as fInstance:
                fInstance.writelines(['{}\n'.format(line) for line in lines])
