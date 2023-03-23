# Problem C from https://egr.vcu.edu/media/engineering/documents/cs/VCU_HSContest_2016_Problems.pdf
import sys

from typing import TextIO

class Route:
    def __init__(self, route_list = [], route_set = set()):
        self.route_list: list = route_list
        self.route_set: set = route_set
    def add(self, town):
        if town in self.route_set: return False
        self.route_list.append(town)
        self.route_set.add(town)
        return True
    def get_travel_time(self, path_dict: dict):
        travel_time = 0
        i = 0
        while i < len(self.route_list) - 1:
            current_town = self.route_list[i]
            next_town = self.route_list[i + 1]
            current_town_dict = path_dict.get(current_town)
            travel_time += current_town_dict.get(next_town)
            i += 1
        return travel_time
    def get_last_town(self):
        return(self.route_list[len(self.route_list) - 1])
    def __str__(self):
        route_string = ""
        for town in self.route_list:
            route_string += f"{town} -> "
        return route_string[:-4]
    def copy(self):
        return Route(route_list = self.route_list.copy(), route_set = self.route_set.copy())

def pathfind(route_list: list[Route], path_dict: dict[int, dict[int, int]], target_town: int) -> list[Route]:
    return_list = []
    while len(route_list) > 0:
        new_route_list = []
        for route in route_list:
            last_town_dict = path_dict.get(route.get_last_town())
            if target_town in last_town_dict.keys():
                route.add(target_town)
                return_list.append(route)
            else: 
                for town in last_town_dict.keys():
                    new_route = route.copy()
                    if new_route.add(town): # The add method returns true if it works, therefore I can do this
                        new_route_list.append(new_route)
        route_list = new_route_list
    return return_list
                
# typing for tab completion
def main(input: TextIO, output: TextIO):
    arguments = list(map(int, input.readline().split(" ")))
    total_towns = arguments[0]
    starting_town = arguments[1]
    target_town = arguments[2]
    
    paths : dict[int, dict] = {}
    for line in input:
        road = list(map(int, line.split(" ")))
        speed_limit = road[0]
        i = 1
        while i < len(road) - 2:
            town1 = road[i]
            distance = road[i + 1]
            town2 = road[i + 2]
            time_distance = distance / speed_limit

            town1paths: dict[int, int] = paths.get(town1, dict())
            old_time = town1paths.get(town2)
            if old_time is None or old_time < time_distance:
                town1paths[town2] = time_distance
            paths[town1] = town1paths

            town2paths: dict[int, int] = paths.get(town2, dict())
            old_time = town2paths.get(town1)
            if old_time is None or old_time < time_distance:
                town2paths[town1] = time_distance
            paths[town2] = town2paths

            i += 2

    route = Route()
    route.add(starting_town)
    route_list: list[Route] = [route]
    valid_routes = pathfind(route_list, paths, target_town)
    shortest_time = valid_routes[0].get_travel_time(paths)
    for route in valid_routes[1:]:
        route_time = route.get_travel_time(paths)
        if route_time < shortest_time:
            shortest_time = route_time
    output.write(str(shortest_time))


if __name__ == "__main__":
    main(sys.stdin, sys.stdout)