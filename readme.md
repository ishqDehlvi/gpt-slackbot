## Usage

To use the bot, you will need to install the dependencies and set the `CHATGPT_EMAIL` and `CHATGPT_PASSWORD` environment variables with your OpenAI credentials. You also need to set `SLACK_SIGNING_SECRET` and `SLACK_BOT_TOKEN` environment variables after creating the Slack App. You can then run the `app.py` script to start the bot.

```python
pip install -r requirements.txt
export SLACK_SIGNING_SECRET=slack_signing_secret
export SLACK_BOT_TOKEN=slack_bot_token
export CHATGPT_EMAIL=your_openai_email
export CHATGPT_PASSWORD=your_openai_password
python app.py
```

Alternatively, you can use the containerized version by setting the environment variables in the `variables.env` file and then run

```
docker-compose up -d
```

Once the bot is running, you can mention it in a Slack channel to send it a message. For example, you can type `@my-bot hello` to send the message "hello" to the bot. The bot will respond with a generated message based on the GPT-3 model.