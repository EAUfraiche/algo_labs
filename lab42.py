class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

    def __repr__(self):
        return f"[{self.value}] (пріоритет: {self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, value, priority):
        new_node = Node(value, priority)
        self.heap.append(new_node)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def peek(self):
        return self.heap[0] if self.heap else None

    def change_priority(self, value, new_priority):
        for i in range(len(self.heap)):
            if self.heap[i].value == value:
                old_priority = self.heap[i].priority
                self.heap[i].priority = new_priority
                if new_priority > old_priority:
                    self._heapify_up(i)
                else:
                    self._heapify_down(i)
                return True
        return False

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent].priority:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def _heapify_down(self, index):
        largest = index
        left, right = 2 * index + 1, 2 * index + 2
        n = len(self.heap)

        if left < n and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < n and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def display(self):
        if not self.heap:
            print("Черга порожня.")
        else:
            print("Поточна купа:", " -> ".join([str(node) for node in self.heap]))


def main():
    pq = PriorityQueue()
    print("--- Меню керування чергою пріоритетів ---")
    
    while True:
        print("\n1. Додати елемент\n2. Видалити найпріоритетніший\n3. Переглянути чергу\n4. Змінити пріоритет\n5. Вихід")
        choice = input("Оберіть дію: ")

        if choice == '1':
            val = input("Введіть назву/значення: ")
            try:
                pri = int(input("Введіть числовий пріоритет: "))
                pq.insert(val, pri)
                print(f"Додано: {val}")
            except ValueError:
                print("Помилка: Пріоритет має бути цілим числом!")

        elif choice == '2':
            removed = pq.extract_max()
            if removed:
                print(f"Видалено елемент з найвищим пріоритетом: {removed}")
            else:
                print("Черга порожня!")

        elif choice == '3':
            pq.display()
            top = pq.peek()
            if top:
                print(f"Наступний на черзі: {top}")

        elif choice == '4':
            val = input("Введіть назву елемента для зміни: ")
            try:
                new_pri = int(input("Введіть новий пріоритет: "))
                if pq.change_priority(val, new_pri):
                    print("Пріоритет успішно змінено.")
                else:
                    print("Елемент не знайдено.")
            except ValueError:
                print("Помилка: Пріоритет має бути числом!")

        elif choice == '5':
            print("Вихід...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()