class Preprocessing():
    #@staticmethod
    def __init__(self,data):
        self.data = data
    def converttoyolo(self):
        #getting width and height value 
        h1,h2 = self.data['width'],self.data['height']
        #h1 = 1024
        #h2 = 960
        #differantial of width and height
        dw = 1. / h1
        dh = 1. / h2
        
        #fetching bounding box values
        bbox = self.data['bbox']
        x = bbox.str[0]
        y = bbox.str[1]
        w = bbox.str[2]
        h = bbox.str[3]
        self.data['xmin'] = x
        self.data['ymin'] = y
        self.data['xmax'] = w
        self.data['ymax'] = h
        
        #creating a new columns
        self.data['x'] = " "
        self.data['y'] = " "
        self.data['w'] = " "
        self.data['h'] = " "
        
        #converrting cooo format bbox to yolo format bbox [x,y,w,h]
        self.data['x'] = (self.data['xmax'] + self.data['xmin'])*dw/2
        self.data['y'] = (self.data['ymin'] + self.data['ymax'])*dh/2
        self.data['w'] = (self.data['xmax'])/h1
        self.data['h'] = (self.data['ymax'])/h2

        #droppping extra columns
        self.data = self.data.drop(['xmin', 'ymin', 'xmax', 'ymax','height',
        'width','id_x','license_x','image_id','segmentation','iscrowd','bbox','area','license_y'], axis=1)
        return self.data
        
        
    
        
    def replace(self):

        #since yolo excepts only value starting from 0-n during training
        self.data['category_id'] = self.data['category_id'].replace({1: 0, 2: 1})
        return self.data
    