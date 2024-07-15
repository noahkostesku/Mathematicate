from manim import *
import numpy as np

class VectorProjection(Scene): 
    def construct(self):

        problem_text1 = Text("Find the area of triangle formed by vector", font_size=25)
        u_vector = MathTex(r"u=\binom{1}{5}", font_size=33).next_to(problem_text1, RIGHT)
        problem_text2 = Text("and its projection onto vector", font_size=25)
        v_vector = MathTex(r"v=\binom{6}{2}", font_size=33).next_to(problem_text2, RIGHT)

        problem_group1 = VGroup(problem_text1, u_vector)
        problem_group2 = VGroup(problem_text2, v_vector)

        problem_group3 = VGroup(problem_group1, problem_group2).arrange(DOWN, buff=0)
        self.play(Write(problem_group3), run_time=3)
        self.wait(2)
        self.play(problem_group3.animate.to_edge(UP))

        plane = NumberPlane(
            x_range = [-1,7,1],
            y_range = [-1,6,1],
            background_line_style={
                "stroke_opacity":0.5
            }
        ).scale(0.6).shift(LEFT*3+DOWN)

        self.play(Create(plane), run_time=3, lag_ratio=0.5)

        #label grid
        u_coords = np.array([2, 5])
        v_coords = np.array([6, 2])
        u_point = plane.c2p(*u_coords)
        v_point = plane.c2p(*v_coords)
        origin_point = plane.c2p(0, 0)

        # Create arrows for the vectors
        dot = Dot(origin_point, color=RED_B)
        arrow_u = Arrow(origin_point, u_point, color=RED_B, buff=0)
        arrow_v = Arrow(origin_point, v_point, color=RED_B, buff=0)
        u_text = MathTex(r"(2,5)", font_size=30).next_to(arrow_u.get_end(), UP)
        v_text = MathTex(r"(6,2)", font_size=30).next_to(arrow_v.get_end(), RIGHT)
        u_label = MathTex(r"u", font_size=30).next_to(arrow_u.get_center(), LEFT, buff=0.2)
        v_label = MathTex(r"v", font_size=30).next_to(arrow_v.get_center(), DOWN*0.2+RIGHT*4, buff=0.2)

        self.play(
            Succession(
                Create(dot),
                GrowArrow(arrow_u),
                Write(u_label),
                Write(u_text),
                GrowArrow(arrow_v),
                Write(v_label),
                Write(v_text)
            )
        )

        self.wait(1)

        # Calculate the projection of u onto v
        tri_numerator = np.dot(u_coords, v_coords)
        tri_denominator = np.linalg.norm(v_coords) ** 2
        tri_scaler = tri_numerator / tri_denominator
        proj_u_v_coords = tri_scaler * v_coords
        proj_u_v_point = plane.c2p(*proj_u_v_coords)
        arrow_proj = Arrow(origin_point, proj_u_v_point, buff=0, color=BLUE_B)
        proj_text = MathTex(r"\text{proj}_{\mathbf{v}}(\mathbf{u})", font_size=30).next_to(arrow_proj, DOWN, buff=0)

        # Line for right triangle
        line = DashedLine(u_point, proj_u_v_point, buff=0, color=RED_B)
        right_angle = RightAngle(arrow_v, line, length=0.4, color=RED_B, quadrant=(-1, -1))

        self.play(
            Succession(
                Create(line),
                Create(right_angle),
            )
            
        )
        self.wait(1)

        arrow_u_copy = arrow_u.copy()
        triangle = Polygon(origin_point, u_point, proj_u_v_point, fill_color=BLUE_B, fill_opacity=0.5, stroke_opacity=0)
        triangle_copy = triangle.copy()

        self.play(
            Succession(
                Transform(arrow_u_copy, arrow_proj),
                Write(proj_text),
                FadeIn(triangle),
                run_time=4
            )
        )
        self.wait(2)

        self.play(triangle_copy.animate.rotate(-PI/10).move_to(ORIGIN+RIGHT*3), run_time=2)
        self.wait(1)

        pythag_text = Text("Use Pythagorean theorem to find the triangle's height", font_size=20).next_to(triangle_copy.get_center()).shift(DOWN*2+LEFT*3)

        self.play(Write(pythag_text))
        self.wait(1)
        self.play(Unwrite(pythag_text))

        u_label_copy = u_label.copy().move_to(triangle_copy.get_left()).shift(RIGHT*0.8)
        proj_label_copy = proj_text.copy().move_to(triangle_copy.get_bottom()).shift(DOWN*0.3)

        self.play(Write(u_label_copy), Write(proj_label_copy))
        self.wait(1)

        normalize_text = Text("Normalize each side to get its length", font_size=25).next_to(triangle_copy.get_center()).shift(DOWN*3+LEFT*3)

        self.play(Write(normalize_text))
        self.wait(1)

        u_transform = MathTex(r"||{\mathbf{u}}||", font_size=30).move_to(triangle_copy.get_left()).shift(RIGHT*0.6)
        proj_u_transform = MathTex(r"||\text{proj}_{\mathbf{v}}(\mathbf{u})||", font_size=30).move_to(triangle_copy.get_bottom()).shift(DOWN*0.3)

        self.play(ReplacementTransform(u_label_copy, u_transform),
                  ReplacementTransform(proj_label_copy, proj_u_transform)
        )
        self.wait(0.5)
        


        self.play(Unwrite(normalize_text))

        pythag_theorem = MathTex(r"a^2+b^2=c^2", font_size=30).next_to(triangle_copy.get_bottom()).shift(DOWN*1.5+LEFT)
        pythag_theorem2 = MathTex(r"b^2=c^2-a^2", font_size=30).next_to(triangle_copy.get_bottom()).shift(DOWN*1.5+LEFT)
        formula_one = MathTex(r"b=||u-\text{proj}_{\mathbf{v}}(\mathbf{u})||", font_size=30).next_to(triangle_copy.get_bottom()).shift(DOWN*1.5+LEFT)

        self.play(Write(pythag_theorem))
        self.wait(0.5)
        self.play(ReplacementTransform(pythag_theorem, pythag_theorem2))
        self.wait(0.5)
        self.play(ReplacementTransform(pythag_theorem2, formula_one))
        self.wait(0.5)
        self.play(FadeOut(formula_one[0][0:2]),
                  formula_one[0][2:].animate.move_to(triangle_copy.get_right()).shift(RIGHT*1.1)
        )
        
        self.wait(2)

        tri_area = Text("The area of a triangle is", font_size=22).next_to(triangle_copy.get_center()).shift(DOWN*3+LEFT*3)
        tri_formula = MathTex(r"A=\frac{bh}{2}", font_size=30).next_to(tri_area, RIGHT)
        tri_group = VGroup(tri_area, tri_formula)

        self.play(Write(tri_group))
        self.wait(0.5)
        self.play(Unwrite(tri_area))
        self.play(tri_formula.animate.shift(LEFT*1.2))
        self.wait(1)

        self.play(Circumscribe(tri_formula[0][2:4], color = WHITE),
                  Circumscribe(formula_one[0][2:], color= WHITE),
                  Circumscribe(proj_u_transform, color=WHITE),
                  run_time=2
                  )
        self.wait(0.5)

        area_replace1 = MathTex(r"A = \frac{||\text{proj}_{\mathbf{v}}(\mathbf{u})|| \cdot ||\mathbf{u} - \text{proj}_{\mathbf{v}}(\mathbf{u})||}{2}",
                        font_size=30).next_to(triangle_copy.get_center()).shift(DOWN*3 + LEFT*3)

        
        self.play(ReplacementTransform(tri_formula, area_replace1))
        self.wait(0.5)

        area_replace2 = MathTex(r"A=\frac{||\frac{(u \cdot v)}{||v||^2}v|| \cdot ||\frac{(u\cdot v)}{||v||^2}v||}{2}",
                        font_size=35).next_to(triangle_copy.get_center()).shift(DOWN*3+LEFT*2)
        area_replace3 = MathTex(r"A=\frac{||\frac{22}{40}\binom{6}{2}|| \cdot ||\binom{2}{5}-\frac{22}{40}\binom{6}{2}||}{2}",
                        font_size=35).next_to(triangle_copy.get_center()).shift(DOWN*3+LEFT*2)
        area_replace4 = MathTex(r"A=\frac{||\frac{11}{20}\binom{6}{2}|| \cdot ||\binom{2}{5}-\frac{11}{20}\binom{6}{2}||}{2}",
                        font_size=35).next_to(triangle_copy.get_center()).shift(DOWN*3+LEFT*2)
        area_replace5 = MathTex(r"A=\frac{||\binom{\frac{33}{10}}{\frac{11}{10}}|| \cdot ||\binom{\frac{20}{10}}{\frac{50}{10}}-\binom{\frac{33}{10}}{\frac{11}{10}}||}{2}",
                        font_size=35).next_to(triangle_copy.get_center()).shift(DOWN*3+LEFT*2)
        area_replace6 = MathTex(r"A=\frac{\sqrt{(\frac{33}{10})^2+(\frac{11}{10})^2} \cdot \sqrt{(\frac{-13}{10})^2+(\frac{39}{10})^2}}{2}",
                        font_size=35).next_to(triangle_copy.get_center()).shift(DOWN*3+LEFT*3)
        area_replace7 = MathTex(r"A=\frac{\frac{11\sqrt{10}}{10} \cdot \frac{13\sqrt{10}}{10}}{2} ",
                        font_size=30).next_to(triangle_copy.get_center()).shift(DOWN*3+LEFT*2)
        area_replace8 = MathTex(r"A=\frac{\frac{143}{10}}{2} ",
                        font_size=35).next_to(triangle_copy.get_center()).shift(DOWN*3+LEFT)
        area_replace9 = MathTex(r"A=\frac{143}{20} ",
                        font_size=35).next_to(triangle_copy.get_center()).shift(DOWN*3+LEFT)
        
        self.play(ReplacementTransform(area_replace1, area_replace2))
        self.wait(1)
        self.play(ReplacementTransform(area_replace2, area_replace3))
        self.play(TransformMatchingShapes(area_replace3, area_replace4))
        self.wait(1)
        self.play(ReplacementTransform(area_replace4, area_replace5))
        self.wait(0.5)
        self.play(ReplacementTransform(area_replace5, area_replace6))
        self.wait(0.5)
        self.play(ReplacementTransform(area_replace6, area_replace7))
        self.wait(0.5)
        self.play(TransformMatchingShapes(area_replace7, area_replace8))
        self.wait(0.5)
        self.play(TransformMatchingShapes(area_replace8, area_replace9))

        sr = SurroundingRectangle(area_replace9, YELLOW)

        self.play(area_replace9.animate.set_fill(YELLOW),
                  Create(sr))
        self.wait(2)