**Medians and Order Statistics & Elementary Data Structures Implementation and Analysis**
This project implements and analyzes basic data structures including arrays, matrices, stacks, queues, and linked lists in Python.



Installation
This project requires Python 3.6 or later. No additional libraries are needed.

To get started, clone this repository:

Usage
To run the implementations and tests, execute the main Python script:

This will run through all the implemented data structures, perform basic operations, and output the results.

Implemented Data Structures
Matrix (2D Array)
Stack
Queue
Linked List
Each data structure is implemented in its own class with basic operations.

Performance Analysis
The time complexity for basic operations of each data structure is as follows:

Matrix (2D Array)
Access: O(1)
Insertion/Deletion at end: O(1) amortized
Insertion/Deletion at arbitrary position: O(n)
Stack
Push: O(1)
Pop: O(1)
Peek: O(1)
Queue
Enqueue: O(1)
Dequeue: O(n) for array implementation, O(1) for optimized implementations
Front: O(1)
Linked List
Insertion at beginning: O(1)
Insertion at end: O(n)
Deletion: O(n)
Search: O(n)
Summary of Findings
Arrays and Matrices:

Provide fast random access (O(1))
Efficient for scenarios requiring direct indexing
Useful in image processing, scientific computing, and game development
Stacks:

Offer constant time operations for all basic functions
Ideal for LIFO (Last-In-First-Out) scenarios
Commonly used in function call management, undo mechanisms, and expression parsing
Queues:

Efficient for FIFO (First-In-First-Out) operations
Array implementation may have O(n) dequeue, which can be optimized
Essential in task scheduling, breadth-first search, and data buffering
Linked Lists:

Provide dynamic size management
Efficient for frequent insertions and deletions, especially at the beginning
Useful in implementing hash tables, managing dynamic data sets, and representing polynomial arithmetic
