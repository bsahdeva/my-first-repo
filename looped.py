import manim as bb
import numpy as np

from polar_utils import (
    plot_polar_curve,
    cos_lima_looped_pos,
    cos_lima_looped_neg,
    sin_lima_looped_pos,
    sin_lima_looped_neg,
)


class LoopedScene(bb.Scene):

    def construct(self):

        self.add(bb.NumberPlane())

        intro1 = bb.Tex("The next types of curves we will look at are limacons.").shift(
            bb.UP * 3
        )
        intro_rect1 = bb.SurroundingRectangle(intro1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro2 = bb.Tex(
            r"Limacons are described by the formulas $a + b \cdot \sin{(\theta)}$ and $a + b \cdot \cos{(\theta)}$.",
            font_size=35,
        ).move_to(intro1)
        intro_rect2 = bb.SurroundingRectangle(intro2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro3 = bb.Tex(
            r"The shape of the limacon depends on the ratio of $a$ to $b$."
        ).move_to(intro1)
        intro_rect3 = bb.SurroundingRectangle(intro3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro4 = bb.Tex(
            "The limacons all share a few common features no matter their shape.",
            font_size=40,
        ).move_to(intro1)
        intro_rect4 = bb.SurroundingRectangle(intro4, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro5 = bb.Tex(
            r"The first is that the sign of $a$ does not affect the shape."
        ).move_to(intro1)
        intro_rect5 = bb.SurroundingRectangle(intro5, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro6 = bb.Tex(
            r"The second is that sinusoidal limacons will always intersect the x-axis at $(-|a|, 0) and (|a|, 0)$.",
            font_size=40,
        ).move_to(intro1)
        intro_rect6 = bb.SurroundingRectangle(intro6, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro7 = bb.Tex(
            r"Cosine limacons will intersect the y-axis at $(0, -|a|)$ and $(0, |a|)$."
        ).move_to(intro1)
        intro_rect7 = bb.SurroundingRectangle(intro7, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        intro8 = bb.Tex(
            'There are three main types of limacons, the first of which are "looped".',
            font_size=40,
        ).move_to(intro1)
        intro_rect8 = bb.SurroundingRectangle(intro8, color=bb.BLACK).set_fill(
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
        self.play(bb.Transform(intro_rect1, intro_rect5), bb.FadeOut(intro4))
        self.play(bb.Write(intro5))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, intro_rect6), bb.FadeOut(intro5))
        self.play(bb.Write(intro6))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, intro_rect7), bb.FadeOut(intro6))
        self.play(bb.Write(intro7))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, intro_rect8), bb.FadeOut(intro7))
        self.play(bb.Write(intro8))
        self.wait(2)

        cos_loop_plot_p = plot_polar_curve(cos_lima_looped_pos, color=bb.GOLD)
        cos_loop_func_txt_p = bb.Tex(
            r"$a + b \cdot \cos{(\theta)}$, where $a = \frac{1}{2}$ and $b = \frac{3}{2}$",
            font_size=35,
        ).next_to(cos_loop_plot_p, direction=bb.UP)
        cos_loop_plot_n = plot_polar_curve(cos_lima_looped_neg, color=bb.GOLD)
        cos_loop_func_txt_n = bb.Tex(
            r"$a + b \cdot \cos{(\theta)}$, where $a = \frac{1}{2}$ and $b = -\frac{3}{2}$",
            font_size=35,
        ).next_to(cos_loop_plot_n, direction=bb.UP)
        sin_loop_plot_p = plot_polar_curve(sin_lima_looped_pos)
        sin_loop_func_txt_p = bb.Tex(
            r"$a + b \cdot \sin{(\theta)}$, where $a = \frac{1}{2}$ and $b = \frac{3}{2}$",
            font_size=35,
        ).next_to(sin_loop_plot_p, direction=bb.DOWN)
        sin_loop_plot_n = plot_polar_curve(sin_lima_looped_neg)
        sin_loop_func_txt_n = bb.Tex(
            r"$a + b \cdot \sin{(\theta)}$, where $a = \frac{1}{2}$ and $b = -\frac{3}{2}$",
            font_size=35,
        ).next_to(sin_loop_plot_n, direction=bb.UP)

        self.play(bb.Create(sin_loop_plot_p), bb.Write(sin_loop_func_txt_p))

        sin_txt_loop1 = bb.Tex(
            "This looped limacon is described by the equation below."
        ).move_to(intro1)
        sin_rect1 = bb.SurroundingRectangle(sin_txt_loop1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        sin_txt_loop2 = bb.Tex(
            r"Sinusoidal looped limacons are described by the formula $a + b \cdot \sin{(\theta)}$, where $|b| > |a|$.",
            font_size=35,
        ).move_to(intro1)
        sin_rect2 = bb.SurroundingRectangle(sin_txt_loop2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        sin_txt_loop3 = bb.Tex(
            r"If $b$ is positive, then the limacon will point upwards."
        ).move_to(intro1)
        sin_rect3 = bb.SurroundingRectangle(sin_txt_loop3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        sin_txt_loop4 = bb.Tex(
            r"The outermost loop will intersect with the y-axis at $(0, |a| + |b|)$.",
            font_size=42,
        ).move_to(intro1)
        sin_rect4 = bb.SurroundingRectangle(sin_txt_loop4, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        sin_txt_loop5 = bb.Tex(
            r"The innermost loop will intersect with the y-axis at $(0, |b| - |a|)$.",
            font_size=42,
        ).move_to(intro1)
        sin_rect5 = bb.SurroundingRectangle(sin_txt_loop5, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        sin_txt_loop6 = bb.Tex(
            r"If $b$ is negative, then the limacon will point downwards."
        ).move_to(intro1)
        sin_rect6 = bb.SurroundingRectangle(sin_txt_loop6, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        sin_txt_loop7 = bb.Tex(
            r"The outermost loop will intersect with the y-axis at $(0, -(|a| + |b|))$.",
            font_size=42,
        ).move_to(intro1)
        sin_rect7 = bb.SurroundingRectangle(sin_txt_loop7, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        sin_txt_loop8 = bb.Tex(
            r"The innermost loop will intersect with the y-axis at $(0, -(|b| - |a|))$.",
            font_size=42,
        ).move_to(intro1)
        sin_rect8 = bb.SurroundingRectangle(sin_txt_loop8, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.play(bb.Transform(intro_rect1, sin_rect1), bb.FadeOut(intro8))
        self.play(bb.Write(sin_txt_loop1))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, sin_rect2), bb.FadeOut(sin_txt_loop1))
        self.play(bb.Write(sin_txt_loop2))
        self.wait(3)
        self.play(bb.Transform(intro_rect1, sin_rect3), bb.FadeOut(sin_txt_loop2))
        self.play(bb.Write(sin_txt_loop3))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, sin_rect4), bb.FadeOut(sin_txt_loop3))
        self.play(bb.Write(sin_txt_loop4))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, sin_rect5), bb.FadeOut(sin_txt_loop4))
        self.play(bb.Write(sin_txt_loop5))
        self.wait(2)
        self.play(
            bb.Transform(intro_rect1, sin_rect6),
            bb.Transform(sin_loop_plot_p, sin_loop_plot_n),
            bb.Transform(sin_loop_func_txt_p, sin_loop_func_txt_n),
            bb.FadeOut(sin_txt_loop5),
        )
        self.play(bb.Write(sin_txt_loop6))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, sin_rect7), bb.FadeOut(sin_txt_loop6))
        self.play(bb.Write(sin_txt_loop7))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, sin_rect8), bb.FadeOut(sin_txt_loop7))
        self.play(bb.Write(sin_txt_loop8))
        self.wait(2)

        cos_txt_loop1 = bb.Tex(
            r"Cosine looped limacons are described by the formula $a + b \cdot \cos{(\theta)}$, where $|b| > |a|$.",
            font_size=35,
        ).move_to(intro1)
        cos_rect1 = bb.SurroundingRectangle(cos_txt_loop1, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        cos_txt_loop2 = bb.Tex(
            r"If $b$ is positive, then the limacon will point to the right."
        ).move_to(intro1)
        cos_rect2 = bb.SurroundingRectangle(cos_txt_loop2, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        cos_txt_loop3 = bb.Tex(
            r"The outermost loop will intersect with the x-axis at $(|a| + |b|, 0)$.",
            font_size=42,
        ).move_to(intro1)
        cos_rect3 = bb.SurroundingRectangle(cos_txt_loop3, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        cos_txt_loop4 = bb.Tex(
            r"The innermost loop will intersect with the x-axis at $(|b| - |a|, 0)$.",
            font_size=42,
        ).move_to(intro1)
        cos_rect4 = bb.SurroundingRectangle(cos_txt_loop4, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        cos_txt_loop5 = bb.Tex(
            r"If $b$ is negative, then the limacon will point to the left."
        ).move_to(intro1)
        cos_rect5 = bb.SurroundingRectangle(cos_txt_loop5, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        cos_txt_loop6 = bb.Tex(
            r"The outermost loop will intersect with the x-axis at $(-(|a| + |b|), 0)$.",
            font_size=42,
        ).move_to(intro1)
        cos_rect6 = bb.SurroundingRectangle(cos_txt_loop6, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )
        cos_txt_loop7 = bb.Tex(
            r"The innermost loop will intersect with the x-axis at $(-(|b| - |a|), 0)$.",
            font_size=42,
        ).move_to(intro1)
        cos_rect7 = bb.SurroundingRectangle(cos_txt_loop7, color=bb.BLACK).set_fill(
            bb.BLACK, opacity=1
        )

        self.play(
            bb.Transform(intro_rect1, cos_rect1),
            bb.FadeOut(sin_txt_loop8),
            bb.Uncreate(sin_loop_plot_p),
            bb.Uncreate(sin_loop_func_txt_p),
        )
        self.wait(0.2)
        self.play(bb.Create(cos_loop_plot_p), bb.Write(cos_loop_func_txt_p))

        self.play(bb.Write(cos_txt_loop1))
        self.wait(3)
        self.play(bb.Transform(intro_rect1, cos_rect2), bb.FadeOut(cos_txt_loop1))
        self.play(bb.Write(cos_txt_loop2))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, cos_rect3), bb.FadeOut(cos_txt_loop2))
        self.play(bb.Write(cos_txt_loop3))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, cos_rect4), bb.FadeOut(cos_txt_loop3))
        self.play(bb.Write(cos_txt_loop4))
        self.wait(2)
        self.play(
            bb.Transform(intro_rect1, cos_rect5),
            bb.Transform(cos_loop_plot_p, cos_loop_plot_n),
            bb.Transform(cos_loop_func_txt_p, cos_loop_func_txt_n),
            bb.FadeOut(cos_txt_loop4),
        )
        self.play(bb.Write(cos_txt_loop5))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, cos_rect6), bb.FadeOut(cos_txt_loop5))
        self.play(bb.Write(cos_txt_loop6))
        self.wait(2)
        self.play(bb.Transform(intro_rect1, cos_rect7), bb.FadeOut(cos_txt_loop6))
        self.play(bb.Write(cos_txt_loop7))
        self.wait(2)
        self.play(
            bb.FadeOut(cos_txt_loop7),
            bb.Uncreate(cos_loop_plot_p),
            bb.Uncreate(cos_loop_func_txt_p),
        )
        self.wait(0.2)
