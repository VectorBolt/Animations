from manimlib.imports import *

class FactoringAndDistributingScene(Scene):
    def distribute(self, init_expression, final_expression, common_factor_on_left=True, draw_arrows=True):
        # format: a(b+c)
        if common_factor_on_left:
            common_factor = init_expression[0]
            term1 = init_expression[2]
            term2 = init_expression[4]
        # format: (b+c)(a) ---> "(a)" is one index
        else:
            common_factor = init_expression[5]
            term1 = init_expression[1]
            term2 = init_expression[3]
        final_expression[1:4].set_color(ORANGE)
        final_expression[6:].set_color(GREEN)

        if common_factor_on_left:
            arrow_angle = TAU/4
        else:
            arrow_angle = -TAU/4
        
        arrow1 = CurvedArrow(
            common_factor.get_edge_center(DOWN) + 0.2*DOWN, term1.get_edge_center(DOWN) + 0.2*DOWN,
            angle = arrow_angle, color=ORANGE
        )
        arrow2 = CurvedArrow(
            common_factor.get_edge_center(DOWN) + 0.2*DOWN, term2.get_edge_center(DOWN) + 0.2*DOWN,
            angle = arrow_angle, color=GREEN
        )

        if draw_arrows:
            if common_factor_on_left:
                self.play(
                    Write(arrow1),
                    init_expression[1:3].set_color, ORANGE,
                )
            else:
                self.play(
                    Write(arrow1),
                    init_expression[:2].set_color, ORANGE
                )
            if common_factor_on_left:
                self.play(
                    Write(arrow2),
                    init_expression[3:].set_color, GREEN
                )
            else:
                self.play(
                    Write(arrow2),
                    init_expression[2:5].set_color, GREEN
                )
            self.wait()
        
        if common_factor_on_left:
            self.play(
                ReplacementTransform(init_expression[:3].copy(), final_expression[:3]),
                ReplacementTransform(init_expression[5].copy(), final_expression[3])
            )
            self.play(
                ReplacementTransform(init_expression[3].copy(), final_expression[4])
            )
            self.play(
                ReplacementTransform(VGroup(init_expression[:2].copy(), init_expression[4:].copy()), VGroup(final_expression[5:7], final_expression[7:]))
            )
            self.wait()
        else:
            self.play(
                ReplacementTransform(VGroup(init_expression[:2].copy(), init_expression[4].copy()), final_expression[1:4]),
                ReplacementTransform(init_expression[5].copy(), final_expression[0])
            )
            self.play(
                ReplacementTransform(init_expression[2].copy(), final_expression[4])
            )
            self.play(
                ReplacementTransform(init_expression[5].copy(), final_expression[5]),
                ReplacementTransform(VGroup(init_expression[0].copy(), init_expression[3:5].copy()), VGroup(final_expression[6], final_expression[7:]))
            )
            self.wait()
        
    def distribute_four_terms(self, init_expression, final_expression, draw_arrows=True):
        arrow1 = CurvedArrow(
            init_expression[1].get_edge_center(DOWN) + 0.2*DOWN, init_expression[6].get_edge_center(DOWN) + 0.2*DOWN,
            angle = TAU/4, color=ORANGE
        )
        arrow2 = CurvedArrow(
            init_expression[1].get_edge_center(DOWN) + 0.2*DOWN, init_expression[8].get_edge_center(DOWN) + 0.2*DOWN,
            angle = TAU/4, color=GREEN
        )
        arrow3 = CurvedArrow(
            init_expression[3].get_edge_center(UP) + 0.2*UP, init_expression[6].get_edge_center(UP) + 0.2*UP,
            angle = -TAU/4, color=BLUE
        )
        arrow4 = CurvedArrow(
            init_expression[3].get_edge_center(UP) + 0.2*UP, init_expression[8].get_edge_center(UP) + 0.2*UP,
            angle = -TAU/4, color=YELLOW
        )

        if draw_arrows:
            self.play(Write(arrow1))
        self.play(
            ReplacementTransform(
                VGroup(init_expression[1].copy(), init_expression[5:7].copy(), init_expression[9].copy()), 
                VGroup(final_expression[0], final_expression[1:3], final_expression[3])
            )
        )
        self.wait()

        if draw_arrows:
            self.play(Write(arrow2))
        self.play(
            ReplacementTransform(
                VGroup(init_expression[:2].copy(), init_expression[5].copy(), init_expression[7:].copy()), 
                VGroup(final_expression[4:6], final_expression[6], final_expression[7:9])
            )
        )
        self.wait()

        if draw_arrows:
            self.play(Write(arrow3))
        self.play(
            ReplacementTransform(
                VGroup(init_expression[2:4].copy(), init_expression[5:7].copy(), init_expression[9].copy()), 
                VGroup(final_expression[9:11], final_expression[11:13], final_expression[13])
            )
        )
        self.wait()

        if draw_arrows:
            self.play(Write(arrow4))
        self.play(
            ReplacementTransform(
                VGroup(init_expression[2:4].copy(), init_expression[5].copy(), init_expression[7:].copy()), 
                VGroup(final_expression[14:16], final_expression[16], final_expression[17:])
            )
        )
        self.wait()
    
    def factor(self, initial_expression, final_expression, common_color=RED, common_factor_on_left=True):
        to_be_transformed = VGroup()
        for i in [0, 1, 2, 4, 7, 8]:
            to_be_transformed.add(
                initial_expression[i]
            )

        # format: a(b) + a(c)
        if common_factor_on_left:
            self.play(
                initial_expression[0].set_color, common_color,
                initial_expression[5].set_color, common_color
            )
            self.wait()

            self.play(
                initial_expression[5].move_to, initial_expression[0], path_arc=-TAU/3
            )
            self.remove(initial_expression[5])

            self.play(
                FadeOut(initial_expression[3]),
                FadeOut(initial_expression[6])
            )
            self.play(
                ReplacementTransform(to_be_transformed, final_expression[:6])
            )
            self.wait()
        # format: b(a) + c(a)
        else:
            self.play(
                initial_expression[1:4].set_color, common_color,
                initial_expression[6:9].set_color, common_color
            )
            self.wait()

            self.play(
                ReplacementTransform(initial_expression[6:9], final_expression[:3], 
                path_arc=-TAU/3),
                ReplacementTransform(initial_expression[1:4], final_expression[:3], 
                path_arc=TAU/3),
            )
            self.play(
                ReplacementTransform(initial_expression[0], final_expression[4],
                path_arc=TAU/2),
                ReplacementTransform(initial_expression[5], final_expression[6],
                path_arc=TAU/2),
                ReplacementTransform(initial_expression[4], final_expression[5],
                path_arc=TAU/2)
            )
            self.play(
                Write(final_expression[3]),
                Write(final_expression[7])
            )

            """
            self.play(
                FadeOut(initial_expression[init_first_index+3]),
                FadeOut(initial_expression[init_first_index+6])
            )
            self.play(
                ReplacementTransform(to_be_transformed, final_expression[final_first_index : final_first_index+6])
            )
            """
            self.wait()

class Test(FactoringAndDistributingScene):
    CONFIG = {
        "a": 4,
        "b": 2,
        "c": 3
    }
    def construct(self):
        self.distribute_common_factor_on_right()

    def distribute_common_factor_on_left(self):
        a = self.a
        b = self.b
        c = self.c
        # common factor on left
        init_expression = TexMobject("({}+3)".format(a), "(", b, "+", c, ")")
        expression.scale(2).to_edge(UP)

        distribute1 = TexMobject("({}+3)".format(a), "(", b, ")", "+", "({}+3)".format(a), "(", c, ")")
        distribute1.scale(2).next_to(expression, direction=DOWN, buff=1)

        self.add(expression)
        self.distribute(expression, distribute1, common_factor_on_left=True, draw_arrows=True)

    def distribute_common_factor_on_right(self):
        a = self.a
        b = self.b
        c = self.c
        # common factor on right
        expression = TexMobject("(", b, "+", c, ")", "({}+3)".format(a))
        expression.scale(2).to_edge(UP)

        distribute1 = TexMobject("({}+3)".format(a), "(", b, ")", "+", "({}+3)".format(a), "(", c, ")")
        distribute1.scale(2).next_to(expression, direction=DOWN, buff=1)

        self.add(expression)
        self.distribute(expression, distribute1, common_factor_on_left=False, draw_arrows=True)


class TwoRectScene(Scene):
    CONFIG = {
        "height1": 2,
        "width1": 1,
        "width2": 1
    }

    def introduce_initial_rect(self, animate=True):
        # Objects
        initial_rect = Rectangle(height=self.height1, width= self.width1 + self.width2, color=BLUE, fill_opacity=0.7)
        height_label = TexMobject(self.height1)
        width_label = TexMobject(self.width1, "+", self.width2)
        
        height_label.add_updater(lambda m: m.next_to(initial_rect, direction=RIGHT))
        width_label.add_updater(lambda m: m.next_to(initial_rect, direction=DOWN))

        if animate:
            self.play(
                Write(initial_rect)
            )
            self.play(
                Write(height_label)
            )
            self.play(
                Write(width_label)
            )
            self.wait()
        
        self.initial_group = [initial_rect, height_label, width_label]

    def split_rects(self, starting_group, animate=True, area_label=None):
        starting_rect, height_label, width_label = [*starting_group]
        height_label2 = height_label.copy()

        line1 = Line(
            starting_rect.get_vertices()[0] + RIGHT*self.width1, starting_rect.get_vertices()[3] + RIGHT*self.width1,
            color=YELLOW
        )

        left_rect = Polygon(
            starting_rect.get_vertices()[0], line1.get_start(), line1.get_end(), starting_rect.get_vertices()[3],
            color=ORANGE, fill_opacity=0.8
        )
        right_rect = Polygon(
            starting_rect.get_vertices()[1], line1.get_start(), line1.get_end(), starting_rect.get_vertices()[2],
            color=PURPLE, fill_opacity=0.8
        )

        # Area updaters
        def left_area_updater(label):
            label.move_to(left_rect)
        def right_area_updater(label):
            label.move_to(right_rect)

        left_area = TexMobject(self.height1, "(", self.width1, ")").scale(1.5)
        left_area.generate_target()
        left_area.target = TexMobject(self.height1*self.width1).scale(1.5)

        right_area = TexMobject(self.height1, "(", self.width2, ")").scale(1.5)
        right_area.generate_target()
        right_area.target = TexMobject(self.height1*self.width2).scale(1.5)
        
        height_label.clear_updaters()
        width_label.clear_updaters()

        if animate:
            width_label[1].add_updater(
                lambda p: p.set_x(
                    (width_label[0].get_x() + width_label[2].get_x())/2
                )
            )
            self.play(
                GrowFromCenter(line1),
            )
            self.play(
                FadeIn(left_rect),
                FadeIn(right_rect),
                FadeOut(starting_rect),
                FadeOut(line1)
            )
            self.play(
                width_label[0].next_to, left_rect, DOWN,
                width_label[2].next_to, right_rect, DOWN
            )
            self.wait()

            # add width updaters
            width_label[0].add_updater(lambda p: p.next_to(left_rect, direction=DOWN))
            width_label[2].add_updater(lambda p: p.next_to(right_rect, direction=DOWN))
            height_label.add_updater(lambda p: p.next_to(right_rect))
            height_label2.add_updater(lambda p: p.next_to(left_rect))

            self.play(
                ReplacementTransform(height_label.copy(), height_label2),
                FadeOut(width_label[1])
            )
            self.play(
                left_rect.shift, LEFT,
                right_rect.shift, RIGHT
            )
            self.wait()

            left_area.add_updater(left_area_updater)
            right_area.add_updater(right_area_updater)
            left_area.target.add_updater(left_area_updater)
            right_area.target.add_updater(right_area_updater)

            if area_label is None:
                self.play(
                    Write(left_area),
                    Write(right_area)
                )
            else:
                self.play(
                    ReplacementTransform(area_label[:3].copy(), left_area[:3]),
                    ReplacementTransform(area_label[5].copy(), left_area[3])
                )
                self.play(
                    ReplacementTransform(area_label[:2].copy(), right_area[:2]),
                    ReplacementTransform(area_label[4:].copy(), right_area[2:])
                )
            self.wait()
        else:
            left_rect.shift(LEFT)
            right_rect.shift(RIGHT)
            left_area.move_to(left_rect)
            right_area.move_to(right_rect)

            width_label[0].add_updater(lambda p: p.next_to(left_rect, direction=DOWN))
            width_label[2].add_updater(lambda p: p.next_to(right_rect, direction=DOWN))
            height_label.add_updater(lambda p: p.next_to(right_rect))
            height_label2.add_updater(lambda p: p.next_to(left_rect))

            left_area.add_updater(left_area_updater)
            right_area.add_updater(right_area_updater)
            width_label[1].add_updater(
                lambda p: p.set_x(
                    (width_label[0].get_x() + width_label[2].get_x())/2
                )
            )
        
        self.split_rect_group = [left_rect, left_area, right_rect, right_area, height_label2]

    def combine_rects(self, left_rect, right_rect, height_label2, starting_group):
        initial_rect, height_label, width_label = [*starting_group]
        self.play(
            FadeOut(height_label2),
            left_rect.shift, RIGHT,
            right_rect.shift, LEFT,
            ReplacementTransform(height_label2, height_label, path_arc=-TAU/4)
        )
        self.wait()
        self.remove(height_label2)

        self.play(
            FadeIn(initial_rect),
            FadeIn(width_label[1]),
            FadeOut(left_rect),
            FadeOut(right_rect)
        )
        self.wait()


class FourRectScene(Scene):
    CONFIG = {
        "h1": 0,
        "h2": 0,
        "w1": 0,
        "w2": 0
    }

    def introduce_initial_rect(self, animate=True):
        # Objects
        initial_rect = Rectangle(height=self.h1+self.h2, width=self.w1+self.w2, color=BLUE, fill_opacity=0.7)
        height_label = TexMobject(self.h1, "+", self.h2)
        width_label = TexMobject(self.w1, "+", self.w2)
        
        height_label.add_updater(lambda m: m.next_to(initial_rect, direction=RIGHT))
        width_label.add_updater(lambda m: m.next_to(initial_rect, direction=DOWN))
        width_label[1].add_updater(
            lambda p: 
                p.set_x(
                    (width_label[0].get_x() + width_label[2].get_x())/2
                )
                .set_y(
                    (width_label[0].get_y() + width_label[2].get_y())/2
                )
        )
        height_label[1].add_updater(
            lambda p: 
                p.set_x(
                    (height_label[0].get_x() + height_label[2].get_x())/2
                )
                .set_y(
                    (height_label[0].get_y() + height_label[2].get_y())/2
                )
        )

        if animate:
            self.play(
                Write(initial_rect)
            )
            self.play(
                Write(height_label)
            )
            self.play(
                Write(width_label)
            )
            self.wait()
        
        self.initial_group = [initial_rect, height_label, width_label]

    def split_rects(self, starting_group, animate=True, area_label=None):
        starting_rect, height_label, width_label = [*starting_group]
        height_label2 = height_label.copy()
        width_label2 = width_label.copy()

        # lines
        line1 = Line(
            starting_rect.get_vertices()[0] + RIGHT*self.w1, starting_rect.get_vertices()[3] + RIGHT*self.w1,
            color=YELLOW
        )
        line2 = Line(
            starting_rect.get_vertices()[0] + DOWN*self.h1, starting_rect.get_vertices()[1] + DOWN*self.h1,
            color=YELLOW
        )

        # rects
        ul_rect = Polygon(
            starting_rect.get_vertices()[0], line1.get_start(), line1.get_start()+DOWN*self.h1, starting_rect.get_vertices()[0]+DOWN*self.h1,
            color=ORANGE, fill_opacity=0.8
        )
        ur_rect = Polygon(
            starting_rect.get_vertices()[1], line1.get_start(), line1.get_start()+DOWN*self.h1, starting_rect.get_vertices()[1]+DOWN*self.h1,
            color=GREEN, fill_opacity=0.8
        )
        dl_rect = Polygon(
            starting_rect.get_vertices()[3], line1.get_end(), line1.get_end()+UP*self.h2, starting_rect.get_vertices()[3]+UP*self.h2,
            color=BLUE, fill_opacity=0.8
        )
        dr_rect = Polygon(
            starting_rect.get_vertices()[2], line1.get_end(), line1.get_start()+DOWN*self.h1, starting_rect.get_vertices()[1]+DOWN*self.h1,
            color=YELLOW, fill_opacity=0.8
        )

        # Area updaters
        def ul_area_updater(label):
            label.move_to(ul_rect)
        def ur_area_updater(label):
            label.move_to(ur_rect)
        def dl_area_updater(label):
            label.move_to(dl_rect)
        def dr_area_updater(label):
            label.move_to(dr_rect)

        ul_area = TexMobject(self.w1, "(", self.h1, ")").scale(1.5)
        ul_area.generate_target()
        ul_area.target = TexMobject(self.w1*self.h1).scale(1.5)

        ur_area = TexMobject(self.w2, "(", self.h1, ")").scale(1.5)
        ur_area.generate_target()
        ur_area.target = TexMobject(self.w2*self.h1).scale(1.5)

        dl_area = TexMobject(self.w1, "(", self.h2, ")").scale(1.5)
        dl_area.generate_target()
        dl_area.target = TexMobject(self.w1*self.h2).scale(1.5)

        dr_area = TexMobject(self.w2, "(", self.h2, ")").scale(1.5)
        dr_area.generate_target()
        dr_area.target = TexMobject(self.w2*self.h2).scale(1.5)
        
        height_label.clear_updaters()
        width_label.clear_updaters()
        width_label[1].add_updater(
            lambda p: 
                p.set_x(
                    (width_label[0].get_x() + width_label[2].get_x())/2
                )
                .set_y(
                    (width_label[0].get_y() + width_label[2].get_y())/2
                )
        )
        height_label[1].add_updater(
            lambda p: 
                p.set_x(
                    (height_label[0].get_x() + height_label[2].get_x())/2
                )
                .set_y(
                    (height_label[0].get_y() + height_label[2].get_y())/2
                )
        )

        if animate:
            self.play(
                GrowFromCenter(line1),
                GrowFromCenter(line2)
            )
            self.play(
                FadeIn(ul_rect),
                FadeIn(ur_rect),
                FadeIn(dl_rect),
                FadeIn(dr_rect),
                FadeOut(starting_rect),
                FadeOut(line1),
                FadeOut(line2)
            )
            
            self.play(
                width_label[0].next_to, dl_rect, DOWN,
                width_label[2].next_to, dr_rect, DOWN,
                height_label[0].next_to, ur_rect, RIGHT,
                height_label[2].next_to, dr_rect, RIGHT
            )
            self.wait()

            # Updaters for labels
            height_label[0].add_updater(lambda p: p.next_to(ur_rect))
            height_label[2].add_updater(lambda p: p.next_to(dr_rect))
            height_label2[0].add_updater(lambda p: p.next_to(ul_rect))
            height_label2[2].add_updater(lambda p: p.next_to(dl_rect))

            width_label[0].add_updater(lambda p: p.next_to(dl_rect, direction=DOWN))
            width_label[2].add_updater(lambda p: p.next_to(dr_rect, direction=DOWN))
            width_label2[0].add_updater(lambda p: p.next_to(ul_rect, direction=DOWN))
            width_label2[2].add_updater(lambda p: p.next_to(ur_rect, direction=DOWN))

            width_label[1].clear_updaters()
            height_label[1].clear_updaters()

            # PLAY COMMANDS
            # Separating rects
            self.play(
                FadeOut(height_label[1]),
                FadeOut(width_label[1])
            )
            self.play(
                ReplacementTransform(height_label[::2].copy(), height_label2[::2])   
            )
            self.play(
                ReplacementTransform(width_label[::2].copy(), width_label2[::2])
            )
            
            self.play(
                ul_rect.shift, LEFT,
                ur_rect.shift, RIGHT,
                dl_rect.shift, DOWN+LEFT,
                dr_rect.shift, DOWN+RIGHT
            )
            self.wait(2)

            # New Area Labels
            ul_area.move_to(ul_rect)
            ur_area.move_to(ur_rect)
            dl_area.move_to(dl_rect)
            dr_area.move_to(dr_rect)

            ul_area.target.move_to(ul_rect)
            ur_area.target.move_to(ur_rect)
            dl_area.target.move_to(dl_rect)
            dr_area.target.move_to(dr_rect)

            ul_area.add_updater(ul_area_updater)
            ur_area.add_updater(ur_area_updater)
            dl_area.add_updater(dl_area_updater)
            dr_area.add_updater(dr_area_updater)

            if area_label is None:
                self.play(
                    Write(ul_area),
                    Write(ur_area),
                    Write(dl_area),
                    Write(dr_area)
                )
            else:
                self.play(
                    ReplacementTransform(area_label[1].copy(), ul_area[0]),
                    ReplacementTransform(area_label[5:7].copy(), ul_area[1:3]),
                    ReplacementTransform(area_label[9].copy(), ul_area[3]),
                )
                self.play(
                    ReplacementTransform(area_label[1].copy(), dl_area[0]),
                    ReplacementTransform(area_label[5].copy(), dl_area[1]),
                    ReplacementTransform(area_label[8:].copy(), dl_area[2:]),
                )
                self.play(
                    ReplacementTransform(area_label[3].copy(), ur_area[0]),
                    ReplacementTransform(area_label[5:7].copy(), ur_area[1:3]),
                    ReplacementTransform(area_label[9].copy(), ur_area[3]),
                )
                self.play(
                    ReplacementTransform(area_label[3].copy(), dr_area[0]),
                    ReplacementTransform(area_label[5].copy(), dr_area[1]),
                    ReplacementTransform(area_label[8:].copy(), dr_area[2:]),
                )
            self.wait()
        else:
            ul_rect.shift(LEFT)
            ur_rect.shift(RIGHT)
            dl_rect.shift(LEFT+DOWN)
            dr_rect.shift(RIGHT+DOWN)
            ul_area.move_to(ul_rect)
            ur_area.move_to(ur_rect)
            dl_area.move_to(dl_rect)
            dr_area.move_to(dr_rect)

            # Updaters for labels
            height_label[0].add_updater(lambda p: p.next_to(ur_rect))
            height_label[2].add_updater(lambda p: p.next_to(dr_rect))
            height_label2[0].add_updater(lambda p: p.next_to(ul_rect))
            height_label2[2].add_updater(lambda p: p.next_to(dl_rect))

            width_label[0].add_updater(lambda p: p.next_to(dl_rect, direction=DOWN))
            width_label[2].add_updater(lambda p: p.next_to(dr_rect, direction=DOWN))
            width_label2[0].add_updater(lambda p: p.next_to(ul_rect, direction=DOWN))
            width_label2[2].add_updater(lambda p: p.next_to(ur_rect, direction=DOWN))

            ul_area.add_updater(ul_area_updater)
            ur_area.add_updater(ur_area_updater)
            dl_area.add_updater(dl_area_updater)
            dr_area.add_updater(dr_area_updater)

        self.split_rect_group = [ul_rect, dl_rect, ur_rect, dr_rect, ul_area, dl_area, ur_area, dr_area, height_label2, width_label2]

    def combine_rects(self, starting_group, four_rect_group):
        initial_rect, height_label, width_label = [*starting_group]
        ul_rect, dl_rect, ur_rect, dr_rect, ul_area, dl_area, ur_area, dr_area, height_label2, width_label2 = [*four_rect_group]
        self.play(
            ul_rect.shift, RIGHT,
            ur_rect.shift, LEFT,
            dl_rect.shift, UP+RIGHT,
            dr_rect.shift, UP+LEFT,
            ReplacementTransform(height_label2[::2], height_label[::2], path_arc=-TAU/4),
            ReplacementTransform(width_label2[::2], width_label[::2], path_arc=-TAU/4)
        )
        self.wait()
        self.remove(height_label2, width_label2)

        self.play(
            FadeIn(initial_rect),
            FadeIn(width_label[1]),
            FadeIn(height_label[1]),
            FadeOut(ul_rect),
            FadeOut(ur_rect),
            FadeOut(dl_rect),
            FadeOut(dr_rect)
        )
        self.wait()
    
    def combine_into_block(self, rect1, rect2, fadeouts, fadeins, arrangement, block_color):
        rect_group = VGroup(rect1, rect2)
        if arrangement == DOWN or arrangement == UP:
            block_height = rect1.get_height() + rect2.get_height()
            block_width = rect1.get_width()
        else:
            block_height = rect1.get_height() 
            block_width = rect1.get_width() + rect2.get_width()
        block = Rectangle(height=block_height, width=block_width, color=block_color, fill_opacity=0.8)


###########################

class AlgebraicDistribution(FactoringAndDistributingScene):
    def construct(self):
        a=4
        b=2
        c=3
        expression = TexMobject(a, "(", b, "+", c, ")")
        expression.scale(2).to_edge(UP)

        parentheses_first = TexMobject(a, "(", b+c, ")")
        parentheses_first.scale(2).next_to(expression, direction=DOWN, buff=1)
        parentheses_first[1:].set_color(BLUE)

        solution = TexMobject(a*(b+c))
        solution.scale(2).next_to(parentheses_first, direction=DOWN, buff=1)

        distribute1 = TexMobject(a, "(", b, ")", "+", a, "(", c, ")")
        distribute1.scale(2).next_to(expression, direction=DOWN, buff=1)
        distribute1[1:4].set_color(ORANGE)
        distribute1[6:].set_color(GREEN)

        distribute2 = TexMobject(a*b, "+", a*c)
        distribute2.scale(2).next_to(distribute1, direction=DOWN, buff=1)
        distribute2[0].set_color(ORANGE)
        distribute2[2].set_color(GREEN)

        solution_copy = solution.copy().next_to(distribute2, direction=DOWN, buff=1)

        rect1 = SurroundingRectangle(solution, buff=0.2)
        rect2 = SurroundingRectangle(solution_copy, buff=0.2)

        arrow1 = CurvedArrow(
            expression[0].get_edge_center(DOWN) + 0.2*DOWN, expression[2].get_edge_center(DOWN) + 0.2*DOWN,
            angle = TAU/4, color=ORANGE
        )
        arrow2 = CurvedArrow(
            expression[0].get_edge_center(DOWN) + 0.2*DOWN, expression[4].get_edge_center(DOWN) + 0.2*DOWN,
            angle = TAU/4, color=GREEN
        )

        # PLAY COMMANDS - Without distributing
        self.play(
            Write(expression)
        )
        self.wait()

        self.play(
            expression[1:].set_color, BLUE
        )
        self.play(
            ReplacementTransform(expression[:2].copy(), parentheses_first[:2]),
            ReplacementTransform(expression[5].copy(), parentheses_first[3]),
            ReplacementTransform(expression[2:5].copy(), parentheses_first[2])
        )
        self.wait()

        self.play(
            ReplacementTransform(parentheses_first.copy(), solution)
        )
        self.play(
            Write(rect1)
        )
        self.wait()

        self.play(
            FadeOut(
                VGroup(parentheses_first, solution, rect1)
            )
        )
        self.wait()

        # With Distributing
        self.distribute(expression, distribute1, common_factor_on_left=True, draw_arrows=True)

        self.play(
            ReplacementTransform(distribute1[:4].copy(), distribute2[0])
        )
        self.play(
            ReplacementTransform(distribute1[4:].copy(), distribute2[1:])
        )
        self.wait()

        self.play(
            ReplacementTransform(distribute2.copy(), solution_copy)
        )
        self.play(
            Write(rect2)
        )
        self.wait()


class AlgebraicDistribution2(FactoringAndDistributingScene):
    def construct(self):
        a=4
        b=2
        c=3
        d=1
        expression = TexMobject("(", a, "+", b, ")", "(", c, "+", d, ")")
        expression.scale(2).to_edge(UP, buff=1)

        parentheses_first = TexMobject("(",a+b, ")", "(", c+d, ")")
        parentheses_first.scale(2).next_to(expression, direction=DOWN, buff=1)
        parentheses_first[:3].set_color(BLUE)
        parentheses_first[3:].set_color(GREEN)

        solution = TexMobject((a+b)*(c+d))
        solution.scale(2).next_to(parentheses_first, direction=DOWN, buff=1)

        distribute1 = TexMobject(a, "(", c, ")", "+", a, "(", d, ")", "+", b, "(", c, ")", "+", b, "(", d, ")")
        distribute1.scale(2).next_to(expression, direction=DOWN, buff=1)
        distribute1[:4].set_color(ORANGE)
        distribute1[4:9].set_color(GREEN)
        distribute1[9:14].set_color(BLUE)
        distribute1[14:].set_color(YELLOW)

        distribute2 = TexMobject(a*c, "+", a*d, "+", b*c, "+", b*d)
        distribute2.scale(2).next_to(distribute1, direction=DOWN, buff=1)
        distribute2[0].set_color(ORANGE)
        distribute2[1:3].set_color(GREEN)
        distribute2[3:5].set_color(BLUE)
        distribute2[5:].set_color(YELLOW)

        solution_copy = solution.copy().next_to(distribute2, direction=DOWN, buff=1)

        rect1 = SurroundingRectangle(solution, buff=0.2)
        rect2 = SurroundingRectangle(solution_copy, buff=0.2)

        # PLAY COMMANDS - Without distributing
        self.play(
            Write(expression)
        )
        self.wait()

        self.play(
            expression[:5].set_color, BLUE
        )
        self.play(
            expression[5:].set_color, GREEN
        )
        self.wait()

        self.play(
            ReplacementTransform(expression[:5].copy(), parentheses_first[:3])
        )
        self.play(
            ReplacementTransform(expression[5:].copy(), parentheses_first[3:])
        )
        self.wait()

        self.play(
            ReplacementTransform(parentheses_first.copy(), solution)
        )
        self.play(
            Write(rect1)
        )
        self.wait()

        self.play(
            FadeOut(
                VGroup(parentheses_first, solution, rect1)
            )
        )
        self.play(
            expression.set_color, WHITE
        )
        self.wait()

        # With Distributing
        self.distribute_four_terms(expression, distribute1)

        self.play(
            ReplacementTransform(distribute1[:4].copy(), distribute2[0])
        )
        self.play(
            ReplacementTransform(distribute1[4:9].copy(), distribute2[1:3])
        )
        self.play(
            ReplacementTransform(distribute1[9:14].copy(), distribute2[3:5])
        )
        self.play(
            ReplacementTransform(distribute1[14:].copy(), distribute2[5:])
        )
        self.wait()

        self.play(
            ReplacementTransform(distribute2.copy(), solution_copy)
        )
        self.play(
            Write(rect2)
        )
        self.wait()


class DistributingRects(TwoRectScene):
    CONFIG = {
        "height1": 4,
        "width1": 2,
        "width2": 3
    }

    def construct(self):
        area_label = TexMobject(self.height1, "(", self.width1, "+", self.width2, ")").scale(2)
        area_label_simplified = TexMobject(self.height1, "(", self.width1+self.width2, ")").scale(2)
        plus_sign = TexMobject("+")
        final_area = TexMobject(self.height1*self.width1 + self.height1*self.width2).scale(2)

        # PLAY COMMANDS
        self.introduce_initial_rect()
        
        # Manipulate area label
        self.play(
            Write(area_label)
        )
        self.wait()

        self.play(
            Transform(area_label, area_label_simplified),
            rate_func=there_and_back_with_pause,
            run_time=2
        )
        self.wait()

        self.play(
            area_label.to_edge, UP
        )

        # split rects
        self.split_rects(self.initial_group, area_label=area_label)
        left_rect, left_area, right_rect, right_area, height_label2 = self.split_rect_group

        self.play(
            MoveToTarget(left_area)
        )
        self.play(
            MoveToTarget(right_area)
        )
        self.wait(2)

        # Put rects back together
        self.combine_rects(left_rect, right_rect, height_label2, self.initial_group)

        plus_sign.move_to(
            [(left_area.get_x() + right_area.get_x())/2, left_area.get_y(), 0]
        ).scale(1.5)

        # Simplify Area
        self.add(left_area, right_area)
        self.play(
            FadeIn(plus_sign)
        )
        self.wait()
        self.play(
            ReplacementTransform(VGroup(left_area, plus_sign, right_area), final_area)
        )
        self.wait()


class DistributingRects2(FourRectScene):
    CONFIG = {
        "h1": 3,
        "h2": 1,
        "w1": 4,
        "w2": 2
    }
    def construct(self):
        area_label = TexMobject("(", self.w1, "+", self.w2, ")", "(", self.h1, "+", self.h2, ")").scale(2)
        area_label_simplified = TexMobject("(", self.w1+self.w2, ")", "(", self.h1+self.h2, ")").scale(2)
        plus_sign = TexMobject("+")
        final_area = TexMobject((self.w1+self.w2) * (self.h1+self.h2)).scale(2)

        self.introduce_initial_rect()
        
        self.play(
            Write(area_label)
        )
        #self.wait()

        """
        self.play(
            Transform(area_label, area_label_simplified),
            rate_func=there_and_back_with_pause,
            run_time=2
        )
        self.wait()
        """

        self.play(
            area_label.to_edge, UP
        )

        self.split_rects(self.initial_group, area_label=area_label)

        area_labels = self.split_rect_group[4:8]
        area_label_group = VGroup()

        for index, label in enumerate(area_labels):
            self.play(
                MoveToTarget(label)
            )
            area_label_group.add(label)
            if not index == 3:
                area_label_group.add(plus_sign.copy())
        #self.wait()
        
        self.combine_rects(self.initial_group, self.split_rect_group)

        # Simplify Area
        for label in area_labels:
            label.clear_updaters()
        self.play(
            area_label_group.arrange, RIGHT, {"buff": MED_SMALL_BUFF}
        )
        #self.wait()

        self.play(
            ReplacementTransform(area_label_group, final_area)
        )
        self.wait()
        

class FactoringVsDistributing(TwoRectScene):
    CONFIG = {
        "height1": 4,
        "width1": 2,
        "width2": 3
    }
    def construct(self):
        distributing_title = TextMobject("Distributing").scale(1.5).to_edge(UP)
        factoring_title = TextMobject("Factoring").scale(1.5).to_edge(UP)

        expression = TexMobject(self.height1, "(", self.width1, "+", self.width2, ")").scale(1.5)
        expression2 = TexMobject(self.height1, "(", self.width1, ")", "+", self.height1, "(", self.width2, ")").scale(1.5)
        arrow = Arrow(color=YELLOW)
        arrow.set_length(2.5)

        expression_group = VGroup(expression, arrow, expression2)
        expression_group.arrange(RIGHT)
        expression_group.next_to(distributing_title, direction=DOWN)

        expression_group2 = expression_group.copy()
        expression_group2.arrange(LEFT)
        expression_group2.move_to(expression_group)

        # PLAY COMMANDS
        self.add(distributing_title)
        self.introduce_initial_rect(animate=False)
        initial_rect, height_label, width_label = [*self.initial_group]
        for obj in self.initial_group:
            obj.shift(DOWN*0.7)
            self.add(obj)
        initial_rect_label = expression.copy().move_to(initial_rect)
        
        self.play(
            Write(expression)
        )
        self.play(
            Write(arrow)
        )
        self.split_rects(self.initial_group, area_label=expression)
        left_rect, left_area, right_rect, right_area, height_label2 = self.split_rect_group
        self.remove(left_area, right_area)
        self.add(left_area, right_area)

        self.play(
            Write(expression2)
        )
        self.wait(2)

        self.play(
            Transform(distributing_title, factoring_title),
        )
        self.play(
            ReplacementTransform(expression_group, expression_group2, path_arc=TAU/4)
        )
        self.wait()

        self.combine_rects(left_rect, right_rect, height_label2, self.initial_group)
        self.play(
            ReplacementTransform(VGroup(left_area, right_area), initial_rect_label)
        )
        self.wait()


class HowToFactor(TwoRectScene, FactoringAndDistributingScene):
    CONFIG = {
        "height1": 4,
        "width1": 2,
        "width2": 3
    }
    def construct(self):
        # Expressions
        expression = TexMobject(self.height1, "(", self.width1, ")", "+", self.height1, "(", self.width2, ")")
        expression.scale(2).to_edge(UP)
        expression2 = TexMobject(self.height1, "(", self.width1, "+", self.width2, ")")
        expression2.scale(2).to_edge(UP)
        expression2[0].set_color(RED)

        common_factor = TextMobject("Common Factor")
        common_factor.scale(2)
        common_factor.set_color(YELLOW)

        arrow1 = Arrow(
            common_factor.get_top(), expression[0].get_bottom(), color=YELLOW
        )
        arrow2 = Arrow(
            common_factor.get_top(), expression[5].get_bottom(), color=YELLOW
        )

        # PLAY COMMANDS
        self.introduce_initial_rect(animate=False)
        initial_rect, height_label, width_label = [*self.initial_group]

        # Common Factor
        self.add(expression)
        self.play(
            Write(common_factor)
        )
        self.wait()

        self.play(
            expression[0].set_color, RED,
            expression[5].set_color, RED
        )
        self.play(
            ShowCreationThenFadeOut(arrow1),
            ShowCreationThenFadeOut(arrow2),
        )
        self.wait()
        
        # Rects
        self.play(
            FadeOut(common_factor)
        )
        self.split_rects(self.initial_group, animate=False)
        self.play(
            *[FadeIn(obj)
            for obj in self.split_rect_group],
            FadeIn(width_label[0]),
            FadeIn(width_label[2]),
            FadeIn(height_label)
        )
        self.wait()

        left_rect, left_area, right_rect, right_area, height_label2 = [*self.split_rect_group]

        self.play(
            Indicate(height_label, scale_factor=1.8),
            Indicate(height_label2, scale_factor=1.8)
        )
        self.wait()

        height_label_copy = height_label.copy()
        height_label_copy.generate_target()
        height_label_copy.target = expression[5]

        height_label2_copy = height_label2.copy()
        height_label2_copy.generate_target()
        height_label2_copy.target = expression[0]

        # Transform Expression
        self.play(
            MoveToTarget(height_label_copy),
            MoveToTarget(height_label2_copy)
        )
        self.remove(height_label_copy, height_label2_copy)
        self.wait()

        self.factor(expression, expression2)
        
        expression2_copy = expression2.copy().move_to(ORIGIN)
        self.play(
            height_label.set_color, RED
        )
        self.combine_rects(left_rect, right_rect, height_label2, self.initial_group)
        self.play(
            ReplacementTransform(VGroup(left_area, right_area), expression2_copy)
        )
        self.wait()

# TODO
class HowToFactor2(FourRectScene, FactoringAndDistributingScene):
    CONFIG = {
        "h1": 3,
        "h2": 1,
        "w1": 4,
        "w2": 2
    }
    def construct(self):
        # Expressions and Focus Rect
        expression = TexMobject(self.w1, "(", self.h1, ")", "+", self.w1, "(", self.h2, ")", "+", self.w2, "(", self.h1, ")", "+", self.w2, "(", self.h2, ")")
        expression.scale(2).to_edge(UP)

        expression2 = TexMobject(self.w1, "(", self.h1, "+", self.h2, ")", "+", self.w2, "(", self.h1, "+", self.h2, ")")
        expression2.scale(2).to_edge(UP)

        expression3 = TexMobject("(", "{}+{}".format(self.h1, self.h2), ")", "(", self.w1, "+", self.w2, ")")
        expression3.scale(2)
        expression3_copy = expression3.copy()
        expression3.to_edge(UP)
        
        focus_rect = Rectangle(height=FRAME_HEIGHT, width=FRAME_WIDTH/2, fill_color=BLACK, fill_opacity=0.75, stroke_width=0)
        focus_rect.shift(RIGHT*(0.5 + FRAME_WIDTH/4))

        # PLAY COMMANDS
        self.add(expression)
        self.wait()
        
        self.introduce_initial_rect(animate=False)
        initial_rect, height_label, width_label = [*self.initial_group]
        self.split_rects(self.initial_group, animate=False)
        ul_rect, dl_rect, ur_rect, dr_rect, ul_area, dl_area, ur_area, dr_area, height_label2, width_label2 = [*self.split_rect_group]
        self.play(
            *[
            FadeIn(shape)
            for shape in self.split_rect_group[:-2]
            ],
            FadeIn(height_label[::2]),
            FadeIn(width_label[::2]),
            FadeIn(height_label2[::2]),
            FadeIn(width_label2[::2])
        )
        self.wait()

        self.play(
            FadeIn(focus_rect)
        )
        self.wait()
        # TODO

        width_label_copy = width_label.copy()
        width_label2_copy = width_label2.copy()

        height_label2[1].add_updater(
            lambda p: 
                p.set_x(
                    (height_label2[0].get_x() + height_label2[2].get_x())/2)
                .set_y(
                        (height_label2[0].get_y() + height_label2[2].get_y())/2
                    )
        )

        # Transform Expression
        self.play(
            expression[1:4].set_color, ORANGE,
            expression[6:9].set_color, BLUE
        )
        self.play(
            Indicate(width_label[0], scale_factor=1.8),
            Indicate(width_label2[0], scale_factor=1.8)
        )
        self.play(
            Transform(width_label_copy[0], expression[5]),
            Transform(width_label2_copy[0], expression[0])
        )
        self.remove(width_label_copy[0], width_label2_copy[0])
        self.wait()

        self.factor(expression, expression2, common_color=PURPLE)
        self.play(
            FadeOut(width_label2[0]),
            FadeIn(height_label2[1]),
            dl_rect.shift, UP,
            dl_area.shift, UP
        )
        # Left Group
        left_block = Rectangle(height=self.h1+self.h2, width=self.w1, color=PURPLE, fill_opacity=0.8)
        left_block.move_to(VGroup(ul_rect, dl_rect))
        left_block_area = TexMobject(self.w1, "(", self.h1, "+", self.h2, ")")
        left_block_area.move_to(left_block)

        # PLAY COMMANDS
        self.play(
            FadeOut(VGroup(ul_rect, dl_rect)),
            FadeIn(left_block),
            ReplacementTransform(VGroup(ul_area, dl_area), left_block_area)
        )
        self.remove(focus_rect)
        self.add(focus_rect)
        self.wait()

        self.play(
            focus_rect.move_to, LEFT*FRAME_WIDTH/4 + 0.5*RIGHT
        )
        self.wait()

        self.play(
            expression[11:14].set_color, GREEN,
            expression[16:19].set_color, YELLOW
        )
        self.play(
            Indicate(width_label[2], scale_factor=1.8),
            Indicate(width_label2[2], scale_factor=1.8)
        )
        self.play(
            Transform(width_label2_copy[2], expression[10]),
            Transform(width_label_copy[2], expression[15])
        )
        self.remove(width_label_copy[2], width_label2_copy[2])
        self.wait()

        self.factor(expression[10:], expression2[7:])
        self.remove(expression)
        self.play(
            FadeOut(width_label2[2]),
            FadeIn(height_label[1]),
            dr_rect.shift, UP,
            dr_area.shift, UP
        )
        # Right Group
        right_block = Rectangle(height=self.h1+self.h2, width=self.w2, color=RED, fill_opacity=0.8)
        right_block.move_to(VGroup(ur_rect, dr_rect))
        right_block_area = TexMobject(self.w2, "(", self.h1, "+", self.h2, ")")
        right_block_area.move_to(right_block)

        # PLAY COMMANDS
        self.play(
            FadeOut(VGroup(ur_rect, dr_rect)),
            FadeIn(right_block),
            ReplacementTransform(VGroup(ur_area, dr_area), right_block_area)
        )
        self.wait()
        
        self.play(
            FadeOut(focus_rect)
        )
        self.wait(2)

        self.play(
            ShowPassingFlashAround(expression2[1:6]),
            ShowPassingFlashAround(expression2[8:]),
            expression2[1:6].set_color, BLUE,
            expression2[8:].set_color, BLUE
        )
        self.wait()

        self.play(
            Indicate(height_label),
            Indicate(height_label2)
        )
        height_label_copy = height_label.copy()
        height_label2_copy = height_label2.copy()
        expression2_copy = TexMobject(self.w1, "(", "{}+{}".format(self.h1, self.h2), ")", "+", self.w2,"(", "{}+{}".format(self.h1, self.h2), ")")
        expression2_copy.scale(2).to_edge(UP)
        expression2_copy[1:4].set_color(BLUE)
        expression2_copy[6:].set_color(BLUE)

        # TODO wtf
        self.remove(height_label2[1])
        self.add(height_label2[1])
        self.play(
            Transform(height_label2_copy, expression2[1:6]),
            Transform(height_label_copy, expression2[8:])
        )
        self.remove(height_label2_copy, height_label_copy)
        for i in expression:
            self.remove(i)
        for i in expression2:
            self.remove(i)
        self.add(expression2_copy)
        self.wait()

        self.factor(expression2_copy, expression3, common_color=BLUE, common_factor_on_left=False)

        height_label.clear_updaters()
        height_label2.clear_updaters()
        width_label.clear_updaters()
        width_label2.clear_updaters()

        height_y = height_label.get_y()
        height2_y = height_label2.get_y()

        height_label2.add_updater(lambda p: p.next_to(left_block).set_y(height2_y))
        height_label.add_updater(lambda p: p.next_to(right_block).set_y(height_y))
        width_label[0].add_updater(lambda p: p.next_to(left_block, direction=DOWN))
        width_label[2].add_updater(lambda p: p.next_to(right_block, direction=DOWN))
        width_label[1].add_updater(
            lambda p: 
                p.set_x(
                    (width_label[0].get_x() + width_label[2].get_x())/2
                )
                .set_y(
                    (width_label[0].get_y() + width_label[2].get_y())/2
                )
        )

        self.remove(height_label2)
        self.add(height_label2)
        self.play(
            FadeIn(width_label[1]),
            left_block.shift, RIGHT,
            right_block.shift, LEFT
        ) 
        self.play(
            ReplacementTransform(height_label2, height_label, path_arc=PI),
            ReplacementTransform(VGroup(left_block_area, right_block_area), expression3_copy),
            FadeOut(left_block),
            FadeOut(right_block),
            FadeIn(initial_rect)
        )
        self.wait()

        



