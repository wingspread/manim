from manimlib.imports import *
import os
import pyclbr
   
class pandas(Scene):
    CONFIG = {
        'camera_config': {
            'background_color': WHITE,
        }
    }
    def Init_Setting(self):
        '''
        全局变量设置
        '''
        self.prestr=None                    # 字幕临时变量
        self.subtitlesscale=0.7             # 字幕默认缩放比例
        self.subtitlessposition=3.5*DOWN    # 字幕默认位置

        self.code_incolor=GREY
        self.code_runingcolor="#FF0000"
        self.code_runedcolor="#00FF00"
        self.code_scale=0.6
        self.code_font='宋体'

        self.series_elementheight=1.2
        self.series_elementwidth=1

        self.precode=None                   # 上一行代码

    def ShowSubtitles(self,str,delay=1):
        '''
        显示并切换字幕
        '''
        self.txt=Text(str,font="宋体",color='BLACK')
        self.txt.move_to(self.subtitlessposition)
        self.txt.scale(self.subtitlesscale)
        if self.prestr: # 非空
            self.play(ReplacementTransform(self.prestr,self.txt))
        else:
            self.play(ShowCreation(self.txt))
        self.wait(delay)
        self.prestr=self.txt
    
    def HideSubtitles(self):
        if self.prestr:
            # self.play(Uncreate(self.prestr))
            self.prestr=None
    
    def ShowHead(self):
        '''
        开篇动画
        '''
        # 1.矩形出来（从无到有） 颜色1
        txtinrectangle=Text('灵犀\n传媒',font="宋体",
            color=WHITE)
        # self.add(txtinrectangle)
        rectCenter=Rectangle(
            height=1.5,
            width=1.5,
            color=BLUE
        )
        vgCenter=VGroup(txtinrectangle,rectCenter)
        self.play(GrowFromCenter(vgCenter))
        # 2.右边进入一个点，往左运动到为矩形,矩形更换颜色
        rightdot=Dot(
            point=RIGHT_SIDE,    # 圆心位置
            stroke_width=20.0,      # 线宽度
            color=RED,         # 填充颜色
            ) 
        self.play(
            ApplyMethod(rightdot.move_to,0.9*RIGHT))
        self.play(FadeToColor(rectCenter,RED),run_time=0.01)  # 更换颜色 
        # 3.矩形左移动到位置
        self.play(
            ApplyMethod(vgCenter.move_to,2*LEFT))        
        # 4.左边进入一个点，往右运动到矩形
        leftdot=Dot(
            point=LEFT_SIDE,    # 圆心位置
            stroke_width=20.0,      # 线宽度
            color=BLUE,         # 填充颜色
            ) 
        self.play(
            ApplyMethod(leftdot.move_to,2.95*LEFT),
            # ApplyMethod(vgCenter.move_to,2.95*LEFT)
            )
        self.play(FadeToColor(rectCenter,BLUE),run_time=0.01)  # 更换颜色         
        # 5.矩形右移动过到原点,右边点消失
        self.play(
            ApplyMethod(vgCenter.move_to,ORIGIN),
            )     
        # self.play(FadeOut(rightdot),run_time=0.01)   #dot 消失
        self.play(ShrinkToCenter(rightdot),run_time=0.01)   #dot 消失
        
        # 6.左边点旋转，矩形跟着旋转.
        vgAll=VGroup(leftdot,vgCenter)
        self.play(
            Rotating(vgAll,radians=2*PI,run_time=3,axis=OUT,about_point=ORIGIN),rate_func=linear)
        self.play(ShrinkToCenter(leftdot))   #dot 消失

        # 7.文字显示出来
        txtcompany=Text('winspread2222',color=WHITE)
        txtcompany.move_to(2*DOWN)        
        self.play(GrowFromPoint(txtcompany,ORIGIN)) 
        self.wait()
        # 8.所有内容消失
        vgAll.remove(leftdot)
        vgAll.add(txtcompany)
        self.play(ShrinkToCenter(vgAll),run_time=0.5) 

        
        #=============================
        '''
        显示标题及logo
        '''

        lefttitle=Text("PandasLearn",color=RED)
        lefttitle.scale(2)
        lefttitle.move_to(2*UP)
        self.play(FadeInFrom(lefttitle,direction=UP)) 

        studio=Text("Lingxi Studio",color=RED)
        studio.next_to(lefttitle,DOWN)
        self.play(FadeIn(studio))

        img=ImageMobject(
            "xiniu.png",
            height=3,
            invert=False)
        img.next_to(studio,DOWN)
        self.play(FadeIn(img))
        # img.scale(0.25,about_edge=UP)
        self.play(
            ApplyMethod(studio.move_to,6*RIGHT+3.5*UP),
            ApplyMethod(img.move_to,6*LEFT+3.5*UP),
            ApplyMethod(img.scale,0.25),
            )

        self.play(FadeOut(lefttitle))
    
    def ShowCatory(self):
        '''
        显示视频的主要内容
        '''
        t = Paragraph(
            '1.Pandas base knowledge',
            '2.Series',
            '3.DataFrame',
            '4.Panel',
        )
        t.set_all_lines_alignment('left')
        # rect = SurroundingRectangle(t)
        # self.add(t)
        # self.add(rect)
        # self.play(t.set_alignment, "right", 9)
        # self.play(t.set_all_lines_alignment, "left")
        # for i in range(len(t)):
        #     self.play(t.set_alignment, "left", i)
       
        for obj in t:
            self.play(FadeToColor(obj,GRAY),run_time=1)
    
    def ShowBaseKnowledge(self):
        # DATABASE
        lefttitle=Text("DataBase")
        lefttitle.move_to(6*LEFT+3*UP)
        self.play(FadeInFrom(lefttitle,direction=UP))   # 从上边进入
        #矩形
        vgleft=VGroup()   
        for rowindex in range(4):
            for i in range(5):
                rect=Rectangle(height=0.5,width=0.75)
                rect.move_to(RIGHT*i+DOWN*rowindex*0.75)
                vgleft.add(rect)
        vgleft.scale(0.5)
        vgleft.move_to(2*UP+5*LEFT)
        self.play(ShowCreation(vgleft))
        
        # PANDAS
        righttitle=Text("Pandas")
        righttitle.move_to(6*RIGHT+3*UP)
        self.play(FadeInFrom(righttitle,direction=UP)) 
        #矩形
        vgright=VGroup()   
        for rowindex in range(4):
            for i in range(5):
                rect=Rectangle(height=0.5,width=0.75,color="RED")
                rect.move_to(RIGHT*i+DOWN*rowindex*0.75)
                vgright.add(rect)
        vgright.scale(0.5)
        vgright.move_to(2*UP+5*RIGHT)
        self.play(ShowCreation(vgright))

        # 相同之处
        sametitle=Text("SAME:")
        sametitle.move_to(3*UP)
        # sametitle.set_color(RED)
        self.play(ShowCreation(sametitle)) 

        # 相同之处内容
        detildist=['1.asdfadf','2.123132123','3.asdfasdf','4.eqwqweqwe','5.afasdfasd']
        vgdetil=VGroup()
        for textobj in detildist:
            detail=Text('{}'.format(textobj))
            vgdetil.add(detail)
        vgdetil.arrange_submobjects(DOWN,buff=0.5)
        self.play(FadeInFrom(vgdetil,DOWN))

        vgsame=VGroup(sametitle,vgdetil)
        self.play(FadeOut(vgsame))
    
    def ShowSerires(self):
        '''
        Serires 相关知识
        '''
        vgdataH=VGroup()   
        for i in range(8):
            rect=Rectangle(
                height=0.5,
                width=0.75,
                stroke_color=WHITE,    
                stroke_width=2)
            rect.move_to(RIGHT*i*0.75)
            rect.set_fill(color=RED,opacity=1)
            vgdataH.add(rect)
        vgdataH.shift(3*LEFT)
        self.play(FadeIn(vgdataH))
        self.ShowSubtitles('序列Series是pandas中的一维数据结构')
        self.ShowSubtitles('类似于python中的列表和Numpy中的Ndarray对象')     
        
        self.play(
            ApplyMethod(vgdataH.move_to,4*LEFT),
            )
        self.play(
            ApplyMethod(vgdataH[-1].scale,2),
            )
        self.ShowSubtitles('Series中存储的数据类型可以是整数、浮点数、字符串、python对象等')
        t = Paragraph(
            '整数','浮点数','字符串','python对象',
            alignment="left",
            font='宋体'
        )
        t.set_all_lines_alignment('left')
        t.shift(3*RIGHT)       
        for obj in t:
            self.play(FadeToColor(obj,GREY),run_time=0.7)
        def scalemoveto(mob):
            mob.scale(0.2)
            mob.move_to(1.75*LEFT)           
            return mob
        self.play(ApplyFunction(scalemoveto,t),run_time=3)
        t.scale(0.01)        
        self.play(Indicate(vgdataH[-1])) # 提示信息
        self.play(
            ApplyMethod(vgdataH[-1].scale,0.5),
            )
        self.HideSubtitles() # 关闭字幕
        self.play(
            ApplyMethod(vgdataH.move_to,3*LEFT+3*UP),
            )

        data=Text('数据',font="宋体")
        data.scale(0.75)
        data.next_to(vgdataH,LEFT)
        self.play(ShowCreation(data))

        label=Text('标签',font="宋体")
        label.scale(0.75)
        label.next_to(data,UP)
        self.play(ShowCreation(label))

        vglabelH=VGroup()   
        for i in range(8):
            rect=Rectangle(
                height=0.5,
                width=0.75,
                stroke_width=1)  
            rect.set_fill(color=GREY,opacity=0.2)
            rect.move_to(RIGHT*i*0.75)
            vglabelH.add(rect)
        vglabelH.next_to(vgdataH,UP,buff=0.1)
        self.play(ShowCreation(vglabelH))

        self.play(Indicate(vglabelH)) # 提示信
        self.ShowSubtitles('序列的index默认系统自动生成，取值从0到N-1（N为序列的总元素树）')
        self.ShowSubtitles('序列的index也可以自己指定')
    
    def ShowSeriesRectangle_fillData(self,elementlist,pos=4*LEFT):
        '''
        生成series的内容矩形框
        '''
        elementcount=len(elementlist)
        rect=Rectangle(
            height=self.series_elementheight,
            width=self.series_elementwidth*elementcount,
            stroke_color=BLACK,    
            stroke_width=1)
        rect.move_to(pos)
        self.add(rect)
        vgdata=VGroup()
        for i in range(elementcount):   
            elementvalue=Text('{}'.format(elementlist[i]),font="宋体",color=BLACK)
            elementvalue.next_to(rect,RIGHT,aligned_edge=LEFT,buff=(i-1)*self.series_elementwidth-0.8)
            vgdata.add(elementvalue)
        self.play(ShowCreation(vgdata))
        return rect,vgdata

    def ShowCode(self,thisparamgraph):      
        '''
        代码部分处理显示
        '''  
        thisparamgraph.set_color(self.code_incolor).set_all_lines_alignment('left').scale(self.code_scale)
        if self.precode: # 非空
            thisparamgraph.next_to(self.precode,DOWN,buff=0.05,aligned_edge=LEFT)
        else:
            thisparamgraph.shift(2.5*RIGHT+2.6*UP)
        self.play(FadeToColor(thisparamgraph,self.code_runingcolor),run_time=0.5) 
        self.play(FadeToColor(thisparamgraph,self.code_runedcolor),run_time=0.5) 
        self.precode=thisparamgraph
    
    def ClearCode(self):
        '''
        清除code
        '''
        if self.precode:
            self.precode=None
            # self.remove(self.precode)
            # self.play(Uncreate(self.precode))
    
    def ShowSeriesIndexPoint(self,vgdata,keylist=None):
        '''
        显示Series的指针，根据变量控制是否显示key
        '''
        vgtxt=VGroup()
        vgarrow=VGroup()
        for i in range(len(vgdata)):
            if keylist:
                # key
                txt=Text('''s['{}']'''.format(keylist[i]),font='宋体',color=BLACK)
                txt.next_to(vgdata[i],UP,aligned_edge=ORIGIN,buff=1)
                # index
                txtindex=Text('s[{}]'.format(i),font='宋体',color=BLACK)
                txtindex.next_to(txt,UP,aligned_edge=LEFT,buff=0.2)
                vgtxt.add(VGroup(txt,txtindex))
            else:
                # index
                txtindex=Text('s[{}]'.format(i),font='宋体',color=BLACK)
                txtindex.next_to(vgdata[i],UP,aligned_edge=ORIGIN,buff=1)
                vgtxt.add(txtindex)
            # 箭头
            arrow = Arrow(UP,DOWN)
            arrow.set_color("#FF0000")
            arrow.next_to(vgtxt[i],DOWN,buff=-0.3)
            arrow.scale(0.65)
            vgarrow.add(arrow)
        self.add(vgtxt[0],vgarrow[0])
        for i in range(len(vgdata)-1):
            self.play(
                ReplacementTransform(vgtxt[i],vgtxt[i+1]),
                ReplacementTransform(vgarrow[i],vgarrow[i+1]),
                run_time=1)
        self.play(ShrinkToCenter(VGroup(vgtxt,vgarrow)),run_time=0.01)
    
    def GetSourceCodeBoxGroup(self,topborder=1,rightborder=1,downborder=1,codewidth=6):
        '''
        得到源代码Group（Z-index=0.2----0.1）
        '''
        vgall=VGroup()
        clientWidth=15
        clientheight=8.8
        rectbg=Rectangle(height=clientheight,width=clientWidth,          
            opacity=0.5,
            fill_color=WHITE,
            fill_opacity=1,
            stroke_color=WHITE,
            stroke_opacity=1) 
        rectbg.shift(IN*0.2)        
        vgall.add(rectbg)

        # 4.4*7.5    8.8*15
        recttop=Rectangle(height=topborder,width=clientWidth,          
            opacity=0.5,
            fill_color=WHITE,
            fill_opacity=1,
           ) 
        recttop.shift((clientheight/2-topborder)*UP)

        rectdown=Rectangle(height=downborder,width=clientWidth,          
            opacity=0.5,
            fill_color=WHITE,
            fill_opacity=1) 
        rectdown.shift((clientheight/2-downborder)*DOWN)

        rectright=Rectangle(height=clientheight,width=rightborder,          
            opacity=0.5,
            fill_color=WHITE,
            fill_opacity=1) 
        rectright.shift((clientWidth/2-rightborder)*RIGHT)

        wleft=(clientWidth-rightborder-codewidth)/2
        border1=clientWidth/2-wleft
        rectleft=Rectangle(height=clientheight,width=clientWidth-rightborder-codewidth,          
            opacity=0.5,
            fill_color=WHITE,
            fill_opacity=1) 
        rectleft.shift(border1*LEFT)


        vg=VGroup(recttop,rectdown,rectright,rectleft)
        vg.shift(IN*0.1)
        vgall.add(vg)

        rectbox=Rectangle(
            height=clientheight-topborder-downborder,
            width=codewidth)
        rectbox.set_stroke(BLACK,1)
        rectbox.set_fill(color="#EBEBEB",opacity=1)
        # rectbox.shift(IN*0.09+(7.5-rightborder-codewidth)*RIGHT)
        right1=clientWidth/2-codewidth/2-rightborder
        rectbox.move_to(IN*0.09+right1*RIGHT)
        vgall.add(rectbox)

        return vgall

    def ShowSeries_Create(self):
        '''
        Series 创建
        '''
        vgcode=self.GetSourceCodeBoxGroup()
        self.add(vgcode)
        # ===============================================================
        self.ShowSubtitles('第一种创建方式是通过list创建一个Series')
        seriesvaluelist=['a','b','c','d']
        code = Paragraph(
            '''data = ['a','b','c','d']''',
            '''s = pd.Series(data)''',
            font=self.code_font
        )
        self.ShowCode(code)
        rectdata,vgdata=self.ShowSeriesRectangle_fillData(seriesvaluelist)
        self.ShowSubtitles('Series的值可以根据默认生成从0开始的索引值进行访问每一个元素')
        self.ShowSeriesIndexPoint(vgdata)
        self.play(ShrinkToCenter(VGroup(vgdata,rectdata)),run_time=0.01)
        # ===============================================================
        self.ShowSubtitles('第二种创建方式是通过ndarray创建一个Series')
        seriesvaluelist=['e','f','g','h']
        code = Paragraph(
            '''data = np.array(['e','f','g','h'])''',
            '''s = pd.Series(data)''',
            font=self.code_font
        )
        self.ShowCode(code)
        rectdata,vgdata=self.ShowSeriesRectangle_fillData(seriesvaluelist)
        self.ShowSeriesIndexPoint(vgdata)
        self.play(ShrinkToCenter(VGroup(vgdata,rectdata)),run_time=0.01)
        # ===============================================================
        self.ShowSubtitles('第三种创建方式是从字典创建Series')
        data = {'a' : 0, 'b' : 1, 'c' : 2}
        seriesvaluelist=[]
        [seriesvaluelist.append(val) for val in data.values()]
        keylist=[]
        [keylist.append(val) for val in data.keys()]
        code = Paragraph(
            '''data = {'a':0,'b':1,'c':2}''',           
            '''s = pd.Series(data)''',
            font=self.code_font
        )
        self.ShowCode(code)
        rectdata,vgdata=self.ShowSeriesRectangle_fillData(seriesvaluelist)
        self.ShowSubtitles('Series的值可以根据字典key,也可根据索引值访问每一个元素')
        self.ShowSeriesIndexPoint(vgdata,keylist)
        self.play(ShrinkToCenter(VGroup(rectdata,vgdata)),run_time=0.01)    
        # ===============================================================
        self.ShowSubtitles('第四种创建方式是从标量创建Series，此时必须提供索引。重复该值以匹配索引的长度')
        seriesvaluelist = [5,5,5,5]
        code = Paragraph(
            's = pd.Series(5, index=[0, 1, 2, 3])',
            font=self.code_font,
        )
        self.ShowCode(code)
        rectdata,vgdata=self.ShowSeriesRectangle_fillData(seriesvaluelist)
        self.ShowSeriesIndexPoint(vgdata)
        self.play(ShrinkToCenter(VGroup(rectdata,vgdata)),run_time=0.01)    
        self.wait()
        #=================================================================
        self.ShowSubtitles('如果创建Series时，不存在索引对应的值,则值默认为NaN')
        seriesvaluelist = [0,1,'NaN',2]
        code = Paragraph(
            '''data = {'a' : 0., 'b' : 1., 'c' : 2.0}''',
            '''index=['b','c','d','a']''',
            '''s = pd.Series(data,index)''',
            font=self.code_font
        )
        self.ShowCode(code)
        rectdata,vgdata=self.ShowSeriesRectangle_fillData(seriesvaluelist)

        braces=Brace(vgdata,DOWN) # 大括号的使用
        braces.set_color(BLACK)
        bracestext = braces.get_text("元素数量等于提供索引项的个数")
        bracestext.set_color(BLACK).scale(0.5)
        self.play(GrowFromCenter(braces),Write(bracestext))
        self.wait()

    def ShowSeries_DateRectangle(self,vgroup,indexlist,issplit=True):
        '''
        显示给定vgroup的特定元素的围绕矩形，按照index进行显示
        indexlist：索引的id list
        '''
        if issplit: # 每个元素一个矩形
            vg=VGroup()
            for rectindex in indexlist:
                rect=SurroundingRectangle(vgroup[rectindex]).set_color("#FF0000")
                vg.add(rect)
            self.play(
                *[ShowCreationThenFadeOut(rect) for rect in vg])
        else:# 所有元素一个矩形
            vg=VGroup()
            for rectindex in indexlist:
                vg.add(vgroup[rectindex])
            rectbig=SurroundingRectangle(vg).set_color("#FF0000")
            self.play(ShowCreationThenFadeOut(rectbig))
            
    def GetVG_CreateSeries(self,valuelist,dskeylist,itemheight=0.5,ishaveKey=True,isshowindex=True):
        '''
        生成Series的矩形，并返回vgindex,vgkey,vgvalue
        '''
        vgindex=VGroup()
        vgkey=VGroup()
        vgvalue=VGroup()
        index=0
        for key,value in zip(dskeylist,valuelist):
            gdptxt=Text(value,font="宋体",color=BLACK)
            gdptxt.set_height(itemheight)
            vgvalue.add(gdptxt)
            if isshowindex:
                indextxt=Text('{}'.format(index),font="宋体",color=BLACK)
                indextxt.set_color(BLACK)
                indextxt.set_height(itemheight)
                vgindex.add(indextxt)            
            if ishaveKey:
                dstxt=Text(key,font="宋体",color=BLACK)
                dstxt.set_height(itemheight)
                vgkey.add(dstxt)
            index+=1
        if isshowindex:
            vgindex.arrange_submobjects(DOWN,buff=0.415,).scale(0.5)

        vgvalue.arrange_submobjects(DOWN,buff=0.415).scale(0.5)
        if ishaveKey:
            vgkey.arrange_submobjects(DOWN,buff=0.415).scale(0.5)
            if isshowindex:
                vgindex.next_to(vgkey[0],LEFT,
                    submobject_to_align=vgindex[0],
                    aligned_edge=TOP,buff=0.5)

            vgvalue.next_to(vgkey[0],RIGHT,
                submobject_to_align=vgvalue[0],
                aligned_edge=TOP,buff=0.5)
        else:
            if isshowindex:
                vgindex.next_to(vgvalue[0],LEFT,
                    submobject_to_align=vgvalue[0],
                    aligned_edge=TOP,buff=0.5)

        return vgindex,vgkey,vgvalue
        

    def ShowSeries_Select(self):
        '''
        Series 的选择操作
        '''
        # 构造数据
        self.ShowSubtitles('让我们构造一个示例数据(2019年山东省GDP排名)，演示Series的选择操作')

        code = Paragraph(
            '''
            valuelist=[11741.31,9443.37,7653.45,5688.5,4600.25,4370.17,3642.42,3409.98,
                3022.27,2963.73,2916.19,2663.59,2457.19,2259.82,1949.38,1693.91]
            dskeylist='青岛,济南,烟台,潍坊,临沂,济宁,淄博,菏泽,
                    德州,威海,东营,泰安,滨州,聊城,日照,枣庄'.split(',')
            pseries = pd.Series(data=valuelist,index=dskeylist)
            ''',
            font=self.code_font
        )
        code.set_color(self.code_incolor).set_all_lines_alignment('left').scale(self.code_scale)
        self.play(Indicate(code))
        self.wait(2)
        self.play(Uncreate(code))

        title=Text("16地市GDP排名",font="宋体",color=BLACK)
        title.shift(5*LEFT+3.5*UP)
        self.add(title)
        # 显示结果
        valuelist='11741.31,9443.37,7653.45,5688.5,4600.25,4370.17,3642.42,3409.98,3022.27,2963.73,2916.19,2663.59,2457.19,2259.82,1949.38,1693.91'.split(',')
        dskeylist='青岛,济南,烟台,潍坊,临沂,济宁,淄博,菏泽,德州,威海,东营,泰安,滨州,聊城,日照,枣庄'.split(',')
        vgall=VGroup()
        vgindex,vgkey,vgvalue=self.GetVG_CreateSeries(valuelist,dskeylist,itemheight=0.3)
        vgall.add(vgindex,vgkey,vgvalue).next_to(title,DOWN,aligned_edge=LEFT)
        self.play(ShowCreation(vgindex),ShowCreation(vgkey),ShowCreation(vgvalue))
        # 数据解说(行数)
        self.ShowSubtitles('构造的pseries有16个元素,对应山东省16地市')
        braces=Brace(vgvalue,RIGHT).set_color(BLACK)    # 大括号的使用
        bracestext = braces.get_text("Series有16个元素")
        bracestext.set_color(BLACK).scale(0.5)
        self.play(GrowFromCenter(braces),Write(bracestext))
        self.wait(0.5)
        self.play(Uncreate(VGroup(braces,bracestext)))
        # 数据解说（key值）
        self.ShowSubtitles('其中索引值是地市名称')
        rectindex=SurroundingRectangle(vgkey)
        rectindex.set_color("#FF0000")
        self.play(ShowCreationThenDestruction(rectindex),run_time=1)
        # 数据解说（数据）
        self.ShowSubtitles('数据为对应地市的2019年GDP值，单位亿元')
        rectdata=SurroundingRectangle(vgvalue)
        rectdata.set_color("#FF0000")
        self.play(ShowCreationThenDestruction(rectdata),run_time=1)

        # 不带key的选择
        self.ShowSubtitles('第一种选择方式:选择前N项head()和选择后N项tial()')
        commandlist=[
            'pseries.head()  # 选择前5个元素',
            'pseries.head(2) # 选择指定个数的前N个元素',
            'pseries.tial()  # 选择后5个元素',
            'pseries.tial(3) # 选择指定个数的后N个元素',
            'pseries[0]',
            'pseries[0:2]',
            'pseries[[3,5]]',
            'pseries.iloc[[4,6]] # iloc按照位置选择，iloc可以忽略',
            '''pseries['济南']=pseries.loc['济南'] # loc按照索引选择，loc可以忽略''', #9
            '''pseries[['济南','青岛']]=pseries.loc[['济南','青岛']] ''',
            '''pseries['济南':'临沂']] ''',
            'pseries[(pseries>4000)&(pseries<5000)]  #按照条件检索'
            ]
        subtitlelist=[
            ['head()不带参数时，默认选择前5个元素'],
            ['head(N)带参数选择的前N个元素'],
            ['tile()默认选择最后5个元素'],
            ['head(N)带参数选择的前N个元素'],
            ['第二种选择方式，按照位置索引，同常规列表的选择方式相同，可以直接使用[]进行选择'],
            ['也可以象list一样进行切片'],
            ['也可以使用不连续的位置列表选择数据'],
            ['在进行位置检索数据时，等同于iloc'],
            ['第三种选择方式，按照索引进行选择'],   #9 
            ['选择指定索引的数据'],
            ['按照索引切片'],
            ['按照条件检索']
        ]
        selectindexlist=[[0,1,2,3,4],[0,1],[11,12,13,14,15],[13,14,15],[0],[0,1,2],[2,4],[3,5],
                         [1],[0,1],[1,2,3,4],[4,5]]
        onerectflaglist=[False,False,False,False,True,False,False,False,
                        False,False,False,False]
        # 选择数据
        vgCode=VGroup()      
        for commandindex in range(len(commandlist)):
            for strsubtitle in subtitlelist[commandindex]:
                self.ShowSubtitles(strsubtitle)
            code = Paragraph(
                commandlist[commandindex],
                font=self.code_font
            )
            code.set_color(self.code_incolor).set_all_lines_alignment('left').scale(self.code_scale)
            if commandindex==0:
                code.move_to(3*UP)
            else:
                code.next_to(vgCode[len(vgCode)-1],DOWN,buff=0.1,aligned_edge=LEFT)
            vgCode.add(code)
            self.play(Indicate(code))
            self.ShowSeries_DateRectangle(vgvalue,selectindexlist[commandindex],issplit=onerectflaglist[commandindex])
            self.wait()        
        # 杂项操作
        self.play(Uncreate(vgCode))
        vgCode=VGroup()
        self.ShowSubtitles('Series的其他操作包括:求元素个数、遍历、检查重复情况')
        self.ShowSubtitles('Series的元素个数可通过三种方式获取len(),size,count()')   
        code = Paragraph("求元素个数：",font=self.code_font).set_color(self.code_incolor).scale(self.code_scale).move_to(3*UP)
        vgCode.add(code)
        self.play(Indicate(code))
        code0 = Paragraph("len(pseries)=16",font=self.code_font).set_color(self.code_incolor).scale(self.code_scale).move_to(3*UP)
        code0.next_to(code,DOWN,buff=0.1,aligned_edge=LEFT)
        vgCode.add(code0)
        self.play(Indicate(code0))
        code1 = Paragraph("pseries.size=16",font=self.code_font).set_color(self.code_incolor).scale(self.code_scale)
        code1.next_to(code0,DOWN,buff=0.1,aligned_edge=LEFT)
        vgCode.add(code1)
        self.play(Indicate(code1))
        code2 = Paragraph("pseries.count()=16",font=self.code_font).set_color(self.code_incolor).scale(self.code_scale)
        code2.next_to(code1,DOWN,buff=0.1,aligned_edge=LEFT)
        vgCode.add(code2)
        self.play(Indicate(code2))
        
        code3 = Paragraph("使用遍历dictionary的方式进行遍历Series的每个元素",font=self.code_font).set_color(self.code_incolor).scale(self.code_scale)
        code3.next_to(code2,DOWN,buff=0.1,aligned_edge=LEFT)
        vgCode.add(code3)
        self.play(Indicate(code3))
        code4 = Paragraph(
            '''for index, val in pseries.items():
    print(index, val)
            ''',
            font=self.code_font).set_color(self.code_incolor).scale(self.code_scale)
        code4.next_to(code3,DOWN,buff=0.1,aligned_edge=LEFT)
        self.play(Indicate(code4))
        vgCode.add(code4)
        # 重新构造数据
        self.play(Uncreate(vgall),Uncreate(title),Uncreate(vgCode))

        title=Text("SeriesA",font="宋体",color=BLACK)
        title.shift(5*LEFT+3.5*UP)
        self.add(title)
        # 构造SeriesA
        dskeylist='1,2,3,2,5'.split(',')
        valuelist='张三,李四,王五,张三,李四'.split(',')
        vgall=VGroup()
        vgindex,vgkey,vgvalue=self.GetVG_CreateSeries(valuelist,dskeylist,ishaveKey=False)
        vgall.add(vgindex,vgkey,vgvalue).next_to(title,DOWN,aligned_edge=LEFT)
        self.play(ShowCreation(vgindex),ShowCreation(vgvalue))
        vgCode=VGroup()

        #  检查重复情况
        self.ShowSubtitles('可以使用duplicated查看各个值的重复情况')
        code = Paragraph('''pseries.duplicated()''',font=self.code_font)
        code.scale(self.code_scale).set_color(BLACK).move_to(3*UP)
        vgCode.add(code)
        self.play(Indicate(code))
        #结果
        result_title=Text("运算结果",font="宋体",color=BLACK)
        result_title.shift(1.5*DOWN)
        self.add(result_title)
        result_keylist='张三,王五,李四'.split(',')
        result_valuelist='True,False,True'.split(',')
        result_vgindex,result_vgkey,result_vgvalue=self.GetVG_CreateSeries(result_valuelist,result_keylist,ishaveKey=True,isshowindex=False)
        result_vgall=VGroup()
        result_vgall.add(result_vgindex,result_vgkey,result_vgvalue).next_to(result_title,DOWN,aligned_edge=LEFT)
        self.play(ShowCreation(result_vgkey),ShowCreation(result_vgvalue))

        
        #  检查值出现次数
        self.ShowSubtitles('查看各个值出现的次数')
        code1 = Paragraph('pseries.value_counts()',font=self.code_font)
        code1.scale(self.code_scale).set_color(BLACK).next_to(code,DOWN,aligned_edge=LEFT)
        vgCode.add(code1)
        self.play(Indicate(code1))
        # self.play(ReplacementTransform(result_vgkey),Uncreate(result_vgvalue))
        #结果
        result_keylist='张三,王五,李四'.split(',')
        result_valuelist='2,1,2'.split(',')
        result_vgindex,result_vgkey,result_vgvalue=self.GetVG_CreateSeries(result_valuelist,result_keylist,ishaveKey=True,isshowindex=False)
        result_vgall1=VGroup()
        result_vgall1.add(result_vgindex,result_vgkey,result_vgvalue).next_to(result_title,DOWN,aligned_edge=LEFT)
        self.play(ReplacementTransform(result_vgall,result_vgall1))

        code2 = Paragraph('pseries[pseries.duplicated() == False]',font=self.code_font)
        code2.scale(self.code_scale).set_color(BLACK).next_to(code1,DOWN,aligned_edge=LEFT)
        self.ShowSubtitles('选择不重复的行')
        vgCode.add(code2)
        self.play(Indicate(code2))
        #结果
        result_keylist=',,'.split(',')
        result_valuelist='张三,王五,李四'.split(',')
        result_vgindex,result_vgkey,result_vgvalue=self.GetVG_CreateSeries(result_valuelist,result_keylist,ishaveKey=False,isshowindex=True)
        result_vgall=VGroup()
        result_vgall.add(result_vgindex,result_vgkey,result_vgvalue).next_to(result_title,DOWN,aligned_edge=LEFT)
        self.play(ReplacementTransform(result_vgall1,result_vgall))

        #  查询不重复的数据
        self.ShowSubtitles('使用unique查询不重复的数据，返回值列表')
        code3 = Paragraph('pseries.unique()',font=self.code_font)
        code3.scale(self.code_scale).set_color(BLACK).next_to(code2,DOWN,aligned_edge=LEFT)
        vgCode.add(code3)
        self.play(Indicate(code3))
        #结果
        txt=Text("['张三' '王五' '李四']",font="宋体")
        txt.scale(self.code_scale).set_color(BLACK).next_to(result_title,DOWN,aligned_edge=LEFT)
        self.play(ReplacementTransform(result_vgall,txt))

        # 删除重复值
        self.ShowSubtitles('删除重复数据用drop_duplicates')
        code4 = Paragraph('SeriesB = pseries.drop_duplicates()',font=self.code_font)
        code4.scale(self.code_scale).set_color(BLACK).next_to(code3,DOWN,aligned_edge=LEFT)
        vgCode.add(code4)
        self.play(Indicate(code4))
        self.play(Uncreate(txt))
        # SeriesB
        titleB=Text("SeriesB",font="宋体",color=BLACK)
        titleB.shift(5*LEFT)
        self.add(titleB)
        #结果
        result_keylist=',,'.split(',')
        result_valuelist='张三,王五,李四'.split(',')
        result_vgindex,result_vgkey,result_vgvalue=self.GetVG_CreateSeries(result_valuelist,result_keylist,ishaveKey=False,isshowindex=True)
        result_vgall=VGroup()
        result_vgall.add(result_vgindex,result_vgvalue).next_to(titleB,DOWN,aligned_edge=LEFT)
        self.play(ShowCreation(result_vgall))

        # # 显示结果
        # dskeylistB='1,2,3'.split(',')
        # valuelistB='赵四,张三,李四'.split(',')
        # vgallB=VGroup()
        # vgindexB,vgkeyB,vgvalueB=self.GetVG_CreateSeries(valuelistB,dskeylistB,ishaveKey=False)
        # vgallB.add(vgindexB,vgkeyB,vgvalueB).next_to(titleB,DOWN,aligned_edge=LEFT)
        # self.play(ShowCreation(vgindexB),ShowCreation(vgvalueB))
        # self.wait()

    def ShowSeries_DataChange(self):
        '''
        多Series操作：增加数据、删除数据、两个Series相加、重新索引
        '''
        self.ShowSubtitles('让我们看下修改Series的操作')

        
        # 显示Code
        code = Paragraph(
            '''
            seriesA = pd.Series('张三,李四,王五'.split(','))
            ''',
            font=self.code_font
        )
        code.set_color(self.code_incolor).set_all_lines_alignment('left').scale(self.code_scale)
        code.move_to(3*UP)
        self.play(Indicate(code))

        title=Text("SeriesA",font="宋体",color=BLACK)
        title.shift(5*LEFT+3.5*UP)
        self.play(FadeIn(title))
        # 构造数据
        dskeylist='1,2,3,4'.split(',')
        valuelist='青岛,济南,烟台,潍坊'.split(',')
        vgall=VGroup()
        vgindex,vgkey,vgvalue=self.GetVG_CreateSeries(valuelist,dskeylist,itemheight=0.3,ishaveKey=False,isshowindex=True)
        vgall.add(vgindex,vgkey,vgvalue).next_to(title,DOWN,aligned_edge=LEFT)
        self.play(GrowFromPoint(vgall,code.get_center()))
        # self.play(ShowCreation(vgindex),ShowCreation(vgkey),ShowCreation(vgvalue))

        code1 = Paragraph(
            '''
            seriesA.appent(pd.Series('临沂,济宁,淄博'.split(','))
            ''',
            font=self.code_font
        )
        code1.set_color(self.code_incolor).set_all_lines_alignment('left').scale(self.code_scale)
        code1.next_to(code,DOWN,buff=0.5)
        self.play(Indicate(code1))

        #
        dskeylist1='1,2,3,4'.split(',')
        valuelist1='临沂,济宁,淄博'.split(',')
        vgall1=VGroup()
        vgindex1,vgkey1,vgvalue1=self.GetVG_CreateSeries(valuelist1,dskeylist1,itemheight=0.3,ishaveKey=False,isshowindex=True)
        vgall1.add(vgindex1,vgkey1,vgvalue1).next_to(vgall,DOWN,aligned_edge=LEFT)
        self.play(GrowFromPoint(vgall1,code1.get_center()))
        

        # code1 = Paragraph(
        #     '''
        #     seriesA.appent(pd.Series('临沂,济宁,淄博'.split(','))
        #     ''',
        #     font=self.code_font
        # )
        # code1.set_color(self.code_incolor).set_all_lines_alignment('left').scale(self.code_scale)
        # code1.next_to(code,DOWN,buff=0.5)
        # self.play(Indicate(code1))

        # #
        # dskeylist1='1,2,3,4'.split(',')
        # valuelist1='临沂,济宁,淄博'.split(',')
        # vgall1=VGroup()
        # vgindex1,vgkey1,vgvalue1=self.GetVG_CreateSeries(valuelist1,dskeylist1,itemheight=0.3,ishaveKey=False,isshowindex=True)
        # vgall1.add(vgindex1,vgkey1,vgvalue1).next_to(vgall,DOWN,aligned_edge=LEFT)
        # self.play(GrowFromPoint(vgall1,code1.get_center()))
        

        # self.ShowSubtitles('增加数据操作')

        # code = Paragraph(
        #     '''
        #     valuelist=[11741.31,9443.37,7653.45,5688.5,4600.25,4370.17,3642.42,3409.98,
        #         3022.27,2963.73,2916.19,2663.59,2457.19,2259.82,1949.38,1693.91]
        #     dskeylist='青岛,济南,烟台,潍坊,临沂,济宁,淄博,菏泽,
        #             德州,威海,东营,泰安,滨州,聊城,日照,枣庄'.split(',')
        #     pseries = pd.Series(data=valuelist,index=dskeylist)
        #     ''',
        #     font=self.code_font
        # )
        # code.set_color(self.code_incolor).set_all_lines_alignment('left').scale(self.code_scale)
        # self.play(Indicate(code))
        # self.wait(2)
        # self.play(Uncreate(code))

        # title=Text("16地市GDP排名",font="宋体",color=BLACK)
        # title.shift(5*LEFT+3.5*UP)
        # self.add(title)
        # # 显示结果
        # valuelist='11741.31,9443.37,7653.45,5688.5,4600.25,4370.17,3642.42,3409.98,3022.27,2963.73,2916.19,2663.59,2457.19,2259.82,1949.38,1693.91'.split(',')
        # dskeylist='青岛,济南,烟台,潍坊,临沂,济宁,淄博,菏泽,德州,威海,东营,泰安,滨州,聊城,日照,枣庄'.split(',')
        # vgall=VGroup()
        # vgindex,vgkey,vgvalue=self.GetVG_CreateSeries(valuelist,dskeylist,itemheight=0.3)
        # vgall.add(vgindex,vgkey,vgvalue).next_to(title,DOWN,aligned_edge=LEFT)
        # self.play(ShowCreation(vgindex),ShowCreation(vgkey),ShowCreation(vgvalue))
        # # 数据解说(行数)
        # self.ShowSubtitles('构造的pseries有16个元素,对应山东省16地市')
        # braces=Brace(vgvalue,RIGHT).set_color(BLACK)    # 大括号的使用
        # bracestext = braces.get_text("Series有16个元素")
        # bracestext.set_color(BLACK).scale(0.5)
        # self.play(GrowFromCenter(braces),Write(bracestext))
        # self.wait(0.5)
        # self.play(Uncreate(VGroup(braces,bracestext)))
        # # 数据解说（key值）
        # self.ShowSubtitles('其中索引值是地市名称')
        # rectindex=SurroundingRectangle(vgkey)
        # rectindex.set_color("#FF0000")
        # self.play(ShowCreationThenDestruction(rectindex),run_time=1)
        # # 数据解说（数据）
        # self.ShowSubtitles('数据为对应地市的2019年GDP值，单位亿元')
        # rectdata=SurroundingRectangle(vgvalue)
        # rectdata.set_color("#FF0000")
        # self.play(ShowCreationThenDestruction(rectdata),run_time=1)

        # # 不带key的选择
        # self.ShowSubtitles('第一种选择方式:选择前N项head()和选择后N项tial()')
        # commandlist=[
        #     'pseries.head()  # 选择前5个元素',
        #     'pseries.head(2) # 选择指定个数的前N个元素',
        #     'pseries.tial()  # 选择后5个元素',
        #     'pseries.tial(3) # 选择指定个数的后N个元素',
        #     'pseries[0]',
        #     'pseries[0:2]',
        #     'pseries[[3,5]]',
        #     'pseries.iloc[[4,6]] # iloc按照位置选择，iloc可以忽略',
        #     '''pseries['济南']=pseries.loc['济南'] # loc按照索引选择，loc可以忽略''', #9
        #     '''pseries[['济南','青岛']]=pseries.loc[['济南','青岛']] ''',
        #     '''pseries['济南':'临沂']] ''',
        #     'pseries[(pseries>4000)&(pseries<5000)]  #按照条件检索'
        #     ]
        # subtitlelist=[
        #     ['head()不带参数时，默认选择前5个元素'],
        #     ['head(N)带参数选择的前N个元素'],
        #     ['tile()默认选择最后5个元素'],
        #     ['head(N)带参数选择的前N个元素'],
        #     ['第二种选择方式，按照位置索引，同常规列表的选择方式相同，可以直接使用[]进行选择'],
        #     ['也可以象list一样进行切片'],
        #     ['也可以使用不连续的位置列表选择数据'],
        #     ['在进行位置检索数据时，等同于iloc'],
        #     ['第三种选择方式，按照索引进行选择'],   #9 
        #     ['选择指定索引的数据'],
        #     ['按照索引切片'],
        #     ['按照条件检索']
        # ]
        # selectindexlist=[[0,1,2,3,4],[0,1],[11,12,13,14,15],[13,14,15],[0],[0,1,2],[2,4],[3,5],
        #                  [1],[0,1],[1,2,3,4],[4,5]]
        # onerectflaglist=[False,False,False,False,True,False,False,False,
        #                 False,False,False,False]
        # # 选择数据
        # vgCode=VGroup()      
        # for commandindex in range(len(commandlist)):
        #     for strsubtitle in subtitlelist[commandindex]:
        #         self.ShowSubtitles(strsubtitle)
        #     code = Paragraph(
        #         commandlist[commandindex],
        #         font=self.code_font
        #     )
        #     code.set_color(self.code_incolor).set_all_lines_alignment('left').scale(self.code_scale)
        #     if commandindex==0:
        #         code.move_to(3*UP)
        #     else:
        #         code.next_to(vgCode[len(vgCode)-1],DOWN,buff=0.1,aligned_edge=LEFT)
        #     vgCode.add(code)
        #     self.play(Indicate(code))
        #     self.ShowSeries_DateRectangle(vgvalue,selectindexlist[commandindex],issplit=onerectflaglist[commandindex])
        #     self.wait()        
        # # 杂项操作
        # self.play(Uncreate(vgCode))
        # vgCode=VGroup()
        # self.ShowSubtitles('Series的其他操作包括:求元素个数、遍历、检查重复情况')
        # self.ShowSubtitles('Series的元素个数可通过三种方式获取len(),size,count()')   
        # code = Paragraph("求元素个数：",font=self.code_font).set_color(self.code_incolor).scale(self.code_scale).move_to(3*UP)
        # vgCode.add(code)
        # self.play(Indicate(code))
        # code0 = Paragraph("len(pseries)=16",font=self.code_font).set_color(self.code_incolor).scale(self.code_scale).move_to(3*UP)
        # code0.next_to(code,DOWN,buff=0.1,aligned_edge=LEFT)
        # vgCode.add(code0)
        # self.play(Indicate(code0))
        # code1 = Paragraph("pseries.size=16",font=self.code_font).set_color(self.code_incolor).scale(self.code_scale)
        # code1.next_to(code0,DOWN,buff=0.1,aligned_edge=LEFT)
        # vgCode.add(code1)
        # self.play(Indicate(code1))
        # code2 = Paragraph("pseries.count()=16",font=self.code_font).set_color(self.code_incolor).scale(self.code_scale)
        # code2.next_to(code1,DOWN,buff=0.1,aligned_edge=LEFT)
        # vgCode.add(code2)
        # self.play(Indicate(code2))
        



    def ShowDataFrame(self):
        '''
        DataFrame 相关知识
        '''
        pass
    
    def ShowPanel(self):
        '''
        Panel 相关知识
        '''
        pass
    
    def construct(self):
        # 全局变量设置
        self.Init_Setting()
        # Series 知识
        # self.ShowSerires()  
        # Series的创建
        # self.ShowSeries_Create()

        # select 的选择操作
        #self.ShowSeries_Select()

        # 多个Series操作
        self.ShowSeries_DataChange()

        return       
        # 片头
        self.ShowHead()
        # 视频主要内容
        self.ShowCatory()
        # 基础知识
        self.ShowBaseKnowledge()
        # DataFrame知识
        self.ShowDataFrame()
        # Panel 相关知识
        self.ShowPanel()
        

        
