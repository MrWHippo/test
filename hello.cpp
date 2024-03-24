#include <iostream>
using namespace std;


int main(){
        long long total = 0;
        for (int i=0; i<=800000000; i+=1){
            total += i;
        }
        cout << total << '\n';
    return 0;
}