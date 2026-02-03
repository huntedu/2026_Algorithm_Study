package com.boj;

import java.util.*;
import java.io.*;

public class BOJ_2166 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;

        int N = Integer.parseInt(br.readLine());

        st = new StringTokenizer(br.readLine());

        long x = Integer.parseInt(st.nextToken());
        long y = Integer.parseInt(st.nextToken());
        long x1 = x;
        long y1 = y;
        long sum = 0;

        for(int i = 1; i < N; i++){
            st = new StringTokenizer(br.readLine());
            long x2 = Integer.parseInt(st.nextToken());
            long y2 = Integer.parseInt(st.nextToken());

            long a = x * y2;
            long b = y * x2;

            sum += a - b;
            x = x2;
            y = y2;

        }
        sum += x * y1 - y * x1;

        System.out.println(String.format("%.1f", Math.abs(sum)/(2.0)));
    }
}