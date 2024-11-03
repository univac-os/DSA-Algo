class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        #stack or recursion 
        #stack can be better to use
        stack=[]
        for char in expression: #ignore the ,
            if char ==')':
                #we need children and based on operator we will get value
                children=[]
                while stack and stack[-1]!='(':
                    #get all value in (....)
                    children.append(stack.pop())
                stack.pop()#remove (
                operator=stack.pop()
                if operator=='&':
                    stack.append(all(children))
                elif operator=='|':
                    stack.append(any(children))
                elif operator=='!':
                    stack.append(not children[0])
                

            elif char!=',':
                if char=='t':
                    stack.append(True)
                elif char=='f':
                    stack.append(False)
                else:
                    stack.append(char) #any operator
        
        return stack[-1]

        # when we get & | we will call recursive and get the value
        s=expression
        self.i=0
        def rec():
            c=s[self.i]
            self.i+=1
            if c=='t':
                return True
            if c=='f':
                return False
            if c=='!':
                #call recursive
                self.i+=1 # (
                res= not rec()
                self.i+=1 # )
                return res
            #so & or |
            children=[]
            self.i+=1 #(
            while s[self.i]!=')':
                if s[self.i]!=',':
                    children.append(rec())
                else:
                    #move to next 
                    self.i+=1
            self.i+=1 # )
            if c=='&':
                return all(children)
            if c=='|':
                return any(children)
          
        return rec()