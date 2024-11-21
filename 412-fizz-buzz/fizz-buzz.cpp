

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> res(n);
        for(int i=1;i<=n;i++){
            res[i-1]=to_string(i);
            if (!(i%3) && !(i%5)) res[i-1]="FizzBuzz";
            else if(!(i%5))  res[i-1]="Buzz";
            else if(!(i%3)) res[i-1]="Fizz";
        }
        return res;
    }
};