
import datetime
from multiprocessing import log_to_stderr
import time
import threading
from collections import deque
from xml.etree.ElementTree import TreeBuilder





################################################################################
#   Handle all connections and rights for the server
################################################################################
class pump1():


	name = None
	priority = -1
	period = -1
	execution_time = -1
	last_deadline = -1
	last_execution_time = None
	preempted = False


	############################################################################
	def __init__(self, name,period, execution_time ,last_execution):

		self.name = name
		self.period = period
		self.execution_time = execution_time
		self.last_execution_time = last_execution

	############################################################################
	def run(self):

		# Update last_execution_time
		self.last_execution_time = datetime.datetime.now()

	
		global tank
		
		execTime = self.execution_time
		
		
		
		while (tank <= 40  ):
			
			
			tank += 10
			print( "producing 10 oil, you now have :"+ str(tank) + " Oil" )
			execTime -= 1

			time.sleep(1)

			if (execTime <= 0):
				
				return
			
            
		

################################################################################
#   Handle all connections and rights for the server
################################################################################
class pump2():


	name = None
	period = -1
	execution_time = -1
	last_deadline = -1
	last_execution_time = None


	############################################################################
	def __init__(self, name,period, execution_time ,last_execution):

		self.name = name
		self.period = period
		self.execution_time = execution_time
		self.last_execution_time = last_execution
		

	############################################################################
	def run(self):

		# Update last_execution_time
		self.last_execution_time = datetime.datetime.now()

		
		global tank
		
		
		execTime = self.execution_time

		
		
		
		while (tank <= 30 ):
			
			
			tank += 20
			print( "producing 20 oil, you now have " + str(tank) + " Oil" )
			execTime -= 1

			time.sleep(1)

			if (execTime <= 0):
				time.sleep(self.period)
				return
			

		################################################################################
#   Handle all connections and rights for the server
################################################################################
class machine1():


	name = None
	priority = -1
	execution_time = -1
	last_deadline = -1
	last_execution_time = None



	############################################################################
	def __init__(self, name,period, execution_time ,last_execution):

		self.name = name
		self.period = period
		self.execution_time = execution_time
		self.last_execution_time = last_execution
		


	############################################################################
	def run(self):

		# Update last_execution_time
		self.last_execution_time = datetime.datetime.now()

		
		global tank 
		
		
		execTime = self.execution_time

		
		global stock1
		
		
		while (tank >= 25 and stock1 <= (stock2 /4)  ):
			
			print( "Consuming 25 oil" )
			tank-= 25
			print("producing 1 motor")
			stock1 += 1
			execTime -= 1
			time.sleep(1)
			if (execTime <= 0):
				time.sleep(self.period)
				return
			


		################################################################################
#   Handle all connections and rights for the server
################################################################################
class machine2():


	name = None
	execution_time = -1
	last_deadline = -1
	last_execution_time = None
	preempted = False


	############################################################################
	def __init__(self, name,period, execution_time ,last_execution):

		self.name = name
		self.period = period
		self.execution_time = execution_time
		self.last_execution_time = last_execution
		


	############################################################################
	def run(self):

		# Update last_execution_time
		self.last_execution_time = datetime.datetime.now()

		
		global tank , stock2 
		
		execTime = self.execution_time

		
		global stock2
		
		
		while (tank >= 5 and stock1 > (stock2 /4)  ):
			
			print( "Consuming 5 oil" )
			tank-= 5
			print("producing 1 wheel")
			stock2 += 1
			execTime -= 1
			time.sleep(1)
			if (execTime <= 0):
				time.sleep(self.period)
				return
			
####################################################################################################
#
#
#
####################################################################################################
if __name__ == '__main__':
	
	global tank, stock1, stock2
	tank = 0
	stock1 = 0
	stock2 = 0
	

	last_execution = datetime.datetime.now()

	# Instanciation of task objects
	task_list = []
	task_list.append \
        (pump1(name="pump1", period = 5, execution_time = 2, last_execution = last_execution))
	task_list.append \
        (pump2(name="pump2",  period = 15,execution_time = 3, last_execution = last_execution))
	task_list.append \
        (machine1(name="machine1", period = 5,execution_time = 5, last_execution = last_execution))
	task_list.append \
    (machine2(name="machine2",  period = 5,execution_time = 5, last_execution = last_execution))


	# Global scheduling loop
	while(1):
		
		print("You now have " + str(stock1) + " motor " + str(stock2) + " wheels at :" + datetime.datetime.now().strftime("%H:%M:%S") )

		for task_to_run in task_list :
			task_to_run.run()









