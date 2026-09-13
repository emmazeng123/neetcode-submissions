class Solution {
public:
    bool isAnagram(string s, string t) {
    unordered_map<char,int> mySet;

    if (s.size() != t.size()){
        return false;
    }

    for (int i = 0; i < s.size(); i++){
        mySet[s[i]]++;
    }

    for (int j = 0; j < t.size(); j++){
        if (mySet.count(t[j])){
            mySet[t[j]]--;
        }
    }

    for (int i = 0; i < s.size(); i++){
        if (mySet[s[i]] != 0){
            return false;
        }
    }
    return true;
    }
};
