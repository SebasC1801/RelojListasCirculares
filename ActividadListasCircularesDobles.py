class TimeMark:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = TimeMark(data)
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            last.next = new_node
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = TimeMark(data)
        if self.head is None:
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node

    def print_list(self):
        if self.head is None:
            print("Empty list.")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print()


class ClockStructure:
    def __init__(self):
        self.seconds = CircularDoublyLinkedList()
        self.minutes = CircularDoublyLinkedList()
        self.hours = CircularDoublyLinkedList()

        self.current_second = None
        self.current_minute = None
        self.current_hour = None

        self._create_time_marks()

    def _create_time_marks(self):
        for i in range(60):
            self.seconds.insert_at_end(i)
        for i in range(60):
            self.minutes.insert_at_end(i)
        for i in range(24):
            self.hours.insert_at_end(i)

        self.current_second = self.seconds.head
        self.current_minute = self.minutes.head
        self.current_hour = self.hours.head

    def tick(self):
        if self.current_second is not None:
            self.current_second = self.current_second.next
            if self.current_second.data == 0:
                self._increment_minute()

    def _increment_minute(self):
        if self.current_minute is not None:
            self.current_minute = self.current_minute.next
            if self.current_minute.data == 0:
                self.increment_hour()

    def increment_hour(self):
        if self.current_hour is not None:
            self.current_hour = self.current_hour.next

    def get_time(self):
        return (
            self.current_hour.data,
            self.current_minute.data,
            self.current_second.data
        )

    def get_time_str(self):
        h, m, s = self.get_time()
        return f"{h:02d}:{m:02d}:{s:02d}"

    def show_all(self):
        print("Seconds:")
        self.seconds.print_list()
        print("Minutes:")
        self.minutes.print_list()
        print("Hours:")
        self.hours.print_list()

        
    
                
            

            
