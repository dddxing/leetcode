#include <iostream>
#include <unordered_map>
#include <vector>

using std::vector;
using std::unordered_map;
using std::cout;
using std::endl;

class Solution {
public:
    
    vector<int> topKFrequent(vector<int>& nums, int k) {

    	int n = nums.size();
        
        unordered_map<int, int> count;
        std::vector<std::vector <int>> freq(n+1);
        std::vector <int> res;

        for (auto i : nums) {
            count[i] ++;
        }
        
        
        for (auto item : count){
			freq[item.second].push_back(item.first);            
        }

        for (int i=n; i>=0; i--){

        	for (auto j : freq[i]){
        		res.push_back(j);

        		if (res.size() == k) 
        			return res;
        	}
        }
        
    }
};


int main()
{
	vector<int> nums {1,1,1,2,2,3};
	int k = 2;

	Solution s;

	std::cout << s.topKFrequent(nums, k) << std::endl;
	return 0;
}