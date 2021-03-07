from manimlib.imports import *

class Lumlah(Scene):
    def construct(self):
        circle = Circle(stroke_color=ORANGE, stroke_width=10).scale(2.5)
        square = Square(stroke_color=BLUE, stroke_width=10).scale(2.5)
        line = Line(stroke_color=YELLOW, stroke_width=10).scale(2.5)

        self.play(
            LaggedStart(
                Write(circle),
                Write(square),
                Write(line)
            )
        )
      
class WritingText(Scene):
    def construct(self):
        first_text = TextMobject("What's my name?")
        first_text.set_color(BLUE)
        second_text = TextMobject("My name is ", "Avneesh")
        second_text[1].set_color(TEAL)
        self.play(Write(first_text))
        self.wait()
        self.play(Transform(first_text, second_text))
        self.wait()


def fib(x):
    if x > 2:
        return fib(x-1) + fib(x-2)
    else:
        return 1

def creat_fib_list(num):
    fib_list = []
    starting_index = 1
    while starting_index < num+1:
        fib_list.append(fib(starting_index))
        starting_index += 1
    return fib_list


class VoidScene(Scene):
    def setup(self):
        circle = Circle(stroke_color=BLUE, stroke_width=7).scale(2)
        starting_points = []
        start_point=circle.point_from_proportion(1/4)
        for i in range(24):
            starting_points.append(circle.point_from_proportion(i/24))

        end_points = []
        for i in range(24):
            if i+12 < 24:
                end_points.append(circle.point_from_proportion((i+12)/24))
            else:
                end_points.append(circle.point_from_proportion((i-12)/24))

        arcs = []
        for i in range(24):
            arcs.append(
                ArcBetweenPoints(np.array(starting_points[i]), np.array(end_points[i]), angle= -TAU/4, stroke_color=ORANGE, stroke_width=7)
            )
        arc_group = VGroup()
        for i in arcs:
            arc_group.add(i)
            
        lines = []
        for i in range(24):
            lines.append(
                Line(np.array(starting_points[i]), np.array(end_points[i]), stroke_color=TEAL)
            )

        line_group = VGroup()
        for line in lines:
            line_group.add(line)
        
        # self variables
        self.circle = circle
        self.arcs = arcs
        self.lines = lines
        self.arc_group = arc_group
        self.line_group = line_group
        self.void = VGroup(self.circle, self.arc_group)
        

class CircleNetwork(VoidScene):
    """
    CONFIG = {
        "camera_config": {
            "background_color": WHITE
        }
    }
    """
    def construct(self):
        luminate_text = TextMobject("Luminate").scale(2)
        luminate_text.set_color_by_gradient(BLUE, ORANGE)
        luminate_text.next_to(self.circle, direction=DOWN)
        self.play(
            Write(self.circle)
        )
        for arc in self.arcs:
            self.play(Write(arc), run_time=0.05)
        """
        self.play(
            GrowFromCenter(self.line_group)
        )
        """
        self.play(
            Write(luminate_text)
        )
        self.wait()
        


class Void(VoidScene):
    def construct(self):
        self.void.scale(0.5)
        stick_figure = VGroup(
            self.void,
            Line(self.circle.point_from_proportion(3/4), self.circle.point_from_proportion(3/4)+2*DOWN),
            Line(self.circle.point_from_proportion(3/4)+2*DOWN, self.circle.point_from_proportion(3/4)+3*DOWN+LEFT),
            Line(self.circle.point_from_proportion(3/4)+2*DOWN, self.circle.point_from_proportion(3/4)+3*DOWN+RIGHT),
            Line(self.circle.point_from_proportion(3/4)+DOWN, self.circle.point_from_proportion(3/4)+RIGHT),
            Line(self.circle.point_from_proportion(3/4)+DOWN, self.circle.point_from_proportion(3/4)+LEFT)
        )
        stick_figure.shift(UP)
        self.add(stick_figure)


class LightningBolt(Scene):
    def construct(self):
        top_line = Line(
            np.array([-0.5, 2, 0]), np.array([0.5, 2, 0])
        )

        left_line1 = Line(
            np.array([-0.5, 2, 0]), np.array([-0.7, 0.5, 0])
        )
        inset_line1 = Line(
            np.array([-0.7, 0.5, 0]), np.array([-0.3, 0.5, 0])
        )
        left_line2 = Line(
            np.array([-0.3, 0.5, 0]), np.array([-0.5, -0.7, 0])
        )
        inset_line2 = Line(
            np.array([-0.5, -0.7, 0]), np.array([-0.2, -0.7, 0])
        )
        left_line3 = Line(
            np.array([-0.2, -0.7, 0]), np.array([-0.35, -1.5, 0])
        )

        lines = VGroup(top_line, left_line1, inset_line1, left_line2, inset_line2, left_line3)
        self.add(lines)


class VectorBolt(Scene):
    def construct(self, actually_play_it = True, show_channel_name = False):
        point_arrow_upward=True

        # Triangles that form the lightning bolt
        triangle1 = Polygon(
            np.array([0, 0, 0]), np.array([-0.5, 0, 0]), np.array([0.2, 1, 0]),
            stroke_width=0,
            fill_opacity=1,
        )
        triangle1.scale(2)

        triangle2 = triangle1.copy().rotate(PI, about_point=triangle1.get_vertices()[0])

        # create horizontal vector BEFORE shifting triangle2
        vector2 = Arrow(
            triangle1.get_vertices()[1], triangle2.get_vertices()[1], color=YELLOW
        )
        vector2.scale(2)
        vector2.shift(UP*0.2)

        # finish manipulating triangle2
        triangle2.shift(UP*0.4)

        # arrow from tip to bottom
        vector = Arrow(triangle2.get_vertices()[2], triangle1.get_vertices()[2], color=YELLOW)
        vector.scale(1.5)

        # The Vector path through the middle
        buffed_line1 = Line(
            triangle1.get_vertices()[2], vector2.point_from_proportion(7/16), buff=0.2
        )
        vector3 = VGroup(
            Elbow(color=YELLOW, stroke_width=14)
                .set_points_as_corners([buffed_line1.get_start(), vector2.point_from_proportion(13/32), vector2.point_from_proportion(23/32), triangle2.get_vertices()[2]]),
            Arrow(vector2.point_from_proportion(23/32), triangle2.get_vertices()[2], buff=0, color=YELLOW, stroke_width=20)
                .scale(1.17, about_point=vector2.point_from_proportion(23/32))
        )

        # line segments of the triangles
        triangle_1_vertical = Line(
            triangle1.get_vertices()[0], triangle1.get_vertices()[2]
        )
        triangle_1_hyp = Line(
            triangle1.get_vertices()[1], triangle1.get_vertices()[2]
        )
        triangle_2_vertical = Line(
            triangle2.get_vertices()[0], triangle2.get_vertices()[2]
        )
        triangle_2_hyp = Line(
            triangle2.get_vertices()[1], triangle2.get_vertices()[2]
        )

        # Circular boundary around the Bolt
        right_boundary = ArcBetweenPoints(
            triangle_1_hyp.point_from_proportion(7/8) + 0.1*LEFT , triangle_2_vertical.point_from_proportion(7/8) + 0.1*LEFT,
            angle=175*DEGREES, stroke_width=20
        ).shift(0.01*UP + 0.01*LEFT)
        left_boundary = right_boundary.copy().rotate(PI, about_point=vector2.get_center() + 0.02*DOWN)
        boundaries = VGroup(left_boundary, right_boundary)

        everything = VGroup(triangle1, triangle2, vector3, boundaries)
        everything.move_to(ORIGIN).scale(1.8)
        if point_arrow_upward:
            everything.rotate(PI)

        # PLAY COMMANDS
        if actually_play_it:
            self.play(
                GrowFromCenter(triangle1),
                GrowFromCenter(triangle2)
            )
            self.play(Write(vector3))
            self.play(Write(boundaries))
            self.wait()

            if show_channel_name:
                self.play(
                    everything.scale, 0.7,
                    everything.move_to, UP,
                    run_time=0.8
                )

            # Draw Text
            rect =  Rectangle(fill_opacity=0.6, fill_color = BLACK, stroke_width=0)
            rect.to_edge(DOWN)
            underline_vector = Arrow(rect.get_vertices()[3], rect.get_vertices()[2])

            vector_bolt_text = TextMobject("VectorBolt")
            vector_bolt_text.scale(2)
            vector_bolt_text.next_to(everything, direction=DOWN, buff=MED_LARGE_BUFF)
            vector_bolt_text.set_color_by_gradient(TEAL, ORANGE)

            underline_vector.next_to(vector_bolt_text, direction=DOWN)

            #PLAY COMMANDS
            if show_channel_name:
                self.play(Write(vector_bolt_text), run_time=0.5)
                self.play(Write(underline_vector), run_time=0.5)
                self.wait()

        return everything


class VectorBoltBanner(Scene):
    def construct(self):
        func = lambda p: np.array([
            p[0]/2,  # x
            p[1]/2,  # y
            0        # z
        ])
        # Normalized Vector Field
        vector_field = VectorField(lambda p: np.array([
            p[0]/2,  # x
            p[1]/2,  # y
            0        # z
            ])
        )

        vector_bolt_logo = ImageMobject("VectorBolt 2.png")
        void_logo = ImageMobject("CircleNetwork.png").scale(0.85)
        text = TextMobject("VectorBolt").scale(1.5)
        #text.set_color_by_gradient(BLUE, GREEN)
        rect =  Rectangle(fill_opacity=0.6, fill_color = BLACK, stroke_width=0)
        underline_vector = Arrow(rect.get_vertices()[3], rect.get_vertices()[2]).shift(UP*0.4)

        self.play(*[GrowArrow(vector) for vector in vector_field])
        self.wait()

        self.play(
            FadeIn(vector_bolt_logo.shift(LEFT*3)),
            FadeIn(void_logo.shift(RIGHT*3))
        )
        self.play(
            FadeIn(rect),
            Write(text),
            FadeIn(underline_vector)
        )

        self.wait()


class FactoringWithRectangles(Scene):
    def construct(self):
        #x=2

        rectangle1 = Rectangle(width=2, height=4, color=BLUE, fill_opacity=0.7)
        rectangle1.to_corner(UL)

        rectangle2 = Rectangle(width=3, height=4, color=ORANGE, fill_opacity=0.7)
        rectangle2.to_corner(UR)

        rectangle1_width_label = TexMobject("2")
        rectangle1_width_label.next_to(rectangle1, direction=DOWN)
        rectangle1_height_label = TexMobject("x + 2")
        rectangle1_height_label.next_to(rectangle1, direction=RIGHT)

        rectangle2_width_label = TexMobject("3")
        rectangle2_width_label.next_to(rectangle2, direction=DOWN)
        rectangle2_height_label = TexMobject("x + 2")
        rectangle2_height_label.next_to(rectangle2, direction=LEFT)

        rectangle1_height = Line(
            rectangle1.get_vertices()[1], rectangle1.get_vertices()[2], stroke_width=7, color=GREEN
        )
        rectangle2_height = Line(
            rectangle2.get_vertices()[0], rectangle2.get_vertices()[3], stroke_width=7, color=GREEN
        )

        rectangle1_target = rectangle1.copy().move_to(ORIGIN)
        rectangle1_target.shift(LEFT)
        rectangle2_target = rectangle2.copy()
        rectangle2_target.next_to(rectangle1_target, buff=0)

        width_equation = TexMobject("2", "+", "3").next_to(VGroup(rectangle1_target, rectangle2_target), direction=DOWN)
        rectangle1_target_label = width_equation[0]
        rectangle2_target_label = width_equation[2]

        final_height = TexMobject("x + 2")
        final_height.next_to(rectangle2_target)

        self.play(
            Write(rectangle1)
        )
        self.play(
            Write(rectangle1_width_label),
            Write(rectangle1_height_label)
        )
        self.wait()

        self.play(
            Write(rectangle2)
        )
        self.play(
            Write(rectangle2_width_label),
            Write(rectangle2_height_label)
        )
        self.wait()

        self.play(
            Write(rectangle1_height)
        )
        self.wait()
        self.play(
            Write(rectangle2_height)
        )
        self.wait()

        self.play(
            FadeOut(rectangle1_height_label),
            FadeOut(rectangle2_height_label),
            FadeOut(rectangle1_height),
            FadeOut(rectangle2_height)
        )

        self.play(
            ReplacementTransform(rectangle1, rectangle1_target),
            ReplacementTransform(rectangle2, rectangle2_target),
            ReplacementTransform(rectangle1_width_label, rectangle1_target_label),
            ReplacementTransform(rectangle2_width_label, rectangle2_target_label),
            Write(width_equation[1])
        )
        self.wait()
        
        self.play(
            Write(final_height)
        )
        self.wait()


class FibGraph(Scene):
    """CONFIG = {
        "x_min": -6,
        "x_max": 6,
        "y_min": -2,
        "y_max": 25,
        "graph_origin": 3*DOWN,
        "axes_color": BLUE,
        "x_labeled_nums": range(-6, 7),
        "y_labeled_nums": range(-2, 26, 4)
    }"""

    def construct(self):
        #self.setup_axes(animate=True)
        grid = NumberPlane(x_min=-2, x_max=25, y_min=-2, y_max=15)
        grid.shift(3*DOWN+6*LEFT)
        grid.add_coordinates(x_vals = range(-2, 16), y_vals = range(-2, 16))

        func1 = grid.get_graph(lambda x: x**2)
        func2 = grid.get_graph(lambda x: 2*x + 3)


        self.play(
            ShowCreation(grid, run_time=2, lag_ratio=0.1),
        )
        for i,j in zip(range(10), creat_fib_list(10)):
            self.play(
                Write(
                    Dot(grid.coords_to_point(i,j))
                )
            )
        self.wait()


class Lorentz(LinearTransformationScene):
    CONFIG = {
        "show_basis_vectors": False
    }
    def construct(self):
        beta1 = 1/3
        beta2=2/3

        gamma1 = 1/math.sqrt(1 - (beta1 ** 2))
        gamma2 = 1/math.sqrt(1 - (beta2 ** 2))

        matrix1 =[[gamma1, -1 * gamma1 * beta1], 
                 [-1 * gamma1 * beta1, gamma1]]

        matrix2 =[[gamma2, -1 * gamma2 * beta2], 
                 [-1 * gamma2 * beta2, gamma2]]

        def one_third(x):
            return 3*x
        def two_thirds(x):
            return (3*x)/2
        def light(x):
            return x

        stationary = Line(ORIGIN, np.array([0, 10, 0]), stroke_color=YELLOW)
        graph1 = FunctionGraph(one_third, x_min=-10, x_max=10)
        graph2 = FunctionGraph(two_thirds, x_min=-10, x_max=10)
        light_graph = FunctionGraph(light, x_min=-10, x_max=10)

        self.add_transformable_mobject(stationary)
        self.add_transformable_mobject(graph1)
        self.add_transformable_mobject(graph2)
        self.add_transformable_mobject(light_graph)

        self.apply_matrix(matrix1)
        self.wait()


class LinearTransform(LinearTransformationScene):
    def construct(self):
        def line_graph(x):
            return 2*x - 1 
        line = FunctionGraph(line_graph, color=YELLOW)
        self.add_transformable_mobject(line)
        matrix = [[2, 1],
                  [-3, 2]]
        self.apply_matrix(matrix)


class NewtonMethod(MovingCameraScene):
    def construct(self):
        self.camera_frame.move_to(UP*2)

        grid = NumberPlane(y_max=8)
        # Constants of Standard Quadratic Function
        a=0.5
        b=-1
        c=0

        def parabola(x):
            return a*(x**2) + b*x + c
        # derivative of a quadratic
        def derivative(x):
            return 2*a*x + b

        parabola_graph = FunctionGraph(parabola, x_min=-4, x_max=8)
        starting_number = -2.5 # the x-coord to start at
        lines = []
        zoomed_centers = []

        for i in range(4):
            vert_line = Line(
                np.array([starting_number, 0, 0]), np.array([starting_number, parabola(starting_number), 0]), color=PURPLE
            )

            def tangent_func(x):
                return derivative(starting_number)*x + (parabola(starting_number) - derivative(starting_number)*starting_number)

            tangent_line = FunctionGraph(tangent_func, x_min=-6, x_max=6, color=GREEN)
            lines.append(vert_line)
            lines.append(tangent_line)
            starting_number = -1*(parabola(starting_number) - derivative(starting_number)*starting_number) / derivative(starting_number)
            zoomed_centers.append(np.array([starting_number, 0, 0]))

        # PLAY COMMANDS
        self.play(
            ShowCreation(grid, run_time=2, lag_ratio=0.1)
        )
        self.play(
            ShowCreation(parabola_graph)
        )

        self.camera_frame.save_state()
        frame_width = 3
        for i in range(8):
            self.play(
                ShowCreation(lines[i])
            )
            if i > 2 and i%1==0:
                self.play(
                    self.camera_frame.set_width, frame_width,
                    self.camera_frame.move_to, zoomed_centers[int((i-1)/2)]
                )
                frame_width = frame_width / 2
        self.wait()


class AssetTest(Scene):
    def construct(self):
        asset = ImageMobject("cool-rocket.png")
        #asset.scale(10)
        self.play(
            FadeIn(asset)
        )
        self.wait()    


class TestAbstractScene(Scene):
    def setup(self):
        circle = Circle(radius=2)
        square = Square(color=GREEN)

        self.circle = circle
        self.square = square


class PlayAbstractScene(TestAbstractScene):
    def construct(self):
        circle = self.circle
        square = self.square
        self.play(
            Write(circle)
        )
        self.play(
            ReplacementTransform(circle, square)
        )
        self.wait()


class SVGTest(Scene):
    def construct(self):
        graphic = SVGMobject("PiCreatures_plain.svg")
        graphic[2:4].set_color(BLACK)
        graphic[4].set_color(BLUE)
        graphic[5].set_color(BLACK)
        
        for layer in graphic:
            self.play(
                Write(layer)
            )       
        self.wait()
        self.play(
            Write(graphic)
        )
        self.wait()


class RotationMatrix(LinearTransformationScene):
    def construct(self):
        theta = PI/2
        matrix = np.array([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]])

        self.apply_matrix(matrix)
        self.wait()

class BlochSphereTesting(SpecialThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        sphere = self.get_sphere()
        sphere.set_opacity(0.2)
        vector = CurvedArrow(start_point=ORIGIN,end_point=(2)*RIGHT+(2)*UP+(2)*OUT,angle=0*DEGREES,color=GOLD_D)

        # PLAY COMMANDS
        self.add(axes, sphere, vector)
        self.set_camera_orientation(PI/3, 0)
        self.begin_ambient_camera_rotation()
        self.wait(6)
