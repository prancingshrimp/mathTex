class TEXT(object):
    def __init__(self, coordinate_X, coordinate_Y, text_size, text_form, output_text, output_file):
        self.text_size = text_size
        self.text_form = text_form
        self.output_file = output_file
        self.output_text = output_text
        self.a4_paper_width = 210.0

        self.text = "\\block{" + str(self.a4_paper_width) + "mm}{" + str(coordinate_X) +\
                    "mm}{" + str(coordinate_Y) + "mm}{"
        if self.text_size == 'n':
            pass
        elif self.text_size == 'l':
            self.text += "\\large"
        elif self.text_size == 'L':
            self.text += "\\Large"
        else:
            print("What is", self.text_size, "?")
            exit(1)
        self.text += "\\sffamily{"
        if self.text_form == "n":
            self.text += self.output_text + "}}"
        elif self.text_form == "b":
            self.text += "\\textbf{"
            self.text += self.output_text + "}}}"
        elif self.text_form == "i":
            self.text += "\\textit{"
            self.text += self.output_text + "}}}"
        else:
            print("What is", self.text_form, "?")
            exit(1)
        self.output_file.write([self.text])