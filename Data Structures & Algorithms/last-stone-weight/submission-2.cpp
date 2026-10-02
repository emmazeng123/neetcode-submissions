class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq;
        for (int s : stones){
            pq.push(s);
        }
        while (pq.size() > 1){
            int x = pq.top();
            pq.pop();
            int y = pq.top();
            pq.pop();

            if (y < x){
                int z = abs(x-y);
                    pq.push(z);
            }

            if (pq.size() == 0){
                return 0;
            }
        } return pq.top();
    }
};
