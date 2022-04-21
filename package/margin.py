class MARGIN(object):
    def __init__(self, margin_distance, output_file):
        self.output_file = output_file
        self.margin_text = []
        self.a4_paper_height = 297.0
        self.a4_paper_width = 210.0



class LEFTMARGIN(MARGIN):
    def __init__(self, margin_distance, output_file):
        MARGIN.__init__(self, margin_distance, output_file)
        self.margin_text.append("\\begin{textblock*}{" + str(self.a4_paper_height) +\
                           "mm}(" + str(margin_distance) + "mm," + str(self.a4_paper_height) + "mm)")
        self.margin_text.append("\\begin{picture}(0,0)")
        self.margin_text.append("\\line(0,1){2000}")
        self.margin_text.append("\\end{picture}")
        self.margin_text.append("\\end{textblock*}")
        self.output_file.write(self.margin_text)



class RIGHTMARGIN(MARGIN):
    def __init__(self, margin_distance, output_file):
        MARGIN.__init__(self, margin_distance, output_file)
        self.margin_text.append("\\begin{textblock*}{" + str(self.a4_paper_height) +\
                           "mm}(" + str(self.a4_paper_width - margin_distance) + "mm," + str(self.a4_paper_height) + "mm)")
        self.margin_text.append("\\begin{picture}(0,0)")
        self.margin_text.append("\\line(0,1){2000}")
        self.margin_text.append("\\end{picture}")
        self.margin_text.append("\\end{textblock*}")
        self.output_file.write(self.margin_text)



class TOPMARGIN(MARGIN):
    def __init__(self, margin_distance, output_file):
        MARGIN.__init__(self, margin_distance, output_file)
        self.margin_text.append("\\begin{textblock*}{" + str(self.a4_paper_width) +\
                                "mm}(0.0mm," + str(margin_distance) + "mm)")
        self.margin_text.append("\\begin{picture}(0,0)")
        self.margin_text.append("\\line(1,0){2000}")
        self.margin_text.append("\\end{picture}")
        self.margin_text.append("\\end{textblock*}")
        self.output_file.write(self.margin_text)



class BOTTOMMARGIN(MARGIN):
    def __init__(self, margin_distance, output_file):
        MARGIN.__init__(self, margin_distance, output_file)
        self.margin_text.append("\\begin{textblock*}{" + str(self.a4_paper_width) +\
                                "mm}(0.0mm," + str(self.a4_paper_height - margin_distance) + "mm)")
        self.margin_text.append("\\begin{picture}(0,0)")
        self.margin_text.append("\\line(1,0){2000}")
        self.margin_text.append("\\end{picture}")
        self.margin_text.append("\\end{textblock*}")
        self.output_file.write(self.margin_text)