#!/usr/bin/env python
import sys,types
import pyPS4Controller.controller as ds4bt
sprint=sys.stdout.write
ds4=types.SimpleNamespace()
class DS4(ds4bt.Controller):
	def __init__(self, **kwargs):		ds4bt.Controller.__init__(self, **kwargs)
	def on_L3_left(self,value)	:		L3x(value)
	def	on_L3_right(self,value)	:		L3x(value)
	def on_L3_up(self,value)		:		L3y(value)
	def on_L3_down(self,value)	:		L3y(value)

	def on_R3_left(self,value)	:		R3x(value)
	def	on_R3_right(self,value)	:		R3x(value)
	def on_R3_up(self,value)		:		R3y(value)
	def on_R3_down(self,value)	:		R3y(value)

	def on_R3_x_at_rest(self)		:		pass
	def on_R3_y_at_rest(self)		:		pass
	def on_L3_x_at_rest(self)		:		pass
	def on_L3_y_at_rest(self)		:		pass
def start()	-> None :
	sprint('\033[1;1H\033[3;1H')
	sprint('L3 (L-Stick):\033[1EX : 0\033[1EY : 0\033[1E\033[1E')
	sprint('R3 (R-Stick):\033[1EX : 0\033[1EY : 0\033[1E\033[1E')
	sprint('\033[1;1H')
	ds4.bt1=DS4(interface="/dev/input/js0", connecting_using_ds4drv=False)
	ds4.bt1.listen()
	return
def L3x(n)	-> None :
	upd(4, n)
	log('l','x',n)
def L3y(n)	-> None :
	upd(5, n)
	log('l','y',n)
def R3x(n)	-> None :
	upd(8, n)
	log('r','x',n)
def R3y(n)	-> None :
	upd(9, n)
	log('r','y',n)

def upd(c,n)		-> None :
	sprint(f'\033[6;1H\033[{c};5H{" " if n >= 0 else "-"}{str(abs(n))}\033[6;1H')
	
def log(s,a,v) 	-> None :
	with open(f'{s.upper()}3_{a}.log', 'a') as f:
		f.write(f'{str(v)}\n')
		f.flush()
		
start()

