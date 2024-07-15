from manim import *
import numpy as np
from manim import BS381

class RoseCurves(Scene):
    def construct(self):

        title = Text("Rose Curves in Polar Coordinates", font_size=30).shift(UP+LEFT*3)
        rose_formula_sin = MathTex(r"r=a\sin(b\theta)", font_size=40).next_to(title, RIGHT)
        or_text = Text("or", font_size=30).next_to(rose_formula_sin, RIGHT)
        rose_formula_cos = MathTex(r"r=a\cos(b\theta)", font_size=40).next_to(or_text)
        title_group = VGroup(title, rose_formula_sin, or_text, rose_formula_cos)

        self.play(Write(title_group), run_time=2)
        self.wait(2)
        self.play(Unwrite(title_group))

        heading = Text("How do you determine the graph of a rose curve?", font_size=40).shift(UP)

        self.play(Write(heading))
        self.wait(1)
        self.play(Unwrite(heading))
        

        first_graph_title = MathTex(r"r = 2cos(3\theta)", font_size=40).shift(UP)
        self.play(Write(first_graph_title))
        self.play(first_graph_title.animate.shift(UP*2))

        #value tracker to dynamically update value of point on curve
        tracker = ValueTracker(0.00001)
        plane1 = PolarPlane(radius_max=3).add_coordinates().shift(LEFT*2.5).scale(0.75)

        #continuously update function based on function below
        graph1 = always_redraw(
           lambda : ParametricFunction(
               lambda t : plane1.polar_to_point(2*np.cos(3*t), t), #(r, \theta)
               t_range = [0, tracker.get_value()], color=TEAL)
           )
       
        #animate the dot to be on the end of the simultaneusly updating graph
        dot1 = always_redraw(lambda : Dot(fill_color=TEAL).scale(0.6).move_to(graph1.get_end()))

        self.play(LaggedStart(Write(plane1),run_time=3,lag_ratio=0.5),
                  first_graph_title.animate.next_to(plane1, UP, buff=0.5))

        self.add(graph1, dot1)
        
        #animate the value tracker in motion to draw the graph
        self.play(tracker.animate.set_value(PI), run_time=5, rate_func=linear)
        self.wait(2)

        #brace for the radius of a petal
        start_point = np.array([-2.5, 0.3, 0])
        end_point = np.array([-1, 0.3, 0])
        brace1 = Brace(Line(start_point, end_point), direction=UP)
        two_formula = first_graph_title[0][2].copy()

        self.play(GrowFromCenter(brace1))
        self.play(two_formula.animate.next_to(brace1, UP))
        self.wait(0.5)

        rose_cos = MathTex(r"r=a\cos(b\theta)", font_size=40).next_to(first_graph_title, RIGHT*14)
        self.play(Write(rose_cos))
        self.play(FadeOut(brace1))
        
        radius_text = Text("radius =", font_size=30).next_to(rose_cos, DOWN*2).align_to(rose_cos, LEFT)
        self.play(Write(radius_text), two_formula.animate.next_to(radius_text, RIGHT*0.9))
                  
        self.wait(0.5)

        self.play(first_graph_title[0][2].animate.set_fill(BS381.CURRANT_RED),
                  rose_cos[0][2].animate.set_fill(BS381.CURRANT_RED),
                  two_formula.animate.set_fill(BS381.CURRANT_RED))
        self.wait(1)

        radius_group = VGroup(radius_text, two_formula)
        a_text = MathTex(r"a", font_size=40).next_to(radius_text, RIGHT).set_fill(BS381.CURRANT_RED)
        a_group = VGroup(radius_text, a_text)

        self.play(ReplacementTransform(radius_group, a_group))
        
        self.wait(1)

        # a = amplitude, b = frequency
        a = 2 
        b = 3  
        # Function to calculate the points of the petal
        def petal_points(a, b):
            num_points = 100
            points = []
            for i in range(num_points):
                theta = i * (2 * np.pi / num_points)
                r = a * np.cos(b * theta)
                point = plane1.polar_to_point(r, theta)
                points.append(point)
            return points

        # Calculate the points of the petal
        petal_points_0 = petal_points(a, b)

        # Create a closed path from the points
        petal_path = VMobject()
        petal_path.set_points_smoothly(petal_points_0)

        # Create a polygon to represent the area under the curve
        area_under_curve = Polygon(plane1.coords_to_point(0, 0), *petal_points_0, color=BLUE, fill_opacity=1)

        b_rule1 = Text("When", font_size=30).next_to(radius_text, DOWN*2).align_to(rose_cos, LEFT)
        b_text = MathTex(r"b", font_size=40).next_to(b_rule1, RIGHT)
        b_rule1_contd = Text("is odd, ", font_size=30).next_to(b_text, RIGHT)
        b_rule1_contd2 = Text("the graph has b petals", font_size=30).next_to(b_rule1, DOWN).align_to(rose_cos, LEFT)
        
        b_group1 = VGroup(b_rule1, b_text, b_rule1_contd, b_rule1_contd2)

        self.play(Write(b_group1))
        self.wait(0.5)
        self.play(FadeIn(area_under_curve), run_time=2)

        area1 = area_under_curve.copy()

        self.play(area1.animate.next_to(rose_cos.get_center()).shift(DOWN*4.5+LEFT*0.5)
                  ,run_time=2)
        self.wait(0.5)
        self.play(FadeOut(b_rule1, b_rule1_contd,b_rule1_contd2))
        self.play(b_text.animate.shift(LEFT*1.2))
        
        equals3 = MathTex(r"=3", font_size=40).next_to(b_text, RIGHT)
        

        self.play(Write(equals3))
        self.play(first_graph_title[0][7].animate.set_fill(TEAL),
                  equals3[0][1].animate.set_fill(TEAL),
                  rose_cos[0][7].animate.set_fill(TEAL)
                 )
        self.wait(0.5)

        petals = Text("petals =", font_size=30).next_to(radius_text, DOWN*2).align_to(rose_cos, LEFT)
        petal_r = MathTex(r"3", font_size=40).next_to(petals, RIGHT)
        petal_r.set_fill(TEAL)
        petal_group = VGroup(petals, petal_r)
        equal_group = VGroup(b_text, equals3)

        self.play(ReplacementTransform(equal_group, petal_group))
        self.wait(1.5)
        self.play(FadeOut(area1, petal_group, radius_group, rose_cos, a_text))
        self.play(FadeOut(area_under_curve), run_time=2)
        
        angles = [0, 2 * np.pi / 3, 4 * np.pi / 3]
        radius1 = 3

        #Function to create dashed lines on polar plane
        def create_dashed_line(angle):
            end_point = plane1.polar_to_point(radius1, angle)
            return DashedLine(
                start=plane1.polar_to_point(0, 0),
                end=end_point,
                color=WHITE,
                dash_length=0.1
            )

        dashed_lines = [create_dashed_line(angle) for angle in angles]

        for line in dashed_lines:
            self.play(Write(line))

        self.wait(0.5)

        cos_explanation = Text("Cosine graphs are"
                               ,font_size=30).next_to(plane1, RIGHT*4)
        cos_explanation_contd = Text("symmetric over the polar axis",font_size=30).next_to(cos_explanation, DOWN)
        cos_group1 = VGroup(cos_explanation, cos_explanation_contd).arrange(DOWN).shift(RIGHT*3)

        self.play(Write(cos_group1))
        self.wait(0.5)

        cos_explanation2 = Text("Each petal occurs at", font_size=30)
        cos_explanation3 = MathTex(r"\frac{2\pi}{b}", font_size=40).next_to(cos_explanation2, RIGHT)
        cos_explanation4 = Text("from the previous petal", font_size=30)

        cos_expl_group = VGroup(cos_explanation2, cos_explanation3)
        cos_expl_group2 = VGroup(cos_expl_group, cos_explanation4).arrange(DOWN).shift(RIGHT*3)
        
        self.play(Unwrite(cos_group1))
        self.play(Write(cos_expl_group2))


        #polygon area for the polar plane
        sector1 = Sector(
            outer_radius=radius1,
            start_angle=0,
            angle=2 * np.pi / 3,
            color=TEAL,
            stroke_color=WHITE,
            fill_opacity=0.7,
            stroke_width=3
        ).scale(0.75).shift(LEFT*2.7+DOWN*0.4)

        self.play(FadeIn(sector1), run_time=2)
        self.wait(0.5)

        text_sector_label = MathTex(r"\frac{2\pi}{3}", font_size=30).move_to(sector1.get_center())
        self.play(FadeIn(text_sector_label))
        self.wait(0.5)
        
        self.play(Circumscribe(text_sector_label, color=WHITE),
                  Circumscribe(cos_explanation3, color=WHITE),
                  run_time=2)
        self.wait(2)
        self.play(Unwrite(cos_expl_group2))

        sector2 = Sector(
            outer_radius=radius1,
            start_angle=2 * np.pi / 3,
            angle=2 * np.pi / 3,
            color=TEAL,
            stroke_color=WHITE,
            fill_opacity=0.7,
            stroke_width=3
        ).scale(0.75).shift(LEFT*2.1)

        sector3 = Sector(
            outer_radius=radius1,
            start_angle=4 * np.pi / 3,
            angle=2 * np.pi / 3,
            color=TEAL,
            stroke_color=WHITE,
            fill_opacity=0.7,
            stroke_width=3
        ).scale(0.75).shift(LEFT*2.7+UP*0.4)

        text_sector_label2 = text_sector_label.copy().move_to(sector2.get_center())
        text_sector_label3 = text_sector_label.copy().move_to(sector3.get_center())

        self.play(
            Succession(
                FadeIn(sector2),
                Write(text_sector_label2),
                FadeIn(sector3),
                Write(text_sector_label3),
            )
        )
        self.wait(1.5)
        self.play(FadeOut(text_sector_label, text_sector_label2, text_sector_label3,
                          sector1, sector2, sector3))
        
        for line in dashed_lines:
            self.play(Unwrite(line))

        self.wait(0.5)
        
        self.play(FadeOut(plane1, graph1, first_graph_title,dot1))
        self.wait(1)

        ### sin graph ###

        second_graph_title = MathTex(r"r = 2\sin(2\theta)", font_size=40).to_edge(UP)
        self.play(Write(second_graph_title))

        tracker2 = ValueTracker(0.00001)
        plane2 = PolarPlane(radius_max=3).add_coordinates().shift(LEFT*4).scale(0.75)

        graph2 = always_redraw(
           lambda : ParametricFunction(
               lambda t : plane2.polar_to_point(2*np.sin(2*t), t), #(r, \theta)
               t_range = [0, tracker2.get_value()], color=TEAL)
           )
       
       
        dot2 = always_redraw(lambda : Dot(fill_color=TEAL).scale(0.6).move_to(graph2.get_end()))

        self.play(LaggedStart(Write(plane2),run_time=3,lag_ratio=0.5))

        sin_text = Text("Consider the similarities to", font_size=30)
        sin_text2 = Text("the cartesian coordinate graph", font_size=30).next_to(sin_text, DOWN)
        sin_group = VGroup(sin_text, sin_text2).arrange(DOWN).shift(RIGHT*2)

        self.play(Write(sin_group))
        self.wait(0.5)
        self.play(Unwrite(sin_group))

        axes = Axes(x_range=[0,7,1],
                    x_length=6,
                    y_range=[-3,3,1],
                    y_length=3).shift(RIGHT*3.5)
        
        axes.add_coordinates()
        graph3 = always_redraw(lambda :
                               axes.plot(
                                   lambda l : 2*np.sin(2*l),
                                   x_range=[0, tracker2.get_value()], color=TEAL)
                               ).scale(0.75).shift(RIGHT*3.5)
        dot3 = always_redraw(lambda : Dot(fill_color = TEAL, fill_opacity = 0.8).scale(0.6).move_to(graph3.get_end()))
        
        self.play(Create(axes), lag_ratio=0.5, run_time=2)
        self.add(graph2, graph3, dot2, dot3)
        self.wait(0.5)

        origin_text = Text("Notice in both graphs that the horizontal axis is passed through at the same time", font_size=20).to_edge(DOWN)
        self.play(Write(origin_text))
        self.play(tracker2.animate.set_value(2*PI), run_time=10,rate_func=linear)
        self.play(Unwrite(origin_text))
        self.wait(1)

        angles2 = [np.pi/4, 3*np.pi/4, 5*np.pi/4, 7*np.pi/4]
        radius2 = 3

        def create_polar_dashed_line(angle):
            end_point = plane2.polar_to_point(radius2, angle)
            return DashedLine(
                start=plane2.polar_to_point(0, 0),
                end=end_point,
                color=WHITE,
                dash_length=0.1
            )

        #Function that creates dashed lines for the Cartesian graph
        def create_cartesian_dashed_line(angle):
            return DashedLine(
                start=axes.c2p(angle, -3),
                end=axes.c2p(angle, 3),
                color=WHITE,
                dash_length=0.1
            )

        polar_dashed_lines = [create_polar_dashed_line(angle) for angle in angles2]
        cartesian_dashed_lines = [create_cartesian_dashed_line(angle) for angle in angles2]
        cartesian_labels = [
            MathTex(r"\frac{\pi}{4}", font_size=24),
            MathTex(r"\frac{3\pi}{4}", font_size=24),
            MathTex(r"\frac{5\pi}{4}", font_size=24),
            MathTex(r"\frac{7\pi}{4}", font_size=24)
        ]

        # Position the labels next to the corresponding dashed lines
        for label, angle in zip(cartesian_labels, angles2):
            label.next_to(axes.c2p(angle, 3), UP)

        # Animate both sets of dashed lines and labels simultaneously
        for polar_line, cartesian_line, label in zip(polar_dashed_lines, cartesian_dashed_lines, cartesian_labels):
            self.play(Write(polar_line), Write(cartesian_line), Write(label), run_time=1)
        self.wait(2)
        # Animate both sets of dashed lines and labels simultaneously
        
        cartesian_text = Text("Notice that where a petal reaches its peak", font_size=25)
        cartesian_text2 = Text("its cartesian's equivalent has a", font_size=25)
        cartesian_text3 = Text("a local minimum or maximum", font_size=25)

        cartesian_text_group = VGroup(cartesian_text, cartesian_text2, cartesian_text3).arrange(DOWN).next_to(axes.get_center(), DOWN*7.4)

        self.play(Write(cartesian_text_group), run_time=5)
        self.wait(3)
        self.play(Unwrite(cartesian_text_group))

        petal_text = Text("Note that rose sin graph's petals start at", font_size=25)
        petal_text2 = MathTex(r"\frac{\pi}{2b}", font_size=30).next_to(petal_text)
        petal_text3 = Text("from", font_size=25)
        petal_text4 = MathTex(r"\theta=0", font_size=30).next_to(petal_text3)

        petal_group1 = VGroup(petal_text, petal_text2)
        petal_group2 = VGroup(petal_text3, petal_text4)
        petal_group = VGroup(petal_group1, petal_group2).arrange(DOWN).to_edge(DOWN)

        sector1_sin = Sector(
            outer_radius=radius2,
            start_angle=0,
            angle=np.pi / 4,
            color=TEAL,
            stroke_color=WHITE,
            fill_opacity=0.7,
            stroke_width=3
        ).scale(0.75).shift(LEFT*4.4+DOWN*0.25)

        pi_two_b = MathTex(r"\frac{\pi}{2b}", font_size=30).move_to(sector1_sin.get_center()).shift(DOWN*0.3)

        self.play(
            Succession(
                Write(petal_group),
                FadeIn(sector1_sin),
                Write(pi_two_b)
            )
        )
        self.wait(1)

        pi_two_two = MathTex(r"\frac{\pi}{2(2)}", font_size=30).move_to(sector1_sin.get_center()).shift(DOWN*0.3)
        pi_4 = cartesian_labels[0].copy().move_to(sector1_sin.get_center()).shift(DOWN*0.3)

        self.play(ReplacementTransform(pi_two_b, pi_two_two))
        self.wait(0.5)
        self.play(ReplacementTransform(pi_two_two, pi_4))
        self.wait(2)
        self.play(FadeOut(sector1_sin, pi_4), Unwrite(petal_group))
        self.wait(1)


        #create all 4 parts of circle
        sector2_sin = Sector(
            outer_radius=radius2,
            start_angle=np.pi / 4,
            angle=np.pi / 2,
            color=TEAL,
            stroke_color=WHITE,
            fill_opacity=0.7,
            stroke_width=3
        ).scale(0.75).shift(LEFT*4+DOWN*0.4)

        sector3_sin = Sector(
            outer_radius=radius2,
            start_angle=3*np.pi / 4,
            angle= np.pi / 2,
            color=TEAL,
            stroke_color=WHITE,
            fill_opacity=0.7,
            stroke_width=3
        ).scale(0.75).shift(LEFT*3.6)

        sector4_sin = Sector(
            outer_radius=radius2,
            start_angle=5*np.pi / 4,
            angle= np.pi/2,
            color=TEAL,
            stroke_color=WHITE,
            fill_opacity=0.7,
            stroke_width=3
        ).scale(0.75).shift(LEFT*4+UP*0.4)

        sector5_sin = Sector(
            outer_radius=radius2,
            start_angle=7*np.pi / 4,
            angle= np.pi / 2,
            color=TEAL,
            stroke_color=WHITE,
            fill_opacity=0.7,
            stroke_width=3
        ).scale(0.75).shift(LEFT*4.4+UP*0.02)

        pi_4_1 = pi_4.copy().move_to(sector2_sin.get_center()).scale(1.5)
        pi_4_2 = pi_4.copy().move_to(sector3_sin.get_center()).scale(1.5)
        pi_4_3 = pi_4.copy().move_to(sector4_sin.get_center()).scale(1.5)
        pi_4_4 = pi_4.copy().move_to(sector5_sin.get_center()).scale(1.5)

        self.play(
            Succession(
                FadeIn(sector2_sin),
                Write(pi_4_1),
                FadeIn(sector3_sin),
                Write(pi_4_2),
                FadeIn(sector4_sin),
                Write(pi_4_3),
                FadeIn(sector5_sin),
                Write(pi_4_4)
            )
        )

        self.wait(1)

        self.play(FadeOut(sector2_sin, sector3_sin, sector4_sin, sector5_sin,
                          pi_4_1, pi_4_2, pi_4_3, pi_4_4))
        self.wait(1)

        petal_text_sin_cos = Text("For cosine or sin rose curves, when b is even,", font_size=25)
        petal_text_sin_cos2 = Text("the number of petals is 2b", font_size=25)
        petal_text_sin_cos_group = VGroup(petal_text_sin_cos, petal_text_sin_cos2).arrange(DOWN).to_edge(DOWN)

        a2= 2
        b2 = 2

        def petal_points2(a2, b2):
            num_points = 100
            points = []
            for i in range(num_points):
                theta = i * (2 * np.pi / num_points)
                r = a2 * np.sin(b2 * theta)
                point = plane2.polar_to_point(r, theta)
                points.append(point)
            return points

        petal_points_2 = petal_points2(a2, b2)

        petal_path_2 = VMobject()
        petal_path_2.set_points_smoothly(petal_points_2)
        area_under_curve2 = Polygon(plane2.coords_to_point(0, 0), *petal_points_2, color=BLUE, fill_opacity=1)

        self.play(FadeIn(area_under_curve2), Write(petal_text_sin_cos_group), run_time=2)
        self.wait(2)
        self.play(FadeOut(area_under_curve2), Unwrite(petal_text_sin_cos_group))

        self.wait(2)



       