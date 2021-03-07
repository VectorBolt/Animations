from manimlib.imports import *

class HadamardSuperposition(Scene):
    def construct(self):
        tex = TexMobject(r"\sqrt{\frac{1}{2}}\ket{0}+\sqrt{\frac{1}{2}}\ket{1}")
        tex.scale(3).set_color(BLACK)
        self.add(tex)

class Coefficients(Scene):
    CONFIG = {
        "coefficients_color": DARK_BLUE
    }
    def construct(self):
        tex = TexMobject(r"\alpha", r"\ket{0}+", r"\beta", r"\ket{1}")
        tex.scale(3).set_color(BLACK)
        tex[0:3:2].set_color(self.coefficients_color)
        tex.shift(UP)

        coefficients_label = TextMobject("Coefficients")
        coefficients_label.scale(2).set_color(self.coefficients_color)
        coefficients_label.shift(DOWN*1.5)

        alpha_arrow = Arrow(coefficients_label.get_edge_center(UP), tex[0].get_edge_center(DOWN), color=self.coefficients_color)
        beta_arrow = Arrow(coefficients_label.get_edge_center(UP), tex[2].get_edge_center(DOWN), color=self.coefficients_color)

        self.add(tex)
        self.add(coefficients_label)
        self.add(alpha_arrow, beta_arrow)
        
class UnitCircleZeroState(Scene):
    def construct(self):
        grid = NumberPlane()
        circle = Circle()
        vector = Vector(color=GREEN)
        state_label = TexMobject(r"\ket{0}")
        state_label.set_color(GREEN).next_to(vector, direction=RIGHT+UP*0.05, buff=SMALL_BUFF)
        self.add(grid, circle, vector, state_label)

class UnitCircleOneState(Scene):
    def construct(self):
        grid = NumberPlane()
        circle = Circle()
        vector = Vector(direction=UP, color=GREEN)
        state_label = TexMobject(r"\ket{1}")
        state_label.set_color(GREEN).next_to(vector, direction=UP+RIGHT*0.05, buff=SMALL_BUFF)
        self.add(grid, circle, vector, state_label)

class UnitCircleSuperposition(Scene):
    def construct(self):
        grid = NumberPlane()
        circle = Circle()
        vector = Vector(direction= math.sqrt(1/2)*(UP+RIGHT), color=GREEN)
        state_label = TexMobject(r"\sqrt{\frac{1}{2}}\ket{0}+\sqrt{\frac{1}{2}}\ket{1}")
        state_label.set_color(GREEN).next_to(vector, direction=UP+RIGHT, buff=SMALL_BUFF).add_background_rectangle()
        self.add(grid, circle, vector, state_label)

class WhySquareRoots(Scene):
    def construct(self):
        grid = NumberPlane()
        circle = Circle()
        vector = Vector(direction= math.sqrt(1/2)*(UP+RIGHT), color=GREEN)
        vector_label = TexMobject("1").set_color(GREEN).next_to(vector, direction=UL, buff=-0.3)

        horizontal_line = Line(ORIGIN, math.sqrt(1/2)*RIGHT, color=YELLOW)
        horizontal_line_label = TexMobject(r"\sqrt{\frac{1}{2}}").set_color(YELLOW).scale(0.4).next_to(horizontal_line, direction=DOWN, buff=SMALL_BUFF)
        vertical_line = Line(math.sqrt(1/2)*RIGHT, math.sqrt(1/2)*(UP+RIGHT), color=PURPLE)
        vertical_line_label = TexMobject(r"\sqrt{\frac{1}{2}}").scale(0.4).set_color(PURPLE).next_to(vertical_line, direction=RIGHT, buff=SMALL_BUFF)

        self.add(grid, circle, vector, vector_label)
        self.add(horizontal_line, horizontal_line_label, vertical_line, vertical_line_label)