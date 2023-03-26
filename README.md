# OpenAI-Dictionary
The web application allows the user to request a definition for a word or phrase in the context of a sentence entered by the user through the chatgpt API.

## How to Get Started:
1. The app uses the `chatgpt` and `GIPHY` APIs for its functionality. Before starting, you should set the appropriate environmental variables `GIPHY_API_KEY` and `OPENAI_API_KEY` with your tokens.
2. The app was created using `Python 3.11.2`. Therefore, you should install Python on your machine before starting.
3. Firstly, launch `backend.py`.
4. After that, you can open http://localhost:5000 in your browser.

## Alternatively, you can create a Docker container:
1. Install Docker on your machine.
2. Follow the Docker instructions for WSL2 installation if you are using Windows 10 or above.
3. Edit and rename the `.env.example` file with your GIPHY and ChatGPT tokens.
4. Build the container by running the following command:  
    ```docker build -t openai-dict .```
5. Run the container with the following command:  
    ```docker run --env-file .env -p 5000:5000 openai-dict```  
This method does not require you to install Python or its libraries on your machine.