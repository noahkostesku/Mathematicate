from manim import *

class Trigsub(Scene):
    def construct(self):

        title = Text("Trigonometric Substitution", font_size=50).to_edge(UP).shift(DOWN*0.5)
        self.play(Write(title, run_time = 3))
        self.wait(1)


        integral1 = MathTex(r"\int \frac{x^2}{\sqrt{(36-x^2)}} \, dx", font_size=30).shift(UP)
        integral2 = MathTex(r"\int \frac{1}{(4x^2-16)^{3/2}} \, dx", font_size=30)
        integral3 = MathTex(r"\int \frac{x^3}{\sqrt{(9+x^2)}} \, dx", font_size=30)

        integral_start_group = VGroup(integral1, integral2, integral3).arrange(buff=2.5)
        integral_start_group.to_edge(UP).shift(DOWN*2)

        self.play(
            Succession(
                Write(integral1),
                Write(integral2),
                Write(integral3), runtime=10
            )
        )

        self.wait(1)
        self.play(Unwrite(title))
        self.play(integral_start_group.animate.shift(UP*1.5))

        identities_text = Text("Identify 1 of 3 identities:", font_size=20)
        identity1 = MathTex(r"\sqrt{a^2-b^2x^2}", font_size=30)
        identity2 = MathTex(r"\sqrt{b^2x^2-a^2}", font_size=30)
        identity3 = MathTex(r"\sqrt{a^2+b^2x^2}", font_size=30)

        identity_group = VGroup(identities_text, identity1, identity2, identity3).arrange(DOWN, buff=0.5)
        self.play(Write(identity_group, run_time=5))

        arrow1 = Arrow(start=LEFT, end=RIGHT*0.1).next_to(identity1, buff=0.1)
        arrow2 = Arrow(start=LEFT, end=RIGHT*0.1).next_to(identity2, buff=0.1)
        arrow3 = Arrow(start=LEFT, end=RIGHT*0.1).next_to(identity3, buff=0.1)
        self.play(FadeIn(arrow1, arrow2, arrow3))
        
        sin_identity = MathTex(r"x=\frac{a}{b}\sin\theta", font_size=30).next_to(arrow1, buff=0.1)
        sec_identity = MathTex(r"x=\frac{a}{b}\sec\theta", font_size=30).next_to(arrow2, buff=0.1)
        tan_identity = MathTex(r"x=\frac{a}{b}\tan\theta", font_size=30).next_to(arrow3, buff=0.1)

        self.play(
            Succession(
                Write(sin_identity),
                Write(sec_identity),
                Write(tan_identity), 
                run_time=5
            )
        )

        sin_group = VGroup(identity1, arrow1, sin_identity)
        sec_group = VGroup(identity2, arrow2, sec_identity)
        tan_group = VGroup(identity3, arrow3, tan_identity)
        self.play(
            sin_group.animate.shift(LEFT*1.2), 
            sec_group.animate.shift(LEFT*1.2),
            tan_group.animate.shift(LEFT*1.2)
        )
                
        self.wait(3)

        whole_step_group = VGroup(identities_text, sin_group, sec_group, tan_group)
        self.play(whole_step_group.animate.to_corner(DR).scale(0.8), run_time=2)
        self.wait(2)
        self.play(Circumscribe(integral1, color=RED_C,run_time=2))
        self.play(FadeOut(integral2, integral3))
        self.wait(1)

        equals1 = MathTex(r"=", font_size=30).next_to(integral1, buff=0.1)
        answer1 = MathTex(r"\int \frac{x^2}{\sqrt{6^2-1^2x^2}} \, dx}", font_size = 30).next_to(equals1, buff=0.1)

        integral1_group = VGroup(equals1, answer1)
        self.play(Write(integral1_group), run_time=1.5)
        self.wait(1)
        self.play(FadeOut(integral1, equals1))
        self.play(answer1.animate.shift(LEFT*2.5))
        self.wait(1)
        self.play(Circumscribe(sin_group, color=RED_C,run_time=2))

        a1 = answer1[0][6]
        b1 = answer1[0][9]
        x1 = answer1[0][11]
        a1_copy = a1.copy()
        b1_copy = b1.copy()
        x1_copy = x1.copy()
        self.play(
            a1.animate.set_color(BLUE),
            b1.animate.set_color(ORANGE),
            x1.animate.set_color(PURE_GREEN)
        )
        integral1_sqaureroot = answer1[0][4:13]
        integral1_square_root_copy = integral1_sqaureroot.copy()
                
        self.wait(1)

        self.play(
            a1_copy.animate.set_color(a1.get_color()),
            b1_copy.animate.set_color(b1.get_color()),
            x1_copy.animate.set_color(x1.get_color()),
            run_time=1
        )
        equals1.next_to(answer1)
        sin_copy = sin_identity.copy()
        
        self.play(Write(equals1))
        
        self.play(integral1_square_root_copy.animate.next_to(equals1), run_time=1.5)

        arrow4 = Arrow(start=LEFT, end=RIGHT*0.1).next_to(integral1_square_root_copy)
        self.play(FadeIn(arrow4))

        self.play(sin_copy.animate.next_to(arrow4).scale(1.3), buff=1, run_time=2)
    
        self.wait(1)

        sin_transform = MathTex(r"x=\frac{6}{1}\sin\theta", font_size=30).next_to(arrow4.get_center()).shift(RIGHT*0.2)
        sin_transform[0][0].set_color(PURE_GREEN)
        sin_transform[0][2].set_color(BLUE)
        sin_transform[0][4].set_color(ORANGE)

        sin_transform2 = MathTex(r"x=6\sin\theta", font_size=30).next_to(arrow4)
        sin_transform2[0][0].set_color(PURE_GREEN)
        sin_transform2[0][2].set_color(BLUE)

        self.play(TransformMatchingShapes(sin_copy, sin_transform))
        self.wait(0.5)
        self.play(TransformMatchingShapes(sin_transform, sin_transform2))

        arrow5= Arrow(start=LEFT, end=RIGHT*0.1).next_to(arrow4.get_center(), DOWN*1.5)
        self.play(Create(arrow5))

        deriv1 = MathTex(r"dx=6\cos\theta \, d\theta", font_size=30).next_to(arrow5)
        deriv1[0][0:2].set_color(PURE_GREEN)
        deriv1[0][3].set_color(BLUE)
        self.play(Write(deriv1))
        

        self.wait(1)

        self.play(FadeOut(equals1, integral1_square_root_copy, arrow4, arrow5))

        sin_deriv_group = VGroup(sin_transform2, deriv1)
        self.play(sin_deriv_group.animate.next_to(answer1, buff=0.5))
        self.wait(1)

        sin_answer = MathTex(
            r"&=\int \frac{(6sin\theta)^26cos\theta}{\sqrt{36-(6sin\theta)^2}} \, d\theta \\"
            r"&=\int \frac{216\sin^2\theta\cos\theta}{\sqrt{36-36\sin^2\theta}} \, d\theta \\"
            r"&=216 \int \frac{\sin^2\theta\cos\theta}{\sqrt{36(1-\sin^2\theta)}} \, d\theta \\"
            r"&=216 \int \frac{\sin^2\theta\cos\theta}{6\sqrt{\cos^2\theta}} \, d\theta \\"
            r"&=36 \int \frac{\sin^2\theta\cos\theta}{\cos\theta} \, d\theta \\"
            r"&=36 \int \sin^2\theta \, d\theta",
            font_size=26).next_to(answer1, DOWN*1.2)
        sin_answer_contd = MathTex(
            r"&=36 \int \frac{1}{2} - \frac{1}{2}\cos2\theta \, d\theta \\",
            r"&=18 \int 1-\cos2\theta \, d\theta \\",
            r"&=18(\theta-\frac{1}{2}\sin2\theta) + C \\",
            r"&=18\theta-9\sin2\theta +C \\",
            r"&=18\theta-(9)(2\sin\theta\cos\theta) + C \\",
            r"&=18\theta-18\sin\theta\cos\theta +C",
            font_size=25).next_to(sin_deriv_group.get_corner(DL)).shift(DOWN*1.8)
        
        self.play(
            Succession(
                Write(sin_answer),
                Write(sin_answer_contd),
                run_time=10
            )
        )
    
        self.wait(1)
        self.play(Circumscribe(sin_answer_contd[5], color = RED_C, run_time=2))

        arrow6 = Arrow(start=LEFT, end=RIGHT*0.1).next_to(sin_deriv_group, buff=0.1).shift(UP*0.2)
        theta_text = Text("Rearrange for theta", font_size=30).next_to(arrow6, RIGHT, buff=0.1)

        self.play(
            Succession(
                FadeIn(arrow6),
                Write(theta_text)
            )
        )
        self.wait(1)
        self.play(Unwrite(theta_text))
        theta_math_sin1 = MathTex(r"\sin\theta=\frac{opposite}{hypoteneuse}", font_size=26).next_to(arrow6, RIGHT, buff=0.1)
        theta_math_sin2 = MathTex(r'\theta=\sin^{-1}(\frac{x}{6})', font_size=26).next_to(arrow6, RIGHT, buff=0.1)
        
        theta_sin_group = VGroup(theta_math_sin1, theta_math_sin2).arrange(DOWN, buff=0.1).next_to(arrow6, RIGHT, buff=0.1).shift(DOWN*0.2)

        self.play(Write(theta_sin_group, run_time=3))
        self.wait(2)

        vertices = [np.array([0, 2.5, 0]), np.array([0, 0, 0]), np.array([1.5, 0, 0])]
        
        righttri = Polygon(*vertices, stroke_color=TEAL_C).to_edge(RIGHT).shift(UP*0.5+LEFT*1.5)
        self.play(Create(righttri, run_time=3))
        self.play(righttri.animate.set_fill(TEAL_C, opacity=0.3), run_time=1.5)
        self.wait(1)

        midpoints = [
            ((vertices[0] + vertices[1]) / 2),
            ((vertices[1] + vertices[2]) / 2),
            ((vertices[2] + vertices[0]) / 2)
        ]
        shift_vector = RIGHT * 3.6 + UP * 0.5
        midpoints = [midpoint + shift_vector for midpoint in midpoints]

        angle = Angle(
            Line(vertices[1], vertices[2]),  # second line (bottom side)
            Line(vertices[2], vertices[0]),  # third line (right side)
        ).to_edge(RIGHT).shift(UP*0.7+LEFT*2.2)
        theta_label = MathTex(r"\theta", font_size=30).next_to(angle.get_center())
        
        self.play(Create(angle), Write(theta_label))
        
        x_sin_copy = theta_math_sin2[0][8].copy()
        six_sin_copy = theta_math_sin2[0][10].copy()

        self.play(x_sin_copy.animate.next_to(midpoints[0]).shift(LEFT*0.5), run_time=2)
        self.play(six_sin_copy.animate.next_to(midpoints[2]), run_time=2)
        

        adj_sin = MathTex(r"\sqrt{6^2-x^2}", font_size=30).next_to(midpoints[1]).shift(DOWN*0.4+LEFT*0.9)
        adj_sin2 = MathTex(r"\sqrt{36-x^2}", font_size=30).next_to(midpoints[1]).shift(DOWN*0.4+LEFT*0.9)
        self.play(Write(adj_sin))
        
        self.play(TransformMatchingShapes(adj_sin, adj_sin2))

        self.play(Circumscribe(sin_answer_contd[5][3], color=PURE_RED),
        Circumscribe(theta_math_sin2, color=PURE_RED), run_time=2)
        self.wait(1)

        self.play(Circumscribe(sin_answer_contd[5][7:11], color=YELLOW),
                  Circumscribe(x_sin_copy, color=YELLOW),
                  Circumscribe(six_sin_copy, color=YELLOW),
                  run_time=2)
        self.wait(1)
        self.play(Circumscribe(sin_answer_contd[5][11:15], color = LIGHT_PINK),
                  Circumscribe(adj_sin2, color = LIGHT_PINK),
                  Circumscribe(six_sin_copy, color=LIGHT_PINK),
                  run_time=2)

        self.wait(2)

        sin_answer_contd2 = MathTex(r"&=18\sin^{-1}(\frac{x}{6})-\frac{18x\sqrt{36-x^2}}{36} + C \\",
                                    r"&=18\sin^{-1}(\frac{x}{6})-\frac{x\sqrt{36-x^2}}{2} + C",
                                    font_size=25).next_to(sin_answer_contd, DOWN, buff=0.1).shift(RIGHT*0.3)
        sin_answer_contd2[1].set_color(YELLOW)
        self.play(Write(sin_answer_contd2), run_time=5)
        self.wait(1)

        sr1 = SurroundingRectangle(sin_answer_contd2[1], color=YELLOW)
        self.play(Create(sr1))
        self.wait(2)
        self.play(FadeOut(sin_transform2, deriv1, arrow6, sin_answer, 
                          sin_answer_contd, sin_answer_contd2,
                          x_sin_copy, six_sin_copy, theta_math_sin1,
                          theta_math_sin2, righttri, answer1, sr1, adj_sin2, 
                          theta_label, a1_copy, b1_copy, x1_copy))

        
        
        self.play(FadeIn(integral2))
        self.play(integral2.animate.shift(LEFT*4.8))
        self.wait(0.5)
        self.play(Circumscribe(sec_group, color=RED_C), run_time=2)
        self.wait(0.5)
        sec_answer1 = MathTex(r"\int \frac{1}{(\sqrt{4x^2-16})^3} \, dx", font_size=30).shift(LEFT*4.8).to_edge(UP).shift(DOWN*0.5)
        sec_x_answer2 = MathTex(r"\int \frac{1}{(\sqrt{2^2x^2-4^2})^3} \, dx", font_size=30).shift(LEFT*4.8).to_edge(UP).shift(DOWN*0.5)
        

        self.play(ReplacementTransform(integral2, sec_answer1))
        self.wait(0.5)
        self.play(ReplacementTransform(sec_answer1, sec_x_answer2))

        sec_x = MathTex(r"x&=\frac{4}{2}\sec\theta \\",
                        r"dx&=\frac{4}{2}\sec\theta\tan\theta \, d\theta", font_size=26).next_to(sec_answer1, buff=0.5)
        self.play(Write(sec_x))

        sec_x_transform = MathTex(r"x&=2\sec\theta \\",
                        r"dx&=2\sec\theta\tan\theta \, d\theta", font_size=26).next_to(sec_answer1, buff=0.5)
        
        self.wait(1)
        self.play(TransformMatchingShapes(sec_x, sec_x_transform))
        

        theta_sec = MathTex(r"\theta=\sec^{-1}(\frac{x}{2})", font_size=26).next_to(sec_x_transform, buff=0.5)

        self.play(Write(theta_sec))

        sec_answer3 = MathTex(
            r"&= \int \frac{2\sec\theta\tan\theta}{(\sqrt{4(2\sec\theta)^2-16})^3} \, d\theta \\",
            r"&=\int \frac{2\sec\theta\tan\theta}{(\sqrt{16\sec^2\theta-16})^3} \, d\theta \\",
            r"&=2\int \frac{\sec\theta\tan\theta}{(\sqrt{16(\sec^2\theta-1)})^3} \, d\theta \\",
            r"&=\frac{2}{4^3} \int \frac{\sec\theta\tan\theta}{(\sqrt{\tan^2\theta})^3} \, d\theta \\",
            r"&=\frac{1}{32} \int \frac{\sec\theta\tan\theta}{\tan^3\theta} \, d\theta \\",
            r"&=\frac{1}{32} \int \frac{\sec\theta}{\tan^2\theta }\, d\theta \\",
            r"&=\frac{1}{32} \int \frac{\frac{1}{\cos\theta}}{\frac{\sin^2\theta}{\cos^2\theta}} \, d\theta"
                            , font_size=26).next_to(sec_x_answer2.get_left(), DOWN, buff=0.4).shift(RIGHT*1.4)
                              
        self.play(Write(sec_answer3, run_time=5))
        self.wait(2)

        sin_cos_transform = MathTex(r"&=\frac{1}{32} \int \frac{\cos\theta}{\sin^2\theta} \, d\theta", font_size=26).next_to(sec_answer3[5].get_left(), DOWN*1, buff=0.4).shift(RIGHT*1)
        self.play(ReplacementTransform(sec_answer3[-1], sin_cos_transform))
        self.wait(0.5)

        u_text = MathTex(r"u&=\sin\theta \\",
                         r"du&=\cos\theta", font_size=26).next_to(sin_cos_transform, DOWN, buff=0.1)
        self.play(Write(u_text))

        sec_answer4 = MathTex(r"&=\frac{1}{32} \int u^{-2} \, du \\",
                              r"&=\frac{-1}{32u}+C \\",
                              r"&=\frac{-1}{32\sin\theta}+C \\",
                              r"&=\frac{-\csc\theta}{32}+C", 
                              font_size=26).next_to(sec_answer3[1], buff=0.5).shift(DOWN*0.5)
        self.play(Write(sec_answer4), run_time=3)

        vertices2 = [np.array([0, 2.5, 0]), np.array([0, 0, 0]), np.array([1.5, 0, 0])]
        
        righttri2 = Polygon(*vertices2, stroke_color=TEAL_C).to_edge(RIGHT).shift(UP*0.5+LEFT*1.5)
        self.play(Create(righttri2, run_time=3))
        self.play(righttri2.animate.set_fill(TEAL_C, opacity=0.3), run_time=1.5)
        self.wait(1)

        midpoints2 = [
            ((vertices2[0] + vertices2[1]) / 2),
            ((vertices2[1] + vertices2[2]) / 2),
            ((vertices2[2] + vertices2[0]) / 2)
        ]
        shift_vector = RIGHT * 3.6 + UP * 0.5
        midpoints2 = [midpoint + shift_vector for midpoint in midpoints2]

        angle = Angle(
            Line(vertices2[1], vertices2[2]),  # second line (bottom side)
            Line(vertices2[2], vertices2[0]),  # third line (right side)
        ).to_edge(RIGHT).shift(UP*0.7+LEFT*2.2)
        theta_label2 = MathTex(r"\theta", font_size=30).next_to(angle.get_center())
        
        self.play(Create(angle), Write(theta_label2))

        x_sec_copy = theta_sec[0][8].copy()
        two_sec_copy = theta_sec[0][10].copy()

        self.play(x_sec_copy.animate.next_to(midpoints2[2]), run_time=2)
        self.play(two_sec_copy.animate.next_to(midpoints2[1]).shift(DOWN*0.2+LEFT*0.3), run_time=2)

        opp_sec = MathTex(r"\sqrt{x^2-2^2}", font_size=30).next_to(midpoints2[0]).shift(LEFT*1.7)
        opp_sec2 = MathTex(r"\sqrt{x^2-4}", font_size=30).next_to(midpoints2[0]).shift(LEFT*1.7)
        self.play(Write(opp_sec))
        self.play(TransformMatchingShapes(opp_sec, opp_sec2))
        self.wait(0.5)
        self.play(Circumscribe(sec_answer4[3][2:6], color=PURPLE_A),
                  Circumscribe(opp_sec2, color=PURPLE_A),
                  Circumscribe(x_sec_copy, color=PURPLE_A),
                run_time=2)
        sec_answer5 = MathTex(r"&=\frac{-x}{32\sqrt{x^2-4}}+C", font_size=26).next_to(sec_answer4.get_corner(DL), DOWN).shift(RIGHT)
        sec_answer5.set_color(YELLOW)
        self.play(Write(sec_answer5))

        sr2 = SurroundingRectangle(sec_answer5, color=YELLOW)
        self.play(Create(sr2), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(sec_x_answer2, theta_sec, sec_answer3,sec_answer4, 
                          u_text, righttri2, x_sec_copy, two_sec_copy,
                          opp_sec2, sec_answer5, theta_label2, sec_x_transform, sr2))
        self.wait(1)
        
        self.play(FadeIn(integral3))
        self.play(integral3.animate.to_edge(LEFT).shift(RIGHT*0.6))
        self.wait(1)
        self.play(Circumscribe(tan_group, color=RED_C), run_time=2)

        integral3_transform = MathTex(r"\int\frac{x^3}{\sqrt{3^2+x^2}} \, dx", font_size=30).shift(LEFT*4.8).to_edge(UP).shift(DOWN*0.5)

        self.play(ReplacementTransform(integral3, integral3_transform))

        tan_x = MathTex(r"x&=\frac{3}{1}\tan\theta \\",
                        r"dx&= \frac{3}{1}\sec^2\theta \, d\theta", font_size=26).next_to(integral3, buff=0.5)
        tan_x_transform = MathTex(r"x&=3\tan\theta \\",
                                  r"dx&=3\sec^2\theta \, d\theta", font_size=26).next_to(integral3, buff=0.5)
        
        self.play(Write(tan_x))
        self.wait(0.5)
        self.play(TransformMatchingShapes(tan_x, tan_x_transform))
        self.wait(0.5)

        tan_theta = MathTex(r"\theta=\tan^{-1}(\frac{x}{3})", font_size=26).next_to(tan_x_transform, buff=0.5)
        self.play(Write(tan_theta))

        tan_answer = MathTex(
            r"&= \int \frac{(3\tan\theta)^3(3\sec^2\theta)}{\sqrt{(3\tan\theta)^2+9}} \, d\theta \\",
            r"&= \int \frac{81\tan^3\theta\sec^2\theta}{\sqrt{9\tan^2\theta+9}} \, d\theta \\",
            r"&= 81\int \frac{\tan^3\theta\sec^2\theta}{\sqrt{9(\tan^2\theta+1)}} \, d\theta \\",
            r"&= \frac{81}{3}\int \frac{\tan^3\theta\sec^2\theta}{\sqrt{\sec^2\theta}} \, d\theta \\",
            r"&= 27\int \tan^3\theta\sec\theta \, d\theta \\",
            r"&= 27\int (\sec^2\theta-1)\sec\theta\tan\theta \, d\theta \\",
            r"&=27\int u^2-1 \, du \\",
            r"&=27(\frac{u^3}{3}-u)+C",
            font_size=26).next_to(integral3_transform.get_left(), DOWN, buff=0.5).shift(RIGHT*1.4)
        tan_u = MathTex(r"u&=\sec\theta \\",
                        r"du&=\sec\theta\tan\theta \, d\theta",
                        font_size=26).next_to(tan_answer[6], buff=0.5)
        self.play(Write(tan_answer), run_time=5)
        self.play(FadeIn(tan_u))
        

        tan_answer2 = MathTex(r"&=9u^3-27u+C \\",
                              r"&=9\sec\theta(\sec^2\theta-3)+C", font_size=26).next_to(tan_answer[0], buff=0.5).shift(DOWN*0.2)
        self.play(Write(tan_answer2))

        vertices3 = [np.array([0, 2.5, 0]), np.array([0, 0, 0]), np.array([1.5, 0, 0])]
        
        righttri3 = Polygon(*vertices3, stroke_color=TEAL_C).to_edge(RIGHT).shift(UP*0.5+LEFT*1.5)
        self.play(Create(righttri3, run_time=3))
        self.play(righttri3.animate.set_fill(TEAL_C, opacity=0.3), run_time=1.5)
        self.wait(1)

        midpoints3 = [
            ((vertices3[0] + vertices3[1]) / 2),
            ((vertices3[1] + vertices3[2]) / 2),
            ((vertices3[2] + vertices3[0]) / 2)
        ]
        shift_vector = RIGHT * 3.6 + UP * 0.5
        midpoints3 = [midpoint + shift_vector for midpoint in midpoints3]

        angle3 = Angle(
            Line(vertices3[1], vertices3[2]),  # second line (bottom side)
            Line(vertices3[2], vertices3[0]),  # third line (right side)
        ).to_edge(RIGHT).shift(UP*0.7+LEFT*2.2)
        theta_label3 = MathTex(r"\theta", font_size=30).next_to(angle3.get_center())
        
        self.play(Create(angle3), Write(theta_label3))

        x_tan_copy = tan_theta[0][8].copy()
        three_tan_copy = tan_theta[0][10].copy()

        self.play(x_tan_copy.animate.next_to(midpoints3[0]).shift(LEFT*0.5), run_time=2)
        self.play(three_tan_copy.animate.next_to(midpoints3[1]).shift(DOWN*0.2+LEFT*0.3), run_time=2)

        hyp_tan = MathTex(r"\sqrt{x^2+3^2}", font_size=30).next_to(midpoints3[2])
        hyp_tan2 = MathTex(r"\sqrt{x^2+9}", font_size=30).next_to(midpoints3[2])

        self.play(Write(hyp_tan))
        self.play(ReplacementTransform(hyp_tan, hyp_tan2))

        tan_answer3 = MathTex(
            r"&=9(\frac{\sqrt{x^2+9}}{3})({(\frac{\sqrt{x^2+9}}{3}})^2-3)+C \\",
            r"&=3\sqrt{x^2+9}(\frac{x^2+9}{3}-\frac{18}{3})+C \\",
            r"&=3\sqrt{x^2+9}(\frac{x^2-18}{3})+C \\",
            r"&=\frac{1}{3}\sqrt{x^2+9}(x^2-18)+C ",
            font_size=26).next_to(tan_answer2.get_corner(DL), DOWN).shift(RIGHT*2.1)
        
        tan_answer3[3].set_color(YELLOW)
        
        
        self.play(
            Circumscribe(tan_answer2[1][2:6], color=PURE_GREEN),
            Circumscribe(tan_answer2[1][7:12],color=PURE_GREEN),
            Circumscribe(hyp_tan2, color=PURE_GREEN),
            Circumscribe(three_tan_copy, color=PURE_GREEN),
            run_time=2
        )
        self.wait(1)
        self.play(Write(tan_answer3), run_time=3)
        self.wait(0.5)

        sr3 = SurroundingRectangle(tan_answer3[3], color=YELLOW)
        self.play(Create(sr3), run_time=2)
        self.wait(3)
        self.play(
            FadeOut(
                integral3_transform, tan_theta, tan_answer,
                tan_answer2, tan_answer3, tan_u, righttri3,
                x_tan_copy, three_tan_copy, hyp_tan2, theta_label3,
                tan_x_transform, whole_step_group, sr3
                )
        )
        self.wait(1)
                            
        
                                    