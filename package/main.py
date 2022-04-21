import os
from sys import exit

from package.time_counter import TIME_COUNTER
from package.output_file import OUTPUT_FILE
from package.file_parser import FILE_PARSER


class MAIN(object):

    def start_time_counter(self):
        self.time_counter = TIME_COUNTER()



    def stop_time_counter(self):
        self.time_counter.stop()
        self.time_counter.print_result()



    def check_arguments(self, argv):
        self.argv_len = len(argv)
        if self.argv_len != 2:
            print("Check Arguments: mathTex <input_file>")
            exit(1)
        self.input_file_name = "./" + argv[1]



    def read_file(self):
        if os.path.isfile(self.input_file_name) != True:
            print("Input file doesn't exist.")
            exit(1)
        self.file_data = []
        with open(self.input_file_name, encoding='utf-8') as File:
            line_number = 0
            for line in File:
                line_number += 1
                if line[0] != '#' and line != '\n':
                    self.file_data.append([line_number,line.strip()])
                    #print(line.strip())
            #print(self.file_data)



    def create_output_file(self):
        self.output_file = OUTPUT_FILE(self.input_file_name)
        self.output_file.write_tex_intro()



    def create_file_parser(self):
        self.file_parser = FILE_PARSER(self.output_file, self.file_data)



    def parse_file_data(self):
        self.file_parser.run()



    def execute_pdflatex(self):
        output_file_name = os.path.splitext(os.path.basename(self.input_file_name))[0]
        os.system("pdflatex " + output_file_name + ".tex")



    def remove_unnecessary_files(self):
        trash_file_name = os.path.splitext(os.path.basename(self.input_file_name))[0]
        try:
            os.remove(trash_file_name + ".log")
            os.remove(trash_file_name + ".aux")
        except:
            pass



    def run(self, argv):
        self.start_time_counter()
        self.check_arguments(argv)
        self.read_file()
        self.create_output_file()
        self.create_file_parser()
        self.parse_file_data()
        self.output_file.write_tex_outro()
        self.execute_pdflatex()
        self.remove_unnecessary_files()
        self.stop_time_counter()