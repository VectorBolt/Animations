from manimlib.imports import *


class Lorentz(LinearTransformationScene):
    CONFIG = {
        "camera_config": {
            "frame_center": 3*UP
        },
        "show_basis_vectors": False,
        "background_plane_kwargs": {
            "y_max": 10
        },
        "include_foreground_plane": False,
        "foreground_plane_kwargs": {
            "y_min": -15,
            "y_max": 15,
            "x_min": -10,
            "x_max": 10
        }
    }
    def construct(self):
        # Assets
        lightlesshouse = ImageMobject ("lightless-house-centered.png")

        rocket = ImageMobject("Rocket.png")
        rocket.scale(0.5)

        chad = ImageMobject("cool-rocket.png")
        chad.scale(0.5)

        photon = ImageMobject("photon.png")
        photon.scale(0.2)

        # Math
        foreground_plane = NumberPlane(y_min=-15, y_max=15, x_min=-10, x_max=10)
        your_beta = 1/3
        chad_beta = 2/3

        your_gamma = 1/math.sqrt(1 - (your_beta ** 2))
        chad_gamma = 1/math.sqrt(1 - (chad_beta ** 2))

        lighthouse_to_you = [[your_gamma, -1 * your_gamma * your_beta], 
                            [-1 * your_gamma * your_beta, your_gamma]]

        lighthouse_to_chad =[[chad_gamma, -1 * chad_gamma * chad_beta], 
                 [-1 * chad_gamma * chad_beta, chad_gamma]]

        # World Line Functions
        def one_third(x):
            return 3*x
        def two_thirds(x):
            return (3*x)/2
        def light(x):
            return x

        # World Lines
        stationary = Line(ORIGIN+DOWN, np.array([0, 8, 0]), stroke_color=RED)
        your_world_line = FunctionGraph(one_third, x_min=-0.4, x_max=3, color=TEAL_B)
        chad_world_line = FunctionGraph(two_thirds, x_min=-0.8, x_max=5.7, color=GREEN)
        light_graph = FunctionGraph(light, x_min=-1.4, x_max=10, color=YELLOW)
        #planet_breakthrough = Line(np.array([4, -1, 0]), np.array([4, 10, 0]), stroke_color=ORANGE)

        assets = [lightlesshouse, rocket, chad, photon]
        paths = [stationary, your_world_line, chad_world_line, light_graph]

        # Slopes
        your_run = Line(
            ORIGIN, np.array([1, 0, 0]), color=MAROON, stroke_width=5
        )
        your_rise = Line(
            np.array([1, 0, 0]), np.array([1, 3, 0]), color=MAROON, stroke_width=5
        )
        your_rise_label = TexMobject("3").next_to(your_rise, direction=RIGHT).add_background_rectangle()
        your_run_label = TexMobject("1").next_to(your_run, direction=DOWN).add_background_rectangle()

        chad_run = Line(
            ORIGIN, np.array([2, 0, 0]), color=MAROON, stroke_width=5
        )
        chad_rise = Line(
            np.array([2, 0, 0]), np.array([2, 3, 0]), color=MAROON, stroke_width=5
        )
        chad_rise_label = TexMobject("3").next_to(chad_rise, direction=RIGHT).add_background_rectangle()
        chad_run_label = TexMobject("2").next_to(chad_run, direction=DOWN).add_background_rectangle()

        light_run = Line(
            ORIGIN, np.array([1, 0, 0]), color=MAROON, stroke_width=5
        )
        light_rise = Line(
            np.array([1, 0, 0]), np.array([1, 1, 0]), color=MAROON, stroke_width=5
        )
        light_rise_label = TexMobject("1").next_to(light_rise, direction=RIGHT).add_background_rectangle()
        light_run_label = TexMobject("1").next_to(light_run, direction=DOWN).add_background_rectangle()

        slopes = ["skip", VGroup(your_rise, your_run, your_rise_label, your_run_label), VGroup(chad_rise, chad_run, chad_rise_label, chad_run_label), VGroup(light_rise, light_run, light_rise_label, light_run_label)]


        # angles
        lines = []
        angles = VGroup()

        # PLAY COMMANDS:
        self.add_transformable_mobject(foreground_plane)

        for asset, path, slope in zip(assets, paths, slopes):
            asset.move_to(path.get_start())
            line = Line(path.get_start(), asset.get_center())
            def draw_line(obj):
                obj.become(
                    Line(path.get_start(), asset.get_center(), color=path.get_color())
                )
            self.play(
                FadeIn(asset)
            )
            self.add(line)
            self.play(
                MoveAlongPath(asset, path),
                UpdateFromFunc(line, draw_line)
            )
            self.add(line)
            if not slope == "skip":
                self.play(
                    FadeIn(slope)
                )
                self.play(
                    FadeOut(slope)
                )
            lines.append(line)
            self.remove(asset)
            self.remove(line)
            self.add_transformable_mobject(line)
            self.wait()

        angle = Arc(start_angle=lines[1].get_angle(), angle=lines[0].get_angle() - lines[1].get_angle(), radius=1)
        self.play(
            FadeIn(angle)
        )
        self.wait()
        self.play(
            FadeOut(angle)
        )
        self.apply_matrix(lighthouse_to_you, run_time=1)
        angle = Arc(start_angle=lines[1].get_angle(), angle=lines[0].get_angle() - lines[1].get_angle(), radius=1)
        self.play(
            FadeOut(foreground_plane),
            FadeIn(angle)
        )
        self.wait()

        self.play(
            WiggleOutThenIn(lines[1])
        )
        self.play(
            Indicate(angle)
        )
        self.play(
            WiggleOutThenIn(lines[3])
        )
        self.wait()


class RaceSimultaneity(Scene):
    def construct(self):
        # Assets
        space = ImageMobject("space.png")
        space.scale(10).shift(LEFT)

        lighthouse = ImageMobject("lightless-house-centered.png")
        lighthouse.move_to([0, -2, 0])

        rocket = ImageMobject("Rocket.png")
        rocket.scale(0.5)
        rocket.move_to(np.array([-6, 2, 0]))

        chad = ImageMobject("cool-rocket.png")
        chad.scale(0.5)
        chad.move_to(np.array([6, 2, 0]))

        collision1 = ImageMobject("asteroid-collision.png")
        collision1.scale(0.5)
        collision1.move_to(lighthouse.get_center()+3*LEFT)

        collision2 = ImageMobject("asteroid-collision.png")
        collision2.scale(0.5)
        collision2.move_to(lighthouse.get_center()+3*RIGHT)

        # Paths

        rocket_path = Line(
            np.array([-6, 2, 0]), np.array([6, 2, 0]), color = BLUE
        )
        rocket_path2 = Line(
            np.array([6, 2, 0]), np.array([-6, 2, 0]), color = BLUE
        )

        # PLAY COMMANDS
        self.add(space)
        self.add(lighthouse)
        self.wait()

        self.play(
            FadeIn(collision1),
            FadeIn(collision2)
        )
        self.play(
            FadeOut(collision1),
            FadeOut(collision2)
        )
        self.wait()

        self.play(
            FadeIn(rocket)
        )
        self.play(
            MoveAlongPath(rocket, rocket_path),
            AnimationGroup(
                FadeIn(collision2),
                FadeIn(collision1),
                lag_ratio=0.4
            ),
            run_time=3
        )
        self.play(
            rocket.flip, UP
        )
        self.play(
            MoveAlongPath(rocket, rocket_path2),
            AnimationGroup(
                FadeIn(collision1),
                FadeIn(collision2),
                lag_ratio=0.4
            ),
            run_time=3
        )
        self.wait()


class Simultaneity(LinearTransformationScene):
    CONFIG = {
        "camera_config": {
            "frame_center": 3*UP
        },
        "show_basis_vectors": False,
        "background_plane_kwargs": {
            "y_max": 10
        },
        "include_foreground_plane": False,
        "foreground_plane_kwargs": {
            "y_min": -15,
            "y_max": 15,
            "x_min": -10,
            "x_max": 10
        }
    }
    def construct(self):
        your_beta = 1/3
        chad_beta = 2/3

        your_gamma = 1/math.sqrt(1 - (your_beta ** 2))
        chad_gamma = 1/math.sqrt(1 - (chad_beta ** 2))

        lighthouse_to_you = [[your_gamma, -1 * your_gamma * your_beta], 
                            [-1 * your_gamma * your_beta, your_gamma]]

        lighthouse_to_chad =[[chad_gamma, -1 * chad_gamma * chad_beta], 
                 [-1 * chad_gamma * chad_beta, chad_gamma]]

        def one_third(x):
            return 3*x
        def negative_one_third(x):
            return -3*x
        def two_thirds(x):
            return (3*x)/2
        def light(x):
            return x

        foreground_plane = NumberPlane(y_min=-15, y_max=15, x_min=-10, x_max=10)

        stationary = Line(ORIGIN+DOWN, np.array([0, 10, 0]), stroke_color=RED)
        your_world_line = FunctionGraph(one_third, x_min=-10, x_max=10, color=TEAL_B)
        your_world_line2 = FunctionGraph(negative_one_third, x_min=-10, x_max=10, color=TEAL_B)
        chad_world_line = FunctionGraph(two_thirds, x_min=-10, x_max=10, color=GREEN)
        light_graph = FunctionGraph(light, x_min=-10, x_max=10, color=YELLOW)
        planet_breakthrough = Line(np.array([4, -1, 0]), np.array([4, 10, 0]), stroke_color=ORANGE)

        collision_one = Dot(np.array([-2, 0, 0]), color=LIGHT_BROWN)
        collision_two = Dot(np.array([2, 0, 0]), color=LIGHT_BROWN)

        time_main = Line(
            collision_one.get_center()+LEFT,
            [collision_one.get_center()[0]-1, collision_two.get_center()[1], 0], 
            color=MAROON, stroke_width=5
            )
        time_tips = VGroup(
            Line(time_main.get_start()+0.3*LEFT, time_main.get_start()+0.3*RIGHT, color=MAROON, stroke_width=5),
            Line(time_main.get_end()+0.3*LEFT, time_main.get_end()+0.3*RIGHT, color=MAROON, stroke_width=5)
        )
        
        time_main.add_updater(
            lambda p: p.become(
                Line(
                    collision_one.get_center()+0.8*LEFT,
                    [collision_one.get_center()[0]-0.8, collision_two.get_center()[1], 0], 
                    color=MAROON, stroke_width=5
                )
            )
        )
        time_tips.add_updater(
            lambda p: p.become(
                VGroup(
                    Line(time_main.get_start()+0.3*LEFT, time_main.get_start()+0.3*RIGHT, color=MAROON, stroke_width=5),
                    Line(time_main.get_end()+0.3*LEFT, time_main.get_end()+0.3*RIGHT, color=MAROON, stroke_width=5)
                )
            )
        )

        time_label = TextMobject("Time Difference:")

        time_number = DecimalNumber(collision_one.get_center()[1] - collision_two.get_center()[1], num_decimal_places=3, include_sign=False)
        time_number.next_to(time_label, direction=DOWN).shift(LEFT)
        time_number.add_updater(lambda p: p.set_value(abs(collision_one.get_center()[1] - collision_two.get_center()[1])))
        time_unit = TextMobject("seconds")
        time_unit.next_to(time_number, direction=RIGHT)

        time_label_group = VGroup(time_label, time_number, time_unit)
        time_label_group.add_background_rectangle()
        time_label_group.add_updater(lambda p: p.next_to(time_main, direction=LEFT))

        collision_label1 = TextMobject("Asteroid Collision").add_background_rectangle()
        collision_label2 = TextMobject("Asteroid Collision").add_background_rectangle()
        collision_label1.move_to([-3, 3, 0])
        collision_label2.move_to([[4, 3, 0]])

        first_collision = TextMobject("First Collision").add_background_rectangle()
        first_collision.move_to(collision_label2)
        second_collision = TextMobject("Second Collision").add_background_rectangle()
        second_collision.move_to(collision_label1)

        arrow1 = Arrow(collision_label1.get_edge_center(DOWN), collision_one.get_center()+0.1*UP)
        arrow2 = Arrow(collision_label2.get_edge_center(DOWN), collision_two.get_center()+0.1*UP)
        arrow1.add_updater(
            lambda m: m.become(Arrow(collision_label1.get_edge_center(DOWN), collision_one.get_center()+0.2*UP))
        )
        arrow2.add_updater(
            lambda m: m.become(Arrow(collision_label2.get_edge_center(DOWN), collision_two.get_center()+0.2*UP))
        )


        self.add_transformable_mobject(foreground_plane)
        self.add_transformable_mobject(stationary)
        self.add_transformable_mobject(your_world_line)
        self.add_transformable_mobject(chad_world_line)
        self.add_transformable_mobject(light_graph)
        self.add_moving_mobject(collision_one)
        self.add_moving_mobject(collision_two)

        self.play(
            Write(time_main),
            Write(time_tips),
            Write(time_label_group),
            Write(collision_one),
            Write(collision_two),
            Write(arrow1),
            Write(arrow2),
            Write(collision_label1),
            Write(collision_label2)
        )
        self.wait()

        self.apply_matrix(lighthouse_to_you, run_time=1)
        self.play(
            FadeOut(foreground_plane),
            ReplacementTransform(collision_label2, first_collision),
            ReplacementTransform(collision_label1, second_collision),
        )
        self.wait()

        self.play(
            FadeIn(foreground_plane),
        )
        self.add(stationary)
        self.apply_inverse(lighthouse_to_you, run_time=1)
        self.wait()

        self.play(
            ReplacementTransform(your_world_line, your_world_line2)
        )
        self.remove(your_world_line2)
        self.apply_inverse(lighthouse_to_you, run_time=1)
        first_collision.generate_target()
        second_collision.generate_target()
        first_collision.target.move_to(collision_label1)
        second_collision.target.move_to(collision_label2)
        self.play(
            FadeOut(foreground_plane),
            MoveToTarget(first_collision),
            MoveToTarget(second_collision)
        )
        self.wait()


class TimeDilation(LinearTransformationScene):
    CONFIG = {
        "camera_config": {
            "frame_center": 3*UP
        },
        "show_basis_vectors": False,
        "background_plane_kwargs": {
            "y_max": 10
        },
        "include_foreground_plane": False
    }
    def construct(self):
        your_beta = 1/3
        chad_beta = 2/3
        chad_new_beta = 3/7

        your_gamma = 1/math.sqrt(1 - (your_beta ** 2))
        chad_gamma = 1/math.sqrt(1 - (chad_beta ** 2))
        chad_new_gamma = 1/math.sqrt(1 - (chad_new_beta ** 2))

        lighthouse_to_you = [[your_gamma, -1 * your_gamma * your_beta], 
                            [-1 * your_gamma * your_beta, your_gamma]]

        lighthouse_to_chad = [[chad_gamma, -1 * chad_gamma * chad_beta], 
                             [-1 * chad_gamma * chad_beta, chad_gamma]]

        you_to_chad = [[chad_new_gamma, -1 * chad_new_gamma * chad_new_beta], 
                      [-1 * chad_new_gamma * chad_new_beta, chad_new_gamma]]

        def one_third(x):
            return 3*x
        def two_thirds(x):
            return (3*x)/2
        def light(x):
            return x

        foreground_plane = NumberPlane(y_min=-4, y_max=17, x_min=-10, x_max=12)

        stationary = Line(ORIGIN+DOWN, np.array([0, 10, 0]), stroke_color=RED)
        your_world_line = FunctionGraph(one_third, x_min=-10, x_max=10, color=TEAL_B)
        chad_world_line = FunctionGraph(two_thirds, x_min=-10, x_max=10, color=GREEN)
        light_graph = FunctionGraph(light, x_min=-10, x_max=15, color=YELLOW)

        collision = Dot(np.array([4, 5, 0]), color=LIGHT_BROWN)
        time = DashedLine(collision.get_center(), [0, collision.get_center()[1], 0], color=MAROON, stroke_width=5)
        time.add_updater(
            lambda p: p.become(
                DashedLine(collision.get_center(), [0, collision.get_center()[1], 0], color=MAROON, stroke_width=5)
                )
        )
        y_coord = DecimalNumber(5, num_decimal_places=3, include_sign=False)
        y_coord.add_updater(lambda p: p.set_value(collision.get_center()[1]))
        y_coord.add_updater(lambda p: p.next_to(collision, direction=UP).add_background_rectangle())
        time_label = TextMobject("Time =").add_background_rectangle()
        time_unit = TextMobject("seconds").add_background_rectangle()
        time_label.add_updater(lambda p: p.next_to(y_coord, direction=LEFT))
        time_unit.add_updater(lambda p: p.next_to(y_coord, direction=RIGHT))

        self.add_transformable_mobject(foreground_plane)
        self.add_transformable_mobject(stationary)
        self.add_transformable_mobject(your_world_line)
        self.add_transformable_mobject(chad_world_line)
        self.add_transformable_mobject(light_graph)
        self.add_moving_mobject(collision)
        self.add(collision)

        self.play(
            Write(time),
            Write(time_label),
            Write(y_coord),
            Write(time_unit)
        )
        self.wait()

        self.apply_matrix(lighthouse_to_you, run_time=1)
        self.play(
            FadeOut(foreground_plane)
        )
        self.wait()
        foreground_plane.apply_matrix(np.linalg.inv(lighthouse_to_you))

        self.play(
            FadeIn(foreground_plane)
        )

        self.apply_matrix(you_to_chad, run_time=1)
        self.play(
            FadeOut(foreground_plane)
        )
        self.wait()


class TimeDilation2(LinearTransformationScene):
    CONFIG = {
        "camera_config": {
            "frame_center": 3*UP
        },
        "show_basis_vectors": False,
        "background_plane_kwargs": {
            "y_max": 10
        },
        "include_foreground_plane": False
    }
    def construct(self):
        your_beta = 1/3
        chad_beta = 2/3
        chad_new_beta = 3/7

        your_gamma = 1/math.sqrt(1 - (your_beta ** 2))
        chad_gamma = 1/math.sqrt(1 - (chad_beta ** 2))
        chad_new_gamma = 1/math.sqrt(1 - (chad_new_beta ** 2))

        lighthouse_to_you = [[your_gamma, -1 * your_gamma * your_beta], 
                            [-1 * your_gamma * your_beta, your_gamma]]

        lighthouse_to_chad = [[chad_gamma, -1 * chad_gamma * chad_beta], 
                             [-1 * chad_gamma * chad_beta, chad_gamma]]

        you_to_chad = [[chad_new_gamma, -1 * chad_new_gamma * chad_new_beta], 
                      [-1 * chad_new_gamma * chad_new_beta, chad_new_gamma]]

        def one_third(x):
            return 3*x
        def two_thirds(x):
            return (3*x)/2
        def light(x):
            return x

        foreground_plane = NumberPlane(y_min=-4, y_max=17, x_min=-10, x_max=12)

        stationary = Line(ORIGIN+DOWN, np.array([0, 10, 0]), stroke_color=RED)
        your_world_line = FunctionGraph(one_third, x_min=-10, x_max=10, color=TEAL_B)
        chad_world_line = FunctionGraph(two_thirds, x_min=-10, x_max=10, color=GREEN)
        light_graph = FunctionGraph(light, x_min=-10, x_max=15, color=YELLOW)

        # collision 1
        collision = Dot(np.array([4, 5, 0]), color=LIGHT_BROWN)
        y_coord = DecimalNumber(5, num_decimal_places=3, include_sign=False)
        y_coord.add_updater(lambda p: p.set_value(collision.get_center()[1]))

        # collision 2
        collision2 = Dot(np.array([2, 3, 0]), color=LIGHT_BROWN)
        y_coord2 = DecimalNumber(3, num_decimal_places=3, include_sign=False)
        y_coord2.add_updater(lambda p: p.set_value(collision2.get_center()[1]))

        # label
        time_main = Line(
            [(collision.get_center()[0] + collision2.get_center()[0])/2, collision.get_center()[1], 0],
            [(collision.get_center()[0] + collision2.get_center()[0])/2, collision2.get_center()[1], 0], 
            color=MAROON, stroke_width=5
            )
        time_tips = VGroup(
            Line(time_main.get_start()+0.3*LEFT, time_main.get_start()+0.3*RIGHT, color=MAROON, stroke_width=5),
            Line(time_main.get_end()+0.3*LEFT, time_main.get_end()+0.3*RIGHT, color=MAROON, stroke_width=5)
        )
        
        time_main.add_updater(
            lambda p: p.become(
                Line(
                    [(collision.get_center()[0] + collision2.get_center()[0])/2, collision.get_center()[1], 0],
                    [(collision.get_center()[0] + collision2.get_center()[0])/2, collision2.get_center()[1], 0], 
                    color=MAROON, stroke_width=5
                )
            )
        )
        time_tips.add_updater(
            lambda p: p.become(
                VGroup(
                    Line(time_main.get_start()+0.3*LEFT, time_main.get_start()+0.3*RIGHT, color=MAROON, stroke_width=5),
                    Line(time_main.get_end()+0.3*LEFT, time_main.get_end()+0.3*RIGHT, color=MAROON, stroke_width=5)
                )
            )
        )

        time_label = TextMobject("Time Difference:")

        time_number = DecimalNumber(collision.get_center()[1] - collision2.get_center()[1], num_decimal_places=3, include_sign=False)
        time_number.next_to(time_label, direction=DOWN).shift(LEFT)
        time_number.add_updater(lambda p: p.set_value(collision.get_center()[1] - collision2.get_center()[1]))
        time_unit = TextMobject("seconds")
        time_unit.next_to(time_number, direction=RIGHT)

        time_label_group = VGroup(time_label, time_number, time_unit)
        time_label_group.add_background_rectangle()
        time_label_group.add_updater(lambda p: p.next_to(time_main, direction=RIGHT))
        
        self.add_transformable_mobject(foreground_plane)
        self.add_transformable_mobject(stationary)
        self.add_transformable_mobject(your_world_line)
        self.add_transformable_mobject(chad_world_line)
        self.add_transformable_mobject(light_graph)
        self.add_moving_mobject(collision)
        self.add_moving_mobject(collision2)

        self.play(
            Write(time_main),
            Write(time_tips),
            Write(time_label_group)
        )
        self.wait()

        self.apply_matrix(lighthouse_to_you, run_time=1)
        self.play(
            FadeOut(foreground_plane)
        )
        self.wait()
        foreground_plane.apply_matrix(np.linalg.inv(lighthouse_to_you))

        self.play(
            FadeIn(foreground_plane)
        )

        self.apply_matrix(you_to_chad, run_time=1)
        self.play(
            FadeOut(foreground_plane)
        )
        self.wait()


class RocketPath(Scene):
    def construct(self):
        rocket_path = Line(
            np.array([-6, 0, 0]), ORIGIN, color=BLUE
        )
        space_path = Line(
            ORIGIN, np.array([-20, 0, 0]),  color=BLUE
        )

        rocket = ImageMobject("Rocket")
        rocket.move_to(
            np.array([-6, 0, 0])
        )

        space = ImageMobject("Space.png").scale(10)

        # PLAY COMMANDS
        self.add(space)
        self.add(rocket)
        self.wait()

        self.play(
            MoveAlongPath(rocket, rocket_path)
        )
        self.wait()

        self.play(
            MoveAlongPath(space, space_path)
        )
        self.wait()


class ConditionOne(Scene):
    CONFIG = {
        "camera_config": {
            "frame_center": 3*UP
        }
    }
    def construct(self):
        plane = NumberPlane(y_min=-2, y_max=12)

        # World Line Functions
        def one_third(x):
            return 3*x
        def two_thirds(x):
            return (3*x)/2
        def light(x):
            return x

        # World Lines
        stationary = Line(ORIGIN+DOWN, np.array([0, 8, 0]), stroke_color=RED)
        your_world_line = FunctionGraph(one_third, x_min=-0.4, x_max=3, color=TEAL_B)
        chad_world_line = FunctionGraph(two_thirds, x_min=-0.8, x_max=5.7, color=GREEN)
        light_graph = FunctionGraph(light, x_min=-1.4, x_max=10, color=YELLOW)

        # Observer
        observer = TextMobject("Observer").move_to([-4, 6, 0]).scale(1.5).add_background_rectangle()
        arrow = CurvedArrow(
            observer.get_edge_center(direction=DOWN) + 0.1*DOWN, np.array([-0.1, 3.4, 0]), color=RED, buff=5
        )

        # PLAY COMMANDS
        self.add(plane, stationary, your_world_line, chad_world_line, light_graph)
        self.play(
            Write(observer),
            Write(arrow)
        )
        self.wait()
        

class ConditionTwo(Scene):
    def construct(self):
        # Paths
        rocket_path = Line(
            np.array([0, 2, 0]), np.array([6, 2, 0]), color=BLUE
        )
        lighthouse_path = Line(
            np.array([0, -2, 0]), np.array([-6, -2, 0]),  color=BLUE
        )
        space_path = Line(
            ORIGIN, np.array([-6, 0, 0]),  color=BLUE
        )

        # Assets
        rocket = ImageMobject("Rocket")
        rocket.move_to(
            np.array([0, 2, 0])
        )
        lighthouse = ImageMobject("lightless-house-centered.png")
        lighthouse.move_to(np.array([0, -2, 0]))

        space = ImageMobject("Space.png").scale(10)

        # UpdaterFunctions
        your_speed = TexMobject("Speed = \\frac{1}{3}\ c").scale(0.8).next_to(rocket, direction=LEFT)
        lighthouse_speed = TexMobject("Speed = \\frac{1}{3}\ c").scale(0.8).next_to(lighthouse, direction=RIGHT)
        def rocket_text(obj):
            obj.next_to(rocket, direction=LEFT)
        def lighthouse_text(obj):
            obj.next_to(lighthouse, direction=RIGHT)

        your_speed.add_updater(rocket_text)
        lighthouse_speed.add_updater(lighthouse_text)
        # PLAY COMMANDS
        self.add(space)
        self.add(rocket)
        self.add(your_speed)
        self.add(lighthouse)
        self.wait()

        self.play(
            MoveAlongPath(rocket, rocket_path)
        )

        self.wait()
        self.play(
            ReplacementTransform(your_speed, lighthouse_speed),
            rocket.move_to, np.array([0, 2, 0]), run_time=0.5
        )

        self.play(
            MoveAlongPath(space, space_path),
            MoveAlongPath(lighthouse, lighthouse_path)
        )
        self.wait()


class ConditionTwoAngle(Scene):
    CONFIG = {
        "camera_config": {
            "frame_center": 3*UP
        }
    }
    def construct(self):
        plane = NumberPlane(y_min=-2, y_max=12)

        # World Line Functions
        def one_third(x):
            return 3*x
        def negative_one_third(x):
            return -3*x

        # World Lines
        stationary = Line(ORIGIN+DOWN, np.array([0, 8, 0]), stroke_color=RED)
        stationary.generate_target()
        stationary_target_graph = FunctionGraph(negative_one_third, x_min=-3, x_max=0.4, color=RED)
        stationary.target = Line(stationary_target_graph.get_end(), stationary_target_graph.get_start(), color=RED)

        your_world_line_graph = FunctionGraph(one_third, x_min=-0.4, x_max=3, color=TEAL_B)
        your_world_line = Line(your_world_line_graph.get_start(), your_world_line_graph.get_end(), color=TEAL_B)
        your_world_line.generate_target()
        your_world_line.target = Line(ORIGIN+DOWN, np.array([0, 8, 0]), stroke_color=TEAL_B)

        angle = Arc(start_angle=your_world_line.get_angle(), angle=stationary.get_angle() - your_world_line.get_angle(), radius=2, color=ORANGE)
        angle.generate_target()
        angle.target = Arc(start_angle=your_world_line.target.get_angle(), angle=stationary.target.get_angle() - your_world_line.target.get_angle(), radius=2, color=ORANGE)

        # PLAY COMMANDS
        self.add(plane, stationary, your_world_line, angle)
        self.play(
            Indicate(angle)
        )
        self.play(
            MoveToTarget(stationary),
            MoveToTarget(your_world_line),
            MoveToTarget(angle)
        )
        self.play(
            Indicate(angle)
        )
        self.wait()


class ConditionThree(Scene):
    CONFIG = {
        "camera_config": {
            "frame_center": 3*UP
        }
    }
    def construct(self):
        # World Line Functions
        def one_third(x):
            return 3*x
        def two_thirds(x):
            return (3*x)/2
        def light(x):
            return x
        def negative_light(x):
            return -1*x

        # World Lines
        stationary = Line(ORIGIN+DOWN, np.array([0, 8, 0]), stroke_color=RED)
        your_world_line = FunctionGraph(one_third, x_min=-0.4, x_max=3, color=TEAL_B)
        chad_world_line = FunctionGraph(two_thirds, x_min=-0.8, x_max=5.7, color=GREEN)
        light_graph = FunctionGraph(light, x_min=-10, x_max=10, color=YELLOW)
        flipped_light_graph = FunctionGraph(negative_light, x_min=-10, x_max=10, color=YELLOW)

        # slope
        light_run = Line(
            ORIGIN, np.array([1, 0, 0]), color=MAROON, stroke_width=5
        )
        light_rise = Line(
            np.array([1, 0, 0]), np.array([1, 1, 0]), color=MAROON, stroke_width=5
        )
        light_rise_label = TexMobject("1").next_to(light_rise, direction=RIGHT).add_background_rectangle()
        light_run_label = TexMobject("1").next_to(light_run, direction=DOWN).add_background_rectangle()

        foreground_plane = NumberPlane(y_min=-4, y_max=17, x_min=-10, x_max=12)

        # PLAY COMMANDS:
        self.add(foreground_plane, stationary, your_world_line, chad_world_line, light_graph)
        self.play(
            WiggleOutThenIn(light_graph)
        )
        self.wait()
        self.play(
            *[FadeOut(i) for i in [stationary, your_world_line, chad_world_line]],
            Write(light_run),
            Write(light_rise),
            Write(light_run_label),
            Write(light_rise_label)
        )
        self.wait()

        shifter = 1
        self.play(Write(flipped_light_graph))
        for i in range(5):
            self.play(Write(light_graph.copy().shift(shifter*UP)))
            self.play(Write(flipped_light_graph.copy().shift(shifter*UP)))
            self.play(Write(light_graph.copy().shift(shifter*DOWN)))
            self.play(Write(flipped_light_graph.copy().shift(shifter*DOWN)))
            shifter += 1
        self.wait()


class Race(Scene):
    def construct(self):
        # Assets
        space = ImageMobject("space.png")
        space.scale(10).shift(LEFT)

        lighthouse_position = np.array([-4.6, -3, 0])
        lighthouse = ImageMobject("space-lighthouse.png")
        lighthouse.move_to(lighthouse_position)

        lightlesshouse = ImageMobject ("space-lightless-house.png")
        lightlesshouse.move_to(lighthouse_position)

        rocket = ImageMobject("Rocket.png")
        rocket.scale(0.5)
        rocket.move_to(np.array([-6, 0, 0]))

        chad = ImageMobject("cool-rocket.png")
        chad.scale(0.5)
        chad.move_to(np.array([-6, 3, 0]))

        photon = ImageMobject("photon.png")
        photon.move_to(np.array([-5, -2.35, 0]))
        photon.scale(0.2)

        # Labels
        lighthouse_label = TextMobject("Interstellar Lighthouse").next_to(lighthouse, direction=RIGHT, buff = 1.5)
        rocket_label = TextMobject("You").next_to(rocket, direction=RIGHT, buff = 3)
        chad_label = TextMobject("Chad").next_to(chad, direction=RIGHT, buff = 2.8)

        lighthouse_arrow = Arrow(lighthouse_label.get_left(), lighthouse.get_right() + LEFT, buff = SMALL_BUFF)
        rocket_arrow = Arrow(rocket_label.get_left(), rocket.get_right(), buff = SMALL_BUFF)
        chad_arrow = Arrow(chad_label.get_left(), chad.get_right(), buff = SMALL_BUFF)

        labels = VGroup(lighthouse_label, rocket_label, chad_label, lighthouse_arrow, rocket_arrow, chad_arrow)

        # Paths
        chad_path = Line(
            chad.get_center(), np.array([2, 3, 0]), color = BLUE
        )

        rocket_path = Line(
            rocket.get_center(), np.array([-2, 0, 0]), color = BLUE
        )

        photon_path = Line(
            photon.get_center(), np.array([7, -2.35, 0]), color = BLUE
        )

        line_up = Line(
            chad.get_center() + RIGHT + UP, rocket.get_center() + RIGHT + 4*DOWN, color = RED
        )

        # Time
        """time = DecimalNumber(0, include_sign=False).to_edge(DOWN)
        time.add_updater(lambda p: p.set_value((photon.get_center()[0]+5) * 5/12))
        time_label = TextMobject("Time = ").next_to(time, direction=LEFT)
        time_unit = TextMobject("seconds").next_to(time, direction=RIGHT)"""

        # PLAY COMMANDS
        self.add(space)
        self.add(rocket)
        self.add(chad)
        self.add(lighthouse)
        self.add(time, time_label, time_unit)
        self.wait()
        self.play(
            Write(labels), run_time=0.8
        )

        """self.play(
            FadeIn(line_up)
        )
        self.play(
            FadeOut(line_up)
        )"""
        self.wait(2)

        self.play(
            FadeOut(labels)
        )
        self.wait()

        self.play(
            MoveAlongPath(chad, chad_path),
            MoveAlongPath(rocket, rocket_path),
            MoveAlongPath(photon, photon_path),
            run_time = 3
        )
        self.wait()

        photon_label = TextMobject("Photon").next_to(photon, direction=LEFT, buff = 3)
        photon_arrow = Arrow(photon_label.get_right(), photon.get_left(), buff = SMALL_BUFF)

        # Speed Labels
        your_speed = TexMobject("Speed = \\frac{1}{3}\ c").next_to(rocket, direction=LEFT)
        chad_speed = TexMobject("Speed = \\frac{2}{3}\ c").next_to(chad, direction=LEFT)
        photon_speed = TexMobject("Speed = c").next_to(photon, direction=LEFT)
        c = TextMobject("*c = Speed of Light").scale(0.5).to_corner(DR, buff=0.4)

        self.play(
            Write(photon_label),
            Write(photon_arrow),
        )
        self.wait()
        self.play(
            ReplacementTransform(photon_label, photon_speed),
            FadeOut(photon_arrow),
            FadeIn(your_speed),
            FadeIn(chad_speed),
            Write(c)
        )
        self.wait()
            

class RaceWithCollision(Scene):
    def construct(self):
        # Assets
        space = ImageMobject("space.png")
        space.scale(10).shift(LEFT)

        lighthouse_position = np.array([-4.6, -3, 0])
        lighthouse = ImageMobject("space-lighthouse.png")
        lighthouse.move_to(lighthouse_position)

        lightlesshouse = ImageMobject ("space-lightless-house.png")
        lightlesshouse.move_to(lighthouse_position)

        rocket = ImageMobject("Rocket.png")
        rocket.scale(0.5)
        rocket.move_to(np.array([-6, 0, 0]))

        chad = ImageMobject("cool-rocket.png")
        chad.scale(0.5)
        chad.move_to(np.array([-6, 3, 0]))

        photon = ImageMobject("photon.png")
        photon.move_to(np.array([-5, -2.35, 0]))
        photon.scale(0.2)

        collision = ImageMobject("asteroid-collision.png")
        collision.scale(0.3)

        # Paths
        chad_path = Line(
            chad.get_center(), np.array([2, 3, 0]), color = BLUE
        )

        rocket_path = Line(
            rocket.get_center(), np.array([-2, 0, 0]), color = BLUE
        )

        photon_path = Line(
            photon.get_center(), np.array([7, -2.35, 0]), color = BLUE
        )

        line_up = Line(
            chad.get_center() + RIGHT + UP, rocket.get_center() + RIGHT + 4*DOWN, color = RED
        )

        # Time Updater
        time = DecimalNumber(0, include_sign=False).to_edge(DOWN)
        time.add_updater(lambda p: p.set_value((photon.get_center()[0]+5) * 5/12))
        time_label = TextMobject("Time = ").next_to(time, direction=LEFT)
        time_unit = TextMobject("seconds").next_to(time, direction=RIGHT)

        # PLAY COMMANDS
        self.add(space)
        self.add(rocket)
        self.add(chad)
        self.add(lighthouse)
        self.add(time, time_label, time_unit)
        self.wait()

        self.play(
            MoveAlongPath(chad, chad_path),
            MoveAlongPath(rocket, rocket_path),
            MoveAlongPath(photon, photon_path),
            run_time = 1
        )
        collision.move_to(np.array([4.6, photon.get_center()[1], 0]))
        collision_label = VGroup(
            Line(collision.get_center()+0.5*LEFT, photon_path.get_start()+0.5*RIGHT, color=MAROON),
            Line(photon_path.get_start()+0.5*RIGHT+0.2*UP, photon_path.get_start()+0.5*RIGHT+0.2*DOWN, color=MAROON),
            Line(collision.get_center()+0.5*LEFT+0.2*UP, collision.get_center()+0.5*LEFT+0.2*DOWN, color=MAROON),
        )
        distance = TextMobject("4 light seconds").next_to(collision_label, direction=DOWN, buff=-0.1)

        self.play(
            FadeIn(collision),
        )
        self.play(
            Write(collision_label),
            Write(distance),
            run_time=1
        )

        self.wait()


class SpaceTimeDiagram(Scene):
    CONFIG = {
        "camera_config": {
            "frame_center": 3*UP
        }
    }
    def construct(self):
        plane = NumberPlane(
            axis_config = {
                "include_ticks": True, 
                "include_tip": True
            },
            y_axis_config = {
                "label_direction": DL
            },
            y_min=-2, y_max=12
        )
        plane.add_coordinates(x_vals = range(-7, 7), y_vals=range(-2, 7))
        plane.y_axis.shift(5*DOWN)

        time = TextMobject("Time (seconds)").move_to([1.5, 6.5, 0]).scale(0.7)
        time.add_background_rectangle()
        space = TextMobject("Space (light-seconds)").move_to([5, 0.5, 0]).scale(0.7)
        space.add_background_rectangle()
        title = TextMobject("Spacetime Diagram").shift(3*UP)
        light_second = TextMobject("*1 light second = 299,792,458 meters").move_to([4, -0.6, 0]).scale(0.6)
        light_second.add_background_rectangle()

        #self.add(title)
        self.play(
            #FadeOut(title),
            ShowCreation(plane, run_time=2, lag_ratio=0.1)
        )
        self.wait()

        self.play(
            Indicate(plane.y_axis)
        )
        self.play(
            Write(time)
        )
        self.wait()

        self.play(
            Indicate(plane.x_axis)
        )
        self.play(
            Write(space),
            Write(light_second),
            run_time=1
        )
        self.wait()

        self.play(
            FadeOut(time),
            FadeOut(space),
            FadeOut(light_second)
        )
        self.wait(2)
        
        self.play(
            FadeIn(NumberPlane(y_min=-2, y_max=12)),
            FadeOut(plane)
        )
        self.wait()


class LorentzTransformation(LinearTransformationScene):
    CONFIG = {
        "camera_config": {
            "frame_center": 3*UP
        },
        "show_basis_vectors": False,
        "background_plane_kwargs": {
            "y_max": 10
        },
        "include_foreground_plane": False,
        "foreground_plane_kwargs": {
            "y_min": -15,
            "y_max": 15,
            "x_min": -10,
            "x_max": 10
        }
    }
    def construct(self):
        # Assets
        lightlesshouse = ImageMobject("lightless-house-centered.png")
        lightlesshouse.scale(0.5)

        rocket = ImageMobject("Rocket.png")
        rocket.scale(0.3)

        chad = ImageMobject("cool-rocket.png")
        chad.scale(0.3)

        photon = ImageMobject("photon.png")
        photon.scale(0.3)

        assets = [lightlesshouse, rocket, chad, photon]
        x_coord = 0
        for asset in assets:
            asset.move_to(np.array([x_coord, 6, 0]))
            x_coord += 2

        # Math
        foreground_plane = NumberPlane(y_min=-15, y_max=15, x_min=-10, x_max=10)
        your_beta = 1/3
        chad_beta = 2/3

        your_gamma = 1/math.sqrt(1 - (your_beta ** 2))
        chad_gamma = 1/math.sqrt(1 - (chad_beta ** 2))

        lighthouse_to_you = [[your_gamma, -1 * your_gamma * your_beta], 
                            [-1 * your_gamma * your_beta, your_gamma]]

        lighthouse_to_chad =[[chad_gamma, -1 * chad_gamma * chad_beta], 
                 [-1 * chad_gamma * chad_beta, chad_gamma]]

        # World Line Functions
        def one_third(x):
            return 3*x
        def two_thirds(x):
            return (3*x)/2
        def light(x):
            return x

        # World Lines
        stationary = Line(ORIGIN+DOWN, np.array([0, 8, 0]), stroke_color=RED)
        your_world_line = FunctionGraph(one_third, x_min=-0.4, x_max=3, color=TEAL_B)
        chad_world_line = FunctionGraph(two_thirds, x_min=-0.8, x_max=5.7, color=GREEN)
        light_graph = FunctionGraph(light, x_min=-1.4, x_max=10, color=YELLOW)
        #planet_breakthrough = Line(np.array([4, -1, 0]), np.array([4, 10, 0]), stroke_color=ORANGE)

        paths = [stationary, your_world_line, chad_world_line, light_graph]

        # lists
        lines = []
        angles = VGroup()
        asset_targets = []

        # Perspective
        asset_perspective = ImageMobject("lightless-house-centered.png").scale(0.5).move_to([-3, 3, 0])
        asset_perspective2 = ImageMobject("Rocket.png").scale(0.4).move_to([-3, 3, 0])
        perspective = TextMobject("Perspective:").next_to(asset_perspective, direction=LEFT, buff=0.6).add_background_rectangle()

        # slope
        light_run = Line(
            ORIGIN, np.array([1, 0, 0]), color=MAROON, stroke_width=5
        )
        light_rise = Line(
            np.array([1, 0, 0]), np.array([1, 1, 0]), color=MAROON, stroke_width=5
        )
        light_rise_label = TexMobject("1").next_to(light_rise, direction=RIGHT).add_background_rectangle()
        light_run_label = TexMobject("1").next_to(light_run, direction=DOWN).add_background_rectangle()


        # PLAY COMMANDS
        # adding mobjects
        self.add_transformable_mobject(foreground_plane)
        for asset, path in zip(assets, paths):
            line = Line(path.get_start(), path.get_end(), color=path.get_color())
            lines.append(line)
            asset_target = Dot().move_to(asset)
            self.add_transformable_mobject(line)
            self.add(asset)
            asset_target.apply_matrix(lighthouse_to_you)
            asset_targets.append(asset_target.get_center())
            
        angle = Arc(start_angle=lines[1].get_angle(), angle=lines[0].get_angle() - lines[1].get_angle(), radius=1, color=ORANGE)
        
        self.add(asset_perspective)
        self.add(perspective)
        self.add(light_rise, light_run, light_rise_label, light_run_label)
        self.play(
            FadeIn(angle)
        )
        self.wait()

        self.play(
            *[FadeOut(asset) for asset in assets],
            FadeOut(angle)
        )

        # Apply Matrix
        self.apply_matrix(lighthouse_to_you, run_time=1)
        lightlesshouse.move_to([-2, 6, 0])
        rocket.move_to([0, 6, 0])
        chad.move_to([2.5, 6, 0])

        angle = Arc(start_angle=lines[1].get_angle(), angle=lines[0].get_angle() - lines[1].get_angle(), radius=1, color=ORANGE)
        self.play(
            *[FadeIn(asset) for asset in assets],
            FadeOut(foreground_plane),
            FadeIn(angle),
            FadeIn(asset_perspective2),
            FadeOut(asset_perspective)
            
        )
        self.wait()

        # Emphasize Mobjects
        self.play(
            WiggleOutThenIn(lines[1])
        )
        self.play(
            FocusOn(angle),
            Indicate(angle)
        )
        self.play(
            WiggleOutThenIn(lines[3]),
            WiggleOutThenIn(
                VGroup(light_rise, light_run, light_rise_label, light_run_label)
            )
        )
        self.wait()


class EnterText(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": GREEN_SCREEN
        }
    }
    def construct(self):
        text = TextMobject("Lorentz Transformations")
        text.move_to([-3, 0, 0])
        self.play(Write(text), run_time=0.5)
        self.wait()


class WorldLinesText(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": GREEN_SCREEN
        }
    }
    def construct(self):
        text = TextMobject("World Lines")
        text.scale(2)
        text.move_to([-3, 0, 0])
        self.play(Write(text), run_time=0.5)
        self.wait()


class PastPresentFuture(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": GREEN_SCREEN
        }
    }
    def construct(self):
        past = TextMobject("Past", background_stroke_width=3).scale(1.3)
        past.to_corner(DL)
        present = TextMobject("Present", background_stroke_width=3).scale(1.3)
        present.to_edge(DOWN)
        present.shift(1.5*LEFT)
        future = TextMobject("Future", background_stroke_width=3).scale(1.3)
        future.to_edge(DOWN)
        future.shift(3*RIGHT)
        self.play(Write(past), run_time=0.5)
        self.play(Write(present), run_time=0.5)
        self.play(Write(future), run_time=0.5)
        self.wait()