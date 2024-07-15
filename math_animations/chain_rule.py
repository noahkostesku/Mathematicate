from manim import *

class LimitLaws(Scene):
    def construct(self):

        title = Text("Chain Rule").shift(3 * UP) 
        main_text = MathTex(r"y=f(g(x))", font_size=70).next_to(title, DOWN, buff=2)
        other_text = Text("Inner and Outer Function", font_size=50).next_to(main_text, DOWN, buff=2)

        self.play(Write(title, run_time=2))
        self.wait(0.5)
        self.play(Write(main_text, run_time=2))
        self.wait(0.5)
        self.play(Write(other_text, run_time=2))
        self.wait(0.5)

        self.play(FadeOut(title), FadeOut(other_text))
        self.wait(1)

        self.play(main_text.animate.shift(LEFT * 4))
        self.wait(0.5)

        derivative_rule = Text("Derivative Rule").shift(3*UP)
        self.play(Write(derivative_rule))
        self.wait(0.5)
        
        arrow = Arrow(start=LEFT, end=RIGHT).next_to(main_text, RIGHT, buff=0.5)
        equation = MathTex(r"y'=f'(g(x)) \cdot g'(x)", font_size=70).next_to(arrow, RIGHT, buff=0.5)

        self.play(GrowArrow(arrow))
        self.play(Write(equation))
        self.wait(1)

        self.play(FadeOut(derivative_rule))

        formula_group = VGroup(main_text, arrow, equation)
        self.play(formula_group.animate.shift(2.5*UP).scale(0.5))
        
        step_0 = Text("Steps:", font_size=36)
        
        text_part_1 = Text("1. Identify ", font_size=36)
        math_part_1 = MathTex("f", font_size=36)
        text_part_2 = Text(" and ", font_size=36)
        math_part_2 = MathTex("g(x)", font_size=36)
        step_1 = VGroup(text_part_1, math_part_1, text_part_2, math_part_2).arrange(RIGHT, buff=0.1)
        
        text_part_3 = Text("2. Differentiate ", font_size=36)
        math_part_3 = MathTex("f", font_size=36)
        text_part_4 = Text(" and ", font_size=36)
        math_part_4 = MathTex("g(x)", font_size=36)
        step_2 = VGroup(text_part_3, math_part_3, text_part_4, math_part_4).arrange(RIGHT, buff=0.1)
        
        text_part_5 = Text("3. Apply the chain rule ", font_size=36)
        math_part_5 = MathTex(r"(f \circ g)'(x) = f'(g(x)) \cdot g'(x)", font_size=36)
        step_3 = VGroup(text_part_5, math_part_5).arrange(RIGHT, buff=0.1)
        
        text_part_6 = Text("4. Combine product and simplify", font_size=36)
        step_4 = VGroup(text_part_6).arrange(RIGHT, buff=0.1)

        # Create a VGroup with all steps
        steps_group = VGroup(step_0, step_1, step_2, step_3, step_4).arrange(DOWN, buff=0.4)

        # Add each step to the scene
        for step in steps_group:
            self.play(Write(step))
            self.wait(0.5)

        # Add a SurroundingRectangle to the group
        surround_rec1 = SurroundingRectangle(steps_group, color=YELLOW, buff=0.3)

        # Add the surrounding rectangle to the scene
        self.play(Create(surround_rec1))

        # Create a VGroup containing the steps and the surrounding rectangle
        rec_steps_group = VGroup(steps_group, surround_rec1)

        # Animate shifting and scaling of the group
        self.play(FadeOut(formula_group))
        self.play(rec_steps_group.animate.shift(4.6*RIGHT+2.7*UP).scale(0.45))

        self.wait(1)
        
        self.play(FadeOut(surround_rec1))

        eq1 = MathTex(r"f(x)=e^{x^2+2x+1}", font_size=36)
        f_of_g = MathTex(r"=f(g(x))", font_size = 36).next_to(eq1, RIGHT, buff=0.1)
        
        final_group = VGroup(eq1, f_of_g).shift(UP*3+LEFT*4)
        self.play(Write(final_group))
        self.wait(0.5)

        self.play(Circumscribe(step_1, run_time=1.5, color=WHITE))

        first_brace = Brace(eq1[0][5], DOWN)
        second_brace = Brace(eq1[0][6:], DOWN, buff=0.2)
        first_text = MathTex(r"f", font_size=30).next_to(first_brace, DOWN, buff=0.1)
        second_text  = MathTex(r'g(x)', font_size=30).next_to(second_brace, DOWN, buff=0.1)

        self.play(GrowFromCenter(first_brace))
        self.play(Write(first_text))
        self.wait(0.5)
        self.play(GrowFromCenter(second_brace))
        self.play(Write(second_text))
        self.wait(2)
        self.play(FadeOut(first_brace, second_brace, first_text, second_text))

        arrow4 = Arrow(start=UP, end=DOWN).next_to(final_group, DOWN, buff=0.2).shift(LEFT*1.7)
        diff_text = MathTex(r"f(g(x)) \cdot g'(x)&=e^{x^2+2x+1}\\ f'(g(x))\cdot g'(x)&=e'^{(x^2+2x+1)}\\ f'(g(x))\cdot g'(x)&=e^{x^2+2x+1} \cdot (x^2+2x+1)'\\ f'(g(x))\cdot g'(x)&=e^{x^2+2x+1} \cdot (2x+2)", 
                            font_size=36).next_to(arrow4, DOWN, buff=0.2).shift(RIGHT*2)
        diff_text[0][82:].set_color(YELLOW)
        next_vgroup = VGroup(step_2,step_3, step_4)
        self.play(Circumscribe(next_vgroup, run_time=5, color=WHITE))
        self.play(GrowArrow(arrow4))
        self.play(Write(diff_text, run_time=6))
        self.wait(1)
        
        note0_text = Text("Note: Answer is already simplified", font_size=36).next_to(diff_text, DOWN, buff=0.8).shift(RIGHT*0.5)
        self.play(Write(note0_text))
        self.wait(1)

        surround_rec2 = SurroundingRectangle(diff_text[0][82:], color=YELLOW)
        self.play(Create(surround_rec2, run_time=1.5))
        self.wait(1)

        answer1 = VGroup(diff_text[0][82:], surround_rec2)
        self.play(FadeOut(arrow4, diff_text[0][:82], note0_text))
        self.wait(0.5)
        self.play(answer1.animate.next_to(final_group, DOWN, buff=0.2).align_to(LEFT))
        self.wait(0.5)

        brace_outer = Brace(answer1[0][15:23], DOWN)
        brace_inner = Brace(answer1[0][24:], DOWN)
        brace_out_text = Text("Outer\nDerivative", font_size=25).next_to(brace_outer, DOWN, buff=0.1)
        brace_in_text = Text("Inner\nDerivative", font_size=25).next_to(brace_inner, DOWN, buff=0.1)

        self.play(GrowFromCenter(brace_outer), GrowFromCenter(brace_inner))
        self.play(Write(brace_out_text), Write(brace_in_text))
        self.wait(1.5)
        self.play(FadeOut(brace_outer, brace_inner, brace_out_text, brace_in_text))
        self.wait(1)

        answer1_group = VGroup(answer1, eq1, f_of_g)
        self.play(answer1_group.animate.shift(LEFT*2+UP*0.5).scale(0.5))
        self.wait(1)

        ex_2_text = Text("Example 2:", font_size=25)
        ex_2_math = MathTex(r"f(x)=\sin(\sqrt{x})", font_size=37)
        ex_2_both = VGroup(ex_2_text, ex_2_math).arrange(RIGHT, buff=0.1).shift(4.2*LEFT+UP*1.5)
        self.play(Write(ex_2_both))
        self.wait(0.5)
        self.play(FadeOut(ex_2_text))
        self.play(ex_2_math.animate.shift(LEFT*1.5))
        self.wait(1)

        brace2_down = Brace(ex_2_math[0][5:8], DOWN)
        brace2_up = Brace(ex_2_math[0][8:], UP)
        brace2_down2 = Brace(ex_2_math[0][8:], DOWN)
        brace2_up2 = Brace(ex_2_math[0][5:], UP)

        self.play(Circumscribe(step_1, color=WHITE), run_time=2)
        self.wait(0.5)

        brace2_down_text = MathTex(r"f", font_size=25).next_to(brace2_down, DOWN, buff=0.1)
        brace2_up_text = MathTex(r"u", font_size=25).next_to(brace2_up, UP, buff=0.1)
        brace2_down2_text = MathTex(r"g(x)", font_size=25).next_to(brace2_down2, DOWN, buff=0.1)
        brace2_up2_text = MathTex(r"\sin(u)", font_size=25).next_to(brace2_up2, UP, buff=0.1)

        upper_arrow = Arrow(start=LEFT, end=RIGHT).next_to(brace2_up2_text, RIGHT, buff=0.2)
        lower_arrow = Arrow(start=LEFT, end=RIGHT).next_to(brace2_down2_text, RIGHT, buff=0.2)
        out_func = Text("Outer Function", font_size=16).next_to(upper_arrow, RIGHT, buff=0.2)
        in_func = Text("Inner Function", font_size=16).next_to(lower_arrow, RIGHT, buff=0.2)
        

        self.play(GrowFromCenter(brace2_down), GrowFromCenter(brace2_up))
        self.wait(0.5)
        self.play(Write(brace2_down_text), Write(brace2_up_text))
        self.wait(3)
        self.play(FadeOut(brace2_down, brace2_up, brace2_down_text, brace2_up_text), run_time=1.5)
        self.play(GrowFromCenter(brace2_down2), GrowFromCenter(brace2_up2))
        self.wait(0.5)
        self.play(Write(brace2_up2_text), Write(brace2_down2_text))
        self.play(GrowArrow(upper_arrow), GrowArrow(lower_arrow))
        self.play(Write(out_func), Write(in_func))
        self.wait(2)
        self.play(FadeOut(brace2_down2, brace2_up2, brace2_down2_text, brace2_up2_text, upper_arrow, lower_arrow, out_func, in_func), run_time=1.5)

        self.play(Circumscribe(next_vgroup, color=WHITE, run_time=3))
        self.wait(0.5)

        cos_answer = MathTex(
            r"f'(g(x)) \cdot g'(x)&= \cos'(\sqrt{x}) \\ f'(g(x)) \cdot g'(x)&=cos(\sqrt{x}) \cdot (\sqrt{x})' \\ f'(g(x)) \cdot g'(x)&=cos(\sqrt{x}) \cdot (\frac{1}{2} \cdot x^{-\frac{1}{2}}) \\ f'(g(x)) \cdot g'(x)&=\frac{\cos(\sqrt{x})}{2\sqrt{x}}",
            font_size=37

        ).next_to(ex_2_math, DOWN, buff=0.2).shift(RIGHT*1)
        cos_answer[0][89:].set_color(YELLOW)

        self.play(ex_2_math.animate.shift(RIGHT*0.9))

        self.play(Write(cos_answer, run_time=10))
        self.wait(2)

        surround_rec3 = SurroundingRectangle(cos_answer[0][89:], color=YELLOW)
        answer2 = VGroup(cos_answer[0][89:], surround_rec3)

        self.play(Create(surround_rec3))
        self.wait(1)
        self.play(FadeOut(cos_answer[0][:89]))
        self.wait(0.5)
        self.play(answer2.animate.next_to(ex_2_math, DOWN, buff=0.2).align_to(LEFT))
        self.wait(0.5)

        answer2_group = VGroup(answer2, ex_2_math)

        self.play(answer2_group.animate.next_to(answer1_group, RIGHT, buff=0.7).scale(0.5))
        self.wait(0.5)

        text3 = Text("Notice the recursive pattern of the chain rule", font_size=22)
        text3_1 = Text("The chain rule can be treated as a layering system",font_size=22)
        text3_2 = Text("by starting at the outermost function, taking the derivative of the outermost",font_size=22)
        text3_3 = Text("part only, rewriting the rest of the function, and then multiplying by the derivative",font_size=22)
        text3_4 = Text("of the next layer. This can be applied recursively until the innermost layer is met.",font_size=22)
        text3_5 = Text("Let's see it in practice.", font_size = 22)

        text3_group = VGroup( text3_1, text3_2, text3_3, text3_4, text3_5).arrange(DOWN, buff=0.3)
        self.play(Write(text3))
        self.wait(1)
        self.play(Unwrite(text3))
        self.wait(1)
        self.play(Write(text3_group, run_time=10))
        self.wait(4)
        self.play(FadeOut(text3_group))

        eq3_text = Text("Example 3:", font_size=20)
        eq3 = MathTex(r"f(x)=(\tan(\sin(x^4)))^5", font_size=30)
        eq3_both = VGroup(eq3_text, eq3).arrange(RIGHT, buff=0.1)

        self.play(Write(eq3_both))
        self.wait(1)
        self.play(FadeOut(eq3_text, steps_group))
        self.play(eq3.animate.shift(LEFT))

        br1 = Brace(eq3[0][5:], UP, buff=0.7)
        br2 = Brace(eq3[0][5:19], DOWN, buff=0.7)
        br3 = Brace(eq3[0][10:18], UP, buff=0.05)
        br4 = Brace(eq3[0][14:17], DOWN, buff=0.05)

        br1_text = Text("Layer 1", font_size=15).next_to(br1, UP, buff=0.1)
        br2_text = Text("Layer 2", font_size=15).next_to(br2, DOWN, buff=0.1)
        br3_text = Text("Layer 3", font_size=15).next_to(br3, UP, buff=0.1)
        br4_text = Text("Layer 4", font_size=15).next_to(br4, DOWN, buff=0.1)

        self.play(GrowFromCenter(br1))
        self.play(Write(br1_text))
        self.wait(0.5)
        self.play(GrowFromCenter(br2))
        self.play(Write(br2_text))
        self.wait(0.5)
        self.play(GrowFromCenter(br3))
        self.play(Write(br3_text))
        self.wait(0.5)
        self.play(GrowFromCenter(br4))
        self.play(Write(br4_text))
        self.wait(1)

        under_text = Text("Now the recursive pattern can be applied", font_size=30).shift(DOWN*2.5)
        self.play(Write(under_text))
        self.wait(1)
        self.play(Unwrite(under_text))
        self.play(FadeOut(br1, br2, br3, br4, br1_text, br2_text, br3_text, br4_text))
        
        self.wait(0.5)
        self.play(eq3.animate.shift(LEFT*3+UP*1.5), run_time=2)

        tan_proof = MathTex(r"f'(g(x)) \cdot g'(x)&=5(\tan^4(\sin(x^4))) \cdot \frac{d}{dx}(\tan(\sin(x^4)) \\ f'(g(x))\cdot g'(x)&=5(\tan^4(\sin(x^4))) \cdot \sec^2(\sin(x^4)) \cdot \frac{d}{dx}(\sin(x^4)) \\ f'(g(x))\cdot g'(x)&=5(\tan^4(\sin(x^4))) \cdot \sec^2(\sin(x^4)) \cdot (\cos(x^4)) \cdot \frac{d}{dx}(x^4) \\ f'(g(x))\cdot g'(x)&=5(\tan^4(\sin(x^4))) \cdot \sec^2(\sin(x^4)) \cdot (\cos(x^4)) \cdot 4x^3 \\", font_size=30).next_to(eq3, DOWN, buff=0.2).shift(RIGHT*1.6)
        self.play(Write(tan_proof, run_time=10))
        self.wait(2)
        

        tanbr1 = Brace(tan_proof[0][188:203], DOWN, buff=0.1)
        tanbr2 = Brace(tan_proof[0][204:218], DOWN, buff=0.1)
        tanbr3 = Brace(tan_proof[0][219:227], DOWN, buff=0.1)
        tanbr4 = Brace(tan_proof[0][228:], DOWN, buff=0.1)

        tant1 = Text("Derivative of\n Layer 4 and\n Layers 1, 2, 3", font_size=15).next_to(tanbr1, DOWN, buff=0.1)
        tant2 = Text("Derivative of \nLayer 3\n and Layers\n1, 2", font_size=15).next_to(tanbr2, DOWN, buff=0.1)
        tant3 = Text("Derivative \nof Layer 2 \nand Layer\n 1", font_size=15).next_to(tanbr3, DOWN, buff=0.1)
        tant4 = Text("Derivative of\n Layer 1", font_size=15).next_to(tanbr4, DOWN, buff=0.1).shift(RIGHT*0.2)

        self.play(GrowFromCenter(tanbr1))
        self.play(Write(tant1))
        self.wait(0.5)
        self.play(GrowFromCenter(tanbr2))
        self.play(Write(tant2))
        self.wait(0.5)
        self.play(GrowFromCenter(tanbr3))
        self.play(Write(tant3))
        self.wait(0.5)
        self.play(GrowFromCenter(tanbr4))
        self.play(Write(tant4))
        self.wait(3)
        self.play(FadeOut(tanbr1, tanbr2, tanbr3, tanbr4, tant1, tant2, tant3, tant4))
        self.wait(0.5)

        tan_ans = MathTex(r"f'(g(x))\cdot g'(x)&=20x^3\cos(x^4)\sec^2(\sin(x^4))\tan^4(\sin(x^4))", font_size=30).next_to(tan_proof, DOWN, buff=0.2).shift(LEFT*0.75)
        tan_ans.set_color(YELLOW)
        tan_rec = SurroundingRectangle(tan_ans, color=YELLOW)
        tan_vgroup = VGroup(tan_ans, tan_rec)

        self.play(Write(tan_ans))
        self.wait(0.5)
        self.play(Create(tan_rec, run_time=3))
        self.wait(1)
        self.play(FadeOut(tan_proof))
        self.play(eq3.animate.shift(RIGHT))
        self.play(tan_vgroup.animate.next_to(eq3, DOWN, buff=0.2).align_to(LEFT))
        
        answer3_group = VGroup(tan_vgroup, eq3)
        self.play(answer3_group.animate.next_to(answer2_group, RIGHT, buff=0.7).scale(0.5))
        self.wait(1)

        ans1_ans2 = VGroup(answer1_group, answer2_group)

        last_vgroup = VGroup(answer1_group, answer2_group,answer3_group)

        self.play(ans1_ans2.animate.shift(RIGHT*0.2))
        self.play((last_vgroup.animate.shift(DOWN*3)))
        self.play(answer1_group.animate.shift(RIGHT*1.5), answer3_group.animate.shift(LEFT*2))
        self.play(last_vgroup.animate.scale(1.3))
        self.wait(3)
        self.play(FadeOut(last_vgroup), run_time=2)





