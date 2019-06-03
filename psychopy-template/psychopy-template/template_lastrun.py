#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.82.01), October 19, 2015, at 15:19
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'template'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'T:\\admin\\Projects\\2015-2016\\template.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1600, 1200), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
intro_text = visual.TextStim(win=win, ori=0, name='intro_text',
    text=u'Welcome to this experiment.\n\nPress space to start',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instructions_text = visual.TextStim(win=win, ori=0, name='instructions_text',
    text=u'Lots of instructions here.\n\nAnd here.\n\nPress space to continue',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "practice_prompt"
practice_promptClock = core.Clock()
prac_prompt_text = visual.TextStim(win=win, ori=0, name='prac_prompt_text',
    text=u'You are about to do a practice run.\n\nPress space to continue.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "prac_trial"
prac_trialClock = core.Clock()
prac_stim_text = visual.TextStim(win=win, ori=0, name='prac_stim_text',
    text=u'A single practice trial\n\nPress Z or M to respond.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "main_prompt"
main_promptClock = core.Clock()
main_prompt_text = visual.TextStim(win=win, ori=0, name='main_prompt_text',
    text=u'You are now about to start the main trial.\n\nPress space to continue.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
main_trial_stim_text = visual.TextStim(win=win, ori=0, name='main_trial_stim_text',
    text=u'A single main trial\n\nPress Z or M to respond.',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "End"
EndClock = core.Clock()
end_text = visual.TextStim(win=win, ori=0, name='end_text',
    text=u'Thank you for your participation!',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Intro"-------
t = 0
IntroClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
intro_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
intro_resp.status = NOT_STARTED
# keep track of which components have finished
IntroComponents = []
IntroComponents.append(intro_text)
IntroComponents.append(intro_resp)
for thisComponent in IntroComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Intro"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_text* updates
    if t >= 0.0 and intro_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        intro_text.tStart = t  # underestimates by a little under one frame
        intro_text.frameNStart = frameN  # exact frame index
        intro_text.setAutoDraw(True)
    
    # *intro_resp* updates
    if t >= 0.0 and intro_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        intro_resp.tStart = t  # underestimates by a little under one frame
        intro_resp.frameNStart = frameN  # exact frame index
        intro_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if intro_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instructions_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instructions_resp.status = NOT_STARTED
# keep track of which components have finished
InstructionsComponents = []
InstructionsComponents.append(instructions_text)
InstructionsComponents.append(instructions_resp)
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_text* updates
    if t >= 0.0 and instructions_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_text.tStart = t  # underestimates by a little under one frame
        instructions_text.frameNStart = frameN  # exact frame index
        instructions_text.setAutoDraw(True)
    
    # *instructions_resp* updates
    if t >= 0.0 and instructions_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_resp.tStart = t  # underestimates by a little under one frame
        instructions_resp.frameNStart = frameN  # exact frame index
        instructions_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if instructions_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

#------Prepare to start Routine "practice_prompt"-------
t = 0
practice_promptClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
prac_prompt_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
prac_prompt_resp.status = NOT_STARTED
# keep track of which components have finished
practice_promptComponents = []
practice_promptComponents.append(prac_prompt_text)
practice_promptComponents.append(prac_prompt_resp)
for thisComponent in practice_promptComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "practice_prompt"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = practice_promptClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_prompt_text* updates
    if t >= 0.0 and prac_prompt_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        prac_prompt_text.tStart = t  # underestimates by a little under one frame
        prac_prompt_text.frameNStart = frameN  # exact frame index
        prac_prompt_text.setAutoDraw(True)
    
    # *prac_prompt_resp* updates
    if t >= 0.0 and prac_prompt_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        prac_prompt_resp.tStart = t  # underestimates by a little under one frame
        prac_prompt_resp.frameNStart = frameN  # exact frame index
        prac_prompt_resp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if prac_prompt_resp.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_promptComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "practice_prompt"-------
for thisComponent in practice_promptComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practice_prompt" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
prac_trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'T:\\admin\\Projects\\2015-2016\\template.psyexp',
    trialList=[None],
    seed=None, name='prac_trials')
thisExp.addLoop(prac_trials)  # add the loop to the experiment
thisPrac_trial = prac_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisPrac_trial.rgb)
if thisPrac_trial != None:
    for paramName in thisPrac_trial.keys():
        exec(paramName + '= thisPrac_trial.' + paramName)

for thisPrac_trial in prac_trials:
    currentLoop = prac_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_trial.rgb)
    if thisPrac_trial != None:
        for paramName in thisPrac_trial.keys():
            exec(paramName + '= thisPrac_trial.' + paramName)
    
    #------Prepare to start Routine "prac_trial"-------
    t = 0
    prac_trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    prac_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    prac_resp.status = NOT_STARTED
    # keep track of which components have finished
    prac_trialComponents = []
    prac_trialComponents.append(prac_stim_text)
    prac_trialComponents.append(prac_resp)
    for thisComponent in prac_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "prac_trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = prac_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *prac_stim_text* updates
        if t >= 0.0 and prac_stim_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_stim_text.tStart = t  # underestimates by a little under one frame
            prac_stim_text.frameNStart = frameN  # exact frame index
            prac_stim_text.setAutoDraw(True)
        
        # *prac_resp* updates
        if t >= 0.0 and prac_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            prac_resp.tStart = t  # underestimates by a little under one frame
            prac_resp.frameNStart = frameN  # exact frame index
            prac_resp.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if prac_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "prac_trial"-------
    for thisComponent in prac_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "prac_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1 repeats of 'prac_trials'


#------Prepare to start Routine "main_prompt"-------
t = 0
main_promptClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
main_promptComponents = []
main_promptComponents.append(main_prompt_text)
main_promptComponents.append(key_resp_2)
for thisComponent in main_promptComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "main_prompt"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = main_promptClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *main_prompt_text* updates
    if t >= 0.0 and main_prompt_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        main_prompt_text.tStart = t  # underestimates by a little under one frame
        main_prompt_text.frameNStart = frameN  # exact frame index
        main_prompt_text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in main_promptComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "main_prompt"-------
for thisComponent in main_promptComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "main_prompt" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'T:\\admin\\Projects\\2015-2016\\template.psyexp',
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    main_resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    main_resp.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(main_trial_stim_text)
    trialComponents.append(main_resp)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *main_trial_stim_text* updates
        if t >= 0.0 and main_trial_stim_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            main_trial_stim_text.tStart = t  # underestimates by a little under one frame
            main_trial_stim_text.frameNStart = frameN  # exact frame index
            main_trial_stim_text.setAutoDraw(True)
        
        # *main_resp* updates
        if t >= 0.0 and main_resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            main_resp.tStart = t  # underestimates by a little under one frame
            main_resp.frameNStart = frameN  # exact frame index
            main_resp.status = STARTED
            # keyboard checking is just starting
            main_resp.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if main_resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                main_resp.keys = theseKeys[-1]  # just the last key pressed
                main_resp.rt = main_resp.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if main_resp.keys in ['', [], None]:  # No response was made
       main_resp.keys=None
    # store data for trials (TrialHandler)
    trials.addData('main_resp.keys',main_resp.keys)
    if main_resp.keys != None:  # we had a response
        trials.addData('main_resp.rt', main_resp.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock 
frameN = -1
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = []
EndComponents.append(end_text)
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "End"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if t >= 0.0 and end_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_text.tStart = t  # underestimates by a little under one frame
        end_text.frameNStart = frameN  # exact frame index
        end_text.setAutoDraw(True)
    if end_text.status == STARTED and t >= (0.0 + (3-win.monitorFramePeriod*0.75)): #most of one frame period left
        end_text.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
