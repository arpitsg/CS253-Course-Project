#include<bits/stdc++.h> 
using namespace std; 


int main() {
freopen("out.txt", "r", stdin);
freopen("test_k.txt", "w", stdout);

int n,k;
cin>>n>>k;

string s[n];

for (int i = 0; i < n; i++)
{
    cin>>s[i];
}
int tot_branch=s[0].size();
vector<int>test_k;
int branch_covered[tot_branch];
memset(branch_covered, 0, tot_branch*sizeof(int));
int used[n];
memset(used, 0, n*sizeof(int));

for (int i = 0; i < k; i++)
{   int ma=0;
    int x;
    for (int j = 0; j < n; j++)
    {
        if(used[j])continue;
        int count=0;
         for(int b=0;b<tot_branch;b++)
         {
            if(s[j][b]=='1'&&branch_covered[b]==0)count++;
         }
         if(count>=ma){
             ma=count;
             x=j;
         }
    }
    for(int b=0;b<tot_branch;b++)
        {
            if(s[x][b]=='1')branch_covered[b]=1;
        }
    used[x]=1;
    test_k.push_back(x);
}

for (auto i: test_k)
cout<<i+2<<endl;
return 0;
}