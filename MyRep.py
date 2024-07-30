class MyRep:
    def minn(self,list:list[int]) -> int:
        diff = list[0]
        for i in range(len(list)):
            if list[i] < diff:
                diff = list[i]
        return diff
    def sravnenie(self,list:list[int]) -> int:
        the_final_list = []
        for i in range(len(list)):
            the_final_list.append(self.minn(list))
            list.remove(self.minn(list))
        return the_final_list
