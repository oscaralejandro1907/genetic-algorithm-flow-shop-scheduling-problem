import queue


class Solution:
    def __init__(self, instance):
        self.instance = instance  # problem instance
        self.job_order = list()
        self.makespan = 0

    def calculate_makespan(self, job_order):
        """Calculates the makespan of the given solution"""
        queue_in_machines = []
        queue_status = queue.PriorityQueue()

        # Append a queue object in every machine
        for i in range(self.instance.n_machines):
            queue_in_machines.append(queue.Queue())  # queues objects are init with infinite values

        busy_machines = []  # A list of bool to indicate if a machine is busy or not
        # Initialize each machine as idle (not busy)
        for i in range(self.instance.n_machines):
            busy_machines.append(False)

        time = 0

        # Put the sequence of jobs ids on the first machine to form the queue and begin processing
        for job in job_order:
            queue_in_machines[0].put(job)

        first_job = queue_in_machines[0].get()  # The get() method remove and return the first job from queues
        # pt = int(self.instance.Jobs[first_job].Operations[0].processing_time)
        pt = int(self.instance.Jobs[first_job].processing_time_on_machine[str(0)])
        queue_status.put((time + pt, 0, first_job))  # Put the time, the machine 0, and job
        busy_machines[0] = True

        while True:
            time, machine, job = queue_status.get()
            if job == job_order[-1] and machine == self.instance.n_machines - 1:
                # Break the cycle once it gets the last job and the las machine
                break
            busy_machines[machine] = False

            if not queue_in_machines[machine].empty():
                # if there are jobs in queue to be processed in current machine
                next_job = queue_in_machines[machine].get()
                pt_next_job = int(self.instance.Jobs[next_job].processing_time_on_machine[str(machine)])
                queue_status.put((time + pt_next_job, machine, next_job))  # update status
                busy_machines[machine] = True

            if machine < self.instance.n_machines - 1:
                # if not the last machine
                if not busy_machines[machine + 1]:
                    # and the next machine is available
                    pt_job = int(self.instance.Jobs[job].processing_time_on_machine[str(machine + 1)])
                    queue_status.put((time + pt_job, machine + 1, job))
                    busy_machines[machine + 1] = True
                else:
                    queue_in_machines[machine+1].put(job)

        return time
