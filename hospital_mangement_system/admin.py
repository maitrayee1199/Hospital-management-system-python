from tkinter import *
import h_backend
class MyCanvas(Canvas):
    def define(self,data, parent=None, img=None, *parms, **kparms):
        self.backend=h_backend.h_backend()
        Canvas.__init__(self, parent, *parms, **kparms)
        self._width =  1000;
        self._height = 5000;
        self._starting_drag_position = ()
        self.config(width = self._width, height=self._height, bg='green')
        self._draw_some_example_objects(data)
        self._add_scrollbars()        
        self._addMouseBindings()
        self.pack(fill=BOTH, expand=YES)
    def _add_scrollbars(self):
        self.sbarV = Scrollbar(self.master, orient=VERTICAL)
        self.sbarH = Scrollbar(self.master, orient=HORIZONTAL)
        self.sbarV.config(command=self.yview)
        self.sbarH.config(command=self.xview)
        self.config(yscrollcommand=self.sbarV.set)  
        self.config(xscrollcommand=self.sbarH.set)
        self.sbarV.pack(side=RIGHT, fill=Y)  
        self.sbarH.pack(side=BOTTOM, fill=X)
    def _addMouseBindings(self):    
        self.bind('<4>', lambda event : self.yview('scroll', -1, 'units'))# mouse wheel scroll
        self.bind('<5>', lambda event : self.yview('scroll', 1, 'units'))        
        self.bind("<Button-2>", self.__start_scroll)# dragging canvas with mouse middle button 
        self.bind("<B2-Motion>", self.__update_scroll)
        self.bind("<ButtonRelease-2>", self.__stop_scroll) 
    def __start_scroll(self, event):
        self.config(yscrollincrement=3)# set the scrolling increment. 
        self.config(xscrollincrement=3)# value of 0 is unlimited and very fast 
        self._starting_drag_position = (event.x, event.y)# set it to 1,2,3 to make it slower
        self.config(cursor="fleur")
    def __update_scroll(self, event):
        deltaX = event.x - self._starting_drag_position[0]
        deltaY = event.y - self._starting_drag_position[1]
        self.xview('scroll', deltaX, 'units')
        self.yview('scroll', deltaY, 'units')
        self._starting_drag_position =  (event.x, event.y)
    def __stop_scroll(self, event):
        self.config(xscrollincrement=0) # set scrolling speed back to 0, so that mouse scrolling 
        self.config(yscrollincrement=0)# works as expected.
        self.config(cursor="")
    def _draw_some_example_objects(self,data):
        self.config(scrollregion=(0,0, self._width, self._height),bg='white')  
        self.create_text(0,0,anchor='nw',text=data)

    
