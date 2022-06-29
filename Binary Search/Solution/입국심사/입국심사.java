package com.example.demo;
import java.util.*;

class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        Arrays.sort(times);
        long left= 0;
        long right = n*times[times.length-1];
        
        while(left<=right){
            long count = 0;
            long mid = (left+right)/2;
            for(int i=0; i<times.length; i++){
                count += mid/times[i];
            }
            if(count<n){
                left = mid+1;
            }else{
                right = mid-1;
                answer = mid;
            }
        }
        
        return answer;
    }
}