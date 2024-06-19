import manim as bb
import numpy as np

from polar_utils import plot_polar_curve


class LimaconScene(bb.Scene):

    def construct(self):

        self.add(bb.NumberPlane())

        dimp_intro1 = bb.Tex(
            "The final type of limacon to look at are dimpled limacons."
        ).shift(bb.UP * 3)
        dimp_intro_rect1 = bb.SurroundingRectangle(
            dimp_intro1, color=bb.BLACK
        ).set_fill(bb.BLACK, opacity=1)
        dimp_intro2 = bb.Tex(
            r"Dimpled limcaons are formed when $|\frac{a}{b}| > 1$."
        ).move_to(dimp_intro1)
        dimp_intro_rect2 = bb.SurroundingRectangle(
            dimp_intro2, color=bb.BLACK
        ).set_fill(bb.BLACK, opacity=1)

        self.add(dimp_intro_rect1)
        self.play(bb.Write(dimp_intro1))
        self.wait(2)
        self.play(
            bb.Transform(dimp_intro_rect1, dimp_intro_rect2), bb.FadeOut(dimp_intro1)
        )
        self.play(bb.Write(dimp_intro2))
        self.wait(2)

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

        cos_dimp_plot_p = plot_polar_curve(cos_lima_dimp_pos, color=bb.GOLD)
        cos_dimp_func_txt_p = bb.Tex(
            r"$a + b \cdot \cos{(\theta)}$, where $a = 1$ and $b = \frac{1}{2}$",
            font_size=35,
        ).next_to(cos_dimp_plot_p, direction=bb.UP)
        cos_dimp_plot_n = plot_polar_curve(cos_lima_dimp_neg, color=bb.GOLD)
        cos_dimp_func_txt_n = bb.Tex(
            r"$a + b \cdot \cos{(\theta)}$, where $a = 1$ and $b = -\frac{1}{2}$",
            font_size=35,
        ).next_to(cos_dimp_plot_n, direction=bb.UP)
        sin_dimp_plot_p = plot_polar_curve(sin_lima_dimp_pos)
        sin_dimp_func_txt_p = bb.Tex(
            r"$a + b \cdot \sin{(\theta)}$, where $a = 1$ and $b = \frac{1}{2}$",
            font_size=35,
        ).next_to(sin_dimp_plot_p, direction=bb.UP)
        sin_dimp_plot_n = plot_polar_curve(sin_lima_dimp_neg)
        sin_dimp_func_txt_n = bb.Tex(
            r"$a + b \cdot \sin{(\theta)}$, where $a = 1$ and $b = -\frac{1}{2}$",
            font_size=35,
        ).next_to(sin_dimp_plot_n, direction=bb.DOWN)

        dimp_txt1 = bb.Tex(
            r"Sinusoidal dimpled limacons will point upwards if $b$ is positive.",
            font_size=42,
        ).move_to(dimp_intro1)
        dimp_rect1 = bb.SurroundingRectangle(dimp_txt1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        dimp_txt2 = bb.Tex(
            r"They intersect with the y-axis at $(0, |a| + |b|)$ and $(0, |b| - |a|)$."
        ).move_to(dimp_intro1)
        dimp_rect2 = bb.SurroundingRectangle(dimp_txt2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        dimp_txt3 = bb.Tex(
            r"If $b$ is negative, the limacon will point downwards."
        ).move_to(dimp_intro1)
        dimp_rect3 = bb.SurroundingRectangle(dimp_txt3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        dimp_txt4 = bb.Tex(
            r"It will intersect with the y-axis at $(0, -(|a| + |b|))$ and $(0, -(|b| - |a|))$.",
            font_size=40,
        ).move_to(dimp_intro1)
        dimp_rect4 = bb.SurroundingRectangle(dimp_txt4, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        dimp_txt5 = bb.Tex(
            r"Cosine dimpled limacons will point to the right if $b$ if is positive.",
            font_size=42,
        ).move_to(dimp_intro1)
        dimp_rect5 = bb.SurroundingRectangle(dimp_txt5, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        dimp_txt6 = bb.Tex(
            r"They intersect with the x-axis at $(|a| + |b|, 0)$."
        ).move_to(dimp_intro1)
        dimp_rect6 = bb.SurroundingRectangle(dimp_txt6, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        dimp_txt7 = bb.Tex(
            r"If $b$ is negative, the cardioid will point to the left."
        ).move_to(dimp_intro1)
        dimp_rect7 = bb.SurroundingRectangle(dimp_txt7, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        dimp_txt8 = bb.Tex(
            r"It will intersect with the x-axis at $(-(|a| + |b|), 0)$."
        ).move_to(dimp_intro1)
        dimp_rect8 = bb.SurroundingRectangle(dimp_txt8, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.play(bb.Transform(dimp_intro_rect1, dimp_rect1), bb.FadeOut(dimp_intro2))
        self.wait(0.2)
        self.play(
            bb.Write(dimp_txt1),
            bb.Create(sin_dimp_plot_p),
            bb.Write(sin_dimp_func_txt_p),
        )
        self.wait(2)
        self.play(bb.Transform(dimp_intro_rect1, dimp_rect2), bb.FadeOut(dimp_txt1))
        self.play(bb.Write(dimp_txt2))
        self.wait(2)
        self.play(bb.Transform(dimp_intro_rect1, dimp_rect3), bb.FadeOut(dimp_txt2))
        self.play(
            bb.Write(dimp_txt3),
            bb.Transform(sin_dimp_plot_p, sin_dimp_plot_n),
            bb.Transform(sin_dimp_func_txt_p, sin_dimp_func_txt_n),
        )
        self.wait(2)
        self.play(bb.Transform(dimp_intro_rect1, dimp_rect4), bb.FadeOut(dimp_txt3))
        self.play(bb.Write(dimp_txt4))
        self.wait(2)
        self.play(bb.Transform(dimp_intro_rect1, dimp_rect5), bb.FadeOut(dimp_txt4))
        self.play(
            bb.Write(dimp_txt5),
            bb.Transform(sin_dimp_plot_p, cos_dimp_plot_p),
            bb.Transform(sin_dimp_func_txt_p, cos_dimp_func_txt_p),
        )
        self.wait(2)
        self.play(bb.Transform(dimp_intro_rect1, dimp_rect6), bb.FadeOut(dimp_txt5))
        self.play(bb.Write(dimp_txt6))
        self.wait(2)
        self.play(bb.Transform(dimp_intro_rect1, dimp_rect7), bb.FadeOut(dimp_txt6))
        self.play(
            bb.Write(dimp_txt7),
            bb.Transform(sin_dimp_plot_p, cos_dimp_plot_n),
            bb.Transform(sin_dimp_func_txt_p, cos_dimp_func_txt_n),
        )
        self.wait(2)
        self.play(bb.Transform(dimp_intro_rect1, dimp_rect8), bb.FadeOut(dimp_txt7))
        self.play(bb.Write(dimp_txt8))
        self.wait(2)
        self.play(
            bb.FadeOut(dimp_txt8),
            bb.Uncreate(sin_dimp_plot_p),
            bb.Uncreate(sin_dimp_func_txt_p),
        )
        self.wait(0.1)
