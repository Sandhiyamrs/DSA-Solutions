class MyCircularDeque {
    int[] arr;
    int front, rear, size, cap;

    public MyCircularDeque(int k) {
        cap = k;
        arr = new int[k];
        front = 0;
        rear = -1;
        size = 0;
    }

    public boolean insertFront(int value) {
        if (isFull()) return false;
        front = (front - 1 + cap) % cap;
        arr[front] = value;
        size++;
        return true;
    }

    public boolean insertLast(int value) {
        if (isFull()) return false;
        rear = (rear + 1) % cap;
        arr[rear] = value;
        size++;
        return true;
    }

    public boolean deleteFront() {
        if (isEmpty()) return false;
        front = (front + 1) % cap;
        size--;
        return true;
    }

    public boolean deleteLast() {
        if (isEmpty()) return false;
        rear = (rear - 1 + cap) % cap;
        size--;
        return true;
    }

    public int getFront() {
        return isEmpty() ? -1 : arr[front];
    }

    public int getRear() {
        return isEmpty() ? -1 : arr[rear];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean isFull() {
        return size == cap;
    }
}
