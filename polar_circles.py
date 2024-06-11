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
        
        self.play(bb.Create(bb.NumberPlane()))
        # self.add(bb.NumberPlane())
        
        intro = bb.Tex("The first polar curves we will look at are simple circles.").shift(bb.UP * 3)

        self.play(bb.Write(intro))
        # self.add(intro)
        
        unit_circle_plot = plot_polar_curve(polar_func = unit_circle)
        unit_circle_func_txt = bb.MathTex(r"r(\theta) = 1").next_to(unit_circle_plot, direction = bb.UP)
        unit_circle_func_txt

        self.play(bb.Create(unit_circle_plot), bb.Write(unit_circle_func_txt))
        # self.add(unit_circle_plot)

        unit_txt1 = bb.Tex("This circle is described by the polar equation below.").move_to(intro)
        unit_txt2 = bb.Tex("It has a radius of 1 and is centered at the origin.").move_to(intro)
        unit_txt3 = bb.Tex(r"Polar equations described by $r(\theta)$ = a, where a is a constant, will generate a circle centered at the origin of radius a.", 
                           font_size = 35).move_to(intro)

        self.play(bb.FadeOut(intro))
        self.play(bb.Write(unit_txt1))
        self.wait(2)
        self.play(bb.FadeOut(unit_txt1))
        self.play(bb.Write(unit_txt2))
        self.wait(2)
        self.play(bb.FadeOut(unit_txt2))
        self.play(bb.Write(unit_txt3))
        self.wait(2)
        self.play(bb.FadeOut(unit_txt3), bb.Uncreate(unit_circle_plot), bb.Uncreate(unit_circle_func_txt))
        self.wait(0.2)

        cos_unit_circle_plot_pos = plot_polar_curve(polar_func = cos_unit_circle_pos, color = bb.GOLD)
        cos_func_txt_pos = bb.MathTex(r"r(\theta) = 2 \cdot cos(\theta)").next_to(cos_unit_circle_plot_pos, direction = bb.UP)
        cos_unit_circle_plot_neg = plot_polar_curve(polar_func = cos_unit_circle_neg, color = bb.GOLD)
        cos_func_txt_neg = bb.MathTex(r"r(\theta) = -2 \cdot cos(\theta)").next_to(cos_unit_circle_plot_neg, direction = bb.UP)

        self.play(bb.Create(cos_unit_circle_plot_pos), bb.Write(cos_func_txt_pos))

        cos_txt1 = bb.Tex(r"The next circles we will look at are described by $r(\theta) = a \cdot cos(\theta)$, where a is a constant.",
                          font_size = 35).move_to(intro)
        cos_txt2 = bb.Tex(r"These circles have diameter a, with a focus that lies $\frac{a}{2}$ units from the origin along the x-axis.",
                          font_size = 35).move_to(intro)
        cos_txt3 = bb.Tex(r"If a is positive, the focus will be $\frac{a}{2}$ units to the right of the origin.",
                          font_size = 40).move_to(intro)
        cos_txt4 = bb.Tex(r"If a is negative, the focus will be $\frac{a}{2}$ units to the left of the origin.",
                          font_size = 40).move_to(intro)

        self.play(bb.Write(cos_txt1))
        self.wait(2)
        self.play(bb.FadeOut(cos_txt1))
        self.play(bb.Write(cos_txt2))
        self.wait(2)
        self.play(bb.FadeOut(cos_txt2))
        self.play(bb.Write(cos_txt3))
        self.wait(2)
        self.play(bb.Transform(cos_unit_circle_plot_pos, cos_unit_circle_plot_neg), 
                  bb.Transform(cos_func_txt_pos, cos_func_txt_neg),
                  bb.FadeOut(cos_txt3))
        self.play(bb.Write(cos_txt4))
        self.wait(2)
        self.play(bb.FadeOut(cos_txt4), bb.Uncreate(cos_unit_circle_plot_pos), bb.Uncreate(cos_func_txt_pos))
        self.wait(0.2)

        sin_unit_circle_plot_pos = plot_polar_curve(polar_func = sin_unit_circle_pos, color = bb.GREEN)
        sin_func_txt_pos = bb.MathTex(r"r(\theta) = 2 \cdot sin(\theta)").next_to(sin_unit_circle_plot_pos, direction = bb.DOWN)
        sin_unit_circle_plot_neg = plot_polar_curve(polar_func = sin_unit_circle_neg, color = bb.GREEN)
        sin_func_txt_neg = bb.MathTex(r"r(\theta) = -2 \cdot sin(\theta)").next_to(sin_unit_circle_plot_neg, direction = bb.UP)

        self.play(bb.Create(sin_unit_circle_plot_pos), bb.Write(sin_func_txt_pos))

        sin_txt1 = bb.Tex(r"These circles are described by $r(\theta) = a \cdot sin(\theta)$, where a is a constant.",
                          font_size = 40).move_to(intro)
        sin_txt2 = bb.Tex(r"These circles also have diameter a, with a focus that lies $\frac{a}{2}$ units from the origin along the y-axis.",
                          font_size = 35).move_to(intro)
        sin_txt3 = bb.Tex(r"If a is positive, the focus will be $\frac{a}{2}$ units above the origin.",
                          font_size = 40).move_to(intro)
        sin_txt4 = bb.Tex(r"If a is negative, the focus will be $\frac{a}{2}$ units below the origin.",
                          font_size = 40).move_to(intro)
        
        self.play(bb.Write(sin_txt1))
        self.wait(2)
        self.play(bb.FadeOut(sin_txt1))
        self.play(bb.Write(sin_txt2))
        self.wait(2)
        self.play(bb.FadeOut(sin_txt2))
        self.play(bb.Write(sin_txt3))
        self.wait(2)
        self.play(bb.Transform(sin_unit_circle_plot_pos, sin_unit_circle_plot_neg), 
                  bb.Transform(sin_func_txt_pos, sin_func_txt_neg),
                  bb.FadeOut(sin_txt3))
        self.play(bb.Write(sin_txt4))
        self.wait(2)
        self.play(bb.FadeOut(sin_txt4), bb.Uncreate(sin_unit_circle_plot_pos), bb.Uncreate(sin_func_txt_pos))
        self.wait(0.2)

        # unit_circle_vector = curve_tracing_vector(polar_func = unit_circle, theta = 0)
        # cos_unit_circle_vector = curve_tracing_vector(polar_func = cos_unit_circle, theta = 0)

        
        # self.add(cos_unit_circle_plot, cos_unit_circle_vector)