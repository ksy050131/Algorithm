#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#define MAX 100000

typedef struct {
    int age;
    char name[101];
} element;

void merge(int, int, int, element *);
void mergeSort(int, int, element *);

int main() {
    int testCase;
    scanf("%d", &testCase);
    element* p = (element*)malloc(testCase * sizeof(element));
    if (p == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    for (int i = 0; i < testCase; i++) {
        scanf("%d %s", &p[i].age, p[i].name);
        // printf("%d %s\n", p[i].age, p[i].name);
    }

    mergeSort(0, testCase - 1, p);

    // 정렬 후 출력
    for (int i = 0; i < testCase; i++) {
        printf("%d %s\n", p[i].age, p[i].name);
    }

    free(p);

    return 0;
}

void merge(int row, int mid, int high, element *student) {
    int i = row;
    int j = mid + 1;
    int k = 0;
    element* U = (element*)malloc((high - row + 1) * sizeof(element));  // 동적 할당

    while (i <= mid && j <= high) {
        if (student[i].age <= student[j].age) {  // <=로 해야 안정 정렬됨
            U[k++] = student[i++];
        } else {
            U[k++] = student[j++];
        }
    }

    while (i <= mid) {
        U[k++] = student[i++];
    }

    while (j <= high) {
        U[k++] = student[j++];
    }

    for (int t = row, l = 0; t <= high; t++, l++) {
        student[t] = U[l];
    }

    free(U);  // 동적 할당 해제
}


void mergeSort(int row, int high, element *arr) {
    if (row < high) {
        int mid = (row + high) / 2;
        
        mergeSort(row, mid, arr);
        mergeSort(mid + 1, high, arr);
        merge(row, mid, high, arr);
    }
}