from manimlib.imports import *
import os
import pyclbr

class tempfont(Scene):
    def construct(self):
        txt=Paragraph("12123123123",font="宋体")
        txt1=Paragraph("qqqqqqqqqq",font="宋体")

        self.add(txt,txt1)


# 运行在3.7下 运行方式如下：而不是直接运行
# 在anaconda 命令行中运行
# python -m manim example_scenes.py SquareToCircle -pl
class AllShapes(Scene):
    def construct(self):
        # 圆形
        circle = Circle()
        circle.move_to(6*LEFT+3*UP)
        #圆环
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.move_to(4*LEFT+3*UP)

        # 正方形
        square = Square()
        square.move_to(2*LEFT+3*UP)
        #矩形
        rectangle=Rectangle(height=1.5,width=2.5)
        rectangle.move_to(3*RIGHT+2.5*UP)
        #圆角矩形
        roundrectangle=RoundedRectangle(height=1,width=2)
        roundrectangle.move_to(3.5*RIGHT+2*UP)
         #椭圆
        ellipse=Ellipse(width=2, height=1, color=RED)
        ellipse.shift(2*LEFT+UP)

        # 多边形
        triangle=Polygon(np.array([-5,2,0]),np.array([-5,1,0]),np.array([-4,1,0]))
        #正多边形
        regular=RegularPolygon(start_angle=0)
        regular.move_to(RIGHT+DOWN)
        #只有箭头，没有箭杆
        arrowtip=ArrowTip()
        arrowtip.move_to(RIGHT+2*DOWN)

        #线段
        line=Line(np.array([-3,3.5,0]),np.array([-2,3.5,0]))
        #点划线
        dashline=DashedLine(np.array([-3,3,0]),np.array([-2,3,0]))       
        #直线箭头
        arrow = Arrow(np.array([-4,3.5,0]),np.array([-3,2,0]))
        arrow.move_to(LEFT+UP)
        #箭头，向量
        vect=Vector()
        vect.move_to(RIGHT+2*DOWN)
        #双箭头
        doublearrow=DoubleArrow(np.array([-3,3,0]),np.array([-1,4,0]))
        doublearrow.move_to(LEFT,DOWN)
        #圆弧箭头
        pointer = CurvedArrow(2*LEFT,3*UP,color=MAROON_C)
        pointer.move_to(RIGHT+3*UP)

        #点
        dot=Dot()
        dot.move_to(DOWN+LEFT)
        #小点
        smalldot=SmallDot()
        smalldot.move_to(2*DOWN+LEFT)

        #圆弧，默认四分之一
        arc=Arc(radius=1,start_angle=0,num_components=4,angle=TAU/2)
        arc.move_to(UP+3*RIGHT)
        #扇形（包括中心）
        sector=Sector()
        sector.move_to(DOWN+RIGHT)
        #扇形区域
        annular=AnnularSector(angle=TAU/2)
        annular.move_to(UP+5*RIGHT)
        #两点之间的圆弧
        arcb=ArcBetweenPoints(ORIGIN,UP,TAU / 6)
        arcb.move_to(DOWN+5*RIGHT)
        #带箭头的圆弧
        curarrow=CurvedArrow(start_point=5 * RIGHT, end_point=2 * RIGHT, color=MAROON_C)
        curarrow.move_to(DOWN+4*RIGHT)
        #双向箭头
        curdouarrow=CurvedDoubleArrow(start_point= RIGHT, end_point=3 * UP, color=MAROON_C)
        curdouarrow.move_to(DOWN+3*RIGHT)

        self.play(ShowCreation(arc))
        self.play(ShowCreation(annular))
        self.play(ShowCreation(sector))
        self.play(ShowCreation(arcb))
        self.play(ShowCreation(curarrow))
        self.play(ShowCreation(curdouarrow))
        # self.play(ShowCreation(cub))
        self.play(ShowCreation(circle))
        self.play(FadeIn(ring))
        self.play(GrowFromCenter(square))
        self.play(ShowCreation(line))
        self.play(ShowCreation(dashline))
        self.play(ShowCreation(ellipse))
        self.play(FadeIn(arrow))
        self.play(FadeIn(doublearrow))        
        self.play(FadeIn(pointer))
        self.play(FadeIn(triangle))
        self.play(FadeIn(rectangle))
        self.play(FadeIn(roundrectangle))
        self.play(FadeIn(dot))
        self.play(FadeIn(smalldot))
        self.play(FadeIn(regular))
        self.play(FadeIn(arrowtip))        
        self.play(FadeIn(vect))        

class Shapes(Scene):
    #A few simple shapes
    #Python 2.7 version runs in Python 3.7 without changes
    def construct(self):
        circle = Circle()
        square = Square()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))
        self.add(line)

class MoreShapes(Scene):
    #A few more simple shapes
    #2.7 version runs in 3.7 without any changes
    #Note: I fixed my 'play command not found' issue by installing sox
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse=Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

class MovingShapes(Scene):
    #Show the difference between .shift() and .move_to
    def construct(self):
        circle=Circle(color=TEAL_A)
        circle.move_to(LEFT)
        square=Circle()
        square.move_to(LEFT+3*DOWN)

        self.play(GrowFromCenter(circle), GrowFromCenter(square), rate=5)
        self.play(ApplyMethod(circle.move_to,RIGHT), ApplyMethod(square.shift,RIGHT))
        self.play(ApplyMethod(circle.move_to,RIGHT+UP), ApplyMethod(square.shift,RIGHT+UP))
        self.play(ApplyMethod(circle.move_to,LEFT+UP), ApplyMethod(square.shift,LEFT+UP))

class FadingEffection(Scene):
    #A few more simple shapes
    #2.7 version runs in 3.7 without any changes
    #Note: I fixed my 'play command not found' issue by installing sox
    def construct(self):
        
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.move_to(6*LEFT+3*UP)
        
        ring1=Annulus(inner_radius=.5, outer_radius=1, color=RED)
        ring1.move_to(4*LEFT+3*UP)

        ring2=Annulus(inner_radius=.5, outer_radius=1, color=RED)
        ring2.move_to(2*LEFT+3*UP)
        #圆形
        #淡入效果
        self.play(FadeIn(ring))
        # 淡入效果
        self.play(FadeInFrom(ring2,direction=RIGHT))
        #淡入效果（默认从底部移动上来）
        self.play(FadeInFromDown(ring))
        #从指定位置淡入
        self.play(FadeInFromPoint(ring,point=5*LEFT+2*UP))
        #从大到小淡入
        self.play(FadeInFromLarge(ring1))
        
        #淡出效果
        self.play(FadeOut(ring))
        #淡出效果（默认向下淡出）
        self.play(FadeOutAndShift(ring))
        self.play(FadeOutAndShiftDown(ring))        
        #向右淡出
        self.play(FadeOutAndShift(ring,direction=RIGHT))

class TransFormEffection(Scene):
    def construct(self):

        circle = Circle()
        circle.move_to(LEFT+UP)

        circle2 = Circle()
        circle2.move_to(2*RIGHT+2*DOWN)

        circle3 = Circle()
        circle3.move_to(4*RIGHT+4*DOWN)

        circle4 = Circle()
        circle4.move_to(1*RIGHT+2*DOWN)
        # 正方形
        square = Square()
        square.move_to(2*LEFT+3*UP)
        #圆环
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.move_to(4*LEFT+3*UP)
        
        self.play(ShowCreation(square))     
        #两个形状转换（形状和位置）
        self.play(Transform(square,circle))
        # 转换之后，还是要引用原来的形状！！
        self.play(Transform(square,ring))
        
        #转换且替换
        self.play(ReplacementTransform(square,circle))
        #这样转后用，引用转换后的形状
        # self.play(Transform(circle,ring))
        #转换并保留原来的形状
        self.play(TransformFromCopy(circle,circle2))
        # 转换后可以分别引用
        # self.play(FadeOut(circle))
        # self.play(FadeOut(circle2))

        #圆弧走位并转换
        self.play(ClockwiseTransform(circle2,circle3))
        #
        self.play(CounterclockwiseTransform(circle3,circle4))

        A = TextMobject("Text-A").to_edge(LEFT)
        A.generate_target()  # copyA自身形成A的target属性
        A.target.scale(3).shift(RIGHT*7+UP*2) # 操作A的target

        self.add(A)
        self.wait()
        # self.play(MoveToTarget(A))
        # self.wait()
        # 等于self.play(MoveToTarget(A))的效果
        # self.play(
        #     A.scale, 3,
        #     A.shift, RIGHT*7+UP*2,
        # )
        #等同于self.play(MoveToTarget(A))的效果ok
        # self.play(ScaleInPlace(A,3))
        #  self.play(FadeToColor(A,color=RED))
        #ApplyMethod 的时候，只能执行最后面一步ok
        # self.play(ApplyMethod(A.scale, 3))
        # self.play(ApplyMethod(A.shift, RIGHT*7+UP*2))
        # 这样不行，只能执行最后一个ApplyMethod
        self.play(ApplyMethod(A.scale, 3),ApplyMethod(A.shift, RIGHT*7+UP*2))
        
        #操作后还可以操作A
        self.play(FadeOut(A))

        mobjects = VGroup(
                Square(),
                RegularPolygon(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.play(
            #转换成一个点
            *[ShrinkToCenter(mob) for mob in mobjects]
        )
        
class TransFormEffection2(Scene):
    def construct(self):
        A = TextMobject("Text-A").to_edge(LEFT)        
        B = TextMobject("Text-B").scale(3)
        # 需要return一个mobject
        def function1(mob):
            return mob.scale(3).shift(RIGHT*7+UP*2)
        mat = np.array([
            [1, 3, 1],
            [0.5, 1, 1],
            [1, 1, 1]
        ])
        A.save_state()  # 记录下现在状态，restore会回到此时
        A.scale(3).shift(RIGHT*7+UP*2)
        # A.save_state()  # 如果多次保存状态，仅仅保留最后一次的内容
        #这儿添加的是放大后的
        VGroup(A, B).arrange(RIGHT)
        self.add(A,B)
        self.wait()
        #转换到保存的一个点
        self.play(Restore(A))
        # 针对物体执行一个函数
        self.play(ApplyFunction(function1, A))
        self.play(ApplyMatrix(mat, A))   
        #交换位置     
        self.play(CyclicReplace(A, B)) # 或Swap(A, B)
        self.wait()

        # self.add(A, B)
        # self.wait()
        # self.wait()

class CreationEffection(Scene):
    def construct(self):
        A = TextMobject("Text-A").to_edge(LEFT)  
        circle = Circle()
        circle.move_to(LEFT+UP)
        #显示出来，文本从左到右显示
        self.play(ShowCreation(A)) 
        #圆形逆时针从0度显示出来 
        self.play(ShowCreation(circle))  
        #隐藏与ShowCreation顺序相反
        self.play(Uncreate(A))  

        vmobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        vmobjects.scale(1.5)
        vmobjects.arrange_submobjects(RIGHT,buff=2)
        #画边界，然后填充的效果
        # self.play(
        #     *[DrawBorderThenFill(mob) for mob in vmobjects]
        # )
        #同DrawBorderThenFill基本无差别
        self.play(
            *[Write(mob) for mob in vmobjects]
        )
        text = TextMobject("ShowIncreasingSubsets")
        text.set_width(11)
        text.move_to(DOWN)
        text1 = TextMobject("ShowIncreasingSubsets")
        text1.set_width(11)
        text1.move_to(3*DOWN)
        self.wait()
        self.play(ShowIncreasingSubsets(text[0], run_time=4))
        #一个字符一个字符的显示
        self.play(ShowSubmobjectsOneByOne(text1[0], run_time=4))

class GrouingEffection(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("wingspread").scale(2)
            )
        mobjects.arrange_submobjects(RIGHT,buff=2)
        directions=[UP,LEFT,DOWN,RIGHT]
        # for direction in directions:
        #     self.play(
        #         *[GrowFromPoint(mob,mob.get_center()+direction*3) for mob in mobjects]
        #     )
        self.play(
            #从中间出来
            *[GrowFromCenter(mob) for mob in mobjects]
        )    
        # for direction in directions:
        #     self.play(
        #         #从形状实际的边缘出来
        #         *[GrowFromEdge(mob,direction) for mob in mobjects]
        #     )

        self.play(
            #同GrowFromCenter区别不大，文字是宣传出来的
            *[SpinInFromNothing(mob) for mob in mobjects]
        )

        mobjects1 = VGroup(
                Arrow(LEFT,RIGHT),
                Vector(RIGHT*2)
            )
        mobjects1.scale(3)
        mobjects1.arrange_submobjects(DOWN,buff=2)
        self.play(
            #专门用于箭头
            *[GrowArrow(mob)for mob in mobjects1]
        )


        self.wait() 

#提示信息(重点)        
class IndicationEffection(Scene):
    def construct(self):
        mobjects = VGroup(
            Dot(),
            Circle(fill_opacity=1),
            TexMobject("wignspredasdadfasd")
        )
        mobjects.arrange_submobjects(RIGHT,buff=2)
        mobject_or_coord = [
            *mobjects,                    # Mobjects: Dot and "x"
            mobjects.get_right()+RIGHT*2  # Coord
        ]
        txt=TexMobject("wignspredasdadfasd")
        circle1=Circle(fill_opacity=1)
        txt.move_to(2*DOWN)
        colors=[GRAY,RED,BLUE]

        self.add(mobjects)
        # for obj,color in zip(mobject_or_coord,colors):
        #     self.play(FocusOn(obj,color=color))

        # for obj,color in zip(mobject_or_coord,colors):
        #     #flash 闪光效果（专用于圆点，字符等体积小的形状）
        #     self.play(Flash(obj,color=color,flash_radius=0.5))

        for obj in mobjects:
            #圆形提示，无-显示-放大-缩小-消失
            self.play(CircleIndicate(obj))

        # self.play(ShowCreation(circle1))
        # # 圆形从大到小，缩小到形状上
        # self.play(FocusOn(circle1,color=RED))
        # #形状变大在缩小
        self.play(Indicate(txt))
        self.wait(0.3)
        # 点绕一圈
        self.play(ShowPassingFlashAround(txt))
        self.wait(0.3)
        # 消失
        self.play(ShowPassingFlash(txt))

        # self.play(Flash(mobjects))


        self.wait(0.3)

#提示信息(重点)        
class ShowCreationEffection(Scene):
    def construct(self):
        mobjects = VGroup(
                Circle(),
                Circle(fill_opacity=1),
                TextMobject("Text").scale(2)
            )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        # self.play(
        #     #出来之后就销毁
        #     *[ShowCreationThenDestruction(mob) for mob in mobjects]
        # )
        # self.play(
        #     #出来之后淡出
        #     *[ShowCreationThenFadeOut(mob) for mob in mobjects]
        # )
        self.add(mobjects)
        self.play(
             #类似反转效果
            *[TurnInsideOut(mob) for mob in mobjects]
        )
        self.play(
            #放大再缩小
            *[WiggleOutThenIn(mob) for mob in mobjects]
        )
        self.play(
            #波动效果
            *[ApplyWave(mob) for mob in mobjects]
        )
        self.play(
            #出来围绕的矩形后，淡出
            *[ShowCreationThenFadeAround(mob) for mob in mobjects]
        )
        # self.play(
        #     #显示出来之后，围绕形状，线段走一圈
        #     *[ShowPassingFlashAround(mob) for mob in mobjects]
        #     # 比上者好像线段长点
        #     *[ShowCreationThenDestructionAround(mob) for mob in mobjects]
        # )


        self.wait(0.3)
        
#移动效果      
class MoveEffection(Scene):
    def construct(self):
        def plane_wave_homotopy(x, y, z, t):
            norm = get_norm([x, y])
            tau = interpolate(5, -5, t) + norm/FRAME_X_RADIUS
            alpha = sigmoid(tau)
            return [x, y + 0.5*np.sin(2*np.pi*alpha)-t*SMALL_BUFF/2, z]

        mobjects=VGroup(
            TextMobject("wingspread").scale(3),
            Square(),
        ).arrange_submobjects(RIGHT,buff=2)
        mobjects.move_to(3*UP)

        self.add(mobjects)
        self.play(
            #波动效果
            *[Homotopy(
                plane_wave_homotopy,
                mob
            ) for mob in mobjects]
        )
        self.wait(0.3)
        text1=TextMobject("lashen Effection").scale(3)
        text1.move_to(DOWN)
        self.play(ShowCreation(text1))
        self.wait(1)
        self.play(FadeOut(text1))

        def func(t):
            return t*0.5*RIGHT
        mobjects=VGroup(
            TextMobject("Text").scale(3),
            Square(),
        ).arrange_submobjects(RIGHT,buff=2)

        self.play(
            #拉伸
            *[PhaseFlow(
                func, mob,
                run_time = 2,
            )for mob in mobjects]
        )
        text1=TextMobject("Move with path").scale(3)
        text1.move_to(DOWN)
        self.play(ShowCreation(text1))
        self.wait(1)
        self.play(FadeOut(text1))
        # 路径移动
        line=Line(ORIGIN,RIGHT*FRAME_WIDTH,buff=1)
        line.move_to(ORIGIN)
        dot=Dot()
        dot.move_to(line.get_start())

        self.add(line,dot)
        self.play(
            #延路径移动
            MoveAlongPath(dot,line)
        )

#数字变换效果   
class NumberEffection(Scene):
    def construct(self):
        number = DecimalNumber(0).scale(2)
        number.move_to(UP)
        number1 = DecimalNumber(0).scale(2)
        number1.move_to(DOWN)

        def update_func(t):
            return t * 1 #控制每秒运行的数量 1=>1  10=>10(最终数字)
        self.add(number)
        self.add(number1)
        self.wait()
        #从指定数字到.runtime
        self.play(ChangingDecimal(number, update_func), run_time=10)
        #从指定数字到指定数字（指定运行时间）
        self.play(ChangeDecimalToValue(number1, 30), run_time=2)
        self.wait()

#旋转效果
class RotatingEffection(Scene):
    def construct(self):
        square=Square()
        self.add(square)
        self.play(
            #逆时针旋转
            Rotating(
                square,
                radians=PI/2, #总共旋转的角度
                run_time=2    #旋转的总秒数，越大越慢
            )
        )
        self.wait(0.3)
        self.play(
            #内外旋转
            Rotating(
                square,
                radians=PI,
                run_time=1,
                axis=RIGHT
            )
        )
        #不建议使用，不如上边平滑
        # self.play(
        #     Rotate(
        #         square,
        #         PI/4,
        #         run_time=2
        #     )
        # )
        # self.wait(0.3)
        # self.play(
        #     Rotate(
        #         square,
        #         PI,
        #         run_time=2,
        #         axis=RIGHT
        #     )
        # )
        self.wait(0.3)

# 更新效果
class UpdateEffection(Scene):
    def construct(self):
        square = Square().to_edge(UP)
        mobject = TextMobject("Text").scale(2).next_to(square, RIGHT)
        #保持再squart的右边，这样不用建立group，单独控制即可
        def update_func(mob):
            mob.next_to(square, RIGHT)
        #传入的函数含有参数alpha，表示动画完成度(0~1之间)
        def update_func1(mob, alpha):
            mob.next_to(square, RIGHT, buff=0.05 + alpha)

        self.add(square, mobject)
        self.wait()
        self.play(
            square.to_edge, DOWN,
            #按照函数要求单独控制
            UpdateFromFunc(mobject, update_func)
        )
        self.play(
            square.to_edge, LEFT,
            #同时控制alpha通道
            UpdateFromAlphaFunc(mobject, update_func1)
        )
        self.play(
            square.to_edge, RIGHT,
            #保持相对位置
            MaintainPositionRelativeTo(mobject, square)
        )
        self.wait()

# 组件组合效果
# 1.针对group中的同时执行
# 2.组中的依次执行
# 3.依次执行有一定的延迟
# 4.同时执行，按照传入的动作类型（跟1 差不多）
class ComponnentEffection(Scene):
    def construct(self):
        cir=Circle()
        mobjects = VGroup(
            cir,
            Circle(fill_opacity=1),
            TextMobject("Text").scale(2)
        )
        mobjects.scale(1.5)
        mobjects.arrange_submobjects(RIGHT,buff=2)

        self.wait()
        #组成一个系列同时执行
        anims = AnimationGroup(
            *[GrowFromCenter(mob) for mob in mobjects]
        )
        self.play(anims)
        #Growup中的依次执行
        anims = Succession(
            *[ApplyMethod(mob.shift, DOWN) for mob in mobjects]
        )
        #下一个动画延迟上一个动画执行5%的时候执行
        anims = LaggedStart(
            *[ApplyMethod(mob.shift, DOWN) for mob in mobjects]
        )
        #根据传入的动作执行动画，本例为淡出
        anims = LaggedStartMap(
            FadeOut, mobjects
        )
        self.play(anims)
        #group后仍可以单独操作形状
        # cir.shift(UP+LEFT)
        self.wait()


#文字效果Demo
class TextEffection(Scene):
    def construct(self):
        # #gradient: set color trans
        # text = Text('Hello, world!',gradient=(BLUE, GREEN), font='Arial Black',slant=ITALIC)
        # #\t equals 4 spavce
        # #t2g: set part of string gradient
        # #t2f:set part of string font
        # #t2c:set part of string color
        # #t2s:set part of string Italic
        # #t2w:set part of string Bold
        # text1 = Text('Hello,\tworld! world,world ',
        #     t2g={'world':(BLUE, GREEN)},
        #     t2f={'[1:4]':'Arial Black'},
        #     t2c={'hello':BLUE},
        #     t2s={'[1:3]':ITALIC},
        #     t2w={'world':BOLD})
        # text1.next_to(text,DOWN)
        # #t2c:search and set style ,but not for word,eg:world1 only set color world
        # text2 = Text('Hello,\tworld! world1 is best!',color=GREEN,t2c={'hello':BLUE})
        # text2.next_to(text1,DOWN)
        
        # text3 = Text('Hello,world is best!',color=GREEN,t2c={'[1:4]':YELLOW})
        # text3.next_to(text2,DOWN)
        # self.play(Write(text))
        # self.play(Write(text1))
        # self.play(Write(text2))
        # self.play(Write(text3))

        # textg = Text(
        #     'Googl,你好！',
        #     t2c={
        #         '[:1]':'#3174f0', '[1:2]':'#e53125',
        #         '[2:3]':'#fbb003', '[3:4]':'#3174f0',
        #         '[4:5]':'#269a43', '[5:]':'#e53125',
        #     })
        # textg.next_to(text3)
        # self.play(Write(textg))

        t = Paragraph(
            'this is a awesome',
            'paragraph',
            'With \nNewlines',
            '\tWith Tabs',
            '  With Spaces',
            'With Alignments',
            'center', "left", "right",
            line_spacing=0.1,
            alignment="left",
            t2c={"Tabs": RED}
        )
        # t.set_alignment("center", 7)
        # t.set_alignment("left", 8)
        # t.set_alignment("right", 9)
        # t[0][5].set_color(GREEN)
        # t[0][6].set_color(GREEN)
        # t[1][0:4].set_color(YELLOW)
        # rect = SurroundingRectangle(t)
        # self.add(t,rect)

        self.add(t)
        self.play(t.shift, RIGHT)
        rect = SurroundingRectangle(t)
        self.add(rect)
        self.play(t.set_alignment, "right", 9)
        self.play(t.set_all_lines_alignment, "center")
        self.wait()

class Test_camera(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cube_yellow = Cube(fill_color=YELLOW, stroke_width=2, stroke_color=WHITE)
        sphere_blue = Sphere(fill_color=BLUE, checkerboard_colors=None).shift(OUT * 2)
        cube_green = Cube(fill_color=GREEN).scale([2, 0.5, 0.5]).shift(RIGHT * 3.25)

        phi_0, theta_0 = 0, 0 # 起始角度
        phi, theta = 60 * DEGREES, -120 * DEGREES # 目标角度

        self.set_camera_orientation(phi=phi_0, theta=theta_0)
        self.add(axes, cube_yellow, sphere_blue, cube_green)
        self.wait()
        dt = 1/15
        delta_phi, delta_theta = (phi - phi_0) / 30, (theta - theta_0) / 60
        for i in range(30):
            phi_0 += delta_phi
            self.set_camera_orientation(phi=phi_0, theta=theta_0)
            self.wait(dt)
        for i in range(60):
            theta_0 += delta_theta
            self.set_camera_orientation(phi=phi_0, theta=theta_0)
            self.wait(dt)
        self.wait(2)

class Curve_3D_test(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        axes = ThreeDAxes()
        r = 2 # radius
        w = 4
        circle = ParametricFunction(lambda t: r * complex_to_R3(np.exp(1j * w * t)),
                                    t_min=0, t_max=TAU * 1.5, color=RED, stroke_width=8)
        spiral_line = ParametricFunction(lambda t: r * complex_to_R3(np.exp(1j * w * t)) + OUT * t,
                                    t_min=0, t_max=TAU * 1.5, color=PINK, stroke_width=8)
        circle.shift(IN * 2.5), spiral_line.shift(IN * 2.5)

        self.add(axes, circle)
        self.wait()
        self.play(TransformFromCopy(circle, spiral_line, rate_func=there_and_back), run_time=4)
        self.wait(2)

class Surface_test_01(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        axes = self.get_axes()
        # create surface: z = sin(x ^ 2 + y ^ 2)
        surface = ParametricSurface(lambda u, v: np.array([u, v, np.sin(u ** 2 + v ** 2)]),
                                    u_min=-4, u_max=4, v_min=-4, v_max=4, resolution=(120, 120))
        self.add(axes, surface)
        self.wait(5)

class Surface_test_02(SpecialThreeDScene):
    CONFIG = {
        "default_angled_camera_position": {
            "phi": 65 * DEGREES, # Angle off z axis
            "theta": -60 * DEGREES, # Rotation about z axis
            "distance": 50,
            "gamma": 0,  # Rotation about normal vector to camera
            },
        }
    def construct(self):
        self.set_camera_to_default_position()
        axes = self.get_axes()
        w = 1
        surface_01 = ParametricSurface(lambda u, v: v * complex_to_R3(np.exp(1j * w * u)),
                                       u_min=0, u_max=TAU, v_min=1, v_max=3, checkerboard_colors=None,
                                       fill_color=BLUE_B, fill_opacity=0.8, stroke_color=BLUE_A, resolution=(60, 10))
        surface_02 = ParametricSurface(lambda u, v: v * complex_to_R3(np.exp(1j * w * u)) + OUT * u/PI * 2,
                                       u_min=0, u_max=TAU, v_min=1, v_max=3, checkerboard_colors=None,
                                       fill_color=BLUE_D, fill_opacity=0.8, stroke_color=BLUE_A, resolution=(60, 10))
        self.add(axes, surface_01)
        self.wait()
        self.play(TransformFromCopy(surface_01, surface_02, rate_func=linear), run_time=5)
        self.wait(2)


# 刻度效果
class NumberLineEffection(GraphScene):
    def construct(self):
        axis=NumberLine(
            x_min=-2,
            x_max=2,
            unit_size=3,
            include_numbers=0.5,
            include_tip=False,
            label_direction=DOWN,
            color=RED,
            #刻度的高度
            tick_size=0.1,
            tick_frequency=0.5,
            include_ticks=True).shift(3*LEFT)
        axis.add_numbers(1.5,-1.5)
        #n2p point to number
        dot=Dot(axis.n2p(1))
        dot.set_fill(color=BLUE)
        #1.0
        print(axis.p2n(dot.get_center()))

        self.add(dot)
        self.play(ShowCreation(axis))
# 展示自定义函数
class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),
    }   
    def construct(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph)

        self.play(ShowCreation(func_graph))
    #展示的函数
    def func_to_graph(self,x):
        return x*x/20

# 坐标系效果展示
class AxisDemo(GraphScene):   
    def construct(self):
        self.setup_axes(animate=True)

class AxisDemo2(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 6,
        "x_axis_width": 4,  #宽度
        "x_tick_frequency": 2,
        "x_leftmost_tick": None,  # Change if different from x_min
        "x_labeled_nums": [2,4,6],
        "x_axis_label": "HH",
        "y_min": 0,
        "y_max": 6,
        "y_axis_height": 3, #高度
        "y_tick_frequency": 0.5,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": [1,2,3],
        "y_axis_label": "$x^2$",
        "axes_color": GREEN,
        "graph_origin": 3* DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "area_opacity": 0.8,
    }
    def construct(self):
        self.setup_axes(animate=False)
        fg1 = self.get_graph(self.x_2, WHITE,x_min=1,x_max=2)
        #注意两种方式基本相同
        fg2=ParametricFunction(self.x2,color=WHITE,t_min=1,t_max=2,step_size=0.01)
        self.add(fg1)
        self.add(fg2)
        self.wait()
    
    def x2(self,t):
        return self.coords_to_point(t,t**2)

    def x_2(self, t):
        return t**2+2

class AxisDemo3(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 6,
        "x_axis_width": 3,
        "y_min": 0,
        "y_max": 6,
        "y_axis_height": 3,
        }

    def x_2(self, t):
        return t**2
    def x_3(self, t):
        return t**2+3

    def construct(self):
        self.graph_origin=3*DOWN+3*LEFT
        self.axes_color=RED
        self.setup_axes(animate=True)
        fg = self.get_graph(self.x_2, WHITE,x_min=1,x_max=2)
        self.add(fg) #第一幅图完成

        self.graph_origin=ORIGIN
        self.axes_color=BLUE
        self.y_max=10
        self.setup_axes(animate=True)
        fg = self.get_graph(self.x_3, YELLOW,x_min=1,x_max=2)
        self.add(fg)#第二幅图完成

        self.wait()

class CameraDemo(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        cube = Cube(fill_color=GREEN).scale([2, 2, 2])
        cube.move_to(4*RIGHT+4*UP+3*IN)

        theta_0 = 0 # 起始角度
        theta =  -120 * DEGREES # 目标角度

        self.set_camera(ThreeDCamera(background_color=BLUE))
        #设置帧的像素宽与高 就是视频的尺寸
        self.camera.reset_pixel_shape(854,854)
        self.set_camera_orientation(60 * DEGREES, theta=theta_0)
        self.add(axes, cube)
        self.wait()
        dt = 1/15
        delta_theta = (theta - theta_0) / 60
        for i in range(60):
            theta_0 += delta_theta
            self.set_camera_orientation(theta=theta_0)
            self.wait(dt)
        self.wait(2)

class CameraDemo2(Scene):
    def construct(self):
        numberplane = NumberPlane()
        numberplane.add_coordinates()
        self.camera.set_frame_width(8)
        self.camera.resize_frame_shape()
        text = Text("frame_width=8")
        self.add(numberplane,text)
        self.wait(2)
class AddingText(Scene):
    #Adding text on the screen
    def construct(self):
        my_first_text=TextMobject("Writing with manim is fun")
        second_line=TextMobject("and easy to do!")
        second_line.next_to(my_first_text,DOWN)
        third_line=TextMobject("for me and you!")
        third_line.next_to(my_first_text,DOWN)

        self.add(my_first_text, second_line)
        self.wait(2)
        self.play(Transform(second_line,third_line))
        self.wait(2)
        second_line.shift(3*DOWN)
        self.play(ApplyMethod(my_first_text.shift,3*UP))
        ###Try uncommenting the following###
        #self.play(ApplyMethod(second_line.move_to, LEFT_SIDE-2*LEFT))
        #self.play(ApplyMethod(my_first_text.next_to,second_line))


class AddingMoreText(Scene):
    #Playing around with text properties
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)
        quote2 = TextMobject("A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)
        author=TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)

        self.add(quote)
        self.add(author)
        self.wait(2)
        self.play(
            Transform(quote,quote2),
            ApplyMethod(author.move_to,quote2.get_corner(DOWN+RIGHT)+DOWN+2*LEFT))
        self.play(ApplyMethod(author.scale,1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))

class RotateAndHighlight(Scene):
    #Rotation of text and highlighting with surrounding geometries
    def construct(self):
        square=Square(side_length=5,fill_color=YELLOW, fill_opacity=1)
        label=TextMobject("Text at an angle")
        label.bg=BackgroundRectangle(label,fill_opacity=1)
        label_group=VGroup(label.bg,label)  #Order matters
        label_group.rotate(TAU/8)
        label2=TextMobject("Boxed text",color=BLACK)
        label2.bg=SurroundingRectangle(label2,color=BLUE,fill_color=RED, fill_opacity=.5)
        label2_group=VGroup(label2,label2.bg)
        label2_group.next_to(label_group,DOWN)
        label3=TextMobject("Rainbow")
        label3.scale(2)
        label3.set_color_by_gradient(RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE)
        label3.to_edge(DOWN)

        self.add(square)
        self.play(FadeIn(label_group))
        self.play(FadeIn(label2_group))
        self.play(FadeIn(label3))

class BasicEquations(Scene):
    #A short script showing how to use Latex commands
    def construct(self):
        eq1=TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        eq2=TexMobject(r"\vec{F}_{net} = \sum_i \vec{F}_i")
        eq2.shift(2*DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))

class ColoringEquations(Scene):
    #Grouping and coloring parts of equations
    def construct(self):
        line1=TexMobject(r"\text{The vector } \vec{F}_{net} \text{ is the net }",r"\text{force }",r"\text{on object of mass }")
        line1.set_color_by_tex("force", BLUE)
        line2=TexMobject("m", "\\text{ and acceleration }", "\\vec{a}", ".  ")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })
        sentence=VGroup(line1,line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))



class UsingBraces(Scene):
    #Using braces to group text together
    def construct(self):
        eq1A = TextMobject("4x + 3y")
        eq1B = TextMobject("=")
        eq1C = TextMobject("0")
        eq2A = TextMobject("5x -2y")
        eq2B = TextMobject("=")
        eq2C = TextMobject("3")
        eq1B.next_to(eq1A,RIGHT)
        eq1C.next_to(eq1B,RIGHT)
        eq2A.shift(DOWN)
        eq2B.shift(DOWN)
        eq2C.shift(DOWN)
        eq2A.align_to(eq1A,LEFT)
        eq2B.align_to(eq1B,LEFT)
        eq2C.align_to(eq1C,LEFT)

        eq_group=VGroup(eq1A,eq2A)
        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.add(eq1A, eq1B, eq1C)
        self.add(eq2A, eq2B, eq2C)
        self.play(GrowFromCenter(braces),Write(eq_text))


class UsingBracesConcise(Scene):
    #A more concise block of code with all columns aligned
    def construct(self):
        eq1_text=["4","x","+","3","y","=","0"]
        eq2_text=["5","x","-","2","y","=","3"]
        eq1_mob=TexMobject(*eq1_text)
        eq2_mob=TexMobject(*eq2_text)
        eq1_mob.set_color_by_tex_to_color_map({
            "x":RED_B,
            "y":GREEN_C
            })
        eq2_mob.set_color_by_tex_to_color_map({
            "x":RED_B,
            "y":GREEN_C
            })
        for i,item in enumerate(eq2_mob):
            item.align_to(eq1_mob[i],LEFT)
        eq1=VGroup(*eq1_mob)
        eq2=VGroup(*eq2_mob)
        eq2.shift(DOWN)
        eq_group=VGroup(eq1,eq2)
        braces=Brace(eq_group,LEFT)
        eq_text = braces.get_text("A pair of equations")

        self.play(Write(eq1),Write(eq2))
        self.play(GrowFromCenter(braces),Write(eq_text))

class PlotFunctions(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10.3,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),

    }   
    def construct(self):
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        func_graph2=self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        graph_lab2=self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU,func_graph)
        two_pi.next_to(label_coord,RIGHT+UP)



        self.play(ShowCreation(func_graph),ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2),ShowCreation(two_pi))


    def func_to_graph(self,x):
        return np.cos(x)

    def func_to_graph2(self,x):
        return np.sin(x)


class ExampleApproximation(GraphScene):
    CONFIG = {
        "function" : lambda x : np.cos(x), 
        "function_color" : BLUE,
        "taylor" : [lambda x: 1, lambda x: 1-x**2/2, lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4), lambda x: 1-x**2/2+x**4/math.factorial(4)-x**6/math.factorial(6),
        lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8), lambda x: 1-x**2/math.factorial(2)+x**4/math.factorial(4)-x**6/math.factorial(6)+x**8/math.factorial(8) - x**10/math.factorial(10)],
        "center_point" : 0,
        "approximation_color" : GREEN,
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -1,
        "y_max" : 1,
        "graph_origin" : ORIGIN ,
        "x_labeled_nums" :range(-10,12,2),

    }
    def construct(self):
        self.setup_axes(animate=True)
        func_graph = self.get_graph(
            self.function,
            self.function_color,
        )
        approx_graphs = [
            self.get_graph(
                f,
                self.approximation_color
            )
            for f in self.taylor
        ]

        term_num = [
            TexMobject("n = " + str(n),aligned_edge=TOP)
            for n in range(0,8)]
        #[t.to_edge(BOTTOM,buff=SMALL_BUFF) for t in term_num]


        #term = TexMobject("")
        #term.to_edge(BOTTOM,buff=SMALL_BUFF)
        term = VectorizedPoint(3*DOWN)

        approx_graph = VectorizedPoint(
            self.input_to_graph_point(self.center_point, func_graph)
        )

        self.play(
            ShowCreation(func_graph),
        )
        for n,graph in enumerate(approx_graphs):
            self.play(
                Transform(approx_graph, graph, run_time = 2),
                Transform(term,term_num[n])
            )
            self.wait()


class DrawAnAxis(Scene):
    CONFIG = { "plane_kwargs" : { 
        "x_line_frequency" : 2,
        "y_line_frequency" :2
        }
    }

    def construct(self):
        my_plane = NumberPlane(**self.plane_kwargs)
        my_plane.add(my_plane.get_axis_labels())
        self.add(my_plane)
        #self.wait()

class SimpleField(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED
        },
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs) #Create axes and grid
        plane.add(plane.get_axis_labels())  #add x and y label
        self.add(plane)  #Place grid on screen

        points = [x*RIGHT+y*UP
            for x in np.arange(-5,5,1)
            for y in np.arange(-5,5,1)
            ]     #List of vectors pointing to each grid point

        vec_field = []  #Empty list to use in for loop
        for point in points:
            field = 0.5*RIGHT + 0.5*UP   #Constant field up and to right
            result = Vector(field).shift(point)   #Create vector and shift it to grid point
            vec_field.append(result)   #Append to list

        draw_field = VGroup(*vec_field)   #Pass list of vectors to create a VGroup


        self.play(ShowCreation(draw_field))   #Draw VGroup on screen


class FieldWithAxes(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)  #doesn't work in most recent commit
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        self.play(ShowCreation(field))


    def calc_field(self,point):
        #This calculates the field at a single point.
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        #efield = np.array((-y,x,0))/math.sqrt(x**2+y**2)  #Try one of these two fields
        #efield = np.array(( -2*(y%2)+1 , -2*(x%2)+1 , 0 ))/3  #Try one of these two fields
        return Vector(efield).shift(point)

class ExampleThreeD(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)   #Doesn't work in most recent commit
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        self.set_camera_orientation(phi=PI/3,gamma=PI/5)
        self.play(ShowCreation(field2D))
        self.wait()
        #self.move_camera(gamma=0,run_time=1)   #Doesn't work in most recent commit
        #self.move_camera(phi=3/4*PI, theta=-PI/2)   #Doesn't work in most recent commit
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)

    def calc_field2D(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)


class EFieldInThreeD(ThreeDScene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)  #Doesn't work in most recent commit
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field2D = VGroup(*[self.calc_field2D(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])

        field3D = VGroup(*[self.calc_field3D(x*RIGHT+y*UP+z*OUT)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            for z in np.arange(-5,5,1)])



        self.play(ShowCreation(field3D))
        self.wait()
        #self.move_camera(0.8*np.pi/2, -0.45*np.pi)   #Doesn't work in most recent commit
        self.begin_ambient_camera_rotation()
        self.wait(6)


    def calc_field2D(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)

    def calc_field3D(self,point):
        x,y,z = point
        Rx,Ry,Rz = self.point_charge_loc
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2+(z-Rz)**2)
        efield = (point - self.point_charge_loc)/r**3
        #efield = np.array((-y,x,z))/math.sqrt(x**2+y**2+z**2)
        return Vector(efield).shift(point)


class MovingCharges(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_loc" : 0.5*RIGHT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)  #Doesn't work in most recent commit
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.calc_field(x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])
        self.field=field
        source_charge = self.Positron().move_to(self.point_charge_loc)
        self.play(FadeIn(source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()

    def calc_field(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return Vector(efield).shift(point)

    def moving_charge(self):
        numb_charges=4
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(*[
            self.Positron().move_to(point)
            for point in points
        ])
        for particle in particles:
            particle.velocity = np.array((0,0,0))

        self.play(FadeIn(particles))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)

    def field_at_point(self,point):
        x,y = point[:2]
        Rx,Ry = self.point_charge_loc[:2]
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2)
        efield = (point - self.point_charge_loc)/r**3
        return efield

    def continual_update(self, *args, **kwargs):
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration
            for p in self.moving_particles:
                accel = self.field_at_point(p.get_center())
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)


    class Positron(Circle):
        CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
        }
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)

class FieldOfMovingCharge(Scene):
    CONFIG = {
    "plane_kwargs" : {
        "color" : RED_B
        },
    "point_charge_start_loc" : 5.5*LEFT-1.5*UP,
    }
    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        #plane.main_lines.fade(.9)   #Doesn't work in most recent commit
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.create_vect_field(self.point_charge_start_loc,x*RIGHT+y*UP)
            for x in np.arange(-9,9,1)
            for y in np.arange(-5,5,1)
            ])
        self.field=field
        self.source_charge = self.Positron().move_to(self.point_charge_start_loc)
        self.source_charge.velocity = np.array((1,0,0))
        self.play(FadeIn(self.source_charge))
        self.play(ShowCreation(field))
        self.moving_charge()

    def create_vect_field(self,source_charge,observation_point):
        return Vector(self.calc_field(source_charge,observation_point)).shift(observation_point)

    def calc_field(self,source_point,observation_point):
        x,y,z = observation_point
        Rx,Ry,Rz = source_point
        r = math.sqrt((x-Rx)**2 + (y-Ry)**2 + (z-Rz)**2)
        if r<0.0000001:   #Prevent divide by zero
            efield = np.array((0,0,0))  
        else:
            efield = (observation_point - source_point)/r**3
        return efield



    def moving_charge(self):
        numb_charges=3
        possible_points = [v.get_start() for v in self.field]
        points = random.sample(possible_points, numb_charges)
        particles = VGroup(self.source_charge, *[
            self.Positron().move_to(point)
            for point in points
        ])
        for particle in particles[1:]:
            particle.velocity = np.array((0,0,0))
        self.play(FadeIn(particles[1:]))
        self.moving_particles = particles
        self.add_foreground_mobjects(self.moving_particles )
        self.always_continually_update = True
        self.wait(10)


    def continual_update(self, *args, **kwargs):
        Scene.continual_update(self, *args, **kwargs)
        if hasattr(self, "moving_particles"):
            dt = self.frame_duration

            for v in self.field:
                field_vect=np.zeros(3)
                for p in self.moving_particles:
                    field_vect = field_vect + self.calc_field(p.get_center(), v.get_start())
                v.put_start_and_end_on(v.get_start(), field_vect+v.get_start())

            for p in self.moving_particles:
                accel = np.zeros(3)
                p.velocity = p.velocity + accel*dt
                p.shift(p.velocity*dt)


    class Positron(Circle):
        CONFIG = {
        "radius" : 0.2,
        "stroke_width" : 3,
        "color" : RED,
        "fill_color" : RED,
        "fill_opacity" : 0.5,
        }
        def __init__(self, **kwargs):
            Circle.__init__(self, **kwargs)
            plus = TexMobject("+")
            plus.scale(0.7)
            plus.move_to(self)
            self.add(plus)


HEAD_INDEX   = 0
BODY_INDEX   = 1
ARMS_INDEX   = 2
LEGS_INDEX   = 3


class StickMan(SVGMobject):
    CONFIG = {
        "color" : BLUE_E,
        "file_name_prefix": "stick_man",
        "stroke_width" : 2,
        "stroke_color" : WHITE,
        "fill_opacity" : 1.0,
        "height" : 3,
    }
    def __init__(self, mode = "plain", **kwargs):
        digest_config(self, kwargs)
        self.mode = mode
        self.parts_named = False
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "%s_%s.svg" % (self.file_name_prefix, mode)
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No %s design with mode %s" %
                            (self.file_name_prefix, mode))
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "stick_man_plain.svg",
            )
            SVGMobject.__init__(self, mode="plain", file_name=svg_file, **kwargs)


    def name_parts(self):
        self.head = self.submobjects[HEAD_INDEX]
        self.body = self.submobjects[BODY_INDEX]
        self.arms = self.submobjects[ARMS_INDEX]
        self.legs = self.submobjects[LEGS_INDEX]
        self.parts_named = True

    def init_colors(self):
        SVGMobject.init_colors(self)
        if not self.parts_named:
            self.name_parts()
        self.head.set_fill(self.color, opacity = 1)
        self.body.set_fill(RED, opacity = 1)
        self.arms.set_fill(YELLOW, opacity = 1)
        self.legs.set_fill(BLUE, opacity = 1)
        return self

class Waving(Scene):
    def construct(self):
        start_man = StickMan()
        plain_man = StickMan()
        waving_man = StickMan("wave")

        self.add(start_man)
        self.wait()
        self.play(Transform(start_man,waving_man))
        self.play(Transform(start_man,plain_man))

        self.wait()

class CirclesAndSquares(SVGMobject):
    CONFIG = {
        "color" : BLUE_E,
        "file_name_prefix": "circles_and_squares",
        "stroke_width" : 2,
        "stroke_color" : WHITE,
        "fill_opacity" : 1.0,
        "height" : 3,
        "start_corner" : None,
        "circle_index" : 0,
        "line1_index" :1,
        "line2_index" : 2,
        "square1_index" : 3,
        "square2_index" : 4,
    }
    def __init__(self, mode = "plain", **kwargs):
        digest_config(self, kwargs)
        self.mode = mode
        self.parts_named = False
        try:
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "%s_%s.svg" % (self.file_name_prefix, mode)
            )
            SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        except:
            warnings.warn("No %s design with mode %s" %
                            (self.file_name_prefix, mode))
            svg_file = os.path.join(
                SVG_IMAGE_DIR,
                "circles_and_squares_plain.svg",
            )
            SVGMobject.__init__(self, mode="plain", file_name=svg_file, **kwargs)


    def name_parts(self):
        self.circle = self.submobjects[self.circle_index]
        self.line1 = self.submobjects[self.line1_index]
        self.line2 = self.submobjects[self.line2_index]
        self.square1 = self.submobjects[self.square1_index]
        self.square2 = self.submobjects[self.square2_index]
        self.parts_named = True

    def init_colors(self):
        SVGMobject.init_colors(self)
        self.name_parts()
        self.circle.set_fill(RED, opacity = 1)
        self.line1.set_fill(self.color, opacity = 0)
        self.line2.set_fill(self.color, opacity = 0)
        self.square1.set_fill(GREEN, opacity = 1)
        self.square2.set_fill(BLUE, opacity = 1)
        return self


class OpeningManimExample(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()

class TestMove(Scene):
    def construct(self):
        txt = TextMobject("你好世界~")
        self.add(txt)
        txt.move_to(LEFT * 3, aligned_edge=LEFT)  # 左对齐
        self.play(Write(txt))
        txt.move_to(LEFT * 3, aligned_edge=RIGHT)  # 右对齐
        self.play(Write(txt))
        txt.move_to(RIGHT * 5, aligned_edge=RIGHT)  # 右对齐
        self.play(Write(txt))
        self.wait(2)

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.move_to(3*LEFT+2*DOWN)
        square = Square()
        square.move_to(3*RIGHT+2*UP)
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(ShowCreation(square))         # 正方形显示出来
        self.play(Transform(square, circle))    # 正方形变换成圆形
        self.play(FadeOut(square))              # 然后消失不见


class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()

class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "中国",
            tex_to_color_map={"text": YELLOW}
        )
        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()


class UpdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()

class SVGCircleAndSquare(Scene):
    def construct(self):
        thingy = CirclesAndSquares()

        self.add(thingy)
        self.wait()

if __name__ == "__main__":
    # Call this file at command line to make sure all scenes work with version of manim
    # type "python manim_tutorial_P37.py" at command line to run all scenes in this file
    #Must have "import os" and  "import pyclbr" at start of file to use this
    ###Using Python class browser to determine which classes are defined in this file
    module_name = 'tutorial'   #Name of current file
    module_info = pyclbr.readmodule(module_name)

    for item in module_info.values():
        if item.module==module_name:
            print(item.name)
            os.system("python -m manim tutorial.py %s -l" % item.name)  #Does not play files


