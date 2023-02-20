# quackerjack
![QuackerJack](https://user-images.githubusercontent.com/42438803/220203822-b20ae3e6-cd83-42c0-8a4f-40c2492c938f.png)


## Inspiration
Rubber duck debugging is a centuries-old technique trusted by programmers all over the world. However, traditionally programmers have had to supply both sides of the conversation when talking to their duck. This wastes valuable developer time, which is bad for maximizing shareholder value.

## What it does
QuackerJack is a fully autonomous rubber duck capable of not only listening but also responding to all your troubles, coding-related or otherwise. We offer 2 modes: Get Wrecked and Get Therapy, as studies have shown that some people respond better to positive reinforcement and others to negative reinforcement. In Get Wrecked mode, you will be thoroughly and diligently roasted, causing you to evaluate your life choices and hopefully try harder next time. In Get Therapy mode, you will be lifted back up to an appropriate level of self-esteem so you can continue making mistakes. Finally, we pave the way for a sustainable business model by offering the occasional mid-conversation ad, in which QuackerJack will try to convince you to buy Tesla stock.

## How we built it
We used a Flask API for the backend, hosted on Google App Engine. GAE was chosen over Compute Engine for its ease of deployment. The backend communicates with the OpenAI GPT-3 API to generate responses. An Android app written in Kotlin serves as the frontend, and it is responsible for speech-to-text transcription (on hearing wake word) and text-to-speech generation after receiving the response from the server. Buttons on the app control the speech mode and also allow the user to delete their chat history.

## Challenges we ran into
* Setting up the Flask API on GAE was a bit tricky, as the backend was written on a Windows machine while GAE runs on a read-only version of Linux.
* We also ran into issues trying to make HTTP requests from the Kotlin frontend.

## Accomplishments that we're proud of
Our system provides a streamlined user experience. Conversations with QuackerJack feel very natural.

## What we learned
* We learned how to build Android applications using speech to text and wake word detection. We also learned about the intricacies of debugging Flask applications on GCP.

## What's next for QuackerJack
IPO in May 2023. Also in a more serious iteration of this project we will further explore the healthcare applications of a voice chatbot system, including providing companionship in nursing homes and monitoring patient wellbeing for long-term hospital stays.
