class Solution {
public:
    bool isValid(string s) {
        std::map<char,char> dic= {{')','('},{'}','{'},{ ']','['},
        {'(', ')'}, {'[', ']'}, {'{', '}'}};
        std::stack<char> sta;

        for (char c : s){
            if (c == dic[')'] || 
                c == dic['}'] || 
                c == dic[']']) {
                    sta.push(c);
            }
            if (!sta.empty() && dic[c] == sta.top()){
                sta.pop();
            }
        
        }
        return sta.empty();
    }
};
