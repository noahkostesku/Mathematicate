from manim import *

class euler_identity(Scene):
    def construct(self):

        eq = MathTex(r"e^{i\pi}=-1", font_size=40).shift(UP*2)
        self.play(Write(eq), run_time=1.5)
        text1 = Text("But Why?", font_size=30).move_to(ORIGIN)
        text2 = Text("By using Mclaurin series of different functions,", font_size=30)
        text3 = Text("a valid proof can be demonstrated", font_size=30)

        text2_3_group = VGroup(text2, text3).arrange(DOWN, buff=0.2)
        self.wait(0.5)
        self.play(Write(text1))
        self.wait(1)
        self.play(Unwrite(text1))
        self.play(Write(text2_3_group), run_time=3)
        self.wait(1)
        self.play(Unwrite(text2_3_group), FadeOut(eq))
        self.wait(1)

        text4 = Text("Consider the mclaurin series for", font_size=30).shift(LEFT*3+UP*3)

        ex_mclaurin = MathTex(r"e^x =\sum_{n=0}^{\infty} \frac{x^n}{n!} = 1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\frac{x^4}{4!}+\frac{x^5}{5!}+\frac{x^6}{6!}+\frac{x^7}{7!}+\cdots}", font_size=40).next_to(text4, DOWN).align_to(text4, LEFT)

        e_x = ex_mclaurin[0][0:2].copy().next_to(text4, RIGHT)

        ex_text4_group = VGroup(text4, e_x)

        self.play(Write(ex_text4_group))
        self.wait(0.5)
        self.play(Write(ex_mclaurin), run_time=3)
        self.wait(1)

        text5 = Text("Use series rules to plug in:", font_size = 30).shift(LEFT*3.5+UP*3)
        i_text = eq[0][1].copy().next_to(text5, RIGHT).scale(1.25)
        i_text2 = Text("for every x term", font_size=30).next_to(i_text, RIGHT)
        text5_group = VGroup(text5, i_text, i_text2)
        
        self.play(
            Succession(
                Unwrite(ex_text4_group),
                Write(text5_group)
            )
        )
        self.wait(0.5)

        ex_mclaurin_with_i = MathTex(
            r"e^{ix} = \sum_{n=0}^{\infty} \frac{(ix)^n}{n!} = (1i)^0 + (ix)^1 + \frac{(ix)^2}{2!} + \frac{(ix)^3}{3!} + \frac{(ix)^4}{4!} \\",
            r"+ \frac{(ix)^5}{5!}+ \frac{(ix)^6}{6!} + \frac{(ix)^7}{7!} + \cdots",
            font_size=40
        ).next_to(text5, DOWN).align_to(text5, LEFT)

        ex_mclaurin_with_i2 = MathTex(
            r"e^{ix} = \sum_{n=0}^{\infty} \frac{i^nx^n}{n!} = 1^0i^0 + i^1x^1 + \frac{i^2x^2}{2!} + \frac{i^3x^3}{3!} + \frac{i^4x^4}{4!} \\",
            r"+ \frac{i^5x^5}{5!}+ \frac{i^6x^6}{6!} + \frac{i^7x^7}{7!} + \cdots",
            font_size=40
        ).next_to(text5, DOWN).align_to(text5, LEFT)

        self.play(ReplacementTransform(ex_mclaurin, ex_mclaurin_with_i))
        self.wait(1)
        self.play(ReplacementTransform(ex_mclaurin_with_i, ex_mclaurin_with_i2))

        text7 = Text("Using the cyclic property of", font_size=30).shift(LEFT*3.5)
        i_text2 = eq[0][1].copy().next_to(text7, RIGHT).scale(1.25)
        text8 = Text("each term can be simplified via the table below", font_size=30).next_to(text7, DOWN).align_to(text7, LEFT)
        i_group = VGroup(text7, i_text2, text8)
        i_prop1 = MathTex(r"i^0 = 1", font_size=30)
        i_prop2 = MathTex(r"i^1 = i", font_size=30)
        i_prop3 = MathTex(r"i^2 = -1", font_size=30)
        i_prop4 = MathTex(r"i^3 = -i", font_size=30)

        self.play(Write(i_group), run_time=3)

        i_prop_group = VGroup(i_prop1, i_prop2, i_prop3, i_prop4).arrange(DOWN, buff=0.2).move_to(text8, DOWN).shift(DOWN*2.2+LEFT*2.6)

        self.play(Write(i_prop_group))
        self.wait(1)
        self.play(FadeOut(i_group))
        self.play(i_prop_group.animate.shift(UP+RIGHT))

        ex_mclaurin_with_i3 = MathTex(
            r"e^{ix} = \sum_{n=0}^{\infty} \frac{i^nx^n}{n!} = 1 + i^1x^1 + \frac{i^2x^2}{2!} + \frac{i^3x^3}{3!} + \frac{i^4x^4}{4!} \\",
            r"+ \frac{i^5x^5}{5!}+ \frac{i^6x^6}{6!} + \frac{i^7x^7}{7!} + \cdots",
            font_size=40
        ).next_to(text5, DOWN).align_to(text5, LEFT)

        self.play(Circumscribe(ex_mclaurin_with_i2[0][17:21], color=TEAL_C),
                  Circumscribe(i_prop1, color=TEAL_C), run_time=2)
        self.play(ReplacementTransform(ex_mclaurin_with_i2, ex_mclaurin_with_i3))
        self.wait(0.5)

        ex_mclaurin_with_i4 = MathTex(
            r"e^{ix} = \sum_{n=0}^{\infty} \frac{i^nx^n}{n!} = 1 + ix + \frac{i^2x^2}{2!} + \frac{i^3x^3}{3!} + \frac{i^4x^4}{4!} \\",
            r"+ \frac{i^5x^5}{5!}+ \frac{i^6x^6}{6!} + \frac{i^7x^7}{7!} + \cdots",
            font_size=40
        ).next_to(text5, DOWN).align_to(text5, LEFT)

        self.play(Circumscribe(ex_mclaurin_with_i3[0][19:23], color=TEAL_C),
                  Circumscribe(i_prop2, color=TEAL_C), run_time=2)
        self.play(ReplacementTransform(ex_mclaurin_with_i3, ex_mclaurin_with_i4))
        self.wait(0.5)

        ex_mclaurin_with_i5 = MathTex(
            r"e^{ix} = \sum_{n=0}^{\infty} \frac{i^nx^n}{n!} = 1 + ix - \frac{x^2}{2!} + \frac{i^3x^3}{3!} + \frac{i^4x^4}{4!} \\",
            r"+ \frac{i^5x^5}{5!}+ \frac{i^6x^6}{6!} + \frac{i^7x^7}{7!} + \cdots",
            font_size=40
        ).next_to(text5, DOWN).align_to(text5, LEFT)

        self.play(Circumscribe(ex_mclaurin_with_i5[0][22:28], color=TEAL_C),
                  Circumscribe(i_prop3, color=TEAL_C), run_time=2)
        self.play(ReplacementTransform(ex_mclaurin_with_i4, ex_mclaurin_with_i5))
        self.wait(0.5)

        ex_mclaurin_with_i6 = MathTex(
            r"e^{ix} = \sum_{n=0}^{\infty} \frac{i^nx^n}{n!} = 1 + i^1x^1 - \frac{x^2}{2!} - \frac{ix^3}{3!} + \frac{i^4x^4}{4!} \\",
            r"+ \frac{i^5x^5}{5!}+ \frac{i^6x^6}{6!} + \frac{i^7x^7}{7!} + \cdots",
            font_size=40
        ).next_to(text5, DOWN).align_to(text5, LEFT)

        self.play(Circumscribe(ex_mclaurin_with_i6[0][29:36], color=TEAL_C),
                  Circumscribe(i_prop4, color=TEAL_C), run_time=2)
        self.play(ReplacementTransform(ex_mclaurin_with_i5, ex_mclaurin_with_i6))
        self.wait(0.5)

        ex_mclaurin_with_i7 = MathTex(
            r"e^{ix} = \sum_{n=0}^{\infty} \frac{i^nx^n}{n!} = 1 + ix - \frac{x^2}{2!} - \frac{ix^3}{3!} + \frac{x^4}{4!} \\",
            r"+ \frac{ix^5}{5!} - \frac{x^6}{6!} - \frac{ix^7}{7!} + \cdots",
            font_size=40
        ).next_to(text5, DOWN).align_to(text5, LEFT)

        self.play(ReplacementTransform(ex_mclaurin_with_i6, ex_mclaurin_with_i7))
        self.wait(0.5)
        self.play(FadeOut(text5_group))
        self.play(ex_mclaurin_with_i7.animate.shift(UP*0.6+LEFT*0.5))
        self.play(FadeOut(i_prop_group))

        text6 = Text("Consider the following series", font_size=30).shift(LEFT*3.5)
        sinx_mclaurin = MathTex(r"\sin(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots",
                                font_size=40).next_to(text6, DOWN).align_to(text6, LEFT)
        cosx_mclaurin = MathTex(r"\cos(x) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!} = 1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots", 
                                font_size=40).next_to(sinx_mclaurin, DOWN).align_to(sinx_mclaurin, LEFT)
        
        self.play(Write(text6))
        self.wait(0.5)
        self.play(
            Succession(
                Write(sinx_mclaurin),
                Write(cosx_mclaurin),
                run_time=3
            )
        )
        self.wait(1)
        self.play(Unwrite(text6))

        text9 = Text("Notice the series above can be rewritten", font_size=30).shift(LEFT*2.5)
        ex_rewritten1 = MathTex(r"e^{ix}= (1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots)+(ix-\frac{ix^3}{3!}+\frac{ix^5}{5!}-\frac{ix^7}{7!}+\cdots)",
                                font_size=40).shift(UP*3+LEFT)
        
        self.play(Write(text9))
        self.wait(0.5)
        self.play(ReplacementTransform(ex_mclaurin_with_i7, ex_rewritten1))
        self.wait(1)

        text10 = Text("Factor out the", font_size=30)
        i_text3 = eq[0][1].copy().next_to(text10, RIGHT).scale(1.25)
        text10_igroup = VGroup(text10, i_text3).shift(LEFT*4.8)

        self.play(Unwrite(text9))
        self.play(Write(text10_igroup))
        self.wait(0.5)

        ex_rewritten2 = MathTex(r"e^{ix}= (1-\frac{x^2}{2!}+\frac{x^4}{4!}-\frac{x^6}{6!}+\cdots)+i(x-\frac{x^3}{3!}+\frac{x^5}{5!}-\frac{x^7}{7!}+\cdots)",
                                font_size=40).shift(UP*3+LEFT)
        
        self.play(ReplacementTransform(ex_rewritten1, ex_rewritten2))
        self.play(Unwrite(text10_igroup))
        self.wait(0.5)

        cos_brace = Brace(ex_rewritten2[0][4:29], DOWN)
        cosx_copy = cosx_mclaurin[0][0:6].copy()
        sin_brace = Brace(ex_rewritten1[0][33:], DOWN)
        sinx_copy = sinx_mclaurin[0][0:6].copy()

        self.play(GrowFromCenter(cos_brace))
        self.play(Succession(ex_rewritten2[0][5:28].animate.set_fill(LIGHT_PINK),cosx_mclaurin[0][27:].animate.set_fill(LIGHT_PINK),
            cosx_mclaurin[0][0:6].animate.set_fill(YELLOW), cosx_copy.animate.set_fill(YELLOW)))
        self.play(cosx_copy.animate.next_to(cos_brace, DOWN, buff=0.2))

        self.play(GrowFromCenter(sin_brace))
        self.play(Succession(ex_rewritten2[0][32:55].animate.set_fill(TEAL_C),sinx_mclaurin[0][31:].animate.set_fill(TEAL_C),
                             sinx_mclaurin[0][0:6].animate.set_fill(YELLOW),sinx_copy.animate.set_fill(YELLOW),
                             ))
        self.play(sinx_copy.animate.next_to(sin_brace, DOWN, buff=0.2)) 


        text11 = Text("Therefore a simplification can be made", font_size=30).shift(UP*0.5)

        self.play(Write(text11))
        self.wait(1)
        self.play(Unwrite(text11))
        self.play(Succession(
            FadeOut(sinx_mclaurin, cosx_mclaurin),
            FadeOut(cos_brace, sin_brace)
            )
        )
        self.play(cosx_copy.animate.set_fill(WHITE), 
                  sinx_copy.animate.set_fill(WHITE),
                  FadeOut(ex_rewritten2[0][4:29], ex_rewritten2[0][31:]))
        self.play(cosx_copy.animate.next_to(ex_rewritten2[0][3], RIGHT),
                  ex_rewritten2[0][29:31].animate.shift(LEFT*3.5),
                  sinx_copy.animate.shift(UP*1.3+LEFT*5.2)
        )
        self.wait(1)

        answer_group = VGroup(ex_rewritten2[0][0:4], ex_rewritten2[0][29:31], sinx_copy, cosx_copy)
        self.play(answer_group.animate.move_to(ORIGIN))
        text12 = Text("Make the substituion for ", font_size = 30).shift(UP)
        x_pi = MathTex(r"x=\pi", font_size=40).next_to(text12, RIGHT)
        x_pi_text12_group = VGroup(text12, x_pi)

        self.play(Write(x_pi_text12_group))
        self.wait(0.5)

        answer1 = MathTex(r"e^{i\pi}=\cos(\pi)+i\sin(\pi)", font_size = 40)

        self.play(ReplacementTransform(answer_group, answer1))
        self.play(Unwrite(x_pi_text12_group))
        self.wait(1)
        

        cos_pi_brace = Brace(answer1[0][4:10], DOWN)
        sin_pi_brace = Brace(answer1[0][11:], DOWN)
        cos_pi_ans = MathTex(r"-1", font_size=40).next_to(cos_pi_brace, DOWN)
        sin_pi_ans = MathTex(r"0", font_size=40).next_to(sin_pi_brace, DOWN)

        self.play(
            Succession
                (GrowFromCenter(cos_pi_brace),
                Write(cos_pi_ans)
            )
        )
        self.play(
            Succession
                (GrowFromCenter(sin_pi_brace),
                Write(sin_pi_ans)
            )
        )
        self.wait(0.5)

        self.play(FadeOut(cos_pi_brace, cos_pi_ans, sin_pi_brace, sin_pi_ans))

        answer2 = MathTex(r"e^{i\pi}=-1+0", font_size=40)
        answer3 = MathTex(r"e^{i\pi}=-1", font_size=40).set_color(YELLOW)
        sr = SurroundingRectangle(answer3, color=YELLOW)
        final_text = Text("Q.E.D", font_size=30).shift(DOWN)

        self.play(ReplacementTransform(answer1, answer2))
        self.wait(0.5)
        self.play(ReplacementTransform(answer2, answer3))
        self.play(Create(sr))
        self.wait(0.5)
        self.play(Write(final_text))
        self.wait(2)
                          
     


        
        
        

