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
- [x] Inventory should load automatically upon instantiation, creating a default `manifest.json` if missing
- [ ] Inventory of the AI should save automatically through callbacks and load automatically on instantiation
- [ ] Goal: .aidoc with attachements being PDFs will respond with a document loader AI
- [ ] Eventually: Finacial Manager to download picture of bank account and save to .csv file