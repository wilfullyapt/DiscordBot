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
nano config.yaml    # Update your keys for access
```
#### Run the Bot

`python main.py`

### Development Path

- [x] AIDoc: Any PDF uploaded is captured by AIDoc and saved
- [x] AIDoc: Create and Load embeddings
- [x] AIDoc: Query embeddings
- [ ] AIDoc: `from_url=URL` -> Converts a webpage or downloadable pdf to a `source` and embeds it
- [ ] ImGen: Image Generator. /imgem prompt="image prompt"
- [ ] ImGen: Base slash command to alter defaults through manifest.json?

### Long term feature additions
- [ ] Finacial Manager to download picture of bank account and save to .csv file over time
- [ ] `on_message` reminder system
- [ ] X Platform interfacing
- [ ] Image Note, FileSystemTree, Tables, Graphes, Mermaid Charts
- [ ] Interface to a business / AI that entirely runs a business for you
- [ ] Bible verse loader. KJV / NIV / Other versions. Query a book chapter:verse, 2Kings 13:1-4
- [ ] Implement AI.Brain to act as a dataclass for `core_thought` and `list(thoughts)` recording messages as thoughts.