
class Possible_paths:
    def __init__(self, edges):
        self.edges = edges
        self.path_dict = {}
        

        for start_city, end_city in self.edges:
            #print(start_city,end_city)
            if start_city in self.path_dict:
                self.path_dict[start_city].append(end_city)
            else:
                self.path_dict[start_city] = [end_city]
        # print(self.path_dict)

    def get_path_between_two_cities(self, start_city, end_city, path=[]):
        path = path + [start_city]

        if start_city == end_city:
            return [path]
        if start_city not in self.path_dict:
            return []

        paths = []
        for node in self.path_dict[start_city]:
            if node not in path:
                new_paths = self.get_path_between_two_cities(node, end_city, path)
                for p in new_paths:
                    paths.append(p)

        return paths