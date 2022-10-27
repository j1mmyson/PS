#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    int boat = 0;
    int size = people.size();
    int start = 0;
    int end = 0;
    
    sort(people.begin(), people.end());
    
    while(start + end < size){
        boat = limit;
        boat -= people[size-end-1];
        end++;
        if(people[start] <= boat) {
            start++;
        }
        answer++;
    }
    
    return answer;
}
