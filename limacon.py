import manim as bb
import numpy as np
import functools

# converts given polar function from polar to rectangular
def parametric_func(t, polar_func):
    r = polar_func(t)
    return [
        r * np.cos(t),
        r * np.sin(t),
        0
    ]

class LimaconScene(bb.Scene):

    def construct(self):

        def plot_polar_curve(polar_func, color = bb.RED, t_range = [0, 2 * bb.PI]):
            
            fn = functools.partial(parametric_func, polar_func = polar_func)
            
            # creates polar curve by putting x and y into a parametric function
            polar_curve = bb.ParametricFunction(
                fn,
                t_range = t_range,
                color = color
            )

            return polar_curve
        
        self.add(bb.NumberPlane())

        intro1 = bb.Tex("The next types of curves we will look at are limacons.").shift(bb.UP * 3)
        intro2 = bb.Tex(r"Limacons are described by the formulas $a + b \cdot \sin{(\theta)}$ and $a + b \cdot \cos{(\theta)}$.",
                        font_size = 35).move_to(intro1)
        intro3 = bb.Tex(r"The shape of the limacon depends on the ratio of $a$ to $b$.").move_to(intro1)
        intro4 = bb.Tex("The limacons all share a few common features no matter their shape.",
                        font_size = 40).move_to(intro1)
        intro5 = bb.Tex(r"The first is that the sign of $a$ does not affect the shape.").move_to(intro1)
        intro6 = bb.Tex(r"The second is that sinusoidal limacons will always intersect the x-axis at $(-|a|, 0) and (|a|, 0)$.",
                        font_size = 40).move_to(intro1)
        intro7 = bb.Tex(r"Cosine limacons will intersect the y-axis at $(0, -|a|) and (0, |a|)$.").move_to(intro1)
        intro8 = bb.Tex('There are three main types of limacons, the first of which are "looped".', font_size = 35).move_to(intro1)
        
        self.play(bb.Write(intro1))
        self.wait(2)
        self.play(bb.FadeOut(intro1))
        self.play(bb.Write(intro2))
        self.wait(2)
        self.play(bb.FadeOut(intro2))
        self.play(bb.Write(intro3))
        self.wait(2)
        self.play(bb.FadeOut(intro3))
        self.play(bb.Write(intro4))
        self.wait(2)
        self.play(bb.FadeOut(intro4))
        self.play(bb.Write(intro5))
        self.wait(2)
        self.play(bb.FadeOut(intro5))
        self.play(bb.Write(intro6))
        self.wait(2)
        self.play(bb.FadeOut(intro6))
        self.play(bb.Write(intro7))
        self.wait(2)
        self.play(bb.FadeOut(intro7))
        self.play(bb.Write(intro8))
        self.wait(2)
        self.play(bb.FadeOut(intro8))
        
        def cos_lima_looped_pos(theta):
            r = 0.5 + 1.5 * np.cos(theta)
            return r

        def cos_lima_looped_neg(theta):
            r = 0.5 - 1.5 * np.cos(theta)
            return r
        
        def sin_lima_looped_pos(theta):
            r = 0.5 + 1.5 * np.sin(theta)
            return r
        
        def sin_lima_looped_neg(theta):
            r = 0.5 - 1.5 * np.sin(theta)
            return r
        
        cos_loop_plot_p = plot_polar_curve(cos_lima_looped_pos, color = bb.GOLD)
        cos_loop_func_txt_p = bb.MathTex(r"\frac{1}{2} + \frac{3}{2} \cdot \cos{(\theta)}").next_to(cos_loop_plot_p, direction = bb.UP)
        cos_loop_plot_n = plot_polar_curve(cos_lima_looped_neg, color = bb.GOLD)
        cos_loop_func_txt_n = bb.MathTex(r"\frac{1}{2} - \frac{3}{2} \cdot \cos{(\theta)}").next_to(cos_loop_plot_n, direction = bb.UP)
        sin_loop_plot_p = plot_polar_curve(sin_lima_looped_pos)
        sin_loop_func_txt_p = bb.MathTex(r"\frac{1}{2} + \frac{3}{2} \cdot \sin{(\theta)}").next_to(sin_loop_plot_p, direction = bb.RIGHT)
        sin_loop_plot_n = plot_polar_curve(sin_lima_looped_neg)
        sin_loop_func_txt_n = bb.MathTex(r"\frac{1}{2} - \frac{3}{2} \cdot \sin{(\theta)}").next_to(sin_loop_plot_n, direction = bb.LEFT)

        self.play(bb.Create(sin_loop_plot_p), bb.Write(sin_loop_func_txt_p))

        sin_txt_loop1 = bb.Tex("This looped limacon is described by the equation below.").move_to(intro1)
        sin_txt_loop2 = bb.Tex(r"Sinusoidal looped limacons are described by the formula $a + b \cdot \sin{(\theta)}$, where $|b| > |a|$.",
                               font_size = 35).move_to(intro1)
        sin_txt_loop3 = bb.Tex(r"If $b$ is positive, then the limacon will point upwards.").move_to(intro1)
        sin_txt_loop4 = bb.Tex(r"The outermost loop will intersect with the y-axis at $(0, |a| + |b|)$.", 
                               font_size = 42).move_to(intro1)
        sin_txt_loop5 = bb.Tex(r"The innermost loop will intersect with the y-axis at $(0, |b| - |a|)$.",
                               font_size = 42).move_to(intro1)
        sin_txt_loop6 = bb.Tex(r"If $b$ is negative, then the limacon will point downwards.").move_to(intro1)
        sin_txt_loop7 = bb.Tex(r"The outermost loop will intersect with the y-axis at $(0, -(|a| + |b|))$.",
                               font_size = 42).move_to(intro1)
        sin_txt_loop8 = bb.Tex(r"The innermost loop will intersect with the y-axis at $(0, -(|b| - |a|))$.",
                               font_size = 42).move_to(intro1)

        self.play(bb.Write(sin_txt_loop1))
        self.wait(2)
        self.play(bb.FadeOut(sin_txt_loop1))
        self.play(bb.Write(sin_txt_loop2))
        self.wait(3)
        self.play(bb.FadeOut(sin_txt_loop2))
        self.play(bb.Write(sin_txt_loop3))
        self.wait(2)
        self.play(bb.FadeOut(sin_txt_loop3))
        self.play(bb.Write(sin_txt_loop4))
        self.wait(2)
        self.play(bb.FadeOut(sin_txt_loop4))
        self.play(bb.Write(sin_txt_loop5))
        self.wait(2)
        self.play(bb.Transform(sin_loop_plot_p, sin_loop_plot_n), 
                  bb.Transform(sin_loop_func_txt_p, sin_loop_func_txt_n),
                  bb.FadeOut(sin_txt_loop5))
        self.play(bb.Write(sin_txt_loop6))
        self.wait(2)
        self.play(bb.FadeOut(sin_txt_loop6))
        self.play(bb.Write(sin_txt_loop7))
        self.wait(2)
        self.play(bb.FadeOut(sin_txt_loop7))
        self.play(bb.Write(sin_txt_loop8))
        self.wait(2)
        self.play(bb.FadeOut(sin_txt_loop8), bb.Uncreate(sin_loop_plot_p), bb.Uncreate(sin_loop_func_txt_p))
        self.wait(0.2)

        self.play(bb.Create(cos_loop_plot_p), bb.Write(cos_loop_func_txt_p))

        cos_txt_loop1 = bb.Tex(r"Cosine looped limacons are described by the formula $a + b \cdot \cos{(\theta)}$, where $|b| > |a|$.",
                               font_size = 35).move_to(intro1)
        cos_txt_loop2 = bb.Tex(r"If $b$ is positive, then the limacon will point to the right.").move_to(intro1)
        cos_txt_loop3 = bb.Tex(r"The outermost loop will intersect with the x-axis at $(|a| + |b|, 0)$.", 
                               font_size = 42).move_to(intro1)
        cos_txt_loop4 = bb.Tex(r"The innermost loop will intersect with the x-axis at $(|b| - |a|, 0)$.",
                               font_size = 42).move_to(intro1)
        cos_txt_loop5 = bb.Tex(r"If $b$ is negative, then the limacon will point to the left.").move_to(intro1)
        cos_txt_loop6 = bb.Tex(r"The outermost loop will intersect with the x-axis at $(-(|a| + |b|), 0)$.",
                               font_size = 42).move_to(intro1)
        cos_txt_loop7 = bb.Tex(r"The innermost loop will intersect with the x-axis at $(-(|b| - |a|), 0)$.",
                               font_size = 42).move_to(intro1)

        self.play(bb.Write(cos_txt_loop1))
        self.wait(3)
        self.play(bb.FadeOut(cos_txt_loop1))
        self.play(bb.Write(cos_txt_loop2))
        self.wait(2)
        self.play(bb.FadeOut(cos_txt_loop2))
        self.play(bb.Write(cos_txt_loop3))
        self.wait(2)
        self.play(bb.FadeOut(cos_txt_loop3))
        self.play(bb.Write(cos_txt_loop4))
        self.wait(2)
        self.play(bb.Transform(cos_loop_plot_p, cos_loop_plot_n), 
                  bb.Transform(cos_loop_func_txt_p, cos_loop_func_txt_n),
                  bb.FadeOut(cos_txt_loop4))
        self.play(bb.Write(cos_txt_loop5))
        self.wait(2)
        self.play(bb.FadeOut(cos_txt_loop5))
        self.play(bb.Write(cos_txt_loop6))
        self.wait(2)
        self.play(bb.FadeOut(cos_txt_loop6))
        self.play(bb.Write(cos_txt_loop7))
        self.wait(2)
        self.play(bb.FadeOut(cos_txt_loop7), bb.Uncreate(cos_loop_plot_p), bb.Uncreate(cos_loop_func_txt_p))
        self.wait(0.2)

        card_intro1 = bb.Tex("The next type of limacons we will look at are cardioids, named for their heart shape.",
                             font_size = 40).move_to(intro1)
        card_intro2 = bb.Tex(r"Cardioids are formed when $|\frac{a}{b}| = 1$.").move_to(intro1)

        self.play(bb.Write(card_intro1))
        self.wait(2)
        self.play(bb.FadeOut(card_intro1))
        self.play(bb.Write(card_intro2))
        self.wait(2)
        self.play(bb.FadeOut(card_intro2))

        def cos_lima_card_pos(theta):
            r = 0.5 + 0.5 * np.cos(theta)
            return r
        
        def cos_lima_card_neg(theta):
            r = 0.5 - 0.5 * np.cos(theta)
            return r
        
        def sin_lima_card_pos(theta):
            r = 0.5 + 0.5 * np.sin(theta)
            return r
        
        def sin_lima_card_neg(theta):
            r = 0.5 - 0.5 * np.sin(theta)
            return r
        
        cos_card_plot_p = plot_polar_curve(cos_lima_card_pos, color = bb.GOLD)
        cos_card_func_txt_p = bb.MathTex(r"\frac{1}{2} + \frac{1}{2} \cdot \cos{(\theta)}").next_to(cos_card_plot_p, direction = bb.UP)
        cos_card_plot_n = plot_polar_curve(cos_lima_card_neg, color = bb.GOLD)
        cos_card_func_txt_n = bb.MathTex(r"\frac{1}{2} - \frac{1}{2} \cdot \cos{(\theta)}").next_to(cos_card_plot_n, direction = bb.UP)
        sin_card_plot_p = plot_polar_curve(sin_lima_card_pos)
        sin_card_func_txt_p = bb.MathTex(r"\frac{1}{2} + \frac{1}{2} \cdot \sin{(\theta)}").next_to(sin_card_plot_p, direction = bb.RIGHT)
        sin_card_plot_n = plot_polar_curve(sin_lima_card_neg)
        sin_card_func_txt_n = bb.MathTex(r"\frac{1}{2} - \frac{3}{2} \cdot \sin{(\theta)}").next_to(sin_card_plot_n, direction = bb.LEFT)

        card_txt1 = bb.Tex("As they are also a type of limacon, cardioids have similar patterns to looped limacons.",
                           font_size = 38).move_to(intro1)
        card_txt2 = bb.Tex(r"Sinusoidal cardioids will point upwards if $b$ is positive.").move_to(intro1)
        card_txt3 = bb.Tex(r"They intersect with the y-axis at $(0, |a| + |b|)$.").move_to(intro1)
        card_txt4 = bb.Tex(r"If $b$ is negative, the cardioid will point downwards.").move_to(intro1)
        card_txt5 = bb.Tex(r"It will intersect with the y-axis at $(0, -(|a| + |b|))$.").move_to(intro1)

        card_txt6 = bb.Tex(r"Cosine cadioids will point to the right if $b$ if is positive.").move_to(intro1)
        card_txt7 = bb.Tex(r"They intersect with the x-axis at $(|a| + |b|, 0)$.").move_to(intro1)
        card_txt8 = bb.Tex(r"If $b$ is negative, the cardioid will point to the left.").move_to(intro1)
        card_txt9 = bb.Tex(r"It will intersect with the x-axis at $(-(|a| + |b|), 0)$.").move_to(intro1)


        self.play(bb.Write(card_txt1))
        self.wait(2)
        self.play(bb.FadeOut(card_txt1))
        self.wait(0.1)
        self.play(bb.Write(card_txt2), bb.Create(sin_card_plot_p), bb.Write(sin_card_func_txt_p))
        self.wait(2)
        self.play(bb.FadeOut(card_txt2))
        self.play(bb.Write(card_txt3))
        self.wait(2)
        self.play(bb.FadeOut(card_txt3))
        self.play(bb.Write(card_txt4), bb.Transform(sin_card_plot_p, sin_card_plot_n), bb.Transform(sin_card_func_txt_p, sin_card_func_txt_n))
        self.wait(2)
        self.play(bb.FadeOut(card_txt4))
        self.play(bb.Write(card_txt5))
        self.wait(2)
        self.play(bb.FadeOut(card_txt5))
        self.play(bb.Write(card_txt6), bb.Transform(sin_card_plot_p, cos_card_plot_p), bb.Transform(sin_card_func_txt_p, cos_card_func_txt_p))
        self.wait(2)
        self.play(bb.FadeOut(card_txt6))
        self.play(bb.Write(card_txt7))
        self.wait(2)
        self.play(bb.FadeOut(card_txt7))
        self.play(bb.Write(card_txt8), bb.Transform(sin_card_plot_p, cos_card_plot_n), bb.Transform(sin_card_func_txt_p, cos_card_func_txt_n))
        self.wait(2)
        self.play(bb.FadeOut(card_txt8))
        self.play(bb.Write(card_txt9))
        self.wait(2)
        self.play(bb.FadeOut(card_txt9), bb.Uncreate(sin_card_plot_p), bb.Uncreate(sin_card_func_txt_p))
        self.wait(0.2)

        dimp_intro1 = bb.Tex("The final type of limacon to look at are dimpled limacons.").move_to(intro1)
        dimp_intro2 = bb.Tex(r"Dimpled limcaons are formed when $|\frac{a}{b}| > 1$.").move_to(intro1)

        self.play(bb.Write(dimp_intro1))
        self.wait(2)
        self.play(bb.FadeOut(dimp_intro1))
        self.play(bb.Write(dimp_intro2))
        self.wait(2)
        self.play(bb.FadeOut(dimp_intro2))
        self.wait(0.2)

        def cos_lima_dimp_pos(theta):
            r = 1 + 0.5 * np.cos(theta)
            return r
        
        def cos_lima_dimp_neg(theta):
            r = 1 - 0.5 * np.cos(theta)
            return r
        
        def sin_lima_dimp_pos(theta):
            r = 1 + 0.5 * np.sin(theta)
            return r
        
        def sin_lima_dimp_neg(theta):
            r = 1 - 0.5 * np.sin(theta)
            return r
        
        cos_dimp_plot_p = plot_polar_curve(cos_lima_dimp_pos, color = bb.GOLD)
        cos_dimp_func_txt_p = bb.MathTex(r"1 + \frac{1}{2} \cdot \cos{(\theta)}").next_to(cos_dimp_plot_p, direction = bb.UP)
        cos_dimp_plot_n = plot_polar_curve(cos_lima_dimp_neg, color = bb.GOLD)
        cos_dimp_func_txt_n = bb.MathTex(r"1 - \frac{1}{2} \cdot \cos{(\theta)}").next_to(cos_dimp_plot_n, direction = bb.UP)
        sin_dimp_plot_p = plot_polar_curve(sin_lima_dimp_pos)
        sin_dimp_func_txt_p = bb.MathTex(r"1 + \frac{1}{2} \cdot \sin{(\theta)}").next_to(sin_dimp_plot_p, direction = bb.RIGHT)
        sin_dimp_plot_n = plot_polar_curve(sin_lima_dimp_neg)
        sin_dimp_func_txt_n = bb.MathTex(r"1 - \frac{3}{2} \cdot \sin{(\theta)}").next_to(sin_dimp_plot_n, direction = bb.LEFT)

        dimp_txt1 = bb.Tex(r"Sinusoidal dimpled limacons will point upwards if $b$ is positive.",
                           font_size = 42).move_to(intro1)
        dimp_txt2 = bb.Tex(r"They intersect with the y-axis at $(0, |a| + |b|)$ and $(0, |b| - |a|)$.").move_to(intro1)
        dimp_txt3 = bb.Tex(r"If $b$ is negative, the limacon will point downwards.").move_to(intro1)
        dimp_txt4 = bb.Tex(r"It will intersect with the y-axis at $(0, -(|a| + |b|))$ and $(0, -(|b| - |a|))$.",
                           font_size = 40).move_to(intro1)
        dimp_txt5 = bb.Tex(r"Cosine dimpled limacons will point to the right if $b$ if is positive.",
                           font_size = 42).move_to(intro1)
        dimp_txt6 = bb.Tex(r"They intersect with the x-axis at $(|a| + |b|, 0)$.").move_to(intro1)
        dimp_txt7 = bb.Tex(r"If $b$ is negative, the cardioid will point to the left.").move_to(intro1)
        dimp_txt8 = bb.Tex(r"It will intersect with the x-axis at $(-(|a| + |b|), 0)$.").move_to(intro1)

        self.play(bb.Write(dimp_txt1), bb.Create(sin_dimp_plot_p), bb.Write(sin_dimp_func_txt_p))
        self.wait(2)
        self.play(bb.FadeOut(dimp_txt1))
        self.play(bb.Write(dimp_txt2))
        self.wait(2)
        self.play(bb.FadeOut(dimp_txt2))
        self.play(bb.Write(dimp_txt3), bb.Transform(sin_dimp_plot_p, sin_dimp_plot_n), bb.Transform(sin_dimp_func_txt_p, sin_dimp_func_txt_n))
        self.wait(2)
        self.play(bb.FadeOut(dimp_txt3))
        self.play(bb.Write(dimp_txt4))
        self.wait(2)
        self.play(bb.FadeOut(dimp_txt4))
        self.play(bb.Write(dimp_txt5), bb.Transform(sin_dimp_plot_p, cos_dimp_plot_p), bb.Transform(sin_dimp_func_txt_p, cos_dimp_func_txt_p))
        self.wait(2)
        self.play(bb.FadeOut(dimp_txt5))
        self.play(bb.Write(dimp_txt6))
        self.wait(2)
        self.play(bb.FadeOut(dimp_txt6))
        self.play(bb.Write(dimp_txt7), bb.Transform(sin_dimp_plot_p, cos_dimp_plot_n), bb.Transform(sin_dimp_func_txt_p, cos_dimp_func_txt_n))
        self.wait(2)
        self.play(bb.FadeOut(dimp_txt7))
        self.play(bb.Write(dimp_txt8))
        self.wait(2)
        self.play(bb.FadeOut(dimp_txt8), bb.Uncreate(sin_dimp_plot_p), bb.Uncreate(sin_dimp_func_txt_p))
        self.wait(0.1)