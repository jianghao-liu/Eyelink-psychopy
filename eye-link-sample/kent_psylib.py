class PPTrigger:
	"""Wrapper class for calling parallel triggers in code for PsychoPy

	"""
	status = False #Is the parallel mode enabled?
	address = 0xE010 #What is the address?

	
	def __init__(self, win, address, status=True):
		"""Initialization of class with address required
		"""
		#Populate defaults
		self.status = status
		self.address = address
		self.win = win

		#Initialize parallel port if required
		if self.status == True:
			#Pull in library
			from psychopy import parallel
			self.parallel = parallel
			#Set the address
			self.parallel.setPortAddress(self.address)
			#Clear it right away
			self.clear()

	
	def fire(self,trigger,flip=True):
		"""Function to fire the trigger
		"""
		#Are we calling this trigger on a flip?
		if flip == True:
			self.win.callOnFlip(self.mainFire, trigger=trigger)
		else:
			#Nope - just fire.
			self.mainFire(trigger=trigger)
	
	
	def mainFire(self, trigger):
		"""Fires trigger, but defined to use as a callback on fire function
		"""
		if self.status == True:
			self.parallel.setData(trigger)
			
	def clear(self,trigger=0):
		"""Wrapper function to fire a clearing trigger ... 
		
		can override if needs to be different to 0
		"""
		self.mainFire(trigger)
		


class Eyetracker:
	"""Wrapper class for eyetracker configuration - should support other configurations
	"""
	enabled = False #Is the eyetracker enabled?
	io_config = "eyelink1000.yaml" #What is the YAML configuration path?  Eyelink1000.yaml config in same location is default
	recording = False #Are we recording?
	calibrating_mode = False #Are we in a calibration mode?

	def __init__(self, win, io_config="eyelink1000.yaml", enabled=True):
		"""Initialization of class with address required

		:param str msg: Marker/message to be sent to tracker
		"""	
		#Populate defaults
		self.enabled = enabled
		self.io_config = io_config
		self.win = win
		self.eyetracker = False
		self.io = False

		#Initialize eyetracker if enabled (via enabled)
		if self.enabled == True:
			from psychopy.iohub import EventConstants,ioHubConnection,load,Loader

			#Load the specified iohub configuration file converting it to a python dict.
			io_config_data = load(file(self.io_config,'r'), Loader=Loader)

			#Create an ioHubConnection instance, which starts the ioHubProcess, and informs it of the requested devices and their configurations.
			self.io = ioHubConnection(io_config_data)

			#Create a link to the tracker via iohub
			if self.io.getDevice('tracker'):
				self.eyetracker = self.io.getDevice('tracker')
		
		
	def isRecording(self):
		"""Return recording state
		"""	
		return self.recording
		
	def startRecording(self):
		"""Start recording
		"""
		
		#Only record if we have a valid eyetracker instance and we are not already recording
		if self.enabled == True and self.eyetracker and self.recording == False:
			self.io.clearEvents('all')
			self.eyetracker.setRecordingState(True)
			self.recording = True
			
	def stopRecording(self):
		"""Stop recording
		"""
		
		#Only stop recording if we are actually recording and have a valid eyetracker instance
		if self.enabled == True and self.eyetracker and self.recording == True:
			self.io.clearEvents('all')
			self.eyetracker.setRecordingState(False)
			self.recording = False
		
	def sendMarker(self, msg="default message"):
		"""Send a marker message to the eyetracker if we are active state

		:param str msg: Marker/message to be sent to tracker
		"""
		if self.enabled == True and self.eyetracker:
			self.io.clearEvents('all')
			self.eyetracker.sendMessage(str(msg))	

	def calibrate(self, resume_recording=True):
		"""Call up the calibration screen

		:param bool resume_recording: Should we automatically resume recording if we were recording?
		"""		
		was_recording = False
	
		#Only call if we have a valid eyetracker and not already calibrating
		if self.enabled == True and self.eyetracker and self.calibrating_mode == False:
			
			#If we are recording already, we need to stop it.
			if self.recording == True:
				was_recording = True
				#Stop it...
				self.stopRecording()
		
			#We are now calibrating...
			self.calibrating_mode = True
		
			#Now lets do calibration
			self.win.winHandle.set_visible(False)
			self.eyetracker.runSetupProcedure()
			self.win.fullscr = True
			self.win.winHandle.maximize()
			self.win.winHandle.set_visible(visible=True) 
			self.win.winHandle.set_fullscreen(True) 
			self.win.winHandle.activate()
			self.win._setCurrent()
			self.win.winHandle.switch_to()
			self.win.flip()
			
			#Now we are not calibrating...
			self.calibrating_mode = False
			
			#Do we need to resume?
			if was_recording == True and resume_recording == True:
				self.startRecording()
			