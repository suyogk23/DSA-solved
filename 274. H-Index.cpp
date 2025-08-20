class Solution {
public:
//h>=h no of papers with no of citation >=h
    int hIndex(vector<int>& citations) {
        //sort in non-increasing order
        sort(citations.begin(),citations.end(),greater<int>());
        int len=citations.size();
        int maxh=0;
        for(int i=0; i<len; i++){
            //min no of papers that satisfy: no of papers with citations>=h
            if(citations[i]>=i+1){
                maxh=i+1;
            }
            else{
                break;
            }
        }
        return maxh;
    }
};
