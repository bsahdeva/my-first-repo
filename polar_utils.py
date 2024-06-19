import functools

import manim as bb
import numpy as np

# converts given polar function from polar to rectangular
def parametric_func(t, polar_func):
    r = polar_func(t)
    return [r * np.cos(t), r * np.sin(t), 0]


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
