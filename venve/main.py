from find_posible_paths import Possible_paths
from Find_Senic_and_distance_cumilative_list import  Find_senic_distance_list

if __name__=='__main__':
    routes = [
        ("Katuwana", "Matara"),
        ("Matara", "Galle"),
        ("Matara", "Colombo"),
        ("Galle", "Colombo"),
        ("Colombo", "Kandy"),
        ("Kandy", "Nuwara Eliya"),

        ("Katuwana", "Embilipitiya"),
        ("Embilipitiya", "Palmadulla"),
        ("Embilipitiya", "Balangoda"),
        ("Palmadulla", "Balangoda"),
        ("Balangoda", "Haputhale"),
        ("Haputhale", "Walimada"),
        ("Haputhale", "Nuwara Eliya"),
        ("Walimada", "Nuwara Eliya"),

    ]
    distance_dic = {
        1: ["KatuwanaEmbilipitiya", 24],
        2: ["EmbilipitiyaPalmadulla", 67],
        3: ["EmbilipitiyaBalangoda", 89],
        4: ["PalmadullaBalangoda", 79],
        5: ["BalangodaHaputhale", 67],
        6: ["HaputhaleWalimada", 12],
        7: ["HaputhaleNuwara Eliya", 45],
        8: ["WalimadaNuwara Eliya", 89],
        9: ["KatuwanaMatara", 67],
        10: ["MataraGalle", 89],
        11: ["MataraColombo", 45],
        12: ["GalleColombo", 23],
        13: ["ColomboKandy", 45],
        14: ["KandyNuwara Eliya", 67],
    }
    scenic_dic = {
        1: ["KatuwanaEmbilipitiya", 2],
        2: ["EmbilipitiyaPalmadulla", 5],
        3: ["EmbilipitiyaBalangoda", 7],
        4: ["PalmadullaBalangoda", 8],
        5: ["BalangodaHaputhale", 12],
        6: ["HaputhaleWalimada", 34],
        7: ["HaputhaleNuwara Eliya", 56],
        8: ["WalimadaNuwara Eliya", 12],
        9: ["KatuwanaMatara", 7],
        10: ["MataraGalle", 89],
        11: ["MataraColombo", 7],
        12: ["GalleColombo", 4],
        13: ["ColomboKandy", 3],
        14: ["KandyNuwara Eliya", 8],
    }


start_city="Katuwana"
end_city="Nuwara Eliya"


route_graph=Possible_paths(routes)
x=route_graph.get_path_between_two_cities(start_city,end_city)
print('\n')
print(f'All posible routes are :\n')
for i in x:
    print(i)

F_S_L=Find_senic_distance_list(distance_dic,scenic_dic)

y=F_S_L.make_distance_list_scenic_list(x)
m=F_S_L.find_better_path(y[0],y[1],x)

print(f'\nBest route for traveller   :{m}\n')

