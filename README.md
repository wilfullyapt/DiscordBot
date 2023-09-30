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

- [ ] Add OpenAI API key to config and include an AI under `.comands` or `/commands`
- [ ] Understand intent of user
- [ ] Deliver upon user's requests