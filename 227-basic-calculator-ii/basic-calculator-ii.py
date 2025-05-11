class Solution:
       def calculate(self, s: str) -> int:
        """
        stack solution 
        keep number with sign and if we get * or / then take out prev and do opeartion
        here instead of add val into stack we can add to variable
        """
        total,prev_num=0,0
        # stack=[]
        num=0
        prev_op="+"
        s+="+"#add this dummy to finally we want add result
        for ch in s:
            if ch.isdigit():
                num=num*10+int(ch)
            elif ch in "+-*/":
                if prev_op=="+":
                    # stack.append(num)
                    total+=num
                    prev_num=num
                elif prev_op=="-":
                    # stack.append(-num)
                    total-=num
                    prev_num=-num
                elif prev_op=="*":
                    # prev=stack.pop()
                    # stack.append(prev*num)
                    total-=prev_num
                    prev_num=prev_num*num
                    total+=prev_num
                elif prev_op=="/":
                    # prev=stack.pop()
                    # stack.append(int(prev/num))
                    total-=prev_num
                    prev_num=int(prev_num/num)
                    total+=prev_num
                prev_op=ch
                num=0
        # return stack
        return total


    
