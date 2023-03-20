def round_robin(tasks, quantum):
    time = 0
    completed_tasks = []
    queue = []
    waiting_tasks = tasks.copy()

    while True: #this simulates cpu clock cycling 
        if not waiting_tasks: #stop program when there are no more tasks
            if not queue:
                return completed_tasks

        #create a list of tasks that can now be processed
        queue += [tuple for tuple in waiting_tasks if tuple[1]<=time]
        for tuple in queue:
            if tuple in waiting_tasks:
                #tasks in queue can now be processed by cpu 
                waiting_tasks.remove(tuple)


        #if list is not empty do the task
        if queue:
            task = queue[0]
            name, arrival_time, burst_time = task
            queue.pop(0)
            #task is not completed in this quantum
            if burst_time > quantum:
                burst_time = burst_time - quantum
                queue.append((name,arrival_time,burst_time))
                time+=quantum
            else: #task is completed in this quantum
                end_time = time + burst_time
                completed_tasks.append((name, arrival_time, burst_time, end_time))
                time+=burst_time
        else:
            time += 1

def shortest_job_first(tasks):
    time = 0
    completed_tasks = []
    queue = []
    waiting_tasks = tasks.copy()

    while True: #this simulates cpu clock cycling 
        if not waiting_tasks: #stop program when there are no more tasks
            if not queue:
                #tasks in queue can now be processed by cpu 
                return completed_tasks

        #create a list of tasks that can now be processed
        queue += [tuple for tuple in waiting_tasks if tuple[1]<=time]
        for tuple in queue:
            if tuple in waiting_tasks:
                waiting_tasks.remove(tuple)

        #sort tasks by length
        queue.sort(key=lambda x: x[2])

        #do the shortest task
        if queue:
            task = queue[0]
            name, arrival_time, burst_time = task
            queue.pop(0)
            end_time = time + burst_time
            completed_tasks.append((name, arrival_time, burst_time, end_time))
            time+=burst_time
        else:
            time += 1


#name, arrival time, burst time
tasks = [    ("task1", 0, 10),    ("task2", 1, 5),    ("task3", 2, 9),  ("task4", 4, 2)]
tasks.sort(key=lambda x: x[1])

#name, arrival time, burst time, end time
completed_tasks = round_robin(tasks, 1)
print("Round-robin: ",completed_tasks)

completed_tasks = shortest_job_first(tasks)
print("SJF: ",completed_tasks)
print(" ")






def fifo(pages, frame_size):
    frame = []
    page_faults = 0

    #for each page in the list of pages
    for page in pages:
        if page not in frame:
            page_faults += 1
            #if the frame is full
            if len(frame) == frame_size:
                #remove the oldest page 
                frame.pop(0)
            #add the page to the frame
            frame.append(page)
        print(frame)

    print("Page faults: ", page_faults)
    return page_faults

def lru(pages, frame_size):
    frame = []
    page_faults = 0

    #for each page in the list of pages
    for page in pages:
        if page not in frame:
            page_faults += 1
            #if the frame is full
            if len(frame) == frame_size:
                #remove the least recently used page
                frame.pop(0)
            #add the page to the frame
            frame.append(page)
        else:
            #if the page is in the frame, remove it
            frame.remove(page)
            #add the page to the end of the frame (since it was just accessed)
            frame.append(page)
        print(frame)

    print("Page faults: ", page_faults)
    return page_faults

#a list of inregers representing pages
pages = [2, 1, 5, 6, 3, 5, 1, 2, 1, 4]
#integer representing size of memory frame
frame_size = 3

print("FIFO: ")
fifo(pages, frame_size)
print(" ")

print("LRU: ")
lru(pages, frame_size)

