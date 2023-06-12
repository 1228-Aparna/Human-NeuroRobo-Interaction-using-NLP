# Human-NeuroRobo-Interaction-using-NLP

Last Updated: 12:06:2023 21:30 IST

In this project, we present the Talk to Me, Let Me Guess, and I Am a Mimic modules which collectively form an integrated system designed to provide an immersive and engaging user experience. The system leverages state-of- the-art techniques and technologies to enable conversational interactions,object recognition and real-time facial mimicry.

The resources used for developing this project include:
	1. Visual Studio Code
	2. SparkAR
	3. Blender
	
MODULE - 1: Talk to Me

The Talk to Me module employs a state-of-the-art Transformers model from HuggingFace.io and Google Text-to-Speech and Speech-to-Text conversion techniques to provide a conversational experience. To make the generated responses more lifelike, the module utilizes Mel-Frequency Cepstral Coefficients (MFCCs) to animate the facial model’s 56 shape keys, which correspond to different phonemes, vowels, and other sounds. The facial model is designed with 270 bones to enable realistic movements which are key to delivering a natural conversation experience.

MODULE - 2: Let Me Guess

The Let Me Guess module is designed to recognize objects through the webcam using the YOLOv3 model trained on 80 object labels. This module captures an image through the webcam, recognizes the object, and returns the recognized object label to the user.

MODULE - 3: I Am a Mimic

The I Am a Mimic module employs SparkAR technology to map the user’s facial movements to the facial model’s actions in real-time.This module enables the facial model to mimic the user’s facial movements and gestures, providing a more immersive and natural interaction. The user can switch to the video mode to enable the model to imitate the movements and actions from the video.

OVERALL SYSTEM

Our proposed method provides a unique and effective solution for real-time interactions between users and computer systems.The advanced techniques used in the Talk to Me module allow for a natural and conversational experience, while the Let Me Guess and I Am a Mimic modules enhance the interaction by recognizing objects and mimicking the user’s facial movements, respectively. Our proposed method has
the potential to enhance the user experience across a wide range of applications, including chatbots, virtual assistants, and interactive simulations.
