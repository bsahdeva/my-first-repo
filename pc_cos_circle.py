import manim as bb
import numpy as np
import functools


# converts given polar function from polar to rectangular
def parametric_func(t, polar_func):
    r = polar_func(t)
    return [r * np.cos(t), r * np.sin(t), 0]


class CircleScene(bb.Scene):

    def construct(self):

        def plot_polar_curve(polar_func, color=bb.RED, t_range=[0, 2 * bb.PI]):

            fn = functools.partial(parametric_func, polar_func=polar_func)

            # creates polar curve by putting x and y into a parametric function
            polar_curve = bb.ParametricFunction(fn, t_range=t_range, color=color)

            return polar_curve

        def curve_tracing_vector(
            polar_func, theta: float, tip_length=0.15, tip_width=0.15, arc_radius=0.5
        ):

            fn = functools.partial(parametric_func, polar_func=polar_func)

            vector = bb.Line(start=bb.ORIGIN, end=fn(theta)).add_tip(
                tip_length=tip_length, tip_width=tip_width
            )
            angle = bb.Arc(angle=theta, radius=arc_radius)

            return bb.VGroup(vector, angle)

        def unit_circle(theta):
            r = 1
            return r

        def circle(theta):
            r = 2
            return r

        def cos_unit_circle_pos(theta):
            r = 2 * np.cos(theta)
            return r

        def cos_unit_circle_neg(theta):
            r = -2 * np.cos(theta)
            return r

        def sin_unit_circle_pos(theta):
            r = 2 * np.sin(theta)
            return r

        def sin_unit_circle_neg(theta):
            r = -2 * np.sin(theta)
            return r

        # self.play(bb.Create(bb.NumberPlane()))
        self.add(bb.NumberPlane())

        # intro = bb.Tex("The first polar curves we will look at are simple circles.").shift(bb.UP * 3)
        # intro_rect = bb.SurroundingRectangle(intro, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)
        intro = bb.Tex(
            r"The next circles we will look at are described by $r(\theta) = 2a \cdot \cos{(\theta)}$, where $a$ is a constant.",
            font_size=35,
        ).shift(bb.UP * 3)
        intro_rect = bb.SurroundingRectangle(intro, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        self.add(intro_rect)
        self.play(bb.Write(intro))
        self.wait(2)

        cos_unit_circle_plot_pos = plot_polar_curve(
            polar_func=cos_unit_circle_pos, color=bb.GOLD
        )
        cos_func_txt_pos = bb.Tex(
            r"$r(\theta) = 2a \cdot \cos{(\theta)}$, where $a = 1$"
        ).next_to(cos_unit_circle_plot_pos, direction=bb.UP)
        pcos_line = bb.Line([0, 0, 0], [1, 0, 0])
        pcos_len_brace = bb.Brace(pcos_line, sharpness=1).shift(bb.UP * 0.2)
        a2_txt = bb.MathTex("a", font_size=38).next_to(
            pcos_len_brace, direction=bb.DOWN
        )
        cos_unit_circle_plot_neg = plot_polar_curve(
            polar_func=cos_unit_circle_neg, color=bb.GOLD
        )
        cos_func_txt_neg = bb.Tex(
            r"$r(\theta) = 2a \cdot \cos{(\theta)}$, where $a = -1$"
        ).next_to(cos_unit_circle_plot_neg, direction=bb.UP)
        ncos_line = bb.Line([0, 0, 0], [-1, 0, 0])
        ncos_len_brace = bb.Brace(ncos_line, sharpness=1).shift(bb.UP * 0.2)

        cos_txt2 = bb.Tex(
            r"These circles have radius $a$, with a center that lies $a$ units from the origin along the x-axis.",
            font_size=35,
        ).move_to(intro)
        cos_rect2 = bb.SurroundingRectangle(cos_txt2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        cos_txt3 = bb.Tex(
            r"If $a$ is positive, the center will be $a$ units to the right of the origin.",
            font_size=40,
        ).move_to(intro)
        cos_rect3 = bb.SurroundingRectangle(cos_txt3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        cos_txt4 = bb.Tex(
            r"If $a$ is negative, the center will be $a$ units to the left of the origin.",
            font_size=40,
        ).move_to(intro)
        cos_rect4 = bb.SurroundingRectangle(cos_txt4, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.play(
            bb.Create(cos_unit_circle_plot_pos),
            bb.Write(cos_func_txt_pos),
            bb.Create(pcos_len_brace),
            bb.Write(a2_txt),
        )
        self.wait(2)
        self.play(bb.Transform(intro_rect, cos_rect2), bb.FadeOut(intro))
        self.play(bb.Write(cos_txt2))
        self.wait(2)
        self.play(bb.Transform(intro_rect, cos_rect3), bb.FadeOut(cos_txt2))
        self.play(bb.Write(cos_txt3))
        self.wait(2)
        self.play(
            bb.Transform(intro_rect, cos_rect4),
            bb.Transform(cos_unit_circle_plot_pos, cos_unit_circle_plot_neg),
            bb.Transform(cos_func_txt_pos, cos_func_txt_neg),
            bb.Transform(pcos_len_brace, ncos_len_brace),
            a2_txt.animate.next_to(ncos_len_brace, direction=bb.DOWN),
            bb.FadeOut(cos_txt3),
        )
        self.play(bb.Write(cos_txt4))
        self.wait(3)
