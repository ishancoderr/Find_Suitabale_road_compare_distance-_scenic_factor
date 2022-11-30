
class Find_senic_distance_list:
    def __init__(self, distance_dic,scenic_dic):
        self.distance_dic = distance_dic
        self.scenic_dic =scenic_dic
     
    def make_distance_list_scenic_list(self,x):    
        a = []
        for m in x:
            res = [i + j for i, j in zip(m, m[1:])]
            a.append(res)
        #print(a)
    
        distance_list = []
        scenic_list = []
    
        for b in a:
            full_distance = 0
            secenic_cumilative = 0
            for i in range(len(b)):
                for k, j in self.distance_dic.values():
                    if b[i] == k:
                        full_distance = full_distance + j
    
                for k, j in self.scenic_dic.values():
                    if b[i] == k:
                        secenic_cumilative = secenic_cumilative + j
    
            scenic_list.append(secenic_cumilative)
            distance_list.append(full_distance)

        print(f'\nDistance list :{distance_list} \nScenic list :{scenic_list}\n')
        return distance_list,scenic_list

    def find_better_path(self,distance_list,scenic_list,x):
        
        sorted_distance_list = sorted(distance_list)
        sorted_scenic_list = sorted(scenic_list, reverse=True)

        print(f'\nShorted distance list :{sorted_distance_list}')
        #print(distance_list)
        print(f'sorted_scenic_list    :{sorted_scenic_list}\n')
        #print(scenic_list)

        index_array_sorted_distance = []
        index_array_sorted_scenic = []

        for s1 in range(len(sorted_distance_list)):
            for s2 in range(len(distance_list)):
                if sorted_distance_list[s1] == distance_list[s2]:
                    index_array_sorted_distance.append(s2)

                if sorted_scenic_list[s1] == scenic_list[s2]:
                    index_array_sorted_scenic.append(s2)

        print(f'index list of shorted distance :{index_array_sorted_distance}')
        print(f'index list of shorted scenic :{index_array_sorted_scenic}\n')
        # print(x)

        f = []
        f1 = []
        for s in index_array_sorted_distance:
            f.append(x[s])

        for s in index_array_sorted_scenic:
            f1.append(x[s])

        #print(f)
        #print(f1)
        print(f'Absolute routes for distance :{f}')
        print(f'Absolute routes for  scenic  :{f1}\n')

        print(f'The shortest path   :{f[0]}')
        print(f'Most scenic path    :{f1[0]}\n')

        ls1 = []
        index = 0
        print(f'point system with all posibilities:')
        for v1 in range(len(index_array_sorted_distance)):
            for v2 in range(len(index_array_sorted_scenic)):
                if index_array_sorted_distance[v1] == index_array_sorted_scenic[v2]:
                    print(f"{v1 + 1}---{v2 + 1}")
                    n = 2 * (v1 + 1) + 1 * (v2 + 1)
                    print(n)

                    if v1 == 0:
                        minimum = n
                        index = v1
                        print(minimum)
                        print(index)
                    elif minimum > n:
                        minimum = n
                        index = v1
                        print(minimum)
                        print(index)

        return f[index]
        
  
    
    
    