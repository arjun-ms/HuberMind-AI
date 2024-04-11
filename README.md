# HuberMind-AI

HuberMind AI is an innovative tool inspired by the expertise of neuroscientist **Andrew Huberman**. Just 'Ask Andrew' anything you want to know, and get intelligent, AI-powered responses.

## Demo

Click the Image to see how the tool works:
[![HuberMind AI](https://github.com/arjun-ms/HuberMind-AI/assets/64315213/59eaa237-3568-4c71-a68d-46d603e9494c)](https://youtu.be/BILcnys0luY)

## How to run the tool
#### Prerequisites

1. Make sure that [Python](https://www.python.org/downloads/) 3.10 or above is installed on your machine.
2. Download and Install [Pip](https://pip.pypa.io/en/stable/installation/) to manage project packages.
3. Create an [OpenAI](https://openai.com/) account and generate a new API Key: To access the OpenAI API, you will need to create an API Key. You can do this by logging into the [OpenAI website](https://openai.com/product) and navigating to the API Key management page.
4. Obtain your YouTube Channel ID:
   - To get a channel ID, visit the channel page on YouTube,
   e.g `https://www.youtube.com/@hubermanlab`
    - Right-click on your browser and click View Page Source.
    - Search (Ctrl-F) for `https://www.youtube.com/channel/` in the page source.
    - The channel ID will appear directly after the /channel/ text in the URL path. 
5. Get a YouTube API Key:
   - Visit the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or select an existing one.
   - Navigate to 'APIs & Services' > 'Credentials'.
   - Click on ‘Create Credentials’ and select ‘API Key’. This will generate a new API key for you.
   - To restrict the API Key to YouTube Data API v3, click on the newly generated API key and set the API restrictions accordingly.

Remember to keep your API Key secure and never share it publicly.

---

```Then, follow the easy steps to install and start using this app. There are 2 ways to run this app:```

### Run with Docker

1. Rename the `.env_sample` file in the root directory of the project to `.env`. Replace the `OPENAI_API_TOKEN` configuration value with your key `{OPENAI_API_KEY}`. Other properties are optional to change and be default.

2. Run the transcriber.py file to get transcripts for all the videos in the youtube channel.

3. From the project root folder, open your terminal and run `docker compose build`.

4. Run `docker compose up` to start the app.

5. Navigate to `localhost:8501` on your browser when docker installion is successful.

### Run from the source

#### Step 1: Clone the repository

This is done with the `git clone` command followed by the URL of the repository:

```bash
git clone https://github.com/arjun-ms/HuberMind-AI.git
```

Next,  navigate to the project folder:

```bash
cd HuberMind-AI
```

#### Step 2: Set environment variables

Rename the `.env_sample` file in the root directory of the project to `.env`. Replace the `OPENAI_API_TOKEN` configuration value with your key `{OPENAI_API_KEY}`. Other properties are optional to change and be default.


Replace YT_CHANNEL_ID and YT_API_KEY as mentioned in the pre-requisites and optionally, you customize other values.

#### Step 3 (Optional): Create a new virtual environment

Create a new virtual environment in the same folder and activate that environment:

```bash
python -m venv venv && source venv/bin/activate
```

#### Step 4: Install the app dependencies

Install the required packages:

```bash
pip install --upgrade -r requirements.txt
```

#### Step 5: Run the YouTube Transcript Transcriber

To download and save YouTube video transcripts, execute `transcriber.py`:

```bash
python transcriber.py
```

#### Step 6: Run the Pathway API

You start the application by running `main.py`:

```bash
python main.py
```

#### Step 7: Run Streamlit UI

You can run the UI separately by running Streamlit app:
```bash
streamlit run ui.py
```
It connects to the Pathway's backend API automatically and you will see the UI frontend is running on your browser.
