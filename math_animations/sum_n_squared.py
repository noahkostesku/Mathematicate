from manim import *
import numpy as np

class NSquared(ThreeDScene):
    def construct(self):

        sum_series= MathTex(r"\sum_{k=1}^{n} k^2 = 1^2+2^2+3^2+4^2+\dots+n^2=", font_size=40).shift(UP)
        qmark = Text("?", font_size=28).next_to(sum_series, buff=0.3)
        sum_group = VGroup(sum_series, qmark)

        self.play(
            Succession(
                Write(sum_series),
                Write(qmark),
                run_time=4
            )
        )
        self.wait(2)
        self.play(sum_group.animate.shift(UP*1.5))
        self.wait(0.5)

        colors = [RED, GOLD, GREEN_C, BLUE_C, PURPLE_C]
        
        #Create all the square groups
        square_groups = VGroup()
        for n in range(1, 6):
            #Create a group of squares for the current n
            square_group = VGroup()
            for i in range(n):
                for j in range(n):
                    square = Cube(side_length=0.4)
                    square.set_fill(colors[n-1])
                    square.set_stroke(color=BLACK, width=2)
                    square.move_to(np.array([j*0.4, -i*0.4, 0]))
                    square_group.add(square)
            
            # Shift the group to the right position
            if n > 1:
                 # Spacing between groups
                square_group.next_to(square_groups, RIGHT, buff=0.5)

            # Add the current group to the main group
            square_groups.add(square_group)
        
        # Center the square groups on the screen
        # Adjust for spacing between groups
        total_width = sum((n * 0.4) for n in range(1, 6)) + 0.5 * 4
        square_groups.shift(LEFT * (total_width / 2))

        # Animate the creation of the blocks
        self.play(Create(square_groups), run_time=3)
        self.wait(1)
        one_sq = sum_series[0][8:10]
        one_copy = one_sq.copy()
        two_sq = sum_series[0][11:13]
        two_copy = two_sq.copy()
        three_sq = sum_series[0][14:16]
        three_copy = three_sq.copy()
        four_sq = sum_series[0][17:19]
        four_copy = four_sq.copy()
        n_sq = sum_series[0][24:26]
        n_copy = n_sq.copy()
        #layer labels
        self.play(one_copy.animate.next_to(square_groups[0].get_top()).shift(UP*0.4+LEFT*0.4),
                  two_copy.animate.next_to(square_groups[1].get_top()).shift(UP*0.4+LEFT*0.4),
                  three_copy.animate.next_to(square_groups[2].get_top()).shift(UP*0.4+LEFT*0.4),
                  four_copy.animate.next_to(square_groups[3].get_top()).shift(UP*0.4+LEFT*0.4),
                  n_copy.animate.next_to(square_groups[4].get_top()).shift(UP*0.4+LEFT*0.4),
                  run_time=2.5
        )                       
        
        
        self.wait(2)
        self.play(FadeOut(one_copy, two_copy, three_copy, four_copy, n_copy))
        self.wait(1)

        self.play(Rotating(square_groups, radians=PI/2, axis=RIGHT), run_time=1)

        self.wait(1)

        self.play(square_groups.animate.shift(DOWN*1.5))
        self.wait(1)

        #align the pyramid to the lower left corner

        initial_position = square_groups[0].get_corner(DL)

        pyramid = VGroup()
        # Start from the largest layer
        for n in range(5, 0, -1): 
            layer = VGroup()
            for i in range(n):
                for j in range(n):
                    cube = Cube(side_length=0.4)
                    cube.set_fill(colors[5 - n])  
                    cube.set_stroke(color=BLACK, width=2)
                    #Block positioning in 3D space
                    cube.move_to(np.array([j * 0.4, 0, -i * 0.4]))  
                    layer.add(cube)
            # Position each layer in the bottom-left corner
            layer.shift(UP * (5 - n) * 0.4)
            pyramid.add(layer)

        # Position the pyramid at the bottom-left corner of the screen
        pyramid.shift(DOWN*2)
        # Animate the transformation from flat squares to the 3D pyramid
        self.play(Transform(square_groups, pyramid), run_time=3)
        self.wait(1)
        

        self.wait(1)
        self.play(Rotating(square_groups, radians=2*PI, axis=UP), run_time=3)
        self.wait(1)

        pyramid_copy1 = square_groups.copy()
        pyramid_copy2 = square_groups.copy()

        series_label_1 = MathTex(r"3 \cdot", font_size=40).next_to(sum_series, LEFT)
        series_label_2 = MathTex(r"6 \cdot", font_size=40).next_to(sum_series, LEFT)

        self.play(pyramid_copy1.animate.shift(RIGHT*3),
                  pyramid_copy2.animate.shift(LEFT*3),
                  Write(series_label_1)
        )
  
        self.play(
            Succession(
                Rotating(pyramid_copy1, radians=PI/2, axis=UP),
                Rotating(pyramid_copy1, radians=PI/2, axis=OUT),
                run_time=3
                )
        )

        self.play(
            Succession(
                Rotating(pyramid_copy2, radians=PI/2, axis=LEFT),
                Rotating(pyramid_copy2, radians=PI, axis=UP),
                Rotating(pyramid_copy2, radians=PI/2, axis=OUT),
                run_time=3
            )
        )
        self.wait(2)

        self.play(pyramid_copy1.animate.shift(UP*0.4+LEFT*3),
                  pyramid_copy2.animate.shift(RIGHT*3+IN*0.4)
        )
        self.wait(0.5)

        half_pyr_group = VGroup(square_groups, pyramid_copy1, pyramid_copy2)

        self.play(
            Succession(
                Rotating(half_pyr_group, radians=2*PI, axis=UP),
                Rotating(half_pyr_group, radians=-PI/2, axis=LEFT),
                run_time=5      
            )           
        )

        self.play(half_pyr_group.animate.shift(LEFT*2))
        self.wait(1)

        #build second pyramid same as first but different axis positioning (upper left alignment instad of lower left)
        colors = [RED, GOLD, GREEN_C, BLUE_C, PURPLE_C]  

        square_groups2 = VGroup()
        for n in range(1, 6):
            # Create a group of squares for the current n
            square_group = VGroup()
            for i in range(n):
                for j in range(n):
                    square = Cube(side_length=0.4)
                    square.set_fill(colors[n-1])
                    square.set_stroke(color=BLACK, width=2)
                    square.move_to(np.array([j*0.4, -i*0.4, 0]))
                    square_group.add(square)
            
            # Shift the group to the right position
            if n > 1:
                square_group.next_to(square_groups2, RIGHT, buff=0.5)  # Spacing between groups

            # Add the current group to the main group
            square_groups2.add(square_group)
        
        # Center the square groups on the screen
        total_width = sum((n * 0.4) for n in range(1, 6)) + 0.5 * 4 
        square_groups2.shift(LEFT * (total_width / 2))

        # Create the 3D pyramid and position it in the top-left corner
        pyramid2 = VGroup()
        for n in range(5, 0, -1):  
            layer = VGroup()
            for i in range(n):
                for j in range(n):
                    cube = Cube(side_length=0.4)
                    cube.set_fill(colors[5 - n]) 
                    cube.set_stroke(color=BLACK, width=2)
                    cube.move_to(np.array([j * 0.4,0, i * 0.4]))
                    layer.add(cube)
            # Position each layer in the top-left corner
            layer.shift((UP * (5 - n) * 0.4)) 
            pyramid2.add(layer)

        #assign pyramid to the pyramid itself stored in square_groups2
        square_groups2 = pyramid2
        
        pyramid_copy3 = square_groups2.copy()
        pyramid_copy4 = square_groups2.copy()

        pyramid_copy3.shift(RIGHT*3)
        pyramid_copy4.shift(LEFT*3)
                  
        pyramid_copy3.rotate(-PI/2, axis=LEFT)
        pyramid_copy3.rotate(-PI/2, axis=UP)

        pyramid_copy4.rotate(-PI/2, axis=LEFT)
        pyramid_copy4.rotate(PI, axis=UP)
        pyramid_copy4.rotate(PI/2, axis=OUT)

        half_pyr_group2 = VGroup(pyramid2, pyramid_copy3, pyramid_copy4)
        pyramid_copy3.shift(UP*0.4+LEFT*3)
        pyramid_copy4.shift(RIGHT*3+OUT*0.4)
        half_pyr_group2.rotate(-PI/2, axis=LEFT)
        
        half_pyr_group2.next_to(half_pyr_group2, RIGHT*4)

        self.play(FadeIn(half_pyr_group2.next_to(half_pyr_group, RIGHT*4)),
                  ReplacementTransform(series_label_1, series_label_2))
        self.wait(1)

        self.play(Succession(
            Rotating(half_pyr_group, radians=PI/2, axis=UP),
            Rotating(half_pyr_group2, radians=-PI/2, axis=UP),
            run_time=4
            )
        )
        self.wait(1)

        self.play(half_pyr_group.animate.shift(RIGHT))
        self.wait(0.5)
        
        full_group = VGroup(half_pyr_group, half_pyr_group2)

        label1 = MathTex(r"n", font_size=30).shift(DOWN*2.5+LEFT*0.7)
        label2 = MathTex(r"(n+1)", font_size=30).shift(DOWN*0.8+LEFT*2)
        label3 = MathTex(r"(2n+1)", font_size=30).shift(RIGHT*0.8+UP*0.5)


        self.play(Rotating(full_group, radians=PI/4, axis=UP),
                  run_time=2)
        self.play(Write(label1), Write(label2), Write(label3))
        self.wait()
        self.play(FadeOut(qmark))

        
        self.play(label1.animate.next_to(sum_series, RIGHT).shift(UP*0.2))
        self.play(label2.animate.next_to(label1, RIGHT).shift(LEFT*0.2))
        self.play(label3.animate.next_to(label2, RIGHT).shift(LEFT*0.2))
        self.wait(0.5)

        numerator_group = VGroup(label1, label2, label3)

        answer = MathTex(r"\frac{n(n+1)(2n+1)}{}", font_size = 30).next_to(sum_series).shift(UP*0.2)

        self.play(ReplacementTransform(numerator_group, answer))
        self.wait(0.5)

        self.play(FadeOut(series_label_2[0][1:]))
        self.play(series_label_2[0][0].animate.move_to(answer.get_center()).shift(DOWN*0.5).scale(0.75), run_time=2)
        
        self.wait(0.5)

        answer_group = VGroup(answer, series_label_2[0][0])
        rec = SurroundingRectangle(answer_group, color=YELLOW)

        self.play(Create(rec), answer_group.animate.set_fill(YELLOW), run_time=2)
        self.wait(2)
