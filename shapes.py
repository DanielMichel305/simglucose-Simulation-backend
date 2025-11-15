import dearpygui.dearpygui as dpg
from enum import Enum





class Shape:
    def __init__(self, startPos :tuple[int, int],fillColor : tuple[int, int, int,int] =(255,255,255,255), textLabel : str = "" , textLabelSize: int =14):
        self.xpos = startPos[0]
        self.ypos = startPos[1]
        self.textLabel = textLabel
        self.textLabelSize = textLabelSize
        self.fill = fillColor

class Circle(Shape):
    def __init__(self,center :tuple[int, int], radius :int, fillColor : tuple[int, int, int,int],textLabel : str = "" , textLabelSize: int =14):
        super().__init__(startPos=center, textLabel=textLabel, textLabelSize=textLabelSize, fillColor=fillColor)
        self.radius = radius
        dpg.draw_circle(center=center,radius=radius, fill=fillColor)
        dpg.draw_text(pos=center, text=self.textLabel, size=self.textLabelSize, color=(0,0,0,255))



class Rectangle(Shape):
    def __init__(self,v1 :tuple[int, int], height: int, width: int, fillColor : tuple[int, int, int,int],textLabel : str = "" , textLabelSize: int =14):
        super().__init__(startPos=v1, textLabel=textLabel, textLabelSize=textLabelSize, fillColor=fillColor)
        self.height = height
        self.width =width
        v2 = (v1[0] + width, v1[1] + height)

        dpg.draw_rectangle(pmin=v1, pmax=v2,fill=fillColor)
        
        txtPos = ((v1[0]+self.width/2.5)-len(textLabel) , (v2[0]+self.width)/2)
        dpg.draw_text(pos=txtPos, text=self.textLabel, size=self.textLabelSize, color=(0,0,0,255))  


class ShapeConnection():
    def __init__(self, shape1 : Shape, shape2: Shape):
        startPos = (shape1.xpos, shape1.ypos)
        endPos = (shape2.xpos, shape2.ypos)
        dpg.draw_arrow(startPos, endPos, color=(255,255,255,255))