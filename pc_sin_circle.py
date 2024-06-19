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
            r"These circles are described by $r(\theta) = 2a \cdot \sin{(\theta)}$, where $a$ is a constant.",
            font_size=40,
        ).shift(bb.UP * 3)
        intro_rect = bb.SurroundingRectangle(intro, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.add(intro_rect)
        self.play(bb.Write(intro))
        self.wait(2)

        sin_unit_circle_plot_pos = plot_polar_curve(
            polar_func=sin_unit_circle_pos, color=bb.GREEN
        )
        sin_func_txt_pos = bb.Tex(
            r"$r(\theta) = 2a \cdot \sin{(\theta)}$, where $a = 1$"
        ).next_to(sin_unit_circle_plot_pos, direction=bb.DOWN)
        psin_len_brace = bb.BraceBetweenPoints([0, 0, 0], [0, 1, 0], sharpness=1).shift(
            bb.LEFT * 0.2
        )
        a_txt = (
            bb.MathTex("a", font_size=38)
            .next_to(psin_len_brace, direction=bb.RIGHT)
            .shift(bb.LEFT * 0.1)
        )

        sin_txt2 = bb.Tex(
            r"These circles also have radius $a$, with a center that lies $a$ units from the origin along the y-axis.",
            font_size=35,
        ).move_to(intro)
        sin_rect2 = bb.SurroundingRectangle(sin_txt2, color=bb.BLACK).set_fill(
            bb.BLACK,
            opacity=1,
        )
        sin_txt3 = bb.Tex(
            r"If $a$ is positive, the center will be $a$ units above the origin.",
            font_size=40,
        ).move_to(intro)
        sin_rect3 = bb.SurroundingRectangle(sin_txt3, color=bb.BLACK).set_fill(
            bb.BLACK,
            opacity=1,
        )

        self.play(
            bb.Create(sin_unit_circle_plot_pos),
            bb.Write(sin_func_txt_pos),
            bb.Create(psin_len_brace),
            bb.Write(a_txt),
        )
        self.wait(2)
        self.play(bb.Transform(intro_rect, sin_rect2), bb.FadeOut(intro))
        self.play(bb.Write(sin_txt2))
        self.wait(3)
        self.play(bb.Transform(intro_rect, sin_rect3), bb.FadeOut(sin_txt2))
        self.play(bb.Write(sin_txt3))
        self.wait(2)

        sin_unit_circle_plot_neg = plot_polar_curve(
            polar_func=sin_unit_circle_neg, color=bb.GREEN
        )
        sin_func_txt_neg = bb.Tex(
            r"$r(\theta) = 2a \cdot \sin{(\theta)}$, where $a = -1$"
        ).next_to(sin_unit_circle_plot_neg, direction=bb.UP)
        nsin_len_brace = bb.BraceBetweenPoints(
            [0, 0, 0], [0, -1, 0], sharpness=1, direction=bb.LEFT
        ).shift(bb.RIGHT * 0.2)
        sin_txt4 = bb.Tex(
            r"If $a$ is negative, the center will be $a$ units below the origin.",
            font_size=40,
        ).move_to(intro)
        sin_rect4 = bb.SurroundingRectangle(sin_txt4, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.play(
            bb.Transform(intro_rect, sin_rect4),
            bb.Transform(sin_unit_circle_plot_pos, sin_unit_circle_plot_neg),
            bb.Transform(sin_func_txt_pos, sin_func_txt_neg),
            bb.Transform(psin_len_brace, nsin_len_brace),
            a_txt.animate.next_to(nsin_len_brace, direction=bb.LEFT).shift(
                bb.RIGHT * 0.1
            ),
            bb.FadeOut(sin_txt3),
        )
        self.play(bb.Write(sin_txt4))
        self.wait(3)
        self.play(
            bb.FadeOut(sin_txt4),
            bb.Uncreate(sin_unit_circle_plot_pos),
            bb.Uncreate(sin_func_txt_pos),
            bb.FadeOut(intro_rect),
        )
        self.wait(0.2)
