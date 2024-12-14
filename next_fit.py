def next_fit(memory_blocks, process_sizes):
    last_allocated = 0  # Pointer to the last allocated memory block
    allocations = [-1] * len(process_sizes)  # Initialize allocation results
   
    for p_index, process_size in enumerate(process_sizes):
        allocated = False  # Track whether the process is allocated
       
        # Search for a suitable memory block starting from last_allocated
        for i in range(last_allocated, len(memory_blocks)):
            if memory_blocks[i] >= process_size:
                allocations[p_index] = i  # Allocate process to memory block
                memory_blocks[i] -= process_size  # Update memory block size
                last_allocated = i  # Update pointer to the last allocated block
                allocated = True
                break

        # If no suitable block is found, wrap around to the beginning
        if not allocated:
            for i in range(0, last_allocated):
                if memory_blocks[i] >= process_size:
                    allocations[p_index] = i
                    memory_blocks[i] -= process_size
                    last_allocated = i
                    allocated = True
                    break

        # If process could not be allocated
        if not allocated:
            print(f"Process {p_index} with size {process_size} cannot be allocated.")
   
    return allocations

# Testing function for multiple cases
def test_cases():
    test_data = [
        {
            "memory_blocks": [100, 500, 200, 300, 600],
            "process_sizes": [212, 417, 112, 426],
            "description": "Test Case 1: Processes exceed memory availability"
        },
        {
            "memory_blocks": [300, 600, 350, 200],
            "process_sizes": [100, 250, 300, 150],
            "description": "Test Case 2: All processes fit in available blocks"
        },
        {
            "memory_blocks": [400, 100, 600, 200],
            "process_sizes": [300, 500, 100, 50],
            "description": "Test Case 3: Partial allocation due to fragmentation"
        }
    ]

    for index, data in enumerate(test_data):
        print(f"--- {data['description']} ---")
        memory_blocks = data["memory_blocks"][:]
        process_sizes = data["process_sizes"]
        allocations = next_fit(memory_blocks, process_sizes)
        print("Allocations:", allocations)
        print("Remaining Memory Blocks:", memory_blocks)
        print()

# Run the test cases
test_cases()
