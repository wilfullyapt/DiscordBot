## Discord Bot
#### Installation

1. Clone this repository
2. Navigate into the repository
3. Install the dependencies (preferred in an virtual environment)
4. Update the config file

```shell
git clone https://github.com/wmawhinney1990/DiscordBot
cd DiscordBot
pip install -r requirements.txt
cp config-example.yaml config.yaml
nano config.yaml
```
#### Run the Bot

`python main.py`

### Development Path

- [x] AI accepting commands and conversations via LangChain and OpenAI
- [ ] Prompt user to reply to message, recognize reply
- [ ] Capturing pictures and saving them to a "workarea"