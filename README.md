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

- [x] AIDoc: ".aidoc" + document attachment -> Document saved and embedding vector store created
- [ ] AIDoc: ".aidoc {query}" -> question all the docuements
- [ ] AIDoc: ".aidoc [specific, vecotr stores, to query] {query}" -> question the specific documents
- [ ] Eventually: Finacial Manager to download picture of bank account and save to .csv file