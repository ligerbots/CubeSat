#!/usr/bin/python3
import json
import os.path
import time


class DataWriter:
    '''Save the info about images and plastic to a data file'''

    def __init__(self, save_dir_arg):
        self.save_dir = save_dir_arg
        return

    def write(self, data):
        '''Write the data to a file'''

        filename = "DATA_" + str(int(time.time())) + ".json"
        full_filename = os.path.join(self.save_dir, filename)
        # print('saving to', full_filename)
        with open(full_filename, 'w') as fout:
            json.dump(data, fout)
        return
