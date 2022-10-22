#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <stdlib.h>

// int maxAreaOfIsland(vector<vector<int>>&grid){
//         int Max=0;
//          int row = grid.size();
//     int col = grid[0].size();
//     for(int i=0;i<row;i++){
//         for(int j=0;j<col;j++){
//                int  cnt=1;
//             if( grid[i][j]==1){
//                 dfs(grid, i, j, cnt);
//                Max = max(Max, cnt);  }  
//         }
//     }
//        return Max;
// }

// int dfs(vector<vector<int>>& grid, int i, int j, int& cnt){
//     if( i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() || grid[i][j] == 0){
//     return 0;
//     }
//     grid[i][j]=0;
//     if(dfs(grid, i+1,j, cnt))cnt++;
//         if(dfs(grid, i-1,j, cnt))cnt++;
//         if(dfs(grid, i,j-1, cnt))cnt++;
//         if(dfs(grid, i,j+1, cnt))cnt++;
//     return 1;
// }
double randZeroToOne(){
    return rand() / (RAND_MAX + 1.);
};

std::vector<std::vector<int> create_grid(int size){
    std::cout << size << "\n " << p;
    std::vector<std::vector<int>> result(size, std::vector<int>(size, 0));
    // std::generate(result.begin(), result.end(), [](float p) {
    // return randZeroToOne() <= p;
    // });
    return result;
};


int main() {

    double p = 0.5;
    // std::cout << p ;
    // std::vector<std::vector<int> g = create_grid(10, p);
    // std::cout << grid.size();
    // for (int i = 0; i < grid.size(); i++)
    // {
    // for (int j = 0; j < grid[i].size(); j++)
    // {
    //     std::cout << grid[i][j];
    // }
    // }
    return 0;
}
