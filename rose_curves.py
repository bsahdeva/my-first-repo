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

class RoseScene(bb.Scene):

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

        intro1 = bb.Tex("The third type of shape we will look at are called rose curves.").shift(bb.UP * 3)
        intro_rect1 = bb.SurroundingRectangle(intro1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro2 = bb.Tex("Rose curves are named such for their flower-like appearance.").move_to(intro1)
        intro_rect2 = bb.SurroundingRectangle(intro2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro3 = bb.Tex(r"Rose curves are defined by $a \cdot \sin(b \cdot \theta)$ and $a \cdot \cos(b \cdot \theta)$.",
                        font_size = 45).move_to(intro1)
        intro_rect3 = bb.SurroundingRectangle(intro3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro4 = bb.Tex(r"$a$ is the distance from the origin to the tip of a petal and $b$ determines the amount of petals.",
                        font_size = 40).move_to(intro1)
        intro_rect4 = bb.SurroundingRectangle(intro4, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        
        self.add(intro_rect1)
        self.play(bb.Write(intro1))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, intro_rect2), bb.FadeOut(intro1))
        self.play(bb.Write(intro2))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, intro_rect3), bb.FadeOut(intro2))
        self.play(bb.Write(intro3))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, intro_rect4), bb.FadeOut(intro3))
        self.play(bb.Write(intro4))
        self.wait(2)

        def cos_rose_2(theta):
            r = np.cos(2 * theta)
            return r

        def cos_rose_3(theta):
            r = np.cos(3 * theta)
            return r
        
        cos_rose_2_plot = plot_polar_curve(cos_rose_2, color = bb.GOLD)
        cos_rose_2_func_txt = bb.MathTex(r"r(\theta) = \cos(2 \cdot \theta)").next_to(cos_rose_2_plot, direction = bb.UP)
        cos_rose_3_plot = plot_polar_curve(cos_rose_3, color = bb.GOLD)
        cos_rose_3_func_txt = bb.MathTex(r"r(\theta) = \cos(3 \cdot \theta)").next_to(cos_rose_3_plot, direction = bb.UP)
        
        rose_txt1 = bb.Tex(r"When $b$ is even, the rose curve will have $b \cdot 2$ petals.").move_to(intro1)
        rose_rect1 = bb.SurroundingRectangle(rose_txt1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        rose_txt2 = bb.Tex(r"When $b$ is odd, the rose curve will have $b$ petals.").move_to(intro1)
        rose_rect2 = bb.SurroundingRectangle(rose_txt2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.play(bb.Transform(intro_rect1, rose_rect1), bb.FadeOut(intro4))
        self.wait(2)
        self.play(bb.Write(rose_txt1), bb.Create(cos_rose_2_plot), bb.Write(cos_rose_2_func_txt))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, rose_rect2), bb.FadeOut(rose_txt1))
        self.play(bb.Write(rose_txt2), bb.Transform(cos_rose_2_plot, cos_rose_3_plot), bb.Transform(cos_rose_2_func_txt, cos_rose_3_func_txt))
        self.wait(2)
        self.play(bb.FadeOut(rose_txt2), bb.Uncreate(cos_rose_2_plot), bb.Uncreate(cos_rose_2_func_txt), bb.Uncreate(intro_rect1))
        self.wait(0.1)