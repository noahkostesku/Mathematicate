from manim import *
from manim import AS2700

class TanInverse(Scene):
    def construct(self):

        title = Text("The intuition behind", font_size = 35).shift(UP*1.5)
        tan_inverse = MathTex(r"\tan^{-1}(x) = \sum_{n=0}^{\infty} (-1)^n\frac{x^{2n+1}}{2n+1}", font_size = 40)

        self.play(
            Succession(
                Write(title),
                Write(tan_inverse)
            )
        )
        self.wait(1)

        self.play(Unwrite(title))
        self.play(tan_inverse.animate.to_corner(UL))
        self.wait(0.5)
        
        text2 = Text("Consider a known series", font_size=30).next_to(tan_inverse, DOWN*2).align_to(tan_inverse, LEFT)
        geom_ser = MathTex(r"\sum_{n=0}^{\infty} ar^n = \frac{a}{1-r}", font_size = 40).next_to(text2, RIGHT)

        self.play(
            Succession(
                Write(text2),
                Write(geom_ser)
            )
        )
        self.wait(1)

        text3 = Text("By getting", font_size=30).next_to(text2, DOWN*3).align_to(text2, LEFT)
        tan = tan_inverse[0][0:8].copy().next_to(text3, RIGHT)
        text4 = Text("in terms of the geometric series", font_size =30).next_to(tan, RIGHT)
        text5 = Text("a proof can be demonstrated", font_size=30).next_to(text2, DOWN*5).shift(RIGHT*0.3)
        proof_group = VGroup(text3, tan, text4, text5)

        self.play(Write(proof_group), run_time=5)
        self.wait(1)

        self.play(Unwrite(text2), Unwrite(text3), Unwrite(text4), Unwrite(text5), Unwrite(tan))
        self.play(geom_ser.animate.to_edge(UP).shift(RIGHT*2))
        self.wait(0.5)

        tan_inv_copy = tan_inverse[0][0:9].copy()

        self.play(tan_inv_copy.animate.move_to(ORIGIN+LEFT*0.4+DOWN*0.5))

        text6 = Text("Notice the derivative property", font_size = 35).shift(UP*1)
        d_dx = MathTex(r"\frac{d}{dx}", font_size=40).next_to(tan_inv_copy, LEFT)
        tan_inv_deriv = MathTex(r"\frac{1}{1+x^2}", font_size=40).next_to(tan_inv_copy, RIGHT)

        self.play(Write(text6))
        self.wait(0.5)
        self.play(
            Succession(
                FadeIn(d_dx),
                Write(tan_inv_deriv)
            )
        )
        self.wait(0.5)

        tan_inv_deriv2 = MathTex(r"\frac{1}{1-(-x^2)}", font_size=40).next_to(tan_inv_copy, RIGHT)

        self.play(ReplacementTransform(tan_inv_deriv, tan_inv_deriv2))
        self.play(Unwrite(text6))
        
        text7 = Text("See the similarities to the geometric series", font_size=35).shift(UP*1)

        self.play(Write(text7))
        self.play(Circumscribe(geom_ser, color = PURE_RED), Circumscribe(tan_inv_deriv, color=PURE_RED), run_time=2)
        self.wait(0.5)
        self.play(Unwrite(text7))
        self.play(
            geom_ser[0][9].animate.set_fill(AS2700.X13_MARIGOLD),
            geom_ser[0][5].animate.set_fill(AS2700.X13_MARIGOLD),
            tan_inv_deriv2[0][0].animate.set_fill(AS2700.X13_MARIGOLD)
        )

        equals = tan_inverse[0][8].copy().move_to(ORIGIN).shift(LEFT+UP)
        equals2 = tan_inverse[0][8].copy().move_to(ORIGIN).shift(RIGHT+UP)
        geom_a_copy = geom_ser[0][9].copy()
        tan_one_copy = tan_inv_deriv2[0][0].copy()

        self.play(Write(equals))
        self.play(geom_a_copy.animate.next_to(equals, LEFT), tan_one_copy.animate.next_to(equals, RIGHT))
        self.wait(0.5)

        self.play(geom_ser[0][13].animate.set_fill(AS2700.B41_BLUEBELL),
                  geom_ser[0][6].animate.set_fill(AS2700.B41_BLUEBELL),
                  tan_inv_deriv2[0][5:8].animate.set_fill(AS2700.B41_BLUEBELL))
        
        geom_r_copy = geom_ser[0][13].copy()
        tan_r_copy = tan_inv_deriv2[0][5:8].copy()

        self.play(Write(equals2))
        self.play(geom_r_copy.animate.next_to(equals2, LEFT), tan_r_copy.animate.next_to(equals2, RIGHT))
        self.wait(1)

        self.play(FadeOut(geom_a_copy, equals, tan_one_copy, geom_r_copy, equals2, tan_r_copy))
        
        deriv_tan_group = VGroup(tan_inv_copy, d_dx, tan_inv_deriv2)

        self.play(deriv_tan_group.animate.shift(LEFT*2.2))

        equals.next_to(deriv_tan_group, RIGHT)

        self.play(
            Succession(
                Write(equals),
                geom_ser.animate.next_to(equals, RIGHT)
            )
        )
        self.wait(1)

        geom_ser_new = MathTex(r"\sum_{n=0}^{\infty} 1(-x^2)^n ", font_size=40).next_to(equals, RIGHT)
        geom_ser_new[0][5].set_fill(AS2700.X13_MARIGOLD)
        geom_ser_new[0][7:10].set_fill(AS2700.B41_BLUEBELL)

        self.play(ReplacementTransform(geom_ser, geom_ser_new))
        self.wait(0.5)

        geom_ser_new2 = MathTex(r"\sum_{n=0}^{\infty} (-1)^nx^{2n} ", font_size=40).next_to(equals, RIGHT)

        self.play(tan_inv_deriv2[0][0].animate.set_fill(WHITE),
                  tan_inv_deriv2[0][5:8].animate.set_fill(WHITE),
                  ReplacementTransform(geom_ser_new, geom_ser_new2))
        self.wait(0.5)

        self.play(FadeOut(equals, tan_inv_deriv2))

        deriv_tan = VGroup(tan_inv_copy, d_dx)

        self.play(deriv_tan.animate.shift(RIGHT*1.5), geom_ser_new2.animate.shift(LEFT))
        self.wait(1)

        text8 = Text("Taking the integral of both sides cancels out the derivative on the left side", font_size = 30).shift(UP)

        self.play(Write(text8))
        self.wait(1)

        integral1 = MathTex(r"\int\frac{d}{dx}\tan^{-1}(x)dx=", font_size = 40).shift(LEFT*2.2+DOWN)
        geom_ser_new3 = MathTex(r"\int\sum_{n=0}^{\infty} (-1)^nx^{2n} dx ", font_size=40).next_to(integral1, RIGHT)

        self.play(ReplacementTransform(deriv_tan, integral1),
                  ReplacementTransform(geom_ser_new2, geom_ser_new3))
        self.wait(0.5)
        self.play(Unwrite(text8))
        
        text9 = Text("Move integral inside the summation", font_size = 35).shift(UP)

        self.play(Write(text9))

        original_tan_inv = MathTex(r"\tan^{-1}(x)=", font_size = 40).shift(LEFT*2.2+DOWN)
        geom_ser_new4 = MathTex(r"\sum_{n=0}^{\infty} \int(-1)^nx^{2n} dx ", font_size=40).next_to(original_tan_inv, RIGHT)

        self.play(ReplacementTransform(integral1, original_tan_inv),
                  ReplacementTransform(geom_ser_new3, geom_ser_new4))
        self.wait(0.5)
        self.play(Unwrite(text9))

        text10 = Text("Apply the power rule of integration:", font_size = 30).shift(UP+LEFT*1.5)
        power_rule  = MathTex(r"\int x^ndx = \frac{x^{n+1}}{n+1} + C", font_size=40).next_to(text10, RIGHT)
        power_rule_group = VGroup(text10, power_rule)

        self.play(Write(power_rule_group))

        tan_int_with_c = MathTex(r"\sum_{n=0}^{\infty} (-1)^n\frac{x^{2n+1}}{2n+1} + C").next_to(original_tan_inv, RIGHT)

        self.wait(0.5)
        self.play(ReplacementTransform(geom_ser_new4, tan_int_with_c))
        self.wait(0.5)
        self.play(Unwrite(power_rule_group))

        text11 = Text("To solve for C any x value can be used", font_size = 30).shift(UP)

        self.play(Write(text11))
        self.wait(1.5)
        self.play(Unwrite(text11))

        text12 = Text("Let", font_size=30).shift(UP+LEFT)
        x_text = MathTex(r"x=0", font_size=40).next_to(text12, RIGHT)
        x_text_group = VGroup(text12, x_text)

        self.play(Write(x_text_group))

        tan_with_0 = MathTex(r"\tan^{-1}(0)=\sum_{n=0}^{\infty} (-1)^n\frac{0^{2n+1}}{2n+1} + C", font_size=40).shift(DOWN)
        tan_int_sum_with_c_group = VGroup(original_tan_inv, tan_int_with_c)

        self.play(TransformMatchingShapes(tan_int_sum_with_c_group, tan_with_0))
        self.wait(0.5)
        self.play(Unwrite(x_text_group))

        brace1 = Brace(tan_with_0[0][0:8], DOWN)
        brace2 = Brace(tan_with_0[0][9:29], DOWN)
        zero1 = MathTex(r"0", font_size=40).next_to(brace1, DOWN)
        zero2 = MathTex(r"0", font_size=40).next_to(brace2, DOWN)

        self.play(
            Succession(
                GrowFromCenter(brace1),
                Write(zero1)
            )
        )
        self.play(
            Succession(
                GrowFromCenter(brace2),
                Write(zero2)
            )
        )

        self.wait(0.5)
        self.play(FadeOut(tan_with_0[0][0:8],tan_with_0[0][9:29], brace1, brace2))
        self.play(zero1.animate.next_to(tan_with_0[0][8], LEFT),
                  zero2.animate.next_to(tan_with_0[0][8], RIGHT),
                  tan_with_0[0][29:].animate.shift(LEFT*2.6)
        )

        c_answer = MathTex(r"C=0", font_size=40).shift(DOWN+LEFT*0.5).set_fill(YELLOW)

        c_0_group = VGroup(zero1, zero2,tan_with_0[0][29:], tan_with_0[0][8])
        sr1 = SurroundingRectangle(c_answer, color=YELLOW)

        self.play(
            Succession(
            TransformMatchingShapes(c_0_group, c_answer),
            Create(sr1)
            )
        )
        self.wait(0.5)
        
        c_rec = VGroup(c_answer, sr1)

        self.play(c_rec.animate.shift(UP*1.5))

        tan_int_with_0 = MathTex(r"\tan^{-1}(x)=\sum_{n=0}^{\infty} (-1)^n\frac{x^{2n+1}}{2n+1} + 0", font_size=40).shift(DOWN)
        penultimate_answer = MathTex(r"\tan^{-1}(x)=\sum_{n=0}^{\infty} (-1)^n\frac{x^{2n+1}}{2n+1}", font_size=40).shift(DOWN)
        final_answer = MathTex(r"\tan^{-1}(x)=\sum_{n=0}^{\infty} (-1)^n\frac{x^{2n+1}}{2n+1}", font_size=40).shift(DOWN)

        self.play(FadeIn(tan_int_sum_with_c_group))
        self.wait(0.5)
        self.play(TransformMatchingShapes(tan_int_sum_with_c_group, tan_int_with_0))
        self.wait(0.5)
        self.play(FadeOut(c_rec))
        self.play(TransformMatchingShapes(tan_int_with_0, penultimate_answer))
        self.wait(0.5)
        self.play(TransformMatchingShapes(penultimate_answer, final_answer))

        sr2 = SurroundingRectangle(final_answer, color=YELLOW)
        sr3 = SurroundingRectangle(tan_inverse, color=YELLOW)

        self.play(tan_inverse.animate.set_fill(YELLOW),
                  final_answer.animate.set_fill(YELLOW),
                  Create(sr2),
                  Create(sr3)
        )
        self.wait(1)
        
        original_tan_inverse_group = VGroup(tan_inverse, sr3)
        final_tan_inverse_group = VGroup(final_answer, sr2)

        self.play(FadeOut(original_tan_inverse_group))
        self.play(final_tan_inverse_group.animate.move_to(ORIGIN))
        self.wait(2)


        
        



           


        
        