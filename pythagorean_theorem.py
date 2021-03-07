from manimlib.imports import *

def pulse(self, shapes, pulse_color):
    for shape in shapes:
        original_color = shape.get_color()
        self.play(
            shape.scale, 8/7,
            shape.set_color, pulse_color,
            run_time=0.3
        )
        self.play(
            shape.scale, 7/8,
            shape.set_color, original_color,
            run_time=0.3
        )

def prove_angle_is_a_right_angle(self, large_triangle, upper_triangle, elbow_to_be_proved, shift_factor, is_not_for_adjacent_angles):
    # FOCUS ON ONE TRIANGLE
    self.play(
        large_triangle.scale, 1.8,
        large_triangle.shift, shift_factor,
        path_arc=-2,
        run_time=2
    )

    # Points on Triangle
    large_triangle_right_angle_vertex = large_triangle.get_vertices()[0]
    large_triangle_rightmost_vertex = large_triangle.get_vertices()[2]
    large_triangle_upper_vertex = large_triangle.get_vertices()[1]

    # Line Segments
    hypotenuse_segment = Line(
        np.array(large_triangle_upper_vertex), np.array(large_triangle_rightmost_vertex),
        stroke_width=5,
        color=GREEN
    )
    height_segment = Line(
        np.array(large_triangle_upper_vertex), np.array(large_triangle_right_angle_vertex),
        stroke_width=5,
        color=GREEN
    )
    base_segment = Line(
        np.array(large_triangle_right_angle_vertex), np.array(large_triangle_rightmost_vertex),
        stroke_width=5,
        color=GREEN
    )

    # Angles of Triangle

    # Right Angle
    right_angle_point_1 = np.array(large_triangle_right_angle_vertex + 0.3*UP)
    right_angle_point_2 = np.array(large_triangle_right_angle_vertex + 0.3*RIGHT)
    right_angle_middle_point = np.array(large_triangle_right_angle_vertex + 0.3*UP + 0.3*RIGHT)
    right_angle = Elbow()
    right_angle.set_points_as_corners([right_angle_point_1, right_angle_middle_point, right_angle_point_2])

    angle_x = Arc(
        start_angle=height_segment.get_angle(),
        angle=hypotenuse_segment.get_angle() - height_segment.get_angle(),
        radius=0.4,
        arc_center=large_triangle_upper_vertex
    )
    angle_y = Arc(
        start_angle=base_segment.get_angle(),
        angle=hypotenuse_segment.get_angle(),
        radius=1,
        arc_center=large_triangle_rightmost_vertex
    )
    angle_y.rotate(180*DEGREES, about_point=large_triangle_rightmost_vertex)

    angle_x_label = TexMobject(r"x", background_stroke_width=0).next_to(angle_x, direction=DOWN, buff=0.05)
    angle_x_label.shift(0.2*RIGHT)
    angle_y_label = TexMobject(r"y", background_stroke_width=0).next_to(angle_y, direction=LEFT, buff=0.2)
    right_angle_label = TexMobject(r"90^{\circ}", background_stroke_width=0).scale(0.8)
    right_angle_label.next_to(right_angle, direction=RIGHT+UP, buff=SMALL_BUFF)

    # Sum of angles in a triangle
    angle_sum_equation = TexMobject(r"90^{\circ}", "+", "x", "+", "y", "=", "180^{\circ}")
    angle_sum_equation.next_to(large_triangle, direction=DOWN, buff=1)

    subtract_90_left_side = TexMobject(r"-90^{\circ}")
    subtract_90_left_side.next_to(angle_sum_equation[0], direction=DOWN)
    subtract_90_left_side.shift(LEFT*0.2)
    subtract_90_right_side = TexMobject(r"-90^{\circ}")
    subtract_90_right_side.next_to(angle_sum_equation[6], direction=DOWN)
    subtract_90_right_side.shift(LEFT*0.1)

    left_side_90s = VGroup(angle_sum_equation[0], subtract_90_left_side)
    eliminate_left_side = Cross(left_side_90s)

    right_side = VGroup(angle_sum_equation[6], subtract_90_right_side)

    right_side_final = TexMobject(r"90^{\circ}")
    right_side_final.move_to(angle_sum_equation[6].get_center())

    angle_sum_equation_final = VGroup(angle_sum_equation[2:6], right_side_final)

    large_triangle_group = VGroup(
        large_triangle, angle_x, angle_x_label, angle_y, angle_y_label, right_angle, base_segment, height_segment, hypotenuse_segment
    )

    # PLAY COMMANDS
    self.play(
        Write(right_angle),
        Write(right_angle_label)
    )
    self.wait()

    self.play(
        Write(angle_x),
        Write(angle_y),
        Write(angle_x_label),
        Write(angle_y_label)
    )
    self.wait(2)

    self.play(
        ReplacementTransform(right_angle_label.copy(), angle_sum_equation[0]),
        Write(angle_sum_equation[1]),
        ReplacementTransform(angle_x_label.copy(), angle_sum_equation[2]),
        Write(angle_sum_equation[3]),
        ReplacementTransform(angle_y_label.copy(), angle_sum_equation[4]),
        Write(angle_sum_equation[5]),
        Write(angle_sum_equation[6])
    )
    self.wait()

    self.play(
        Write(subtract_90_left_side),
        Write(subtract_90_right_side),
    )
    self.wait(1)

    self.play(
        ShowCreation(eliminate_left_side)
    )
    self.wait()

    self.play(
        FadeOut(left_side_90s),
        FadeOut(eliminate_left_side),
        FadeOut(angle_sum_equation[1]),
    )
    self.wait()

    self.play(
        ReplacementTransform(right_side, right_side_final)
    )

    self.wait(2)

    # Put triangle back in
    self.play(
        FadeOut(right_angle_label),
    )
    self.play(
        large_triangle_group.scale, 5/9,
        large_triangle_group.shift, -shift_factor,
        path_arc=-2,
        run_time=2
    )
    self.play(
        FadeOut(base_segment),
        FadeOut(height_segment),
        FadeOut(hypotenuse_segment),
        angle_x_label.shift, 0.04*DOWN,
        angle_x_label.shift, 0.04*RIGHT,
        angle_y_label.shift, 0.04*LEFT,
        angle_sum_equation_final.move_to, UP+RIGHT*2,
    )
    self.play(
        angle_x_label.scale, 1.6,
        angle_y_label.scale, 1.6
    )

    # Flash Upper Triangle
    pulse(self, upper_triangle, YELLOW)

    # Angles of Upper Triangle
    upper_triangle_right_angle_vertex = upper_triangle.get_vertices()[0]
    right_angle_vertex_1 = np.array(upper_triangle_right_angle_vertex + 0.2*RIGHT)
    right_angle_vertex_2 = np.array(upper_triangle_right_angle_vertex + 0.2*RIGHT + 0.2*DOWN)
    right_angle_vertex_3 = np.array(upper_triangle_right_angle_vertex + 0.2*DOWN)
    upper_triangle_right_angle = Elbow()
    upper_triangle_right_angle.set_points_as_corners([right_angle_vertex_1, right_angle_vertex_2, right_angle_vertex_3])

    upper_triangle_angle_x_vertex = upper_triangle.get_vertices()[1]
    upper_triangle_angle_y_vertex = upper_triangle.get_vertices()[2]

    # Line Segments for angle_y_2
    line_segment_b = Line(
        np.array(upper_triangle_right_angle_vertex), np.array(upper_triangle_angle_y_vertex),
        stroke_width = 5,
        color = GREEN
    )

    hypotenuse_segment_c = Line(
        np.array(upper_triangle_angle_x_vertex), np.array(upper_triangle_angle_y_vertex),
        stroke_width = 5,
        color = GREEN
    )

    angle_y_2 = Arc(
        start_angle=hypotenuse_segment_c.get_angle(),
        angle=line_segment_b.get_angle() - hypotenuse_segment_c.get_angle(),
        radius=0.7,
        arc_center=upper_triangle_angle_y_vertex
    )
    angle_y_2.rotate(180*DEGREES, about_point=upper_triangle_angle_y_vertex)
    angle_y_2_label = TexMobject(r"?", background_stroke_width=0).next_to(angle_y_2, direction=UP, buff=0.1)
    angle_y_2_label.shift(RIGHT*0.04)
    angle_y_2_label.scale(0.7)

    angle_y_2_label_transformed = TexMobject(r"y", background_stroke_width=0).next_to(angle_y_2, direction=UP, buff=0.1)
    angle_y_2_label_transformed.shift(RIGHT*0.04)
    angle_y_2_label_transformed.scale(0.7)

    rect_around_angle_y = SurroundingRectangle(
        VGroup(
            angle_y_label, angle_y, Dot(large_triangle.get_vertices()[2])
            ),
            buff=0.05
        )
    rect_around_angle_y.generate_target()
    rect_around_angle_y.target = SurroundingRectangle(angle_y_2_label)

    # Line Segments for angle_x_2
    line_segment_a = Line(
        np.array(upper_triangle_angle_x_vertex), np.array(upper_triangle_right_angle_vertex),
        stroke_width = 5,
        color = GREEN
    )

    angle_x_2 = Arc(
        start_angle= line_segment_a.get_angle(),
        angle= hypotenuse_segment_c.get_angle() + line_segment_a.get_angle(),
        radius=0.7,
        arc_center=upper_triangle_angle_x_vertex
    )
    angle_x_2_label = TexMobject(r"?", background_stroke_width=0).next_to(angle_x_2, direction=DL, buff=-0.1)
    #angle_x_2_label.scale(0.8)

    angle_x_2_label_transformed = TexMobject(r"x", background_stroke_width=0).next_to(angle_x_2, direction=DL, buff=-0.1)

    rect_around_angle_x = SurroundingRectangle(
        VGroup(
            angle_x_label, angle_x, Dot(large_triangle.get_vertices()[1])
            ),
            buff=0.05
        )
    rect_around_angle_x.generate_target()
    rect_around_angle_x.target = SurroundingRectangle(angle_x_2_label)
    
    # PROVING THAT IT IS A RIGHT ANGLE
    if is_not_for_adjacent_angles:
        self.play(
            Write(upper_triangle_right_angle)
        )
        self.wait()
        self.play(
            FadeIn(line_segment_b),
            FadeIn(hypotenuse_segment_c)
        )
        self.wait()
        self.play(
            Write(angle_y_2),
            Write(angle_y_2_label)
        )
        self.play(
            FadeIn(base_segment),
            FadeIn(hypotenuse_segment)
        )
        self.play(
            Write(rect_around_angle_y)
        )

        self.wait()

        self.play(
            MoveToTarget(rect_around_angle_y)
        )
        self.play(
            ReplacementTransform(angle_y_2_label, angle_y_2_label_transformed)
        )
        self.play(
            FadeOut(rect_around_angle_y),
            FadeOut(base_segment),
            FadeOut(hypotenuse_segment),
            FadeOut(line_segment_b),
            FadeOut(hypotenuse_segment_c)
        )

        self.wait(2)

        # Finally proving it is a right angles
        c_line_1 = Line(
            np.array(upper_triangle_angle_y_vertex), np.array(upper_triangle_angle_x_vertex)
        )
        c_line_2 = Line(
            np.array(upper_triangle_angle_y_vertex), np.array(large_triangle.get_vertices()[2])
        )
        arc_between_c_lines = Arc(
            start_angle=c_line_1.get_angle(),
            angle=c_line_2.get_angle() - c_line_1.get_angle(),
            radius=0.4,
            arc_center=upper_triangle_angle_y_vertex
        )
        arc_between_c_lines.generate_target()
        arc_between_c_lines_label = TexMobject(r"z", background_stroke_width=0).next_to(arc_between_c_lines, buff=0.1)
        arc_between_c_lines_label.generate_target()
        arc_between_c_lines_label.target = TexMobject(r"90^{\circ}", background_stroke_width=0).scale(0.8)
        arc_between_c_lines_label.target.next_to(elbow_to_be_proved, buff=0.1)
        arc_between_c_lines_label.target.shift(UP*0.1)

        rect_around_angles = SurroundingRectangle(VGroup(angle_x, angle_x_label, angle_y_2, angle_y_2_label, arc_between_c_lines_label))

        supplementary_angles_equation_1 = TexMobject(r"x", "+", "y", "+", "z", "=", "180^{\circ}")
        supplementary_angles_equation_1.move_to(0.3*UP+2*RIGHT)

        supplementary_angles_equation_2 = TexMobject(r"90^{\circ}", "+", "z", "=", "180^{\circ}")
        supplementary_angles_equation_2.move_to(0.3*UP+2*RIGHT)
    else:
        self.play(
            Write(upper_triangle_right_angle)
        )
        self.wait()
        self.play(
            FadeIn(line_segment_a),
            FadeIn(hypotenuse_segment_c)
        )
        self.wait()
        self.play(
            Write(angle_x_2),
            Write(angle_x_2_label)
        )
        self.play(
            FadeIn(height_segment),
            FadeIn(hypotenuse_segment)
        )
        self.play(
            Write(rect_around_angle_x)
        )

        self.wait()

        self.play(
            MoveToTarget(rect_around_angle_x)
        )
        self.play(
            ReplacementTransform(angle_x_2_label, angle_x_2_label_transformed)
        )
        self.play(
            FadeOut(rect_around_angle_x),
            FadeOut(height_segment),
            FadeOut(hypotenuse_segment),
            FadeOut(line_segment_a),
            FadeOut(hypotenuse_segment_c)
        )

        self.wait(2)

        # Finally proving it is a right angles
        c_line_1 = Line(
            np.array(upper_triangle_angle_x_vertex), np.array(upper_triangle_angle_y_vertex)
        )
        c_line_2 = Line(
            np.array(large_triangle_upper_vertex), np.array(large_triangle_rightmost_vertex)
        )
        arc_between_c_lines = Arc(
            start_angle=c_line_1.get_angle(),
            angle= c_line_1.get_angle() - c_line_2.get_angle(),
            radius=0.4,
            arc_center=upper_triangle_angle_x_vertex
        )
        
        arc_between_c_lines.generate_target()
        arc_between_c_lines_label = TexMobject(r"z", background_stroke_width=0).next_to(arc_between_c_lines, buff=-0.13)
        arc_between_c_lines_label.generate_target()
        arc_between_c_lines_label.target = TexMobject(r"90^{\circ}", background_stroke_width=0).scale(0.8)
        arc_between_c_lines_label.target.next_to(elbow_to_be_proved, buff=0.1)
        arc_between_c_lines_label.target.shift(UP*0.1)

        rect_around_angles = SurroundingRectangle(VGroup(angle_y, angle_y_label, angle_x_2, angle_x_2_label, arc_between_c_lines_label))

        supplementary_angles_equation_1 = TexMobject(r"x", "+", "y", "=", "z")
        supplementary_angles_equation_1.move_to(0.3*UP+2*RIGHT)

        supplementary_angles_equation_2 = TexMobject(r"90^{\circ}", "=", "z")
        supplementary_angles_equation_2.move_to(0.3*UP+2*RIGHT)

    rect_around_equation_1 = SurroundingRectangle(angle_sum_equation_final)
    rect_around_equation_2 = SurroundingRectangle(supplementary_angles_equation_1[:3])
    rect_around_equation_3 = SurroundingRectangle(supplementary_angles_equation_2[0])

    if is_not_for_adjacent_angles:
        # Simplifying equation
        subtract_90_left_side_2 = TexMobject(r"-90^{\circ}")
        subtract_90_left_side_2.next_to(supplementary_angles_equation_2[0], direction=DOWN)
        subtract_90_left_side_2.shift(LEFT*0.2)
        subtract_90_right_side_2 = TexMobject(r"-90^{\circ}")
        subtract_90_right_side_2.next_to(supplementary_angles_equation_2[4], direction=DOWN)
        subtract_90_right_side_2.shift(LEFT*0.1)

        left_side_90s_2 = VGroup(supplementary_angles_equation_2[0], subtract_90_left_side_2)
        eliminate_left_side_2 = Cross(left_side_90s_2)

        right_side_2 = VGroup(supplementary_angles_equation_2[4], subtract_90_right_side_2)

        right_side_final_2 = TexMobject(r"90^{\circ}")
        right_side_final_2.move_to(supplementary_angles_equation_2[4].get_center())

        supplementary_angles_equation_final = VGroup(supplementary_angles_equation_2[2:4], right_side_final_2)

        rect_around_supp_ang_eq_final = SurroundingRectangle(supplementary_angles_equation_final)

        self.all_objects_in_angle_proof = VGroup(
            angle_x, angle_y, angle_y_2, angle_x_label, angle_y_label, angle_y_2_label_transformed, right_angle, upper_triangle_right_angle, elbow_to_be_proved, rect_around_supp_ang_eq_final
        )
    else:
        rect_around_supp_ang_eq_final = SurroundingRectangle(supplementary_angles_equation_2)
        self.all_objects_in_angle_proof = VGroup(
            angle_x, angle_y, angle_x_2, angle_x_label, angle_y_label, angle_x_2_label_transformed, right_angle, upper_triangle_right_angle, elbow_to_be_proved, rect_around_supp_ang_eq_final
        )
        self.equations = VGroup(
            supplementary_angles_equation_2, angle_sum_equation_final
        )

    self.play(
        Write(arc_between_c_lines),
        Write(arc_between_c_lines_label)
    )
    self.wait()

    self.play(
        Write(rect_around_angles)
    )
    self.wait()

    if is_not_for_adjacent_angles:
        self.play(
            FadeIn(line_segment_b, height_segment),
            FadeIn(height_segment)
        )
        self.wait()

    self.play(
        Write(supplementary_angles_equation_1)
    )
    self.wait()

    self.play(
        Write(rect_around_equation_1)
    )
    self.wait()

    self.play(
        ReplacementTransform(rect_around_equation_1, rect_around_equation_2)
    )
    self.wait()

    self.play(
        ReplacementTransform(supplementary_angles_equation_1, supplementary_angles_equation_2),
        ReplacementTransform(rect_around_equation_2, rect_around_equation_3)
    )
    self.play(
        FadeOut(rect_around_equation_3)
    )
    self.wait()

    if is_not_for_adjacent_angles:
        self.play(
            Write(subtract_90_left_side_2),
            Write(subtract_90_right_side_2)
        )
        self.wait()

        self.play(
            Write(eliminate_left_side_2)
        )
        self.play(
            FadeOut(left_side_90s_2),
            FadeOut(eliminate_left_side_2),
            FadeOut(supplementary_angles_equation_2[1])
        )
        self.wait()

        self.play(
            ReplacementTransform(right_side_2, right_side_final_2)
        )
        self.wait()

    self.play(
        Write(rect_around_supp_ang_eq_final)
    )
    self.wait()

    self.play(
        MoveToTarget(arc_between_c_lines_label),
        ReplacementTransform(arc_between_c_lines, elbow_to_be_proved),
        FadeOut(rect_around_angles),
    )
    if is_not_for_adjacent_angles:
        self.play(
            FadeOut(line_segment_b),
            FadeOut(height_segment)
        )
    self.wait(0.5)

    self.play(
        FadeOut(arc_between_c_lines_label)
    )
    self.wait()


class StatingTheorem(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": GREEN_SCREEN,
            "frame_center": 3.5*RIGHT
        }
    }
    def construct(self):
        triangle = Polygon(
            np.array([-2, -1, 0]), np.array([2, -1, 0]), np.array([-2, 2, 0]),
            fill_opacity=1, fill_color=RED
        )

        # Line Segments
        a_segment = Line(
            triangle.get_vertices()[0], triangle.get_vertices()[2]
        )
        b_segment = Line(
            triangle.get_vertices()[0], triangle.get_vertices()[1]
        )
        hypotenuse = Line(
            triangle.get_vertices()[2], triangle.get_vertices()[1]
        )

        line_segments = [a_segment, b_segment, hypotenuse]

        # labels
        a_label = TexMobject("a").next_to(a_segment, direction=LEFT).scale(1.5)
        b_label = TexMobject("b").next_to(b_segment, direction=DOWN).scale(1.5)
        c_label = TexMobject("c").next_to(hypotenuse, direction=UP, buff=-1).scale(1.5)

        labels = [a_label, b_label, c_label]

        # Theorem
        theorem = TexMobject("c^2", "=", "a^2", "+", "b^2")
        theorem.scale(1.5)
        theorem.to_edge(DOWN, buff=0.6)

        question_mark = TextMobject("?").scale(1.5)
        question_mark.set_color(ORANGE)
        question_mark.next_to(theorem, buff=0.5)

        # PLAY COMMANDS
        self.play(
            LaggedStart(
                Write(triangle),
                LaggedStart(
                    *[
                        Write(label)
                        for label in labels
                    ]
                ),
                LaggedStart(
                    *[
                        Write(line)
                        for line in line_segments
                    ]
                )
            )
        )
        self.wait()

        self.play(
            Write(theorem[0]),
            Indicate(c_label),
            Indicate(hypotenuse)
        )
        self.wait()

        self.play(
            Write(theorem[1])
        )
        self.wait()

        self.play(
            Write(theorem[2]),
            Indicate(a_segment),
            Indicate(a_label)
        )

        self.play(
            Write(theorem[3])
        )
        self.play(
            Write(theorem[4]),
            Indicate(b_label),
            Indicate(b_segment)
        )
        self.wait()

        self.play(
            Write(question_mark)
        )
        self.wait()


class InfinitelyManyTriangles(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": GREEN_SCREEN
        }
    }
    def construct(self):
        triangles = []
        for i in range(16):
            triangles.append(
                VGroup(
                    Polygon(
                        ORIGIN, ORIGIN + random.uniform(0, 4)*RIGHT, ORIGIN + random.uniform(0, 4)*UP,
                        fill_color=ORANGE, fill_opacity=1, stroke_color=PURPLE
                    ),
                )
            )
        
        for triangle in triangles:
            #triangle.rotate(random.uniform(0, TAU))
            triangle.move_to(np.array([random.uniform(-7, 7), random.uniform(-3, 3), 0]))

        for triangle in triangles:
            self.wait(0.07)
            self.add_sound("Pop")
            self.add(triangle)
        self.wait()


class TheoremWithSquares(Scene):
    def construct(self, return_end_scene1=False, return_end_scene2=False):
        triangle = Polygon(
            np.array([-2, -1, 0]), np.array([1, -1, 0]), np.array([-2, 0.5, 0]),
            fill_opacity=0.7
        )
        triangle.shift(UP*0.2)

        # Line Segments
        a_segment = Line(
            triangle.get_vertices()[0], triangle.get_vertices()[2]
        )
        b_segment = Line(
            triangle.get_vertices()[0], triangle.get_vertices()[1]
        )
        hypotenuse = Line(
            triangle.get_vertices()[2], triangle.get_vertices()[1]
        )

        line_segments = [a_segment, b_segment, hypotenuse]

        # labels
        a_label = TexMobject("a").next_to(a_segment, direction=LEFT)
        b_label = TexMobject("b").next_to(b_segment, direction=DOWN)
        c_label = TexMobject("c").next_to(hypotenuse, direction=UP, buff=-0.5)

        labels = [a_label, b_label, c_label]

        # Theorem
        theorem = TexMobject("c^2", "=", "a^2", "+", "b^2")
        theorem.scale(1.5)
        theorem.to_edge(RIGHT, buff=1)
        theorem.shift(0.4*DOWN)

        # Squares
        a_square = Square(
            side_length=a_segment.get_length(), fill_opacity=0.7
        )
        a_square.next_to(a_segment, direction=LEFT, buff=0)

        b_square = Square(
            side_length=b_segment.get_length(), fill_opacity=0.7, color=PURPLE
        )
        b_square.next_to(b_segment, direction=DOWN, buff=0)

        c_square = Square(
            side_length=hypotenuse.get_length(), fill_opacity=0.7, color=ORANGE
        )
        c_square.move_to(triangle.get_vertices()[1])
        c_square.move_to(c_square.get_vertices()[0])
        c_square.rotate(hypotenuse.get_angle(), about_point=triangle.get_vertices()[1])

        squares = [a_square, b_square, c_square]

        everything = VGroup(triangle)
        for label in labels:
            everything.add(label)
        for square in squares:
            everything.add(square)

        # Video End Scene
        if return_end_scene1:
            return everything
        
        # PLAY COMMANDS
        if return_end_scene1==False and return_end_scene2==False:
            self.add(triangle)
            for label in labels:
                self.add(label)
            self.play(
                Write(theorem)
            )
            self.wait(2)

            for square in squares:
                self.play(
                    Write(square)
                )
            self.wait()

            self.play(Indicate(a_square))
            self.play(Indicate(b_square))

            self.wait()
            self.play(Indicate(c_square))
            self.wait()

            self.play(
                Rotate(b_square, 0.75*TAU + hypotenuse.get_angle(), about_point=triangle.get_vertices()[1])
            )
            self.play(
                Rotate(a_square, PI + hypotenuse.get_angle(), about_point=triangle.get_vertices()[2])
            )
            self.wait()
        
        # END SCENE 2
        if return_end_scene2:
            everything = VGroup(triangle)
            for square in squares:
                everything.add(square)
            
            b_square.rotate(0.75*TAU + hypotenuse.get_angle(), about_point=triangle.get_vertices()[1])
            a_square.rotate(PI + hypotenuse.get_angle(), about_point=triangle.get_vertices()[2])
            
            everything.add(a_square)
            everything.add(b_square)
            return everything

        # everything
        everything = VGroup(triangle)
        for label in labels:
            everything.add(label)
        for square in squares:
            everything.add(square)
        
        # PLAY COMMANDS - Cross and Uncross
        if return_end_scene1==False and return_end_scene2==False:
            self.play(
                everything.shift, DOWN
            )
            cross_everything = Cross(everything)
            self.play(
                Write(cross_everything)
            )
            self.wait(2)

            self.play(
                Write(cross_everything),
                rate_func = lambda p: 1-p
            )
            self.wait()

        self.play(
            Transform(VGroup(a_square, b_square), c_square.copy())
        )
        self.wait()
        
        """a_rects = []
        counter = 0
        while counter < 4:
            a_rects.append(
                Polygon(
                    a_square.point_from_proportion(counter/16), a_square.point_from_proportion((counter+1)/16), a_square.point_from_proportion((11-counter)/16), a_square.point_from_proportion((12-counter)/16),
                    color=WHITE, fill_opacity=0.8, stroke_width=0
                )
            )
            counter += 1
        
        # PLAY COMMANDS
        if return_end_scene1==False and return_end_scene2==False:
            for rect in a_rects:
                self.play(
                    Write(rect)
                )
                self.play(
                    Indicate(rect)
                )
            self.remove(a_square)
            self.wait()

            self.play(
                Rotate(VGroup(a_rects[2], a_rects[1], a_rects[0]), about_point=a_rects[3].get_vertices()[3])
            )
            self.play(
                Rotate(VGroup(a_rects[1], a_rects[0]), about_point=a_rects[2].get_vertices()[0], angle = -1.5*PI)
            )
            self.play(
                Rotate(a_rects[0], about_point=a_rects[1].get_vertices()[3], angle=PI)
            )
            location_for_last_two_a_rects = Polygon(
                c_square.get_vertices()[0], c_square.get_vertices()[1], b_square.get_vertices()[0], a_rects[2].get_vertices()[0]
            )
            self.play(
                VGroup(a_rects[1], a_rects[0]).move_to, location_for_last_two_a_rects
            )
            self.wait()"""
            

class RearrangementProof(Scene):
    def construct(self):
        title_text = TextMobject("Proof of the Pythagorean Theorem")
        title_text.to_corner(UL, buff = 0.8)
        square_1 = Square()
        square_1.scale(2)

        points = [] #empty array of points
        #create an array of 4 points around the square; points stored as np.array
        for i in range(4):
            points.append(square_1.point_from_proportion(i * 1/4 + 1/16))   
            # point_from_proportion(fraction) = a point located a proportion of the way around the shape
            # for squares, point_from_proportion(0) = top-left corner

        # corners of the square; points stored as np.array
        corner_points = []
        for i in range(4):
            corner_points.append(square_1.point_from_proportion(i * 1/4))

        """ 
        # In case you forget how these points work, uncomment this and write it in self.play()
        point_location_1 = TextMobject(str(points[1][0]))
        point_location_2 = TextMobject(str(points[1][1]))
        point_location_3 = TextMobject(str(points[1][2]))

        point_location_1.to_corner(DL)
        point_location_2.to_edge(DOWN)
        point_location_3.to_corner(DR)
        """

        # Initial Triangles
        initial_triangles = []
        for i in range(4):
            initial_triangles.append(Polygon(
                np.array(corner_points[i]),
                np.array(points[i]),
                np.array(points[i-1]),
                fill_opacity=0.7,
                stroke_width=5
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
        c_squared.shift(LEFT*3.5)

        c_squared_text = TexMobject(r"c^2")
        c_squared_text.shift(LEFT*3.5)
        c_squared_text.scale(1.5)

        # square_2 settings
        square_2 = Square()
        square_2.scale(2)
        square_2.shift(RIGHT*3.5)

        # points on square_2
        points_2 = []
        for j in [1, 7, 11, 13]:
            points_2.append(square_2.point_from_proportion(j/16))

        corner_points_2 = []
        for j in range(4):
            corner_points_2.append(square_2.point_from_proportion(j * 1/4))

        middle_point = np.array(
            [points_2[0][0], points_2[3][1], 0]
        )

        # second set of triangles
        final_triangles = []
        for i in range(4):
            if i == 1 or i == 3:
                final_triangles.append(Polygon(
                    np.array(middle_point),
                    np.array(points_2[i-2]),
                    np.array(points_2[i-1]),
                    fill_opacity=0.7,
                    stroke_width=2
                )) 
            else:
                final_triangles.append(Polygon(
                    np.array(corner_points_2[i]),
                    np.array(points_2[i]),
                    np.array(points_2[i-1]),
                    fill_opacity=0.7,
                    stroke_width=2
                ))
        all_final_triangles = VGroup()
        for triangle in final_triangles:
            all_final_triangles.add(triangle)

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

        # Equation
        Equation = TexMobject(r"c^2", "=", "a^2", "+", "b^2")
        Equation.scale(1.5)
        Equation.to_edge(DOWN)

        # line segments
        line_a1 = Line(
            np.array(middle_point), np.array(points_2[2]),
            stroke_width = 5,
            stroke_color = GREEN
        )
        a_left_label = TexMobject(r"a").next_to(line_a1, direction=LEFT).shift(LEFT)

        line_a2 = Line(
            np.array(middle_point), np.array(points_2[3]),
            stroke_width = 5,
            stroke_color = GREEN
        )
        a_down_label = TexMobject(r"a").next_to(line_a2, direction=DOWN).shift(DOWN)

        line_b1 = Line(
            np.array(middle_point), np.array(points_2[0]),
            stroke_width = 5,
            stroke_color = GREEN
        )
        b_right_label = TexMobject(r"b").next_to(line_b1, direction=RIGHT).shift(RIGHT*3)

        line_b2 = Line(
            np.array(middle_point), np.array(points_2[1]),
            stroke_width = 5,
            stroke_color = GREEN
        )
        b_up_label = TexMobject(r"b").next_to(line_b2, direction=UP).shift(UP*3)

        # PLAY COMMANDS
        self.play(
            FadeInFromDown(title_text),
            Write(square_1),
            run_time = 1
        )
        for i in range(4):
            self.play(
                Write(initial_triangles[i]),
                run_time=0.5
            )
        
        # Writing the lables
        for i in range(4):
            self.play(
                Write(labels[i]),
                run_time=1
            )
        self.wait()
        
        # Shift initial shapes to the left
        self.play(
            square_1.shift, LEFT*3.5,
            all_initial_triangles.shift, LEFT*3.5,
            labels[0].shift, LEFT*3.5,
            labels[1].shift, LEFT*3.5,
            labels[2].shift, LEFT*3.5,
            labels[3].shift, LEFT*3.5
        )

        self.wait(0.5)

        self.play(
            ShowCreation(c_squared),
            Write(c_squared_text)
        )

        self.wait(0.5)

        self.play(
            ReplacementTransform(square_1.copy(), square_2)
        )
        self.wait()
        self.play(
            ReplacementTransform(all_initial_triangles.copy(), all_final_triangles)
        )
        self.wait(0.5)

        self.play(
            Write(line_a1),
            Write(line_a2)
        )

        self.wait(0.5)

        self.play(
            line_a1.shift, LEFT,
            Write(a_left_label)
        )
        self.play(
            line_a2.shift, DOWN,
            Write(a_down_label)
        )

        self.play(
            ShowCreation(a_squared),
            Write(a_squared_text),
        )

        self.play(
            Write(line_b1),
            Write(line_b2)
        )
        self.wait(0.5)

        self.play(
            line_b1.shift, RIGHT*3,
            Write(b_right_label)
        )
        self.play(
            line_b2.shift, UP*3,
            Write(b_up_label)
        )

        self.play(
            ShowCreation(b_squared),
            Write(b_squared_text)
        )

        self.wait()

        self.play(
            ReplacementTransform(c_squared_text.copy(), Equation[0]),
            Write(Equation[1]),
            ReplacementTransform(a_squared_text.copy(), Equation[2]),
            Write(Equation[3]),
            ReplacementTransform(b_squared_text.copy(), Equation[4])
        )
        self.play(
            Write(
                SurroundingRectangle(Equation, buff=0.1)
            )
        )


class RearrangementProofOneSquare(Scene):
    def construct(self, return_end_scene1=False, return_end_scene2=False):
        title_text = TextMobject("Rearrangement Proof")
        title_text.to_corner(UL, buff = 0.8)
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
        c_squared_text.shift(LEFT*3.5)

        # Drawing Right Angles
        points_on_c_squared = []
        for i in [31, 1, 7, 9, 15, 17, 23, 25]:
            points_on_c_squared.append(c_squared.point_from_proportion(i/32))
        corners_of_c_squared = []
        for i in range(4):
            corners_of_c_squared.append(
                c_squared.point_from_proportion(i/4)
            )

        line_segments_of_c_squared_angles = []
        for i,j in zip(range(8), [0,0,1,1,2,2,3,3]):
            line_segments_of_c_squared_angles.append(Line(
                np.array(points_on_c_squared[i]), np.array(corners_of_c_squared[j])
            ))
        for i,j,k in zip(line_segments_of_c_squared_angles, points_on_c_squared, [270,90,270,90,270,90,270,90]):
            i.rotate(k*DEGREES, about_point=j)

        c_squared_angles = VGroup().copy()
        for i in range(8):
            c_squared_angles.add(line_segments_of_c_squared_angles[i])
        
        # END SCENE 1
        everything = VGroup(all_initial_triangles, c_squared)
        if return_end_scene1:
            return everything
        
        # PLAY COMMANDS
        if return_end_scene1==False and return_end_scene2==False:
            self.play(
                FadeInFromDown(title_text),
                Write(square_1),
                run_time = 2.5
            )
            for i in range(4):
                self.play(
                    Write(initial_triangles[i]),
                    run_time=4
                )
            
            # Writing the lables
            for i in labels[0]:
                self.play(
                    Write(i),
                    run_time=1.5
                )
                self.wait()

            for i in range(3):
                self.play(
                    Write(labels[i+1]),
                    run_time=1
                )

            self.wait(0.5)

            self.play(
                ShowCreation(c_squared),
            )

            self.wait(2)

            # Pulse each shape Yellow
            pulse(self, initial_triangles, YELLOW)
            
            self.wait()
            pulse(self, c_squared, YELLOW)
            self.wait(2)

            # Draw right angles on c_squared
            for i in range(8):
                self.play(
                    Write(line_segments_of_c_squared_angles[i], run_time=0.1)
                )
            self.wait(2)
            for i in range(8):
                self.play(
                    FadeOut(line_segments_of_c_squared_angles[i], run_time=0.1)
                )
            self.wait(2)

            # Shift everything to the left
            self.play(
                *[
                    ApplyMethod(
                        labels[i].shift, LEFT*3.5
                    )
                    for i in range(4)
                ],
                square_1.shift, LEFT*3.5,
                c_squared.shift, LEFT*3.5,
                all_initial_triangles.shift, LEFT*3.5
            )
            self.wait(2)

            # PROVE C_SQUARED HAS RIGHT ANGLES
            c_squared_first_elbow = VGroup(c_squared_angles[6], c_squared_angles[7])
            c_squared_first_elbow.shift(LEFT*3.5)
            prove_angle_is_a_right_angle(self, initial_triangles[3], initial_triangles[0], c_squared_first_elbow, RIGHT*7 + UP*2, True)

            # ...and you can figure this out for all of the angles on c_squared
            for i in range(6):
                self.play(
                    Write(line_segments_of_c_squared_angles[i].shift(LEFT*3.5), run_time=0.1)
                )
            self.wait(2)
            for i in range(6):
                self.play(
                    FadeOut(line_segments_of_c_squared_angles[i], run_time=0.1)
                )
            self.wait()
            self.play(
                Write(c_squared_text)
            )
            self.wait()

        theorem = TexMobject(r"c^2", "=", "a^2", "+", "b^2").scale(1.5)
        theorem.move_to(0.9*DOWN+2*RIGHT)

        c_squared_text.generate_target()
        c_squared_text.target = theorem[0]

        # PLAY COMMANDS
        if return_end_scene1==False and return_end_scene2==False:
            self.play(
                MoveToTarget(c_squared_text),
                Write(theorem[1])
            )

            self.play(
                FadeOut(self.all_objects_in_angle_proof),
                FadeOut(
                    VGroup(c_squared)
                ),
                FadeOut(
                    VGroup(labels[0][2], labels[1], labels[2], labels[3])
                )
            )
            self.wait()

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
            self.wait(2)

        # points on square_2
        square_2 = Square()
        square_2.scale(2)
        square_2.shift(LEFT*3.5)

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

            self.play(
                ShowCreation(a_squared),
                Write(a_squared_text),
            )
            self.wait(0.5)

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


class RearrangementProofShort(Scene):
    def construct(self, return_end_scene1=False, return_end_scene2=False):
        title_text = TextMobject("Rearrangement Proof")
        title_text.to_corner(UL, buff = 0.8)
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
                FadeInFromDown(title_text),
                Write(square_1),
                run_time = 2.5
            )
            for i in range(4):
                self.play(
                    Write(initial_triangles[i]),
                )
            
            # Writing the lables
            for i in labels[0]:
                self.play(
                    Write(i),
                    run_time=1.5
                )
                self.wait()

            for i in range(3):
                self.play(
                    Write(labels[i+1]),
                    run_time=1
                )

            self.wait(0.5)

            self.play(
                ShowCreation(c_squared),
            )

            self.wait(2)
            
            self.wait()
            pulse(self, c_squared, YELLOW)
            self.wait()

            self.play(
                Write(c_squared_text)
            )
            self.wait()

        theorem = TexMobject(r"c^2", "=", "a^2", "+", "b^2").scale(1.5)
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
            self.wait()

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
            self.wait(2)

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

            self.play(
                ShowCreation(a_squared),
                Write(a_squared_text),
            )
            self.wait(0.5)

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
            self.wait()

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


class GarfieldsProof(Scene):
    def construct(self, return_end_scene1=False):
        # base triangle
        base_triangle = Polygon(
            np.array([-1, -2, 0]),  np.array([-1, -0.7, 0]), np.array([2, -2, 0]),
            fill_opacity=0.7
        )

        base_triangle_labels = {
            "a": TexMobject("a").next_to(base_triangle, direction=LEFT),
            "b": TexMobject("b").next_to(base_triangle, direction=DOWN),
            "c": TexMobject("c").next_to(base_triangle, direction=UP, buff=-0.4)
        }

        # vertical triangle
        vertical_triangle = base_triangle.copy()
        vertical_triangle.shift(UP*1.3 + LEFT*3)
        vertical_triangle.rotate(-90*DEGREES, about_point = np.array([-1, -0.7, 0]))

        vertical_triangle_labels = {
            "a": TexMobject(r"a").next_to(vertical_triangle, direction=UP),
            "b": TexMobject(r"b").next_to(vertical_triangle, direction=LEFT),
            "c": TexMobject(r"c").next_to(vertical_triangle, direction=RIGHT, buff=-0.4)
        }

        # steps from base to vertical
        vertical_triangle_step_1 = base_triangle.copy().shift(UP*1.3)
        vertical_triangle_step_2 = vertical_triangle_step_1.copy().shift(LEFT*3)
            
        # c_triangle
        c_triangle_hypotenuse = Line(
            np.array(vertical_triangle.get_vertices()[1]), np.array(base_triangle.get_vertices()[2]),
            stroke_width=5,
            stroke_color=GREEN
        )

        c_triangle = Polygon(
            np.array(base_triangle.get_vertices()[1]), np.array(vertical_triangle.get_vertices()[1]), np.array(base_triangle.get_vertices()[2]),
            fill_opacity=0.7,
            fill_color=ORANGE
        )

        # group of triangles
        self.triangles = VGroup(
            base_triangle, vertical_triangle, c_triangle
        )
        
        # END SCENE
        everything = self.triangles
        if return_end_scene1:
            return everything
        
        # Not end scene
        for label in base_triangle_labels:
            self.triangles.add(base_triangle_labels[label])
        for label in vertical_triangle_labels:
            self.triangles.add(vertical_triangle_labels[label])

        

        # PLAY COMMANDS - drawing triangles and shifting them
        if return_end_scene1==False:
            self.play(
                Write(base_triangle)
            )
            for label in base_triangle_labels:
                self.play(
                    Write(base_triangle_labels[label]),
                    run_time=0.3
                )
            
            self.wait()

            self.play(
                ReplacementTransform(base_triangle.copy(), vertical_triangle_step_1)
            )
            self.play(
                ReplacementTransform(vertical_triangle_step_1, vertical_triangle_step_2)
            )
            self.play(
                Rotate(vertical_triangle_step_2, -90*DEGREES, about_point=vertical_triangle_step_2.get_vertices()[2])
            )
            self.add(vertical_triangle)
            self.remove(vertical_triangle_step_2)
            for label in vertical_triangle_labels:
                self.play(
                    Write(vertical_triangle_labels[label]),
                    run_time=0.3
                )
            self.wait()
                
            self.play(
                Write(c_triangle_hypotenuse)
            )
            self.play(
                ShowCreation(c_triangle)
            )
            self.wait()
                
            self.remove(c_triangle_hypotenuse)
            self.play(
                self.triangles.shift, LEFT*4.5
            )
            self.wait()

        # creating c_triangle's elbow
        c_triangle_elbow_line_1 = Line(
            np.array(c_triangle.get_vertices()[0]), np.array(c_triangle.point_from_proportion(1/24))
        )
        c_triangle_elbow_line_2 = Line(
            np.array(c_triangle.get_vertices()[0]), np.array(c_triangle.point_from_proportion(23/24)),
        )

        c_triangle_elbow_line_1.rotate(90*DEGREES, about_point=c_triangle.point_from_proportion(1/24))
        c_triangle_elbow_line_2.rotate(270*DEGREES, about_point=c_triangle.point_from_proportion(23/24))

        elbow_between_c_lines = VGroup(c_triangle_elbow_line_1, c_triangle_elbow_line_2)

        # proving c_triangle is a right-angled triangle
        if return_end_scene1==False:
            prove_angle_is_a_right_angle(self, base_triangle, vertical_triangle, elbow_between_c_lines, RIGHT*7 + UP*2, True)
            self.wait(2)
            self.add(elbow_between_c_lines)
            self.play(
                FadeOut(self.all_objects_in_angle_proof)
            )
            self.wait()

        # Area of trapezoid
        trapezoid = Polygon(
            base_triangle.get_vertices()[0], base_triangle.get_vertices()[2], vertical_triangle.get_vertices()[1], vertical_triangle.get_vertices()[0],
            fill_opacity=0.7
        )
        if return_end_scene1==False:
            self.add(trapezoid)
            pulse(self, trapezoid, YELLOW)
            self.remove(trapezoid)
            self.wait()

        # Line Segments to refer to when writing equation of area
        base_triangle_segment_b = Line(base_triangle.get_vertices()[0], base_triangle.get_vertices()[2])
        base_triangle_segment_a = Line(base_triangle.get_vertices()[0], base_triangle.get_vertices()[1])

        vertical_triangle_segment_b = Line(vertical_triangle.get_vertices()[0], vertical_triangle.get_vertices()[2])
        vertical_triangle_segment_a = Line(vertical_triangle.get_vertices()[0], vertical_triangle.get_vertices()[1])

        # EQUATION STEPS
        equation_of_area = TexMobject("\\frac{1}{2}\ ", "(", "b", "+", "a", ")", "(", "b", "+", "a", ")", "=", "\\frac{1}{2}\ ", "b", "a", "+", "\\frac{1}{2}\ ", "b", "a", "+", "\\frac{1}{2}\ ", "c^2")
        equation_of_area.next_to(self.triangles)
        equation_of_area.shift(DOWN)

        # factor out 1/2 in Left-Hand Side
        equation_of_area_step1 = TexMobject("\\frac{1}{2}\ ", "(", "b", "+", "a", ")", "(", "b", "+", "a", ")", "=", "\\frac{1}{2}\ ", "(", "b", "a", "+", "b", "a", "+", "c^2", ")")
        equation_of_area_step1.move_to(equation_of_area)

        # simplify ba + ba = 2ba
        equation_of_area_step2 = TexMobject("\\frac{1}{2}\ ", "(", "b", "+", "a", ")", "(", "b", "+", "a", ")", "=", "\\frac{1}{2}\ ", "(", "2", "b", "a", "+", "c^2", ")")
        equation_of_area_step2.move_to(equation_of_area_step1)

        # cancelling out 1/2 on both sides
        rect_around_left_half = SurroundingRectangle(equation_of_area_step2[0])
        rect_around_right_half = SurroundingRectangle(equation_of_area_step2[12])
        cross_left_half = Cross(equation_of_area_step2[0])
        cross_right_half = Cross(equation_of_area_step2[12])

        equation_of_area_step3 = TexMobject("(", "b", "+", "a", ")", "(", "b", "+", "a", ")", "=", "(", "2", "b", "a", "+", "c^2", ")")
        equation_of_area_step3.move_to(equation_of_area_step2)

        # all parentheses gone
        equation_of_area_step4 = TexMobject("b^2", "+", "2ba", "+", "a^2", "=", "2ba", "+", "c^2")
        equation_of_area_step4.move_to(equation_of_area_step3)

        # eliminating 2ba
        subtract_2ba_left_side = TexMobject(r"-2ba")
        subtract_2ba_left_side.next_to(equation_of_area_step4[2], direction=DOWN)
        subtract_2ba_left_side.shift(LEFT*0.2)
        subtract_2ba_right_side = TexMobject(r"-2ba")
        subtract_2ba_right_side.next_to(equation_of_area_step4[6], direction=DOWN)
        subtract_2ba_right_side.shift(LEFT*0.2)

        left_side_2ba_group = VGroup(equation_of_area_step4[2], subtract_2ba_left_side)
        eliminate_left_side = Cross(left_side_2ba_group)

        right_side_2ba_group = VGroup(equation_of_area_step4[6], subtract_2ba_right_side)
        eliminate_right_side = Cross(right_side_2ba_group)

        # final form
        equation_of_area_final = TexMobject("b^2", "+", "a^2", "=", "c^2")
        equation_of_area_final.move_to(equation_of_area_step4)

        # PLAY COMMANDS - equation breakdown
        if return_end_scene1==False:
            self.play(
                Write(equation_of_area[0])
            ),
            self.wait()

            # Left Hand Side of Equation
            pulse(self, [base_triangle_segment_b, vertical_triangle_segment_a], YELLOW)
            self.play(
                Write(equation_of_area[1:6])
            )
            pulse(self, [base_triangle_segment_a, vertical_triangle_segment_b], YELLOW)
            self.play(
                Write(equation_of_area[6:11])
            )
            self.wait()

            # Right Hand Side of Equation
            self.play(
                Write(equation_of_area[11])
            )
            self.play(
                Indicate(base_triangle)
            )
            self.play(
                Indicate(vertical_triangle)
            )
            self.play(
                Indicate(c_triangle)
            )
            self.wait()

            
            pulse(self, base_triangle, YELLOW)
            self.play(
                Write(equation_of_area[12:15])
            )
            self.wait()
            self.play(
                Write(equation_of_area[15])
            )
            pulse(self, vertical_triangle, YELLOW)
            self.play(
                Write(equation_of_area[16:19])
            )
            self.wait()
            pulse(self, c_triangle, YELLOW)
            self.play(
                Write(equation_of_area[19:])
            )
            self.wait()

            # Breaking the equation down
            self.play(
                ReplacementTransform(equation_of_area, equation_of_area_step1)
            )
            self.wait()

            self.play(
                ReplacementTransform(equation_of_area_step1[:12], equation_of_area_step2[:12]),
                ReplacementTransform(equation_of_area_step1[12::], equation_of_area_step2[12::])
            )
            self.add(equation_of_area_step2)
            self.remove(equation_of_area_step1)
            self.wait()

            self.play(
                Write(rect_around_left_half),
                Write(rect_around_right_half)
            )
            self.play(
                Write(cross_left_half),
                Write(cross_right_half)
            )
            self.play(
                FadeOut(rect_around_left_half),
                FadeOut(rect_around_right_half),
                FadeOut(cross_left_half),
                FadeOut(cross_right_half),
                ReplacementTransform(equation_of_area_step2, equation_of_area_step3)
            )
            self.wait(2)

            self.play(
                ReplacementTransform(equation_of_area_step3, equation_of_area_step4)
            )
            self.wait()

            # final equation
            self.play(
            Write(subtract_2ba_left_side),
            Write(subtract_2ba_right_side),
            )
            self.wait()

            self.play(
                ShowCreation(eliminate_left_side)
            )
            self.wait()

            self.play(
                FadeOut(left_side_2ba_group),
                FadeOut(eliminate_left_side),
                FadeOut(equation_of_area_step4[1]),
            )
            self.wait()

            self.play(
                ShowCreation(eliminate_right_side)
            )
            self.wait()
            
            self.play(
                FadeOut(right_side_2ba_group),
                FadeOut(eliminate_right_side),
                FadeOut(equation_of_area_step4[7]),
            )
            self.play(
                ReplacementTransform(equation_of_area_step4[0], equation_of_area_final[0]),
                ReplacementTransform(equation_of_area_step4[8], equation_of_area_final[4])
            )
            self.wait()

            self.remove(equation_of_area_final)
            self.remove(equation_of_area_step4[3], equation_of_area_step4[4], equation_of_area_step4[5])

            # emphasize theorem
            self.add(equation_of_area_final)
            self.wait()
            self.play(
                equation_of_area_final.scale, 1.5
            )
            self.play(
                Write(SurroundingRectangle(equation_of_area_final, buff=0.2))
            )
            self.wait()


class BhaskarasProof(Scene):
    def construct(self, return_end_scene1=False, return_end_scene2=False):
        # creating the original triangles 
        top_triangle = Polygon(
            np.array([-1.5, 1, 0]), np.array([-1.5, 2.2, 0]), np.array([1.5, 1, 0]),
            fill_opacity=0.7,
            stroke_width=1
        )

        triangles = [top_triangle]

        for index, direction in enumerate([RIGHT, DOWN, LEFT]):
            triangles.append(
                triangles[index].copy().shift(direction*1.8)
            )
            triangles[index+1].rotate(
                -90*DEGREES, about_point=np.array(triangles[index+1].get_vertices()[0])
            )

        points_of_middle_square = []
        for triangle in triangles:
            points_of_middle_square.append(
                np.array(triangle.get_vertices()[0])
            )

        # steps to form each triangle
        triangles_formation_transition = []
        for index, direction in enumerate([RIGHT, DOWN, LEFT]):
            triangles_formation_transition.append(
                triangles[index].copy().shift(direction*1.8)
            )

        # the square in the middle
        middle_square = Polygon(
            points_of_middle_square[0], points_of_middle_square[1], points_of_middle_square[2], points_of_middle_square[3],
            fill_opacity=0.7,
            stroke_width=1,
            fill_color=ORANGE
        )

        # END SCENE
        everything = VGroup(middle_square)
        for triangle in triangles:
            everything.add(triangle)
        if return_end_scene1:
            return everything

        # labels of top triangle
        top_triangle_labels = {
            "a": TexMobject(r"a", background_stroke_width=0).next_to(triangles[0], direction=LEFT, buff=-0.25).scale(0.7),
            "b": TexMobject(r"b", background_stroke_width=0).next_to(triangles[0], direction=DOWN, buff=-0.35).scale(0.7),
            "c": TexMobject(r"c").next_to(triangles[0], direction=UP, buff=-0.4)
        }

        # c_squared
        c_squared = Polygon(
            np.array(triangles[0].get_vertices()[1]), np.array(triangles[1].get_vertices()[1]), np.array(triangles[2].get_vertices()[1]), np.array(triangles[3].get_vertices()[1]),
            fill_opacity=0.7
        )
        points_on_c_squared = []
        for i in [47, 1, 11, 13, 23, 25, 35, 37]:
            points_on_c_squared.append(c_squared.point_from_proportion(i/48))
        corners_of_c_squared = []
        for i in range(4):
            corners_of_c_squared.append(
                c_squared.point_from_proportion(i/4)
            )

        # angles of c_squared
        line_segments_of_c_squared_angles = []
        for i,j in zip(range(8), [0,0,1,1,2,2,3,3]):
            line_segments_of_c_squared_angles.append(Line(
                np.array(points_on_c_squared[i]), np.array(corners_of_c_squared[j])
            ))
        for i,j,k in zip(line_segments_of_c_squared_angles, points_on_c_squared, [270,90,270,90,270,90,270,90]):
            i.rotate(k*DEGREES, about_point=j)

        c_squared_angles = VGroup().copy()
        for i in range(8):
            c_squared_angles.add(line_segments_of_c_squared_angles[i])
        
        c_squared_first_elbow = VGroup(c_squared_angles[6], c_squared_angles[7])

        # PLAY COMMANDS - drawing the shapes
        if return_end_scene1==False and return_end_scene2==False:
            self.play(
                Write(triangles[0])
            )
            self.remove(triangles[0])

            for destined_triangle, transition_triangle in zip(triangles, triangles_formation_transition):
                self.add(destined_triangle)
                self.play(
                    ReplacementTransform(destined_triangle.copy(), transition_triangle)
                )
                self.play(
                    Rotate(transition_triangle, -90*DEGREES, about_point=transition_triangle.get_vertices()[0])
                )
                self.remove(transition_triangle)

            self.add(triangles[3])
            self.wait()

            self.play(
                ShowCreation(middle_square)
            )
            self.wait(2)

            for label in top_triangle_labels:
                self.play(
                    Write(top_triangle_labels[label]), run_time=0.3
                )
            self.wait()

            # Draw right angles on c_squared
            pulse(self, triangles, YELLOW)
            self.wait()

            pulse(self, c_squared, YELLOW)
            self.remove(c_squared)
            self.wait()

            for i in range(8):
                self.play(
                    Write(line_segments_of_c_squared_angles[i], run_time=0.1)
                )
            self.wait(2)
            for i in range(8):
                self.play(
                    FadeOut(line_segments_of_c_squared_angles[i], run_time=0.1)
                )
            self.wait(2)

        # Grouping and shifting the shapes
        all_shapes = VGroup(middle_square)
        for triangle in triangles:
            all_shapes.add(triangle)
        for label in top_triangle_labels:
            all_shapes.add(top_triangle_labels[label])

        if return_end_scene1==False and return_end_scene2==False:
            self.play(
                all_shapes.shift, LEFT*3.5
            )

            # PROVE c_squared has right angles
            c_squared_first_elbow = VGroup(c_squared_angles[2], c_squared_angles[3])
            c_squared_first_elbow.shift(LEFT*3.5)
            prove_angle_is_a_right_angle(self, triangles[0], triangles[1], c_squared_first_elbow, RIGHT*7, False)
            self.play(
                FadeOut(self.all_objects_in_angle_proof)
            )
            self.wait()

            for i in range(8):
                if i==2 or i==3:
                    self.play(
                    Write(line_segments_of_c_squared_angles[i], run_time=0.1)
                    )
                else:
                    self.play(
                        Write(line_segments_of_c_squared_angles[i].shift(LEFT*3.5), run_time=0.1)
                    )
            self.wait(2)

            for i in range(8):
                self.play(
                    FadeOut(line_segments_of_c_squared_angles[i], run_time=0.1)
                )
            self.wait(2)

        # c^2 = 
        c_squared.shift(LEFT*3.5)
        theorem = TexMobject("c^2", "=", "a^2", "+", "b^2")
        theorem.to_edge(DOWN)
        theorem.scale(1.5)

        c_squared_label = TexMobject("c^2", background_stroke_width=0)
        c_squared_label.move_to(c_squared.get_center())
        c_squared_label.scale(1.5)

        if return_end_scene1==False and return_end_scene2==False:
            pulse(self, c_squared, YELLOW)
            self.play(
                Write(c_squared_label)
            )
            self.play(
                ReplacementTransform(c_squared_label.copy(), theorem[0]),
                Write(theorem[1])
            )
            self.play(
                FadeOut(c_squared),
                FadeOut(self.equations)
            )

        # Rearranging the shapes
        all_shapes_copy = all_shapes.copy().shift(RIGHT*7)

        all_shapes_copy[1].generate_target()
        all_shapes_copy[1].target = all_shapes_copy[3].copy().rotate(180*DEGREES)

        all_shapes_copy[4].generate_target()
        all_shapes_copy[4].target = all_shapes_copy[2].copy().rotate(180*DEGREES)
        
        # a^2 and b^2
        dot_at_apex_of_dividing_line = Dot(
            np.array(all_shapes_copy[0].get_vertices()[3])
        )
        dot_at_foot_of_dividing_line = dot_at_apex_of_dividing_line.copy().shift(DOWN*1.2)

        dividing_line = Line(
            np.array(dot_at_apex_of_dividing_line.get_center()), np.array(dot_at_foot_of_dividing_line.get_center()),
            stroke_color=GREEN,
        )

        a_squared = Polygon(
            np.array(all_shapes_copy[1].target.get_vertices()[1]), np.array(dot_at_apex_of_dividing_line.get_center()), np.array(dot_at_foot_of_dividing_line.get_center()), np.array(all_shapes_copy[1].target.get_vertices()[0]),
            fill_color=RED,
            fill_opacity=0.9,
            stroke_width=1
        )
        a_squared_label = TexMobject("a^2", background_stroke_width=0).scale(1.5).move_to(a_squared)

        b_squared = Polygon(
            np.array(all_shapes_copy[0].get_vertices()[0]), np.array(all_shapes_copy[4].target.get_vertices()[2]), np.array(all_shapes_copy[4].target.get_vertices()[0]), np.array(dot_at_foot_of_dividing_line.get_center()),
            fill_color=DARK_BLUE,
            fill_opacity=0.9,
            stroke_width=1
        )
        b_squared_label = TexMobject("b^2", background_stroke_width=0).scale(1.5).move_to(b_squared)

        # a_square line segments
        a_squared_left_line = Line(
            np.array(a_squared.get_vertices()[0]), np.array(a_squared.get_vertices()[3]),
            stroke_color=GREEN,
            stroke_width=6
        )
        a_squared_left_line_label = TexMobject("a").next_to(a_squared_left_line, direction=LEFT)
        a_squared_top_line = Line(
            np.array(a_squared.get_vertices()[0]), np.array(a_squared.get_vertices()[1]),
            stroke_color=GREEN,
            stroke_width=6
        )
        a_squared_top_line_label = TexMobject("?").next_to(a_squared_top_line, direction=UP)
        a_squared_top_line_label.generate_target()
        a_squared_top_line_label.target = TexMobject("a").next_to(a_squared_top_line, direction=UP)

        a_squared_top_line_original = Line(
            all_shapes[4].get_vertices()[1], all_shapes[4].get_vertices()[0],
            stroke_color=GREEN,
            stroke_width=6
        )

        # b_sqaured line segments
        b_squared_right_line = Line(
            b_squared.get_vertices()[1], b_squared.get_vertices()[2],
            stroke_color=GREEN,
            stroke_width=6
        )
        b_squared_right_line_label = TexMobject("b").next_to(b_squared_right_line, direction=RIGHT)

        b_squared_top_line = Line(
            b_squared.get_vertices()[0], b_squared.get_vertices()[1],
            stroke_color=GREEN,
            stroke_width=6
        )
        b_squared_top_line_label = TexMobject("?").next_to(b_squared_top_line, direction=UP)
        b_squared_top_line_label.generate_target()
        b_squared_top_line_label.target = TexMobject("b").next_to(b_squared_top_line, direction=UP)

        b_squared_top_line_original = Line(
            all_shapes[1].get_vertices()[0], all_shapes[1].get_vertices()[2],
            stroke_color=GREEN,
            stroke_width=6
        )

        # END SCENE 2
        everything = VGroup(a_squared, b_squared, dividing_line)
        if return_end_scene2:
            return everything

        # PLAY COMMANDS
        self.play(
            ReplacementTransform(all_shapes.copy(), all_shapes_copy)
        )
        self.wait(2)

        self.play(
            FadeOut(all_shapes_copy[5:]),
            MoveToTarget(all_shapes_copy[1]),
            MoveToTarget(all_shapes_copy[4])
        )
        self.play(
            Write(dividing_line)
        )
        self.wait()

        self.play(
            Write(a_squared),
            Write(b_squared)
        )
        self.wait(2)

        self.play(
            Write(a_squared_left_line),
            Write(a_squared_left_line_label)
        )
        bottom_triangle_of_new_shape = all_shapes_copy[1].target.copy()
        pulse(self, bottom_triangle_of_new_shape, YELLOW)
        self.remove(bottom_triangle_of_new_shape)
        self.wait()

        self.play(
            Write(a_squared_top_line),
            Write(a_squared_top_line_label)
        )
        self.wait()
        
        self.play(
            ReplacementTransform(a_squared_top_line.copy(), a_squared_top_line_original)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(a_squared_top_line_original, a_squared_top_line)
        )
        self.play(
            MoveToTarget(a_squared_top_line_label)
        )
        self.wait()

        self.play(
            Write(a_squared_label)
        )
        self.play(
            FadeOut(a_squared_left_line),
            FadeOut(a_squared_top_line),
            FadeOut(a_squared_top_line_label),
            FadeOut(a_squared_left_line_label)
        )
        self.wait(2)

        self.play(
            Write(b_squared_right_line),
            Write(b_squared_right_line_label)
        )
        rightmost_triangle_of_new_shape = all_shapes_copy[4].target.copy()
        pulse(self, rightmost_triangle_of_new_shape, YELLOW)
        self.remove(rightmost_triangle_of_new_shape)
        self.wait()

        self.play(
            Write(b_squared_top_line),
            Write(b_squared_top_line_label)
        )
        self.wait()
        
        self.play(
            ReplacementTransform(b_squared_top_line.copy(), b_squared_top_line_original)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(b_squared_top_line_original, b_squared_top_line)
        )
        self.play(
            MoveToTarget(b_squared_top_line_label)
        )
        self.wait()

        self.play(
            Write(b_squared_label)
        )
        self.play(
            FadeOut(b_squared_right_line),
            FadeOut(b_squared_top_line),
            FadeOut(b_squared_top_line_label),
            FadeOut(b_squared_right_line_label)
        )
        self.wait(2)

        self.play(
            ReplacementTransform(a_squared_label.copy(), theorem[2]),
            Write(theorem[3]),
            ReplacementTransform(b_squared_label.copy(), theorem[4])
        )
        self.play(
            Write(SurroundingRectangle(theorem))
        )


class EndCard(Scene):
    def construct(self):
        theorem_with_squares1 = TheoremWithSquares.construct(self, return_end_scene1=True)
        theorem_with_squares2 = TheoremWithSquares.construct(self, return_end_scene2=True)

        rearrangement1 = RearrangementProofOneSquare.construct(self, return_end_scene1=True)
        rearrangement2 = RearrangementProofOneSquare.construct(self, return_end_scene2=True)

        garfield = GarfieldsProof.construct(self, return_end_scene1=True)

        bhaskara1 = BhaskarasProof.construct(self, return_end_scene1=True)
        bhaskara2 = BhaskarasProof.construct(self, return_end_scene2=True).move_to(ORIGIN)

        end_scenes = [theorem_with_squares1, theorem_with_squares2, rearrangement1, rearrangement2, garfield, bhaskara1, bhaskara2]

        self.play(
            Write(theorem_with_squares1)
        )
        self.wait()
        
        index = 0
        while index+1 < len(end_scenes):
            self.play(
                ReplacementTransform(end_scenes[index], end_scenes[index+1])
            )
            self.wait()
            index += 1


