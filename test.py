from manimlib.imports import *
import os
import pyclbr
from pandas import Series
import pandas as pd


class CodeExample(Scene):
    def construct(self):
        heading = TextMobject("\"Hello, World\" Program", stroke_width=0).scale(1.3)
        heading.to_edge(UP)
        helloworldc = Code(
            "d:/b.cpp",
            run_time=1,
            line_spacing=0.2,
            insert_line_no=False,
            style=code_styles_list[4],
            background="rectangle",
            language=code_languages_list["c"],
        )
        helloworldcpp = Code(
            "d:/b.cpp",
            run_time=1,
            line_spacing=0.2,
            margin=0.3,
            line_no_from=8,
            style=code_styles_list[9],
            background="window",
            corner_radius=0.2,
            language=code_languages_list["cpp"],
        )
        helloworldc.move_to(np.array([-3.6, 0, 0]))
        helloworldcpp.move_to(np.array([3.1, 0, 0]))
        self.play(Write(heading), run_time=0.5)
        self.play(Write(helloworldc), run_time=1.3)
        self.draw_code_all_lines_at_a_time(helloworldcpp)
        self.wait()

    def draw_code_all_lines_at_a_time(self, Code):
        self.play(Write(Code.background_mobject), run_time=0.3)
        self.play(Write(Code.line_numbers), run_time=0.3)
        self.play(*[Write(Code.code[i]) for i in range(Code.code.__len__())],
                  run_time=Code.run_time)

       