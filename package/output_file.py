from os import path

class OUTPUT_FILE(object):
    def __init__(self, file_name):
        self.output_file_name = path.splitext(path.basename(file_name))[0]
        self.output_file_name += ".tex"



    def write_tex_intro(self):
        self.intro_text = []
        self.intro_text.append("\\documentclass[a4paper,12pt]{scrartcl}")
        self.intro_text.append("\\usepackage[ngerman]{babel}")
        self.intro_text.append("\\usepackage[utf8]{inputenc}")
        self.intro_text.append("\\usepackage{amsmath,amsfonts,amssymb}")
        self.intro_text.append("\\usepackage[absolute]{textpos}\n")
        
        self.intro_text.append("\\textblockorigin{0mm}{0mm}")
        self.intro_text.append("\\setlength{\\parindent}{0pt}")
        self.intro_text.append("\\pagestyle{empty}\n")
        
        self.intro_text.append("\\newcommand\\nextpage{\\newpage\\hspace{1cm}\\newpage}")
        self.intro_text.append("\\newcommand{\\block}[4]{\\begin{textblock*}{#1}(#2,#3) #4 \\end{textblock*}}\n")
        
        self.intro_text.append("\\begin{document}")
        
        self.write(self.intro_text, 'w')



    def write_tex_outro(self):
        self.outro_text = ["\\end{document}"]
        self.write(self.outro_text)



    def write(self, text, mode='a'):
        with open(self.output_file_name, mode, encoding='utf-8') as File:
            for line in range(0, len(text)):
                File.write(text[line] + '\n')