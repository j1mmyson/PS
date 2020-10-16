#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int answer = 0;
    int h = triangle.size();
    int i=0,j=0;
    
    for(i=h-2;i>=0;i--){
        for(j=0;j<=i;j++){
            triangle[i][j]=max(triangle[i+1][j],triangle[i+1][j+1])+triangle[i][j];
        }
    }
    
    answer = triangle[0][0];
    return answer;
}
