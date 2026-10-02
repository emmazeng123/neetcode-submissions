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
            } else{
                if (sta.empty() || dic[c] != sta.top()){
                    return false;
                }
                sta.pop();
            }  
        }
        return sta.empty();
    }
};
