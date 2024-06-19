import manim as bb

from polar_utils import (
    plot_polar_curve,
    unit_circle,
    circle,
    cos_unit_circle_pos,
    cos_unit_circle_neg,
    sin_unit_circle_pos,
    sin_unit_circle_neg,
    cos_lima_looped_pos,
    cos_lima_looped_neg,
    sin_lima_looped_pos,
    sin_lima_looped_neg,
    cos_lima_card_pos,
    cos_lima_card_neg,
    sin_lima_card_pos,
    sin_lima_card_neg,
    cos_lima_dimp_pos,
    cos_lima_dimp_neg,
    sin_lima_dimp_pos,
    sin_lima_dimp_neg,
    cos_rose_2,
    cos_rose_3,
)


class UnitCircleCurve(bb.Scene):
    def construct(self):
        self.add(bb.NumberPlane())
        self.add(plot_polar_curve(unit_circle))


class CircleCurve(bb.Scene):
    def construct(self):
        self.add(bb.NumberPlane())
        self.add(plot_polar_curve(circle))


class CosCircleCurve(bb.Scene):
    def construct(self):
        self.add(bb.NumberPlane())
        self.add(plot_polar_curve(cos_unit_circle_pos))


class SinCircleCurve(bb.Scene):
    def construct(self):
        self.add(bb.NumberPlane())
        self.add(plot_polar_curve(sin_unit_circle_pos))


class LoopedCurve(bb.Scene):
    def construct(self):
        self.add(bb.NumberPlane())
        self.add(plot_polar_curve(cos_lima_looped_pos))


class CardioidCurve(bb.Scene):
    def construct(self):
        self.add(bb.NumberPlane())
        self.add(plot_polar_curve(cos_lima_card_pos))


class DimpledCurve(bb.Scene):
    def construct(self):
        self.add(bb.NumberPlane())
        self.add(plot_polar_curve(cos_lima_dimp_pos))


class RoseCurve(bb.Scene):
    def construct(self):
        self.add(bb.NumberPlane())
        self.add(plot_polar_curve(cos_rose_2))
