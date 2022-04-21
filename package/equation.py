class EQUATION(object):
    def __init__(self, coordinate_X, coordinate_Y, equation_text, output_file, variables):
        self.output_file = output_file
        self.equation_text = equation_text
        self.equation_text = equation_text.split('$')

        for item in range(0, len(self.equation_text)):
            try:
                value = variables[self.equation_text[item].split('@')[0]]
                digits = self.equation_text[item].split('@')[1]
                digit_string = "." + digits + "g"
                self.equation_text[item] = str(format(float(value), digit_string))
            except:
                pass

        tmp_equation_text = ""
        for item in range(0, len(self.equation_text)):
            tmp_equation_text += self.equation_text[item]
        self.equation_text = tmp_equation_text

        self.text = "\\block{0mm}{" + str(coordinate_X) +\
                    "mm}{" + str(coordinate_Y) + "mm}{"
        self.text += "\\[" + self.equation_text + "\\]}"
        self.output_file.write([self.text])