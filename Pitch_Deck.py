from manimlib.imports import *

class PieChart(Scene):
    def construct(self):
        # Grade 3
        circle3 = Circle(color=YELLOW).scale(2.5)
        grade3_passed = Sector(
            outer_radius=2.5,
            start_angle=PI/2,
            angle = -58*TAU/100,
            color=BLUE_D
        )
        grade3_failed = Sector(
            outer_radius=2.5,
            start_angle=PI/2,
            angle = 42*TAU/100,
            color=RED_E
        )
        passed_text3 = TexMobject("58%").scale(1.5).shift(1.5*RIGHT+DOWN)
        failed_text3 = TexMobject("42%").scale(1.5).shift(1.5*LEFT+UP)
        grade3_label = TextMobject("Grade 3").scale(1.8).next_to(circle3, direction=DOWN)

        grade3_list = [circle3, grade3_passed, grade3_failed, passed_text3, failed_text3, grade3_label]
        grade3 = VGroup()
        for obj in grade3_list:
            grade3.add(obj)

        # Grade 6
        circle6 = Circle(color=YELLOW).scale(2.5)
        grade6_passed = Sector(
            outer_radius=2.5,
            start_angle=PI/2,
            angle = -48*TAU/100,
            color=BLUE_D
        )
        grade6_failed = Sector(
            outer_radius=2.5,
            start_angle=PI/2,
            angle = 52*TAU/100,
            color=RED_E
        )
        passed_text6 = TexMobject("48%").scale(1.5).shift(1.5*RIGHT+DOWN)
        failed_text6 = TexMobject("52%").scale(1.5).shift(1.5*LEFT+UP)
        grade6_label = TextMobject("Grade 6").scale(1.8).next_to(circle3, direction=DOWN)

        grade6_list = [circle6, grade6_passed, grade6_failed, passed_text6, failed_text6, grade6_label]
        grade6 = VGroup()
        for obj in grade6_list:
            grade6.add(obj)

        # Grade 9
        circle9 = Circle(color=YELLOW).scale(2.5)
        grade9_passed = Sector(
            outer_radius=2.5,
            start_angle=PI/2,
            angle = -44*TAU/100,
            color=BLUE_D
        )
        grade9_failed = Sector(
            outer_radius=2.5,
            start_angle=PI/2,
            angle = 56*TAU/100,
            color=RED_E
        )
        passed_text9 = TexMobject("44%").scale(1.5).shift(1.5*RIGHT+DOWN)
        failed_text9 = TexMobject("56%").scale(1.5).shift(1.5*LEFT+UP)
        grade9_label = TextMobject("Grade 9").scale(1.2).next_to(circle3, direction=DOWN)
        grade9_label2 = TextMobject("Applied").scale(1.2).next_to(grade9_label, direction=DOWN)

        grade9_list = [circle9, grade9_passed, grade9_failed, passed_text9, failed_text9, grade9_label, grade9_label2]
        grade9 = VGroup()
        for obj in grade9_list:
            grade9.add(obj)

        we_failing1 = TextMobject("Our math education").scale(2).to_edge(UP)
        we_failing2 = TextMobject("system is").scale(2).next_to(we_failing1, direction=DOWN).shift(LEFT)
        we_failing3 = TextMobject("failing").scale(2).next_to(we_failing2, direction=RIGHT).set_color(RED)

        # PLAY COMMANDS
        
        self.play(
            *[Write(obj) for obj in grade3_list]
        )
        self.wait()
        
        self.play(
            grade3.scale, 4/5,
            grade3.to_corner, DL,
            run_time=0.5
        )
        self.wait()

        self.play(
            *[Write(obj) for obj in grade6_list]
        )
        self.wait()
        
        self.play(
            grade6.scale, 4/5,
            grade6.to_edge, DOWN,
            run_time=0.5
        )
        self.wait()

        self.play(
            *[Write(obj) for obj in grade9_list],
            FadeOut(grade6_label)
        )
        self.wait()
        
        self.play(
            FadeIn(grade6_label),
            grade9.scale, 4/5,
            grade9.to_corner, DR,
            run_time=0.5
        )
        self.wait()

        self.play(grade9.shift, DOWN*0.45)
        self.play(
            AnimationGroup(
                Write(we_failing1),
                Write(we_failing2),
                Write(we_failing3),
                lag_ratio=0.5
            )
        )
        self.wait()

        
class RearrangementProofShort(Scene):
    def construct(self, return_end_scene1=False, return_end_scene2=False):
        title_text = TextMobject("Pythagorean Theorem:")
        title_text.to_edge(UP, buff = 0.8)
        theorem = TexMobject(r"c^2", "=", "a^2", "+", "b^2").scale(1.5)
        theorem.next_to(title_text, direction=DOWN)
        square_1 = Square()
        square_1.scale(2)

        points = [] #empty array of points
        #create an array of 4 points around the square; points stored as np.array
        for i in range(4):
            points.append(square_1.point_from_proportion(i * 1/4 + 1/16))   

        # corners of the square
        corner_points = []
        for i in range(4):
            corner_points.append(square_1.point_from_proportion(i * 1/4))

        # Initial Triangles
        initial_triangles = []
        for i in range(4):
            initial_triangles.append(Polygon(
                np.array(corner_points[i]),
                np.array(points[i]),
                np.array(points[i-1]),
                fill_opacity=0.7,
                stroke_width=2
            ))
        all_initial_triangles = VGroup()
        for triangle in initial_triangles:
            all_initial_triangles.add(triangle)

        # Labels
        labels = []
        for i,j,k,l in zip(range(4), [UP, RIGHT, DOWN, LEFT], [LEFT, UP, RIGHT, DOWN], [RIGHT, DOWN, LEFT, UP]):
            labels.append(VGroup(
                TexMobject(r"a").next_to(initial_triangles[i], direction=j),
                TexMobject(r"b").next_to(initial_triangles[i], direction=k),
                TexMobject(r"c").next_to(initial_triangles[i], direction=l, buff=-0.3)
            ))

        # c_squared
        c_squared = Polygon(
            np.array(points[0]), np.array(points[1]), np.array(points[2]), np.array(points[3]),
            fill_opacity = 0.7
        )
        c_squared.set_color(ORANGE)

        c_squared_text = TexMobject(r"c^2")
        c_squared_text.scale(1.5)

        # Drawing Right Angles
        points_on_c_squared = []
        for i in [31, 1, 7, 9, 15, 17, 23, 25]:
            points_on_c_squared.append(c_squared.point_from_proportion(i/32))
        corners_of_c_squared = []
        for i in range(4):
            corners_of_c_squared.append(
                c_squared.point_from_proportion(i/4)
            )
        
        # END SCENE 1
        everything = VGroup(all_initial_triangles, c_squared)
        if return_end_scene1:
            return everything
        
        # PLAY COMMANDS
        if return_end_scene1==False and return_end_scene2==False:
            self.play(
                FadeInFrom(title_text, direction=UP),
                Write(theorem)
            )
            self.wait()

            self.play(
                FadeOut(theorem),
                Write(square_1)
            )
            self.play(
                AnimationGroup(*[
                    Write(triangle)
                    for triangle in initial_triangles
                ], lag_ratio=0.5)
            )
            
            # Writing the lables
            self.play(
                AnimationGroup(*[
                    Write(label)
                    for label in labels
                ], lag_ratio=0.8)
            )
            self.play(
                ShowCreation(c_squared),
            )
            self.play(
                Write(c_squared_text)
            )
            self.wait()

        theorem.to_edge(DOWN)

        c_squared_text.generate_target()
        c_squared_text.target = theorem[0]

        # PLAY COMMANDS
        if return_end_scene1==False and return_end_scene2==False:
            self.play(
                MoveToTarget(c_squared_text),
                Write(theorem[1])
            )
            self.play(
                FadeOut(
                    VGroup(c_squared)
                ),
                FadeOut(
                    VGroup(labels[0][2], labels[1], labels[2], labels[3])
                )
            )
            self.play(
                Rotate(initial_triangles[1], -90*DEGREES, about_point=initial_triangles[0].get_vertices()[1])
            )
            self.play(
                Rotate(initial_triangles[2], 90*DEGREES, about_point=initial_triangles[3].get_vertices()[2])
            )
            self.play(
                initial_triangles[2].shift, RIGHT,
                initial_triangles[3].shift, RIGHT
            )
            self.wait()

        # points on square_2
        square_2 = Square()
        square_2.scale(2)

        points_2 = []
        for j in [1, 7, 11, 13]:
            points_2.append(square_2.point_from_proportion(j/16))

        corner_points_2 = []
        for j in range(4):
            corner_points_2.append(square_2.point_from_proportion(j * 1/4))

        middle_point = np.array(
            [points_2[0][0], points_2[3][1], 0]
        )

        # a_squared
        a_squared = Polygon(
            np.array(middle_point), np.array(points_2[2]), np.array(corner_points_2[3]), np.array(points_2[3]),
            fill_opacity = 0.7
        )
        a_squared.set_color(ORANGE)
        a_squared_text = TexMobject(r"a^2")
        a_squared_text.move_to(a_squared.get_center())
        a_squared_text.scale(1.5)

        # b_squared
        b_squared = Polygon(
            np.array(middle_point), np.array(points_2[0]), np.array(corner_points_2[1]), np.array(points_2[1]),
            fill_opacity = 0.7
        )
        b_squared.set_color(ORANGE)
        b_squared_text = TexMobject(r"b^2")
        b_squared_text.move_to(b_squared.get_center())
        b_squared_text.scale(1.5)

        # line segments
        line_a1 = Line(
            np.array(middle_point), np.array(points_2[2]),
            stroke_width = 5,
            stroke_color = GREEN
        )
        a_left_label = TexMobject(r"a")
        a_left_label.add_updater(lambda p: p.next_to(line_a1, direction=LEFT))

        line_a2 = Line(
            np.array(middle_point), np.array(points_2[3]),
            stroke_width = 5,
            stroke_color = GREEN
        )
        a_down_label = TexMobject(r"a")
        a_down_label.add_updater(lambda p: p.next_to(line_a2, direction=DOWN))

        line_b1 = Line(
            np.array(middle_point), np.array(points_2[0]),
            stroke_width = 5,
            stroke_color = GREEN
        )
        b_right_label = TexMobject(r"b")
        b_right_label.add_updater(lambda p: p.next_to(line_b1, direction=RIGHT))

        line_b2 = Line(
            np.array(middle_point), np.array(points_2[1]),
            stroke_width = 5,
            stroke_color = GREEN
        )
        b_up_label = TexMobject(r"b")
        b_up_label.add_updater(lambda p: p.next_to(line_b2, direction=UP))

        if return_end_scene1==False and return_end_scene2==False:
            """
            self.play(
                GrowFromCenter(line_a1),
                Write(a_left_label),
            )
            self.play(
                line_a1.shift, LEFT
            )
            self.wait(0.5)

            self.play(
                GrowFromCenter(line_a2),
                Write(a_down_label)
            )
            self.play(
                line_a2.shift, DOWN
            )
            """

            self.play(
                ShowCreation(a_squared),
                Write(a_squared_text),
            )
            self.wait(0.5)

            """
            self.play(
                GrowFromCenter(line_b1),
                Write(b_right_label),
            )
            self.play(
                line_b1.shift, RIGHT*3
            )
            self.wait(0.5)

            self.play(
                GrowFromCenter(line_b2),
                Write(b_up_label)
            )
            self.play(
                line_b2.shift, UP*3
            )
            """

            self.play(
                ShowCreation(b_squared),
                Write(b_squared_text)
            )
            self.wait()

            self.play(
                ReplacementTransform(a_squared_text.copy(), theorem[2]),
                Write(theorem[3]),
                ReplacementTransform(b_squared_text.copy(), theorem[4])
            )
            self.play(
                Write(
                    SurroundingRectangle(theorem, buff=0.1)
                )
            )

        # END SCENE 2
        everything = VGroup(a_squared.shift(RIGHT*3.5), b_squared.shift(RIGHT*3.5))
        if return_end_scene2:
            initial_triangles[1].rotate(-90*DEGREES, about_point=initial_triangles[0].get_vertices()[1])
            initial_triangles[2].rotate(90*DEGREES, about_point=initial_triangles[3].get_vertices()[2])
            initial_triangles[2].shift(RIGHT)
            initial_triangles[3].shift(RIGHT)
            for triangle in initial_triangles:
                everything.add(triangle)
            return everything


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
            ShowCreation(grid, lag_ratio=0.1)
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


class DeterminantThing(LinearTransformationScene):
    def construct(self):
        matrix = [[2, 1],
                  [-1, 2]]
        
        square = Square(
            fill_opacity=0.7, color=YELLOW
        )
        square.scale(0.5).move_to([0.5, 0.5, 0])
        
        self.add_transformable_mobject(square)
        self.apply_matrix(matrix)
        self.wait()


class Experiment(Scene):
    def construct(self):
        circle = Circle(radius=0.7, color=WHITE)
        stick_figure = VGroup(
            circle,
            Line(circle.point_from_proportion(3/4), circle.point_from_proportion(3/4)+2*DOWN),
            Line(circle.point_from_proportion(3/4)+2*DOWN, circle.point_from_proportion(3/4)+3*DOWN+LEFT),
            Line(circle.point_from_proportion(3/4)+2*DOWN, circle.point_from_proportion(3/4)+3*DOWN+RIGHT),
            Line(circle.point_from_proportion(3/4)+DOWN, circle.point_from_proportion(3/4)+RIGHT),
            Line(circle.point_from_proportion(3/4)+DOWN, circle.point_from_proportion(3/4)+LEFT)
        )
        stick_figure.scale(0.3)

        stick_figures1_row1 = VGroup()
        for i in range(5):
            stick_figures1_row1.add(
                stick_figure.copy()
            )
        stick_figures1_row1.arrange(RIGHT)
        
        stick_figures1 = VGroup()
        for i in range(2):
            stick_figures1.add(
                stick_figures1_row1.copy()
            )
        stick_figures1.arrange(DOWN)

        stick_figures2 = stick_figures1.copy()

        stick_figures1.shift(LEFT*3.5)
        stick_figures2.shift(RIGHT*3.5)
        box1 = SurroundingRectangle(stick_figures1, buff=0.5)
        box2 = SurroundingRectangle(stick_figures2, buff=0.5)

        with_app = TextMobject("With VectorSpace").next_to(box1, direction=UP)
        without_app = TextMobject("Without VectorSpace").next_to(box2, direction=UP)

        # PLAY COMMANDS
        self.play(
            Write(box1),
            Write(box2)
        )
        self.wait()

        self.play(
            Write(stick_figures1),
            Write(with_app),
            run_time=0.7
        )
        self.wait()

        self.play(
            Write(stick_figures2),
            Write(without_app),
            run_time=0.7
        )
        self.wait()
