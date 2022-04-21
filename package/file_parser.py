import math
from sys import exit

from package.margin import LEFTMARGIN
from package.margin import RIGHTMARGIN
from package.margin import TOPMARGIN
from package.margin import BOTTOMMARGIN

from package.text import TEXT
from package.equation import EQUATION


class FILE_PARSER(object):
    def __init__(self, output_file, file_data):
        self.output_file = output_file
        self.file_data = file_data
        self.variables = dict()



    def create_margin(self, margin_data):
        margin_orientation = margin_data.split(':')[1]
        try:
            margin_distance = float(margin_data.split(':')[2])
        except:
            print("What is", margin_data.split(':')[2], "?")
            exit(1)

        if margin_orientation == "left":
            LEFTMARGIN(margin_distance, self.output_file)

        elif margin_orientation == "right":
            RIGHTMARGIN(margin_distance, self.output_file)

        elif margin_orientation == "top":
            TOPMARGIN(margin_distance, self.output_file)

        elif margin_orientation == "bottom":
            BOTTOMMARGIN(margin_distance, self.output_file)

        else:
            print("What is", margin_orientation, "?")
            exit(1)



    def create_newpage(self, line_data):
        self.output_file.write(["\\nextpage{}"])



    def init_variable(self, line_data):
        line_data = line_data.split(':')[1].replace(' ', '')
        var_name = line_data.split('=')[0]
        var_value = line_data.split('=')[1]
        if var_value == "None":
            self.variables[var_name] = var_value
        else:
            try:
                self.variables[var_name] = float(var_value)
            except:
                print("What is", var_value, "?")
                exit(1)



    def compute_variable(self, line_data):
        line_data = line_data.split(':')[1].replace(' ', '')
        var_name = line_data.split('=')[0].replace('$','')
        rhs = line_data.split('=')[1]

        if rhs.count('$') % 2 != 0:
            print("In this computation line is an odd number of $ !")
            exit(1)
        else:
            rhs = rhs.split('$')
            for item in range(0, len(rhs)):
                try:
                    rhs[item] = self.variables[rhs[item]]
                except:
                    pass
            tmp_rhs = ""
            for item in range(0, len(rhs)):
                tmp_rhs += str(rhs[item])
            rhs = tmp_rhs.replace("pi", str(math.pi))
            if rhs.count("None") != 0:
                print("There is a None in the equation!")
                exit(1)
            self.variables[var_name] = eval(rhs)



    def write_equation(self, line_data):
        try:
            coordinate_X = float(line_data.split(':')[1].split(',')[0])
            coordinate_Y = float(line_data.split(':')[1].split(',')[1])
        except:
            print("What is", line_data.split(':')[1], "?")
            exit(1)
        equation_text = line_data.split('"')[1]
        if equation_text.count('$') % 2 != 0:
            print("In this computation line is an odd number of $ !")
            exit(1)
        else:
            EQUATION(coordinate_X, coordinate_Y, equation_text, self.output_file, self.variables)



    def write_text(self, line_data):
        try:
            coordinate_X = float(line_data.split(':')[1].split(',')[0])
            coordinate_Y = float(line_data.split(':')[1].split(',')[1])
        except:
            print("What is", line_data.split(':')[1], "?")
            exit(1)
        text_size = line_data.split(':')[2]
        text_form = line_data.split(':')[3]
        output_text = line_data.split('"')[1]
        TEXT(coordinate_X, coordinate_Y, text_size, text_form, output_text, self.output_file)



    def throw_error(line, line_number):
        print("There occurs an error parsing line number", line_number, "!\nAborted!")
        exit(1)



    def run(self):
        functions = dict(margin = self.create_margin,\
                              i = self.init_variable,\
                              c = self.compute_variable,\
                              e = self.write_equation,\
                              t = self.write_text,\
                              newpage = self.create_newpage)
        for line in self.file_data:
            #functions[line[1].split(':')[0]](line[1])
            try:
                functions[line[1].split(':')[0]](line[1])
            except:
                self.throw_error(line[0])
