Creating an efficient task scheduler involves integrating several components: task management, priority-based scheduling algorithms, and calendar API integration. Below is a simplified version of such an application using Python. This code demonstrates the basic functionality with comments and basic error handling. Note that full integration with real calendar APIs like Google Calendar would require authentication and more advanced code than is feasible to include here, but placeholders will be used for demonstrating where such integrations would occur.

```python
import heapq
from datetime import datetime, timedelta
# Placeholder for calendar API integration
# from some_calendar_api import authenticate, get_free_slots

class Task:
    def __init__(self, name, description, priority, estimated_time):
        self.name = name
        self.description = description
        self.priority = priority  # Lower number indicates higher priority
        self.estimated_time = timedelta(hours=estimated_time)

    def __lt__(self, other):
        """Less than comparison for priority queue"""
        return self.priority < other.priority

    def __str__(self):
        return f"Task(Name: {self.name}, Priority: {self.priority}, Estimated Time: {self.estimated_time})"


class TaskScheduler:
    def __init__(self):
        self.tasks = []
        # Placeholder initialization for calendar API
        # self.calendar = authenticate(credentials_path)
    
    def add_task(self, task):
        try:
            heapq.heappush(self.tasks, task)
            print(f"Task '{task.name}' added successfully.")
        except Exception as e:
            print(f"Error adding task '{task.name}': {e}")

    def schedule_tasks(self):
        try:
            if not self.tasks:
                print("No tasks to schedule.")
                return

            while self.tasks:
                task = heapq.heappop(self.tasks)
                scheduled_time = self.find_next_available_slot(task.estimated_time)
                if scheduled_time:
                    print(f"Task '{task.name}' scheduled from {scheduled_time} to {scheduled_time + task.estimated_time}.")
                else:
                    print(f"No available slot for task '{task.name}'. Need to reschedule.")

        except Exception as e:
            print(f"Error scheduling tasks: {e}")

    def find_next_available_slot(self, duration):
        # Placeholder for integration with a real calendar API
        # example:
        # available_slots = get_free_slots(duration)
        # if available_slots:
        #     return available_slots[0]  # Return the first available slot
        try:
            now = datetime.now()
            return now + timedelta(minutes=10)  # Simplified example
        except Exception as e:
            print(f"Error finding available slot: {e}")
            return None


def main():
    try:
        scheduler = TaskScheduler()

        # Add example tasks
        scheduler.add_task(Task(name="Task 1", description="High priority task", priority=1, estimated_time=2))
        scheduler.add_task(Task(name="Task 2", description="Medium priority task", priority=2, estimated_time=1.5))
        scheduler.add_task(Task(name="Task 3", description="Lower priority task", priority=3, estimated_time=3))

        # Schedule tasks
        scheduler.schedule_tasks()

    except Exception as e:
        print(f"An error occurred during the task scheduling: {e}")

if __name__ == "__main__":
    main()
```

**Key Points of the Program:**
1. **Task Class:** Represents individual tasks with attributes including name, description, priority, and estimated time. Implements comparison on priority to be used in the priority queue.
2. **TaskScheduler Class:** Maintains a priority queue of tasks using Python's `heapq` module to manage and schedule tasks efficiently. It contains methods to add tasks and schedule them using a dummy function `find_next_available_slot` that would ideally interact with an external calendar API.
3. **Error Handling:** The program uses try-except blocks to catch and report errors during task addition and scheduling processes.
4. **Main Function:** This function initializes the task scheduler, adds tasks, and attempts to schedule them.