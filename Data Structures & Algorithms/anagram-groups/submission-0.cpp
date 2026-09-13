class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (string s : strs){ // each string in array 
            string key = s; // string acts as key 
            sort(key.begin(),key.end()); // prevents looping 
            mp[key].push_back(s); // push if new 
        }

        vector<vector<string>> result;
        for(auto& pair : mp){
            result.push_back(pair.second);
        }

        return result;
    }
};
