a=list(map(int,input().split()))
b=int(input())
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==b:
            print(a[i],a[j])
            
            
            
            
            
            
'''
import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<Integer> a = new ArrayList<>();
        String[] input = scanner.nextLine().split(" ");
        for (String num : input) {
            a.add(Integer.parseInt(num));
        }
        int b = scanner.nextInt();
        for (int i = 0; i < a.size(); i++) {
            for (int j = i + 1; j < a.size(); j++) {
                if (a.get(i) + a.get(j) == b) {
                    System.out.println(a.get(i) + " " + a.get(j));
                }
            }
        }
    }
}
'''