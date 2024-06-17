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

class CircleScene(bb.Scene):

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
        
        def curve_tracing_vector(polar_func, theta:float, tip_length = 0.15, tip_width = 0.15, arc_radius = 0.5):

            fn = functools.partial(parametric_func, polar_func = polar_func)
            
            vector = bb.Line(start = bb.ORIGIN, end = fn(theta)).add_tip(tip_length = tip_length, tip_width = tip_width)
            angle = bb.Arc(angle = theta, radius = arc_radius)

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
        
        intro = bb.Tex("The first polar curves we will look at are simple circles.").shift(bb.UP * 3)
        intro_rect = bb.SurroundingRectangle(intro, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)

        self.add(intro_rect)
        self.play(bb.Write(intro))
        self.wait(2)
        
        unit_circle_plot = plot_polar_curve(polar_func = unit_circle)
        unit_circle_func_txt1 = bb.MathTex(r"r(\theta) = 1").next_to(unit_circle_plot, direction = bb.UP)
        unit_circle_func_txt2 = bb.Tex(r"$r(\theta) = a$, where $a = 1$").next_to(unit_circle_plot, direction = bb.UP)
        u_line = bb.Line([0, 0, 0], [1, 0, 0])
        unit_circle_len_brace = bb.Brace(u_line, sharpness = 1).shift(bb.UP * 0.2)
        a_txt = bb.MathTex("a",
                           font_size = 38).next_to(unit_circle_len_brace, direction = bb.DOWN)
        circle_plot = plot_polar_curve(polar_func = circle)
        circle_func_txt = bb.Tex(r"$r(\theta) = a$, where $a = 2$").next_to(circle_plot, direction = bb.DOWN)
        c_line = bb.Line([0, 0, 0], [2, 0, 0])
        circle_len_brace = bb.Brace(c_line, sharpness = 1).shift(bb.UP * 0.2)

        self.play(bb.Create(unit_circle_plot), bb.Write(unit_circle_func_txt1))
        # self.add(unit_circle_plot)

        unit_txt1 = bb.Tex("This circle is described by the polar equation below.").move_to(intro)
        unit_rect1 = bb.SurroundingRectangle(unit_txt1, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)
        unit_txt2 = bb.Tex("It has a radius of 1 and is centered at the origin.").move_to(intro)
        unit_rect2 = bb.SurroundingRectangle(unit_txt2, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)
        unit_txt3 = bb.Tex(r"Polar equations described by $r(\theta) = a$, where $a$ is a constant, will generate a circle centered at the origin of radius $a$.", 
                           font_size = 35).move_to(intro)
        unit_rect3 = bb.SurroundingRectangle(unit_txt3, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)

        self.play(bb.Transform(intro_rect, unit_rect1), bb.FadeOut(intro))
        self.play(bb.Write(unit_txt1))
        self.wait(2)
        self.play(bb.Transform(intro_rect, unit_rect2), bb.FadeOut(unit_txt1))
        self.play(bb.Write(unit_txt2))
        self.wait(2)
        self.play(bb.Transform(intro_rect, unit_rect3), bb.FadeOut(unit_txt2))
        self.play(bb.Write(unit_txt3), bb.Transform(unit_circle_func_txt1, unit_circle_func_txt2), bb.Create(unit_circle_len_brace), bb.Write(a_txt))
        self.wait(3)
        self.play(bb.Transform(unit_circle_plot, circle_plot), 
                  bb.Transform(unit_circle_func_txt1, circle_func_txt), 
                  bb.Transform(unit_circle_len_brace, circle_len_brace),
                  a_txt.animate.next_to(circle_len_brace, direction = bb.DOWN))
        self.wait(3)

        cos_unit_circle_plot_pos = plot_polar_curve(polar_func = cos_unit_circle_pos, color = bb.GOLD)
        cos_func_txt_pos = bb.Tex(r"$r(\theta) = 2a \cdot \cos{(\theta)}$, where $a = 1$").next_to(cos_unit_circle_plot_pos, direction = bb.UP)
        pcos_line = bb.Line([0, 0, 0], [1, 0, 0])
        pcos_len_brace = bb.Brace(pcos_line, sharpness = 1).shift(bb.UP * 0.2)
        a2_txt = bb.MathTex("a",
                           font_size = 38).next_to(pcos_len_brace, direction = bb.DOWN)
        cos_unit_circle_plot_neg = plot_polar_curve(polar_func = cos_unit_circle_neg, color = bb.GOLD)
        cos_func_txt_neg = bb.Tex(r"$r(\theta) = 2a \cdot \cos{(\theta)}$, where $a = -1$").next_to(cos_unit_circle_plot_neg, direction = bb.UP)
        ncos_line = bb.Line([0, 0, 0], [-1, 0, 0])
        ncos_len_brace = bb.Brace(ncos_line, sharpness = 1).shift(bb.UP * 0.2)

        cos_txt1 = bb.Tex(r"The next circles we will look at are described by $r(\theta) = 2a \cdot \cos{(\theta)}$, where $a$ is a constant.",
                          font_size = 35).move_to(intro)
        cos_rect1 = bb.SurroundingRectangle(cos_txt1, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)
        cos_txt2 = bb.Tex(r"These circles have radius $a$, with a center that lies $a$ units from the origin along the x-axis.",
                          font_size = 35).move_to(intro)
        cos_rect2 = bb.SurroundingRectangle(cos_txt2, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)
        cos_txt3 = bb.Tex(r"If $a$ is positive, the center will be $a$ units to the right of the origin.",
                          font_size = 40).move_to(intro)
        cos_rect3 = bb.SurroundingRectangle(cos_txt3, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)
        cos_txt4 = bb.Tex(r"If $a$ is negative, the center will be $a$ units to the left of the origin.",
                          font_size = 40).move_to(intro)
        cos_rect4 = bb.SurroundingRectangle(cos_txt4, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)

        self.play(bb.Transform(intro_rect, cos_rect1), 
                  bb.FadeOut(unit_txt3), 
                  bb.Uncreate(unit_circle_plot), 
                  bb.Uncreate(unit_circle_func_txt1),
                  bb.Uncreate(unit_circle_len_brace),
                  bb.Uncreate(a_txt))
        self.wait(2)
        self.play(bb.Write(cos_txt1))
        self.play(bb.Create(cos_unit_circle_plot_pos), bb.Write(cos_func_txt_pos), bb.Create(pcos_len_brace), bb.Write(a2_txt))
        self.wait(2)
        self.play(bb.Transform(intro_rect, cos_rect2), bb.FadeOut(cos_txt1))
        self.play(bb.Write(cos_txt2))
        self.wait(2)
        self.play(bb.Transform(intro_rect, cos_rect3), bb.FadeOut(cos_txt2))
        self.play(bb.Write(cos_txt3))
        self.wait(2)
        self.play(bb.Transform(intro_rect, cos_rect4), 
                  bb.Transform(cos_unit_circle_plot_pos, cos_unit_circle_plot_neg), 
                  bb.Transform(cos_func_txt_pos, cos_func_txt_neg), 
                  bb.Transform(pcos_len_brace, ncos_len_brace), 
                  a2_txt.animate.next_to(ncos_len_brace, direction = bb.DOWN),
                  bb.FadeOut(cos_txt3))
        self.play(bb.Write(cos_txt4))
        self.wait(3)

        sin_unit_circle_plot_pos = plot_polar_curve(polar_func = sin_unit_circle_pos, color = bb.GREEN)
        sin_func_txt_pos = bb.Tex(r"$r(\theta) = 2a \cdot \sin{(\theta)}$, where $a = 1$").next_to(sin_unit_circle_plot_pos, direction = bb.DOWN)
        psin_line = bb.Line([0, 0, 0], [0, 1, 0])
        psin_len_brace = bb.Brace(psin_line, sharpness = 1)
        a3_txt = bb.MathTex("a",
                           font_size = 38).next_to(psin_len_brace, direction = bb.DOWN)
        sin_unit_circle_plot_neg = plot_polar_curve(polar_func = sin_unit_circle_neg, color = bb.GREEN)
        sin_func_txt_neg = bb.Tex(r"$r(\theta) = 2a \cdot \sin{(\theta)}$, where $a = -1$").next_to(sin_unit_circle_plot_neg, direction = bb.UP)
        nsin_line = bb.Line([0, 0, 0], [0, -1, 0])
        nsin_len_brace = bb.Brace(nsin_line, sharpness = 1)
        
        sin_txt1 = bb.Tex(r"These circles are described by $r(\theta) = 2a \cdot \sin{(\theta)}$, where $a$ is a constant.",
                          font_size = 40).move_to(intro)
        sin_rect1 = bb.SurroundingRectangle(sin_txt1, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)
        sin_txt2 = bb.Tex(r"These circles also have radius $a$, with a center that lies $a$ units from the origin along the y-axis.",
                          font_size = 35).move_to(intro)
        sin_rect2 = bb.SurroundingRectangle(sin_txt2, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)
        sin_txt3 = bb.Tex(r"If $a$ is positive, the center will be $a$ units above the origin.",
                          font_size = 40).move_to(intro)
        sin_rect3 = bb.SurroundingRectangle(sin_txt3, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)
        sin_txt4 = bb.Tex(r"If $a$ is negative, the center will be $a$ units below the origin.",
                          font_size = 40).move_to(intro)
        sin_rect4 = bb.SurroundingRectangle(sin_txt4, color = bb.BLACK).set_fill(bb.BLACK, opacity = 1)
        
        self.play(bb.Transform(intro_rect, sin_rect1), 
                  bb.FadeOut(cos_txt4), 
                  bb.Uncreate(cos_unit_circle_plot_pos), 
                  bb.Uncreate(cos_func_txt_pos), 
                  bb.Uncreate(pcos_len_brace), 
                  bb.Uncreate(a2_txt))
        self.play(bb.Create(sin_unit_circle_plot_pos), bb.Write(sin_func_txt_pos), bb.Create(psin_len_brace), bb.Write(a3_txt))
        self.wait(0.2)
        self.play(bb.Write(sin_txt1))
        self.wait(2)
        self.play(bb.Transform(intro_rect, sin_rect2), bb.FadeOut(sin_txt1))
        self.play(bb.Write(sin_txt2))
        self.wait(2)
        self.play(bb.Transform(intro_rect, sin_rect3), bb.FadeOut(sin_txt2))
        self.play(bb.Write(sin_txt3))
        self.wait(2)
        self.play(bb.Transform(intro_rect, sin_rect4), 
                  bb.Transform(sin_unit_circle_plot_pos, sin_unit_circle_plot_neg), 
                  bb.Transform(sin_func_txt_pos, sin_func_txt_neg),
                  bb.Transform(psin_len_brace, nsin_len_brace), 
                  a3_txt.animate.next_to(ncos_len_brace, direction = bb.DOWN),
                  bb.FadeOut(sin_txt3))
        self.play(bb.Write(sin_txt4))
        self.wait(3)
        self.play(bb.FadeOut(sin_txt4), 
                  bb.Uncreate(sin_unit_circle_plot_pos), 
                  bb.Uncreate(sin_func_txt_pos),
                  bb.FadeOut(intro_rect))
        self.wait(0.2)
