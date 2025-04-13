#include <stdio.h>
#include <stdlib.h>

int arr[41];

int fibonacci(int n) {
    if (n == 0) {
        return 0;
    }
    
    else if (n == 1) {
        return 1;
    }
    else {
        if (arr[n]) return arr[n];

        arr[n] = fibonacci(n - 1) + fibonacci(n - 2);
        return arr[n];
    }
}

int main() {
    arr[0] = 0;
    arr[1] = 1;

    fibonacci(40);
    
    int testCase;
    int ans;
    scanf("%d", &testCase);

    for (int i = 0; i < testCase; i++) {
        int num;
        scanf("%d", &num);

        if (num == 0) printf("1 0\n");
        else if (num == 1) printf("0 1\n");
        else printf("%d %d\n", arr[num - 1], arr[num]);
    }
    
    return 0;
}