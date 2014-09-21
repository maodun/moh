#coding=utf-8
#author: maodun

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import web
import urllib

urls = (
    '/','main',
    '/mouse/(.+)','mouse',
    )

render = web.template.render('templates/')

password = "maodun"

class main:
    def auth(self):
        authcookie = web.cookies().get('auth')
        if(authcookie == password):
            return True
        else:
            return False
    def GET(self):
        if(self.auth()):
            return render.main()
        else:
            return render.pw()
    
    def POST(self):
        pa = web.data()
        index = pa.find("=")
        if(pa[:index] == "pw" and urllib.unquote_plus(pa[index+1:])==password):
            web.setcookie('auth',password,60*60)
            web.redirect('/')
        else:
            return render.pw()
        

from pymouse import PyMouse
ms = PyMouse()
wid,hei = ms.screen_size()
horhop = wid/80
verhop = hei/40

import json

class mouse():
    def auth(self):
        authcookie = web.cookies().get('auth')
        if(authcookie == password):
            return True
        else:
            return False
    def GET(self,typeid):
        if(not self.auth()):
            return render.pw()
        
        web.header('content-type','text/json')
        c_x,c_y = ms.position()
        if('x' in typeid):
            xw = int(typeid[1:])
            new_x = wid*xw/100
            ms.move(new_x,c_y)
            nx,ny = ms.position() 
            result = {'x':str(nx*100/wid)+'%','y':str(ny*100/hei)+'%'}
            return json.dumps(result)
        elif('y' in typeid):
            yw = int(typeid[1:])
            new_y = hei*yw/100
            ms.move(c_x,new_y)
            nx,ny = ms.position() 
            result = {'x':str(nx*100/wid)+'%','y':str(ny*100/hei)+'%'}
            return json.dumps(result)
        else:
            ty = 0
            ty = int(typeid)
        
        if(ty==0):
            #current mouse postion
            result = {'x':str(c_x*100/wid)+'%','y':str(c_y*100/hei)+'%'}
            return json.dumps(result)
        
        elif(ty==1):
            #move left up
            
            new_x = c_x - horhop
            new_y = c_y - verhop
            ms.move(new_x,new_y)
            
        elif(ty==2):
            #move up
            
            new_x = c_x
            new_y = c_y - verhop
            ms.move(new_x,new_y)
            
        elif(ty==3):
            #move right up
            
            new_x = c_x + horhop
            new_y = c_y - verhop
            ms.move(new_x,new_y)
            
        elif(ty==4):
            #move left
            
            new_x = c_x - horhop
            new_y = c_y 
            ms.move(new_x,new_y)
            
        elif(ty==5):
            #move click
            
            new_x = c_x
            new_y = c_y
            ms.click(new_x,new_y,1)
            
        elif(ty==6):
            #move right
            
            new_x = c_x + horhop
            new_y = c_y
            ms.move(new_x,new_y)
            
        elif(ty==7):
            #move left down
            
            new_x = c_x - horhop
            new_y = c_y + verhop
            ms.move(new_x,new_y)
            
        elif(ty==8):
            #move down
            
            new_x = c_x 
            new_y = c_y + verhop
            ms.move(new_x,new_y)
            
        elif(ty==9):
            #move right down
            
            new_x = c_x + horhop
            new_y = c_y + verhop
            ms.move(new_x,new_y)
            
        elif(ty==10):
            #move middle click
            
            new_x = c_x
            new_y = c_y
            
            ms.click(new_x,new_y,3)
            
        elif(ty==11):
            #move right click
            
            new_x = c_x
            new_y = c_y
            
            ms.click(new_x,new_y,2)
            
        elif(ty==12):
            #move double left click
            
            new_x = c_x
            new_y = c_y
            
            ms.click(new_x,new_y,1,2)
            
        else:
            return i.t
        nx,ny = ms.position() 
        result = {'x':str(nx*100/wid)+'%','y':str(ny*100/hei)+'%'}
        return json.dumps(result)
        

    def POST(self):
        pass


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

