from manim import *

class PythagoreanProof(Scene):
    def construct(self):

        righttri = Polygon([0,2.5,0], [0,0,0], [1.5,0,0], stroke_color = TEAL_C).shift(LEFT*4.5+DOWN*1)

        self.play(Create(righttri, run_time=3))
        self.play(righttri.animate.set_fill(TEAL_C, opacity=0.3), run_time=1.5)
        self.wait(1)

        a_lab = MathTex(r"a", font_size=30).next_to(righttri, LEFT)
        b_lab = MathTex(r"b", font_size=30).next_to(righttri, DOWN)
        c_lab = MathTex(r"c", font_size=30).next_to(righttri, RIGHT).shift(LEFT*0.8)

        self.play(Write(a_lab), Write(b_lab), Write(c_lab))

        tri_group1 =VGroup(righttri, a_lab, b_lab, c_lab)
        copytri1 = righttri.copy().shift(DOWN*1.5+LEFT*1.5)
        copytri2 = righttri.copy().shift(DOWN*1.5+LEFT*1.5)
        copytri3 = righttri.copy().shift(DOWN*1.5+LEFT*1.5)

        a_lab_copy1 = a_lab.copy().shift(DOWN*1.5+LEFT*1.5)
        b_lab_copy1 = b_lab.copy().shift(DOWN*1.5+LEFT*1.5)
        c_lab_copy1 = c_lab.copy().shift(DOWN*1.5+LEFT*1.5)
        a_lab_copy2= a_lab.copy().shift(DOWN*1.5+LEFT*1.5)
        b_lab_copy2 = b_lab.copy().shift(DOWN*1.5+LEFT*1.5)
        c_lab_copy2 = c_lab.copy().shift(DOWN*1.5+LEFT*1.5)
        a_lab_copy3 = a_lab.copy().shift(DOWN*1.5+LEFT*1.5)
        b_lab_copy3 = b_lab.copy().shift(DOWN*1.5+LEFT*1.5)
        c_lab_copy3 = c_lab.copy().shift(DOWN*1.5+LEFT*1.5)

        tri_group2 = VGroup(copytri1, a_lab_copy1, b_lab_copy1, c_lab_copy1)
        tri_group3 = VGroup(copytri2, a_lab_copy2, b_lab_copy2, c_lab_copy2)
        tri_group4 = VGroup(copytri3, a_lab_copy3, b_lab_copy3, c_lab_copy3)

        self.play(tri_group1.animate.shift(DOWN*1.5+LEFT*1.5))
        self.wait(0.5)
        self.play(copytri1.animate.shift(UP*2.7+RIGHT*0.5), run_time=2)
        self.play(Rotate(copytri1, -PI/2))
        self.play(
            a_lab_copy1.animate.next_to(copytri1,UP),
            b_lab_copy1.animate.next_to(copytri1, LEFT),
            c_lab_copy1.animate.next_to(copytri1, DOWN).shift(UP*0.8),
            run_time=3
            )

        self.play(copytri2.animate.shift(RIGHT*2.7+DOWN*0.5), run_time=2)
        self.play(Rotate(copytri2, PI/2))
        self.play(
            a_lab_copy2.animate.next_to(copytri2, DOWN),
            b_lab_copy2.animate.next_to(copytri2, RIGHT),
            c_lab_copy2.animate.next_to(copytri2, UP).shift(DOWN*0.8),
            run_time=3
            )
        self.play(copytri3.animate.shift(UP*2.2+RIGHT*3.2), run_time=2)
        self.play(Rotate(copytri3, PI))
        self.play(
            a_lab_copy3.animate.next_to(copytri3, RIGHT),
            b_lab_copy3.animate.next_to(copytri3, UP),
            c_lab_copy3.animate.next_to(copytri3, LEFT).shift(RIGHT*0.8),
            run_time=3
            )
        self.wait(1)
        
        square = Square(side_length=4).shift(RIGHT*3)

        self.play(FadeIn(square), run_time=2)

        copytri1_target = square.get_corner(UL)+(DOWN*0.55)+(RIGHT*1.05)
        copytri2_target = square.get_corner(DR)+(UP*0.55)+(LEFT*1.05)
        copytri3_target = square.get_corner(UR)+(DOWN*1.03)+(LEFT*0.55)
        tri_group_target = square.get_corner(DL)+(UP*1.05)+(RIGHT*0.55)

        self.play(
            tri_group1.animate.move_to(tri_group_target),
            tri_group2.animate.move_to(copytri1_target),
            tri_group3.animate.move_to(copytri2_target),
            tri_group4.animate.move_to(copytri3_target),
            run_time=3
        )
        self.wait(2)


        
        c_side1 = Line(righttri.get_vertices()[0], righttri.get_vertices()[2], color=LIGHT_PINK)
        c_side2 = Line(copytri2.get_vertices()[0], copytri2.get_vertices()[2], color=LIGHT_PINK)
        c_side3 = Line(copytri3.get_vertices()[0], copytri3.get_vertices()[2], color=LIGHT_PINK)
        c_side4 = Line(copytri1.get_vertices()[0], copytri1.get_vertices()[2], color=LIGHT_PINK)
        
        # Find the Intersection for labels moving to each respective triangle
        def find_intersection(line1, line2):
            p1, p2 = line1.get_start_and_end()
            p3, p4 = line2.get_start_and_end()
            
            x1, y1 = p1[:2]
            x2, y2 = p2[:2]
            x3, y3 = p3[:2]
            x4, y4 = p4[:2]

            a1 = y2 - y1
            b1 = x1 - x2
            c1 = a1 * x1 + b1 * y1

            a2 = y4 - y3
            b2 = x3 - x4
            c2 = a2 * x3 + b2 * y3

            determinant = a1 * b2 - a2 * b1

            x = (b2 * c1 - b1 * c2) / determinant
            y = (a1 * c2 - a2 * c1) / determinant
            return np.array([x, y, 0])
        
        # Calculate intersection points
        intersections = [
            find_intersection(c_side1, c_side2),
            find_intersection(c_side2, c_side3),
            find_intersection(c_side3, c_side4),
            find_intersection(c_side4, c_side1),
        ]
        
        # Create and shade the polygon
        shaded_area = Polygon(*intersections, color=LIGHT_PINK)
        shaded_area.set_fill(LIGHT_PINK, opacity=0.3)
        
        
        # Create the shaded polygon
        self.play(
            Succession(
                Write(c_side1),
                Write(c_side2),
                Write(c_side3),
                Write(c_side4), 
                FadeIn(shaded_area)      
            )
        )
        self.wait(1)
        self.play(FadeOut(c_lab_copy1, c_lab_copy3))

        self.play(
            c_lab.animate.move_to(shaded_area.get_center()).shift(LEFT*0.2),
            c_lab_copy2.animate.move_to(shaded_area.get_center()).shift(RIGHT*0.2)
            )
        
        c_midpoint = (c_lab.get_center() + c_lab_copy2.get_center()) / 2

        c_form = MathTex(r"\cdot", font_size = 30).move_to(c_midpoint)
        c_form2 = MathTex(r"c^2", font_size = 30).move_to(shaded_area.get_center())
        c_group = VGroup(c_lab, c_lab_copy2, c_form)

        self.play(FadeIn(c_form), run_time=1.5)
        self.play(TransformMatchingShapes(c_group, c_form2))
        self.wait(1)
        self.play(FadeOut(a_lab_copy1, a_lab_copy3, b_lab_copy3, b_lab_copy2))
        self.wait(1)
        
        sq_bottom_center = (square.get_corner(DL) + square.get_corner(DR)) / 2
        sq_left_center = (square.get_corner(UL) + square.get_corner(DL)) / 2

        plus_sign1 = MathTex(r"+", font_size=30).move_to(sq_bottom_center+DOWN*0.2)
        plus_sign2 = MathTex(r"+", font_size=30).move_to(sq_left_center+LEFT*0.2)

        length_group = VGroup(b_lab, a_lab_copy2, plus_sign1)
        width_group  = VGroup(a_lab, b_lab_copy1, plus_sign2)

        sq_form1 = MathTex(r"(a+b)", font_size=30).move_to(sq_left_center).shift(LEFT*0.6)
        sq_form2 = MathTex(r"(a+b)", font_size=30).move_to(sq_bottom_center).shift(DOWN*0.3)
        
        self.play(
            b_lab_copy1.animate.move_to(sq_left_center).shift(UP*0.3+LEFT*0.2),
            a_lab.animate.move_to(sq_left_center).shift(DOWN*0.3+LEFT*0.2),
            b_lab.animate.move_to(sq_bottom_center).shift(LEFT*0.3+DOWN*0.2),
            a_lab_copy2.animate.move_to(sq_bottom_center).shift(RIGHT*0.3+DOWN*0.2)
        )
        self.play(FadeIn(plus_sign1, plus_sign2))
        self.play(
            TransformMatchingShapes(length_group, sq_form2),
            TransformMatchingShapes(width_group, sq_form1)
        )
        self.wait(1)

        case1 = Text("Proof", font_size = 30).shift(UP*2+LEFT*3)
        self.play(Write(case1))
        self.wait(1)

        shaded_with_lines = VGroup(c_side1, c_side2, c_side3, c_side4, shaded_area)
        shaded_copy = shaded_with_lines.copy()
        square_copy = square.copy()
        square_copy.set_fill(PURE_BLUE, opacity=0.3)
        square_copy.set_stroke(PURE_BLUE)

        equals = MathTex(r'=', font_size = 30).next_to(case1, DOWN*9+LEFT*4)
        plus4 = MathTex(r'+4', font_size=30).next_to(case1, DOWN*9+RIGHT*1)

        sign_midpoint = (equals.get_center() + plus4.get_center() / 2)

        righttri_copy = righttri.copy()
        copytri1_copy = copytri1.copy()

        self.play(Write(equals), Write(plus4), run_time=3)
        self.wait(1)
        self.play(square_copy.animate.next_to(equals).shift(LEFT*3.5).scale(0.4), run_time=3)
        self.wait(1)
        self.play(shaded_copy.animate.next_to(sign_midpoint).shift(UP*0.2).scale(0.4), run_time=3)
        self.wait(1)
        self.play(righttri_copy.animate.next_to(plus4).shift(LEFT*0.3).scale(0.4), run_time=3)
        self.wait(1)

        atri = a_lab.shift(DOWN*0.5)
        btri = b_lab.shift(LEFT)
        self.play(FadeIn(atri, btri))
        self.wait(1)

        square_lengths = VGroup(sq_form1, sq_form2)
        tri_lengths = VGroup(atri, btri)

        div2 = MathTex(r"\frac{}{2}", font_size=30).next_to(righttri_copy.get_corner(DL)).shift(DOWN*0.7)

        self.play(
            Succession(
                sq_form1.animate.move_to(square_copy.get_corner(DL)).shift(DOWN*0.5+RIGHT*0.3)),
                sq_form2.animate.move_to(square_copy.get_corner(DR)).shift(DOWN*0.5+LEFT*0.3),
                run_time=2
                )
        self.wait(2)
        self.play(c_form2.animate.move_to(shaded_copy.get_center()).shift(DOWN*1.2), run_time=2)
        self.wait(2)

        equals_copy = equals.copy()
        bigsq_smallsq_mid = (square_copy.get_corner(DR) + shaded_copy.get_center()) / 2
        self.play(equals_copy.animate.move_to(bigsq_smallsq_mid).shift(DOWN*0.9), run_time=2)

        self.play(Write(div2), run_time=2)

        self.play(
            Succession(
                atri.animate.move_to(div2.get_corner(UL)).shift(UP*0.2)),
                btri.animate.move_to(div2.get_corner(UR)).shift(UP*0.2),
            )
        self.wait(1)

        
        four_copy = plus4[0][1].copy()
        plus_copy = plus4[0][0].copy()
        sq_tri_mid = (shaded_copy.get_center() + righttri_copy.get_corner(DL)) / 2
        ab2_group = VGroup(atri, btri, div2)
        brackets = MathTex(r"(\frac{ab}{2})", font_size=30).move_to(ab2_group.get_center())
        tri_form = MathTex(r"2ab", font_size=30).move_to(ab2_group.get_center()).shift(DOWN*0.15)

        self.play(TransformMatchingShapes(ab2_group, brackets))
        self.play(four_copy.animate.next_to(brackets, LEFT*0.6), run_time=2)
        self.play(TransformMatchingShapes(brackets, tri_form), FadeOut(four_copy))
        self.wait(2)
        self.play(plus_copy.animate.move_to(sq_tri_mid).shift(DOWN*0.95+RIGHT*0.2), run_time=2)
        self.wait(1)

        sq_group = VGroup(sq_form1, sq_form2)
        a_b_sq = MathTex(r"a^2+2ab+b^2", font_size=30).move_to(sq_group.get_center())

        self.play(TransformMatchingShapes(sq_group, a_b_sq), run_time=2)
        self.wait(1)

        second_eq_copy = equals_copy.copy()
        second_plus_copy = plus_copy.copy()

        self.play(
            second_eq_copy.animate.shift(DOWN*0.8+RIGHT*0.5),
            second_plus_copy.animate.shift(DOWN*0.85+LEFT*0.5),
            run_time=2
        )
        self.wait(2)

        a_b_sq_copy = a_b_sq.copy()
        c_form2_copy = c_form2.copy()
        tri_form_copy = tri_form.copy()


        eq_plus_mid = (second_eq_copy.get_center() + second_plus_copy.get_center()) / 2

        self.play(
            a_b_sq_copy.animate.next_to(second_eq_copy, LEFT),
            c_form2_copy.animate.move_to(eq_plus_mid),
            tri_form_copy.animate.next_to(second_plus_copy, RIGHT),
            run_time = 2
        )
        self.wait(1)

        final_group = VGroup(a_b_sq_copy, second_eq_copy,  c_form2_copy, second_plus_copy, tri_form_copy)
        answer = MathTex(r"{{a^2}}+{{2ab}}-{{2ab}}+{{b^2}}={{c^2}}", font_size=30).move_to(final_group.get_center())
        answer2 = MathTex(r"{{a^2}}+{{b^2}}={{c^2}}", font_size = 30, color = YELLOW).move_to(answer.get_center())
        answer_rec = SurroundingRectangle(answer2, color=YELLOW)

        self.play(TransformMatchingShapes(final_group, answer), run_time=2)
        self.wait(1)
        self.play(TransformMatchingShapes(answer, answer2, run_time=2))
        self.wait(0.5)
        self.play(Create(answer_rec), run_time=2)
        self.wait(3)
        



        







        

        
        

        


        






        

                



        

        
        
