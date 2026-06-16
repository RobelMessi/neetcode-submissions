class Solution:
    def isAnagram(self, s: str, t: str):
        s_list = list(s)
        t_list = list(t)
        sorted_list1 = sorted(s_list)
        sorted_list2 = sorted(t_list)
        string1 = ""
        string2 = ""
        for char in sorted_list1:
            string1+=char
        for char in sorted_list2:
            string2+= char
        if string1==string2:
            return True
        else:
            return False
        
       
        
            
        
       

        