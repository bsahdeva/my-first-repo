import manim as bb
import numpy as np

from polar_utils import plot_polar_curve


class LimaconScene(bb.Scene):

    def construct(self):

        self.add(bb.NumberPlane())

        card_intro1 = bb.Tex(
            "The next type of limacons we will look at are cardioids, named for their heart shape.",
            font_size=38,
        ).shift(bb.UP * 3)
        card_intro_rect1 = bb.SurroundingRectangle(
            card_intro1, color=bb.BLACK
        ).set_fill(bb.BLACK, opacity=1)
        card_intro2 = bb.Tex(r"Cardioids are formed when $|\frac{a}{b}| = 1$.").move_to(
            card_intro1
        )
        card_intro_rect2 = bb.SurroundingRectangle(
            card_intro2, color=bb.BLACK
        ).set_fill(bb.BLACK, opacity=1)

        self.add(card_intro_rect1)
        self.play(bb.Write(card_intro1))
        self.wait(2)
        self.play(
            bb.Transform(card_intro_rect1, card_intro_rect2), bb.FadeOut(card_intro1)
        )
        self.play(bb.Write(card_intro2))

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

        cos_card_plot_p = plot_polar_curve(cos_lima_card_pos, color=bb.GOLD)
        cos_card_func_txt_p = bb.Tex(
            r"$a + b \cdot \cos{(\theta)}$, where $a = \frac{1}{2}$ and $b = \frac{1}{2}$",
            font_size=35,
        ).next_to(cos_card_plot_p, direction=bb.UP)
        cos_card_plot_n = plot_polar_curve(cos_lima_card_neg, color=bb.GOLD)
        cos_card_func_txt_n = bb.Tex(
            r"$a + b \cdot \cos{(\theta)}$, where $a = \frac{1}{2}$ and $b = -\frac{1}{2}$",
            font_size=35,
        ).next_to(cos_card_plot_n, direction=bb.UP)
        sin_card_plot_p = plot_polar_curve(sin_lima_card_pos)
        sin_card_func_txt_p = bb.Tex(
            r"$a + b \cdot \sin{(\theta)}$, where $a = \frac{1}{2}$ and $b = \frac{1}{2}$",
            font_size=35,
        ).next_to(sin_card_plot_p, direction=bb.DOWN)
        sin_card_plot_n = plot_polar_curve(sin_lima_card_neg)
        sin_card_func_txt_n = bb.Tex(
            r"$a + b \cdot \sin{(\theta)}$, where $a = \frac{1}{2}$ and $b = -\frac{1}{2}$",
            font_size=35,
        ).next_to(sin_card_plot_n, direction=bb.UP)

        card_txt1 = bb.Tex(
            "As they are also a type of limacon, cardioids have similar patterns to looped limacons.",
            font_size=38,
        ).move_to(card_intro1)
        card_rect1 = bb.SurroundingRectangle(card_txt1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        card_txt2 = bb.Tex(
            r"Sinusoidal cardioids will point upwards if $b$ is positive."
        ).move_to(card_intro1)
        card_rect2 = bb.SurroundingRectangle(card_txt2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        card_txt3 = bb.Tex(
            r"They intersect with the y-axis at $(0, |a| + |b|)$."
        ).move_to(card_intro1)
        card_rect3 = bb.SurroundingRectangle(card_txt3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        card_txt4 = bb.Tex(
            r"If $b$ is negative, the cardioid will point downwards."
        ).move_to(card_intro1)
        card_rect4 = bb.SurroundingRectangle(card_txt4, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        card_txt5 = bb.Tex(
            r"It will intersect with the y-axis at $(0, -(|a| + |b|))$."
        ).move_to(card_intro1)
        card_rect5 = bb.SurroundingRectangle(card_txt5, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        card_txt6 = bb.Tex(
            r"Cosine cadioids will point to the right if $b$ if is positive."
        ).move_to(card_intro1)
        card_rect6 = bb.SurroundingRectangle(card_txt6, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        card_txt7 = bb.Tex(
            r"They intersect with the x-axis at $(|a| + |b|, 0)$."
        ).move_to(card_intro1)
        card_rect7 = bb.SurroundingRectangle(card_txt7, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        card_txt8 = bb.Tex(
            r"If $b$ is negative, the cardioid will point to the left."
        ).move_to(card_intro1)
        card_rect8 = bb.SurroundingRectangle(card_txt8, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        card_txt9 = bb.Tex(
            r"It will intersect with the x-axis at $(-(|a| + |b|), 0)$."
        ).move_to(card_intro1)
        card_rect9 = bb.SurroundingRectangle(card_txt9, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.wait(2)
        self.play(bb.Transform(card_intro_rect1, card_rect1), bb.FadeOut(card_intro2))
        self.play(bb.Write(card_txt1))
        self.wait(2)
        self.play(bb.Transform(card_intro_rect1, card_rect2), bb.FadeOut(card_txt1))
        self.wait(0.1)
        self.play(
            bb.Write(card_txt2),
            bb.Create(sin_card_plot_p),
            bb.Write(sin_card_func_txt_p),
        )
        self.wait(2)
        self.play(bb.Transform(card_intro_rect1, card_rect3), bb.FadeOut(card_txt2))
        self.play(bb.Write(card_txt3))
        self.wait(2)
        self.play(bb.Transform(card_intro_rect1, card_rect4), bb.FadeOut(card_txt3))
        self.play(
            bb.Write(card_txt4),
            bb.Transform(sin_card_plot_p, sin_card_plot_n),
            bb.Transform(sin_card_func_txt_p, sin_card_func_txt_n),
        )
        self.wait(2)
        self.play(bb.Transform(card_intro_rect1, card_rect5), bb.FadeOut(card_txt4))
        self.play(bb.Write(card_txt5))
        self.wait(2)
        self.play(bb.Transform(card_intro_rect1, card_rect6), bb.FadeOut(card_txt5))
        self.play(
            bb.Write(card_txt6),
            bb.Transform(sin_card_plot_p, cos_card_plot_p),
            bb.Transform(sin_card_func_txt_p, cos_card_func_txt_p),
        )
        self.wait(2)
        self.play(bb.Transform(card_intro_rect1, card_rect7), bb.FadeOut(card_txt6))
        self.play(bb.Write(card_txt7))
        self.wait(2)
        self.play(bb.Transform(card_intro_rect1, card_rect8), bb.FadeOut(card_txt7))
        self.play(
            bb.Write(card_txt8),
            bb.Transform(sin_card_plot_p, cos_card_plot_n),
            bb.Transform(sin_card_func_txt_p, cos_card_func_txt_n),
        )
        self.wait(2)
        self.play(bb.Transform(card_intro_rect1, card_rect9), bb.FadeOut(card_txt8))
        self.play(bb.Write(card_txt9))
        self.wait(2)
        self.play(
            bb.FadeOut(card_txt9),
            bb.Uncreate(sin_card_plot_p),
            bb.Uncreate(sin_card_func_txt_p),
        )
        self.wait(0.2)
