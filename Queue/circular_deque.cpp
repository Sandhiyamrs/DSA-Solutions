#include <bits/stdc++.h>
using namespace std;

class MyCircularDeque {
    vector<int> arr;
    int front, rear, size, cap;

public:
    MyCircularDeque(int k) {
        cap = k;
        arr.resize(k);
        front = 0;
        rear = -1;
        size = 0;
    }

    bool insertFront(int value) {
        if(isFull()) return false;
        front = (front - 1 + cap) % cap;
        arr[front] = value;
        size++;
        return true;
    }

    bool insertLast(int value) {
        if(isFull()) return false;
        rear = (rear + 1) % cap;
        arr[rear] = value;
        size++;
        return true;
    }

    bool deleteFront() {
        if(isEmpty()) return false;
        front = (front + 1) % cap;
        size--;
        return true;
    }

    bool deleteLast() {
        if(isEmpty()) return false;
        rear = (rear - 1 + cap) % cap;
        size--;
        return true;
    }

    int getFront() {
        return isEmpty() ? -1 : arr[front];
    }

    int getRear() {
        return isEmpty() ? -1 : arr[rear];
    }

    bool isEmpty() {
        return size == 0;
    }

    bool isFull() {
        return size == cap;
    }
};
