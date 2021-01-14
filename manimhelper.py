from manimlib.imports import *
import os
import pyclbr
from pandas import Series
import pandas as pd

class SeriesSharphelper():
    def __init__(self,
            itemheight=0.7,
            indexwidth=0.5,indexfillcolor="#FCCA9F",indexbordercolor=BLACK,indextxtcolor=BLACK,indextxtfont='宋体',indextxtscale=0.5,
            keywidth=2,keyfillcolor="#FCCA9F",keybordercolor=BLACK,keytxtcolor=BLACK,keytxtfont='宋体',keytxtscale=0.5,
            valuewidth=2,valuefillcolor="#FCCA9F",valuebordercolor=BLACK,valuetxtcolor=BLACK,valuetxtfont='宋体',valuetxtscale=0.5,

            code_font='宋体',
            ishavekey=True,
            isshowkey=True):
        self.itemheight=itemheight

        self.indexwidth=indexwidth
        self.indexfillcolor=indexfillcolor
        self.indexbordercolor=indexbordercolor
        self.indextxtcolor=indextxtcolor   
        self.indextxtfont=indextxtfont
        self.indextxtscale=indextxtscale

        self.keywidth=keywidth
        self.keyfillcolor=keyfillcolor
        self.keybordercolor=keybordercolor
        self.keytxtcolor=keytxtcolor  
        self.keytxtfont=keytxtfont
        self.keytxtscale=keytxtscale       

        self.valuewidth=valuewidth
        self.valuefillcolor=valuefillcolor
        self.valuebordercolor=valuebordercolor
        self.valuetxtcolor=valuetxtcolor  
        self.valuetxtfont=valuetxtfont
        self.valuetxtscale=valuetxtscale   

        self.code_font=code_font
        self.ishavekey=ishavekey
        self.isshowkey=isshowkey
    
    def getSeriesRectangle(self,series):
        '''
        得到series的矩形范围
        '''
        index_txt_Group=VGroup()     #所有index 的txt 的Group
        index_rect_Group=VGroup()    #所有index 的矩形Group

        key_txt_Group=VGroup()
        key_rect_Group=VGroup()

        value_txt_Group=VGroup()
        value_rect_Group=VGroup()

        all_txt_Group=VGroup()
        all_rect_Group=VGroup()

        pre_index_rect=None         # 上一个index的矩形
        pre_index_txt=None          # 上一个index的文本
        pre_key_rect=None           # 上一个key的矩形
        pre_key_txt=None            # 上一个key的文本    
        pre_value_rect=None         # 上一个value的矩形
        pre_value_txt=None          # 上一个value的文本

        allrow_Group=VGroup()       # 按照行方式排列的各个组，每个元素是一个group

        allvg=VGroup()              # 所有内容的Group

        for i in range(series.size):
            # 索引列处理
            index_rect=Rectangle(height=self.itemheight,width=self.indexwidth,color=self.indexbordercolor)
            index_rect.set_fill(color=self.indexfillcolor,opacity=1)
            index_txt = Paragraph(
                '{}'.format(i),
                font=self.indextxtfont,
                color=self.indextxtcolor
            )
            index_txt.scale(self.indextxtscale)
            if pre_index_rect: # 如果不是第一个，临近上一个
                index_rect.next_to(pre_index_rect,DOWN,buff=0,aligned_edge=LEFT)
                index_txt.next_to(pre_index_txt,DOWN,buff=self.itemheight,aligned_edge=TOP)
                index_txt.align_to(pre_index_txt,LEFT)
            else:           # 是第一行内容
                pass
            pre_index_rect=index_rect
            pre_index_txt=index_txt
            index_rect_Group.add(index_rect)
            index_txt_Group.add(index_txt)

            # key值列的处理
            if self.ishavekey and self.isshowkey:
                key_rect=Rectangle(height=self.itemheight,width=self.keywidth,color=self.keybordercolor)
                key_rect.set_fill(color=self.keyfillcolor,opacity=1).next_to(index_rect,RIGHT,buff=0,aligned_edge=TOP)
                key_txt = Paragraph(
                    '{}'.format(series.index[i]),
                    font=self.keytxtfont,
                    color=self.keytxtcolor
                )
                if pre_key_rect:
                    key_rect.next_to(pre_key_rect,DOWN,buff=0,aligned_edge=LEFT)
                    key_txt.scale(self.keytxtscale).next_to(pre_key_txt,DOWN,buff=self.itemheight,aligned_edge=TOP)
                    key_txt.align_to(pre_key_txt,LEFT)
                else:
                    key_txt.next_to(index_rect,RIGHT,buff=0.0).scale(self.keytxtscale)
                pre_key_txt=key_txt
                pre_key_rect=key_rect
                
                key_txt_Group.add(key_txt)
                key_rect_Group.add(key_rect)

            # value 值的处理
            value_rect=Rectangle(height=self.itemheight,width=self.keywidth,color=self.keybordercolor)
            leftrect=None   # 左边的矩形
            if self.ishavekey and self.isshowkey:
                leftrect=key_rect
            else:
                leftrect=index_rect
            value_rect.set_fill(color=self.valuefillcolor,opacity=1).next_to(leftrect,RIGHT,buff=0,aligned_edge=TOP)
            value_txt = Paragraph(
                '{}'.format(series[i]),
                font=self.valuetxtfont,
                color=self.valuetxtcolor
            )
            if pre_value_rect:
                value_rect.next_to(pre_value_rect,DOWN,buff=0,aligned_edge=LEFT)
                value_txt.scale(self.valuetxtscale).next_to(pre_value_txt,DOWN,buff=self.itemheight,aligned_edge=TOP)
                value_txt.align_to(pre_value_txt,LEFT)
            else:
                value_txt.next_to(leftrect,RIGHT,buff=0.1).scale(self.keytxtscale)

            pre_value_txt=value_txt
            pre_value_rect=value_rect
            
            value_txt_Group.add(value_txt)
            value_rect_Group.add(value_rect)

            all_txt_Group.add(index_txt,key_txt,value_txt)
            all_rect_Group.add(index_rect,key_rect,value_rect)
            allrow_Group.add(VGroup(index_rect,index_txt,key_rect,key_txt,value_rect,value_txt))
        allvg.add(all_rect_Group,all_txt_Group)        
        return index_txt_Group,index_rect_Group,\
            key_txt_Group,key_rect_Group,\
            value_txt_Group,value_rect_Group,\
            all_txt_Group,all_rect_Group,\
            allrow_Group,allvg


class DataFrameSharphelper():
    def __init__(self,
            itemheight=0.7,
            indexwidth=0.5,indexfillcolor="#FCCA9F",indexbordercolor=BLACK,indextxtcolor=BLACK,indextxtfont='宋体',indextxtscale=0.5,
            keywidth=2,keyfillcolor="#FCCA9F",keybordercolor=BLACK,keytxtcolor=BLACK,keytxtfont='宋体',keytxtscale=0.5,
            valuewidth=2,valuefillcolor="#FCCA9F",valuebordercolor=BLACK,valuetxtcolor=BLACK,valuetxtfont='宋体',valuetxtscale=0.5,

            code_font='宋体',
            ishavekey=True,
            isshowkey=True):
        self.itemheight=itemheight

        self.indexwidth=indexwidth
        self.indexfillcolor=indexfillcolor
        self.indexbordercolor=indexbordercolor
        self.indextxtcolor=indextxtcolor   
        self.indextxtfont=indextxtfont
        self.indextxtscale=indextxtscale

        self.keywidth=keywidth
        self.keyfillcolor=keyfillcolor
        self.keybordercolor=keybordercolor
        self.keytxtcolor=keytxtcolor  
        self.keytxtfont=keytxtfont
        self.keytxtscale=keytxtscale       

        self.valuewidth=valuewidth
        self.valuefillcolor=valuefillcolor
        self.valuebordercolor=valuebordercolor
        self.valuetxtcolor=valuetxtcolor  
        self.valuetxtfont=valuetxtfont
        self.valuetxtscale=valuetxtscale   

        self.code_font=code_font
        self.ishavekey=ishavekey
        self.isshowkey=isshowkey

    def getDataFrameRectangle(self,dataframe):
        '''
        得到数据框的矩形范围
        '''
        index_txt_Group=VGroup()     #所有index 的txt 的Group
        index_rect_Group=VGroup()    #所有index 的矩形Group

        key_txt_Group=VGroup()
        key_rect_Group=VGroup()

        value_txt_Group=VGroup()
        value_rect_Group=VGroup()

        all_txt_Group=VGroup()
        all_rect_Group=VGroup()

        pre_index_rect=None         # 上一个index的矩形
        pre_index_txt=None          # 上一个index的文本
        pre_key_rect=None           # 上一个key的矩形
        pre_key_txt=None            # 上一个key的文本    
        pre_value_rect=None         # 上一个value的矩形
        pre_value_txt=None          # 上一个value的文本

        allrow_Group=VGroup()       # 按照行方式排列的各个组，每个元素是一个group（按照矩形，文本，矩形，文本的方式排列）

        allvg=VGroup()              # 所有内容的Group
        
        valuetxt_Grouplist=[]           # 因为数据框的列是变化的，这里用list存储各个列的txtvg
        valuerect_Grouplist=[]          # 因为数据框的列是变化的，这里用list存储各个列的txtvg

        header_Group=VGroup()
        
        # 针对每行循环
        for i in range(len(dataframe.index)):
            rowGroup=VGroup()
            # region 索引列处理
            index_rect=Rectangle(height=self.itemheight,width=self.indexwidth,color=self.indexbordercolor)
            index_rect.set_fill(color=self.indexfillcolor,opacity=1)
            index_txt = Paragraph(
                '{}'.format(i),
                font=self.indextxtfont,
                color=self.indextxtcolor
            )
            index_txt.scale(self.indextxtscale)
            if pre_index_rect: # 如果不是第一个，临近上一个
                index_rect.next_to(pre_index_rect,DOWN,buff=0,aligned_edge=LEFT)
                index_txt.next_to(pre_index_txt,DOWN,buff=self.itemheight,aligned_edge=TOP)

            pre_index_rect=index_rect
            pre_index_txt=index_txt
            index_rect_Group.add(index_rect)
            index_txt_Group.add(index_txt)
            # 每行累计
            rowGroup.add(index_rect,index_txt)
            all_txt_Group.add(index_txt)
            all_rect_Group.add(index_rect)
            # endregion

            # region key值列的处理
            if self.ishavekey and self.isshowkey:
                key_rect=Rectangle(height=self.itemheight,width=self.keywidth,color=self.keybordercolor)
                key_rect.set_fill(color=self.keyfillcolor,opacity=1).next_to(index_rect,RIGHT,buff=0,aligned_edge=TOP)
                key_txt = Paragraph(
                    '{}'.format(dataframe.index[i]),
                    font=self.keytxtfont,
                    color=self.keytxtcolor
                )
                key_txt.scale(self.keytxtscale)
                if pre_key_rect:
                    key_rect.next_to(pre_key_rect,DOWN,buff=0,aligned_edge=LEFT)
                # txt的位置依据对应的矩形位置而定                
                key_txt.next_to(key_rect,RIGHT,buff=-0.9,aligned_edge=LEFT)
                   
                pre_key_rect=key_rect
                
                key_txt_Group.add(key_txt)
                key_rect_Group.add(key_rect)
                # 每行累计
                rowGroup.add(key_rect,key_txt)                
                all_txt_Group.add(key_txt)
                all_rect_Group.add(key_rect)
            # endregion

            # region value 值的处理
            pre_value_rect=None
            # 行循环中的列循环
            for colindex in range(len(dataframe.columns)):
                valuetxt_Grouplist.append(VGroup())
                valuerect_Grouplist.append(VGroup())
                isfirstvalue=colindex==0  #是否是第一列
                value_rect=Rectangle(height=self.itemheight,width=self.valuewidth,color=self.valuebordercolor).set_fill(color=self.valuefillcolor,opacity=1)
                if isfirstvalue: # 如果是第一个value 列 则左边的rect是索引（key）的矩形
                    if self.ishavekey and self.isshowkey:
                        pre_value_rect=key_rect
                    else:
                        pre_value_rect=index_rect
                value_txt = Paragraph(
                    '{}'.format(dataframe[dataframe.columns.values[colindex]][i]),
                    font=self.valuetxtfont,
                    color=self.valuetxtcolor
                )
                value_txt.scale(self.valuetxtscale)
                value_rect.next_to(pre_value_rect,RIGHT,buff=0,aligned_edge=TOP)
                value_txt.next_to(value_rect,RIGHT,buff=-0.9,aligned_edge=LEFT)
                rowGroup.add(value_rect,value_txt)

                valuetxt_Grouplist[colindex].add(value_txt)
                valuerect_Grouplist[colindex].add(value_rect)

                pre_value_rect=value_rect
                            
                value_txt_Group.add(value_txt)
                value_rect_Group.add(value_rect)

                all_rect_Group.add(value_rect_Group)
                all_txt_Group.add(value_txt_Group)

            # endregion
            allrow_Group.add(rowGroup)
        allvg.add(all_rect_Group,all_txt_Group)  
        # 最后处理表头（对齐内容按照下面的表格对齐）        
        header_Group=VGroup()   
        head_index_rect=Rectangle(height=self.itemheight,width=self.indexwidth,color=self.indexbordercolor).set_fill(color=self.indexfillcolor,opacity=1)
        head_leftrect=head_index_rect
        header_Group.add(head_index_rect)
        if self.ishavekey and self.isshowkey:
            head_key_rect=Rectangle(height=self.itemheight,width=self.keywidth,color=self.keybordercolor).set_fill(color=self.keyfillcolor,opacity=1)
            head_key_rect.next_to(head_leftrect,RIGHT,buff=0)
            head_leftrect=head_key_rect
            header_Group.add(head_key_rect)
        for colindex in range(len(dataframe.columns)):
            head_value_rect=Rectangle(height=self.itemheight,width=self.valuewidth,color=self.valuebordercolor).set_fill(color=self.valuefillcolor,opacity=1)
            head_value_rect.next_to(head_leftrect,RIGHT,buff=0)
            head_leftrect=head_value_rect   
            head_value_txt= Paragraph(
                    '{}'.format(dataframe.columns.values[colindex]),
                    font=self.valuetxtfont,
                    color=self.valuetxtcolor
                )
            head_value_txt.next_to(head_value_rect,RIGHT,buff=-0.9,aligned_edge=LEFT).scale(self.valuetxtscale)
            header_Group.add(head_value_rect,head_value_txt)
        header_Group.next_to(index_rect_Group,TOP,buff=0,aligned_edge=LEFT)
        header_Group.align_to(index_rect_Group,LEFT)
        allvg.add(header_Group)
        return index_txt_Group,index_rect_Group,\
            key_txt_Group,key_rect_Group,\
            value_rect_Group,value_txt_Group,\
            all_txt_Group,all_rect_Group,\
            valuerect_Grouplist,valuetxt_Grouplist,\
            allrow_Group,header_Group,\
            allvg

class SubTitle():
    def __init__():
        pass

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

class codeboxHelper():
    def __init__(self,
        topborder=1,
        rightborder=1,
        downborder=1,
        codewidth=6,

        background_color=WHITE,
        background_opacity=1,
        background_stroke_color=WHITE,
        background_stroke_opacity=1,
        
        surface_fill_color=WHITE,
        surface_fill_opacity=1,

        code_stroke_color=BLACK,
        code_fill_color="#EBEBEB"
        ):

        self.topborder=topborder
        self.rightborder=rightborder
        self.downborder=downborder
        self.codewidth=codewidth

        self.background_color=background_color                      # 背景层相关属性
        self.background_opacity=background_opacity
        self.background_stroke_color=background_stroke_color
        self.background_stroke_opacity=background_stroke_opacity

        self.surface_fill_color=surface_fill_color
        self.surface_fill_opacity=surface_fill_opacity

        self.code_stroke_color=code_stroke_color
        self.code_fill_color=code_fill_color


    def GetSourceCodeBoxGroup(self):
        '''
        得到源代码Group（Z-index=0.2----0.1）
        '''
        vgall=VGroup()

        # region 背景层
        clientWidth=15
        clientheight=8.8
        rectbg=Rectangle(height=clientheight,width=clientWidth,          
            opacity=0.5,
            fill_color=self.background_color,
            fill_opacity=self.background_opacity,
            stroke_color=self.background_stroke_color,
            stroke_opacity=self.background_stroke_opacity) 
        rectbg.shift(IN*0.2)        
        vgall.add(rectbg)        
        # endregion 

        # region四个矩形
        # 4.4*7.5    8.8*15
        recttop=Rectangle(
            height=self.topborder,
            width=clientWidth,          
            opacity=0.5,
            fill_color=self.surface_fill_color,
            fill_opacity=self.background_opacity,
           ) 
        recttop.shift((clientheight/2-self.topborder)*UP)

        rectdown=Rectangle(
            height=self.downborder,
            width=clientWidth,          
            opacity=0.5,
            fill_color=self.surface_fill_color,
            fill_opacity=self.background_opacity) 
        rectdown.shift((clientheight/2-self.downborder)*DOWN)

        rectright=Rectangle(
            height=clientheight,
            width=self.rightborder,          
            opacity=0.5,
            fill_color=self.surface_fill_color,
            fill_opacity=self.background_opacity) 
        rectright.shift((clientWidth/2-self.rightborder)*RIGHT)

        wleft=(clientWidth-self.rightborder-self.codewidth)/2
        border1=clientWidth/2-wleft
        rectleft=Rectangle(
            height=clientheight,
            width=clientWidth-self.rightborder-self.codewidth,          
            opacity=0.5,
            fill_color=self.surface_fill_color,
            fill_opacity=self.background_opacity) 
        rectleft.shift(border1*LEFT)
        

        vg=VGroup(recttop,rectdown,rectright,rectleft)
        vg.shift(IN*0.1)
        vgall.add(vg)
        # endregion

        # region 顶部的边框矩形
        rectbox=Rectangle(
            height=clientheight-self.topborder-self.downborder,
            width=self.codewidth,
            fill_color=self.code_fill_color,
            fill_opacity=1,
            stroke_color=self.code_stroke_color,
            stroke_opacity=1
            )
        right1=clientWidth/2-self.codewidth/2-self.rightborder
        rectbox.move_to(IN*0.09+right1*RIGHT)
        vgall.add(rectbox)
        # endregion

        return vgall

class test(Scene):
    def construct(self):
        # sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
        # ser=Series(sdata)

        # df={'Name':Series(['xinzhihai','xinlingxi','zhaojinhong'],index=['a','b','c']),
        #     'Age':Series([44,16,45],                            index=['a','b','c']),
        #     'Sex':Series(['male','female','mail'],              index=['a','b','c'])}
        # dataframe=pd.DataFrame(df)
        # print(dataframe)

        # helper=Sharphelper(ishavekey=True)
        # _,_,_,_,_,_,_,_,valuerect_Grouplist,valuetxt_Grouplist,allrow_Group,header,allvg=helper.getDataFrameRectangle(dataframe)
        # allvg.move_to(2*LEFT)
        # # self.play(ShowCreation(allvg))
        # self.play(GrowFromCenter(allvg))
        # self.play(Indicate(header))
        # self.wait()
        code=codeboxHelper()
        vg=code.GetSourceCodeBoxGroup()
        self.play(ShowCreation(vg))

       