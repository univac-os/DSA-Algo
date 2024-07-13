class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        #stack to check opposite moving robot hitting
        #if 1st robots are moving left not to be included as speed is constant so stack should have only Right 
        #moving robot 
        #sort based on position and all other healths and directions array are align with that
        index_map ={p:idx for idx,p in enumerate(positions)}
        stack=[]
        for p in sorted(positions):
            i=index_map[p]
            if directions[i]=="R":
                stack.append(i)
            else:#we have robot moving L
                while stack and healths[i]:
                    #3 condition  
                    #1. if --> <- r>l remove l
                    #2. if -> <-- r<l remove r so add l into stack
                    #3. if -> <- r==l remobe both
                    #how to check this use healths array 
                    i2=stack.pop()
                    if healths[i]>healths[i2]:
                        healths[i2]=0
                        healths[i]-=1
                    elif healths[i]<healths[i2]:
                        healths[i]=0
                        healths[i2]-=1
                        stack.append(i2)
                    else:
                        healths[i]=healths[i2]=0
                    #say -> -> -> <------ L is very big and elminate everyone in stack so finally we dont need to it
                    #as we only consider -> R moving robot in stack
        return [h for h in healths if h >0]


 