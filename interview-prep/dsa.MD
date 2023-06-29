# DSA
# Heap
- Heap is a complete binary tree, maxHeap(highest element at root), minHeap(lowest element at root)
- Heap is stored into array as, for example if node is i^th element its left child will be at index 2i & right child would be at index 2i+1 considering starting index as 1.
- creation of heap, if we consider maxheap for elements [10,20,15,30,40]
    ```
    10 is inserted as root node
    20 is added as left child, compared with root node & shifted to root to maintain maxHeap
            20
        10
        array => [20,10]
    15 is added as right child to node 20, compared with left & root so no changes
            20
         10    15
        array =>[20,10,15]
    30 is added as left child to node 10, compared with 10 so shifted
                30
            20      15
        10
        array => [30,20,15,10]
    40 is added as right child to node 20, compared with left child 10 and node 20, swapped with 20 & 20 again compared with root node 30 & swapped
               40
           30      15 
        10    20
     array => [40,30,15,10,20]
    ```
- insertion into heap, starts at leftmost child & compared with root node and traverses above, similar to creation. for example if 50 is to be added in above heap, place it as left child of 15 & compare with 15(swap) then compare with root node (swap)
- deletion of values from heap, top most node (root node) is popped & then the binary tree is adjusted from top to bottom by placing last element on top(last child). for example if 40 is removed then 20 is placed in place of 40 & tree is adjusted to form maxHeap
- deletion of elements & storing in free spaces of array creates a sorted array
- heapify is process of creating heap from list of elements, following top to down unlike bottup up in creation
    ```
    [10,20,15,12,40,25,18]
    start at last element 18,25,40,12 no child nodes each of them is a maxHeap
    next is element 15, having child nodes 25,18. 15 is swapped with 25 & heap is formed [25,15,18]
    next is element 20 with child nodes 12, 40. 20 is swapped with 40 & heap is formed [40,12,20]
    we have 2 heaps, next is root node 10 having child nodes 25,40. 10 is swapped with 40 [40,10,25]
    10 is compared with 12,20 gets swapped. 25,15,18 is already maxHeap
    so finally [40,20,25,12,10,15,18]
    ```
- Time complexity of creation of new heap is O(n)logn, insertion & deletion is logn, heapify is O(n)
- Priority Queue for smaller number higher priority is minHeap, & maxheap for larger number high priority
