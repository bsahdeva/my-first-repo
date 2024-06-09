import manim as bb
import numpy as np

class CircleScene(bb.Scene):

    def construct(self):
        self.add(bb.NumberPlane())

        def plot_polar_curve(polar_func, color = bb.RED, t_range = [0, 2 * bb.PI]):
            
            def parametric_func(t):
                r = polar_func(t)
                return [
                    r * np.cos(t),
                    r * np.sin(t),
                    0
                ]
            
            polar_curve = bb.ParametricFunction(
                parametric_func,
                t_range = t_range,
                color = color
            )

            return polar_curve

        def unit_circle(theta):
            r = 1
            return r
        
        def cos_unit_circle(theta):
            r = 2 * np.cos(theta)
            return r
        
        def sin_unit_circle(theta):
            r = 2 * np.sin(theta)
            return r
        
        unit_circle_plot = plot_polar_curve(unit_circle)
        cos_unit_circle_plot = plot_polar_curve(cos_unit_circle, color = bb.GOLD)
        sin_unit_circle_plot = plot_polar_curve(sin_unit_circle, color = bb.GREEN)

        self.add(unit_circle_plot, cos_unit_circle_plot, sin_unit_circle_plot)
