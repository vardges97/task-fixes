class VirtualMemory:
    def __init__(self, num_frames, page_size):
        self.num_frames = num_frames
        self.page_size = page_size
        self.memory = [None] * num_frames
        self.page_queue = []

    def allocate_page(self, page_number):
        if page_number in self.page_queue:
            return

        if len(self.page_queue) == self.num_frames:
            evicted_page = self.page_queue.pop(0)
            self.memory[self.memory.index(evicted_page)] = None

        self.page_queue.append(page_number)
        empty_frame = self.memory.index(None)
        self.memory[empty_frame] = page_number

    def access_page(self, page_number):
        if page_number in self.page_queue:
            self.page_queue.remove(page_number)
            self.page_queue.append(page_number)
            return True
        else:
            return False

    def display_memory_status(self):
        print("Memory Status:")
        for i in range(self.num_frames):
            page = self.memory[i]
            if page is not None:
                print(f"Frame {i + 1}: Page {page}")
            else:
                print(f"Frame {i + 1}: Empty")

def main():
    num_frames = 5
    page_size = 2048
    virtual_memory = VirtualMemory(num_frames, page_size)

    while True:
        print("\nMenu:")
        print("1. Allocate Page")
        print("2. Access Page")
        print("3. Display Memory Status")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            page_number = int(input("Enter page number to allocate: "))
            virtual_memory.allocate_page(page_number)
        elif choice == '2':
            page_number = int(input("Enter page number to access: "))
            if virtual_memory.access_page(page_number):
                print(f"Page {page_number} is in memory.")
            else:
                print(f"Page {page_number} is not in memory.")
        elif choice == '3':
            virtual_memory.display_memory_status()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")

    print("Goodbye!")

if __name__ == "__main__":
    main()