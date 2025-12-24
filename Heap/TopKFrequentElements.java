import java.util.*;

class TopKFrequentElements {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for (int n : nums)
            freq.put(n, freq.getOrDefault(n, 0) + 1);

        PriorityQueue<Integer> heap =
                new PriorityQueue<>((a, b) -> freq.get(a) - freq.get(b));

        for (int key : freq.keySet()) {
            heap.offer(key);
            if (heap.size() > k)
                heap.poll();
        }

        int[] res = new int[k];
        for (int i = k - 1; i >= 0; i--)
            res[i] = heap.poll();

        return res;
    }
}
