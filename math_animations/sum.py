from manim import *
import numpy as np

class OneOverNProof(Scene):
    def construct(self):

        series_sum_n = MathTex(r"\sum_{k=1}^{n} k = 1 +2 +3 +4+5+\dots+n=", font_size=40).shift(UP)
        qmark = Text("?", font_size=28).next_to(series_sum_n, buff=0.3)
        sum_group = VGroup(series_sum_n, qmark)

        self.play(
            Succession(
                Write(series_sum_n),
                Write(qmark),
                run_time=4
            )
        )
        self.wait(2)
        self.play(sum_group.animate.shift(UP*1.5))
        self.wait(0.5)

        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PINK, PURPLE]
        num_rows = 7 
        #rows will fill up the VGroup once the for loops are reached
        squares = VGroup()

        #iterate through each row and square, and set colour and position arguments
        for i in range(1, num_rows + 1):
            row = VGroup().shift(UP*2)
            for j in range(i):
                square = Square(side_length=0.5)                
                square.set_fill(colors[i-1], opacity=0.8)
                square.set_stroke(width=2)
                square.move_to(RIGHT * j * 0.5 + DOWN * i * 0.5)
                row.add(square)
            row.shift(LEFT * (num_rows - 1) * 0.2) 
            squares.add(row)

        self.wait(1)

        squares.move_to(DOWN)

        #animate wach row to the scene, one by one
        for i, row in enumerate(squares):
            self.play(FadeIn(row), run_time=0.5)
            self.wait(0.75)

        #create labels for each row
        labels_text = [MathTex(label, font_size=30) for label in [r"1", r"2", r"3", r"4", r"5", r"\dots", r"k"]]
        for i, label in enumerate(labels_text):
            label.next_to(squares[i].get_left(), LEFT)
            self.play(Write(label), run_time=0.5)
        self.wait(0.5)

        labels_transform = MathTex(r"(1+2+3+4+5+\dots+n)=", font_size=30).move_to(squares.get_left()).shift(LEFT*2.5)
        
        self.play(TransformMatchingShapes(VGroup(*labels_text), labels_transform))
        self.wait(1)

        labels_transform2 = MathTex(r"2 \cdot(1+2+3+4+5+\dots+n)=", font_size=30).move_to(squares.get_left()).shift(LEFT*2.5)
        squares_copy = squares.copy()

        self.play(squares_copy.animate.move_to(squares.get_right()), run_time=2)
        self.play(Rotate(squares_copy, PI), TransformMatchingShapes(labels_transform, labels_transform2),
                  run_time=2)
        self.play(squares_copy.animate.shift(LEFT*1.75+UP*0.5))
        self.wait(2)
        
        n_brace = Brace(squares[-1], DOWN)
        n_text = MathTex(r"n", font_size=30).next_to(n_brace, DOWN)

        self.play(
            Succession(
                GrowFromCenter(n_brace),
                Write(n_text)
            )
        )
        self.wait(0.5)

        n_brace_copy = n_brace.copy()
        n_text_copy = n_text.copy()

        self.play(
                n_brace_copy.animate.move_to(squares_copy.get_right()).rotate(PI/2).shift(RIGHT*0.5+DOWN*0.5),
                n_text_copy.animate.move_to(squares_copy.get_right()).shift(RIGHT*0.8+DOWN*0.5),
                run_time=2
            )  
        
        self.wait(2)

        one_brace = Brace(squares_copy[6], RIGHT, buff=0.35)
        one_text = MathTex(r"1", font_size=30).next_to(one_brace, RIGHT*0.4)

        self.play(
            Succession(
                GrowFromCenter(one_brace),
                Write(one_text)
            )
        )
        self.wait(1)

        one_n_group = VGroup(n_text_copy, one_text)
        n_plus_one = MathTex(r"(n+1)", font_size=30).move_to(squares_copy.get_right()).shift(RIGHT*0.6)

        self.play(FadeOut(n_brace_copy, one_brace))
        self.play(TransformMatchingShapes(one_n_group, n_plus_one), run_time=2)
        self.play(
            Succession(
                FadeOut(n_brace),
                n_text.animate.shift(UP*0.5)
            )
        )
        self.wait(1)

        self.play(
            Succession(
                FadeOut(qmark),
                n_plus_one.animate.next_to(series_sum_n, RIGHT).shift(RIGHT*0.3+UP*0.3).scale(1.25),
                n_text.animate.next_to(series_sum_n, RIGHT).shift(LEFT*0.1+UP*0.3).scale(1.25)
            )

        )
        self.wait(0.5)
        
        square_dimensions = VGroup(n_text, n_plus_one)
        div = MathTex(r"\frac{n(n+1)}{}", font_size=30).next_to(series_sum_n, RIGHT).shift(RIGHT*0.15+UP*0.3)

        self.play(TransformMatchingShapes(square_dimensions, div),
                  run_time=2
        )
        
        two_copy = labels_transform2[0][0].copy()

        self.play(two_copy.animate.next_to(div.get_bottom()).shift(DOWN*0.2+LEFT*0.3),
                  TransformMatchingShapes(labels_transform2, labels_transform),
                  run_time=2
                
        )
        self.wait(1)
        self.play(FadeOut(labels_transform))

        answer_group = VGroup(div, two_copy)
        sr = SurroundingRectangle(answer_group, color=YELLOW)

        self.play(answer_group.animate.set_color(YELLOW))
        self.wait(1.5)
        self.play(Create(sr), run_time=2)

        self.wait(2)




        
        
                  

        
        
