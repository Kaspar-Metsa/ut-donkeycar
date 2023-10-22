# Project report
Project for autonomous driving course in UT where we train a model on donkeycar to drive the car autonomously.


# Work done
* Established connection with the car
* Installed the software to interact with donkeycar
* Debugged and solved many problems regarding the joystick controller, battery and running the software
* Recorded training data by driving the car in the track
* Trained the model based on the training data
* Used the trained model for steering, throttle was controlled with joystick by the user
* Car was able to traverse the track without crashing
  * Car was able to avoid the obstacles
* Movies presenting model's performance available here: https://drive.google.com/drive/folders/1je0wvIU8TGhNiOAY3CBUKet5GKjQtLky

## Steering model
For our steering model, we used a default architecture of linear model proposed by Donkeycar. The model was trained on the raw data gathered during driving, without any cropping or image preprocessing.

In our initial training attempt, we utilized approximately 8,000 frames, which equated to around 8 laps recorded on a track without any obstacles, driving only in a counterclockwise direction. As can be seen in the generated movie, the model's performance is mostly similar to the actual steering values. However, during testing on the track, the car encountered challenges, especially when navigating the sharpest turns. One reason for this might be that we had less data from those corners, as we had to delete some frames due to crashes during the recordings. (tub_steering_1)

The next step we took was to record more data to train a model capable of driving through the entire (still obstacle-free) track without crashing. We recorded another 6,000 frames of driving on the track, covering both directions, and introduced a few obstacles, placed in three locations where they were easy to avoid. After retraining the model with this new data, we achieved a level of performance that enabled the car to drive through the track without any crashes. We also attempted to place an obstacle on the track, but the model didn't pay any attention to it, which was predictable given the limited data with obstacles in the training dataset. (tub_steering_2, tub_steering_3)
 ![Your GIF's Alt Text](driving_video.gif) 

 Our next goal was the steering model, that would be able to maneuver between obstacles on the road. For that we've again retrained our model, this time with another 8000 frames of driving on the track with obstacles, both directions, and changing the arrangement of the obstacles after each lap. This time we've recorded data late in the evening, so the light conditions where different, what probably will be important when it comes to the model performance. (tub_steering_4, tub_steering_5)

 All the data used for the training can be found in the "Data "folder https://drive.google.com/drive/folders/1je0wvIU8TGhNiOAY3CBUKet5GKjQtLky.

# Next goals
* Testing the steering model's performance against different obstacle arrangements on the track.
* Completing the steering model by adding arrow sign recognition.
* Creating a model responsible for stopping and starting the car.
* Integrating the models with the car's software to enable the car to complete all challenges.
