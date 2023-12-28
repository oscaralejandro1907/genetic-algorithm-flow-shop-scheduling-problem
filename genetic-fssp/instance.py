class Job:
    def __init__(self, jid):
        self.jobid = jid
        self.processing_time_on_machine = dict()  # List of operations of this job


class Instance:
    """ Instance class with data file information"""
    def __init__(self, filename):
        self.n_jobs = None
        self.n_machines = None

        self.Jobs = list()  # List of objects Job type

        # Parsing instance from filename
        with open(filename) as file:
            #  Read number of jobs and machines
            line = file.readline()
            self.n_jobs = int(line.split()[0])
            self.n_machines = int(line.split()[1])

            # Parsing processing time information of machines for each job
            for j in range(self.n_jobs):
                line = file.readline()
                new_job = Job(j)
                self.Jobs.append(new_job)
                fields = line.split()
                for m in range(0, len(fields), 2):
                    self.Jobs[j].processing_time_on_machine[fields[m]] = fields[m + 1]
