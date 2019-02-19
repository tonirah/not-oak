# not-oak

My name is Toni, and for my CS50 final project, I made a computer vision AI app, that can detect oak leaves! 

<http://not-oak.herokuapp.com/>

 I made a computer vision AI app, that can detect oak leaves! You can upload a closeup picture of a leaf, and the app will hopefully correctly analyze whether it is the leaf of an oak tree, or not. It is inspired by the well-known Not Hotdog app.

Computer vision means, that an image (or video) is used as an input for an algorithm / computer to work with. I will not try to give a clear definition of AI, or artificial intelligence, but we usually mean that a machine is able to perform a task in a way we would consider "smart". Machine learning would probably be the more correct term in this case anyway.

After you uploaded your picture, it gets converted into a vector format the algorithm can work with. It then gets send through an artificial neural network (model), which I trained with around 1000 pictures of leaves I scraped from Google Images. In this training, the model got to see many labeled images of leaves and tried to find relevant patterns, testing itself at the end by looking at images it had not seen before.

Because it is very hard to build and train a model from scratch, I used an existing model (Googles Inception_v3) which can recognize various elements in images (but not oak leaves), and retrained it with my images (transfer learning). Only the last layers of the model are changed, and it can benefit from all the things it previously learned with lots of data and computing power. It's like learning a new piano peace, for a beginner vs. for an expirienced pianist.

I used Python and the TensorFlow framework, which has functions ready to use to handle models and retraining. My web-app has a Flask backend and Bootstrap frontend, is deployed on Heroku, while images are handled with Cloudinary.