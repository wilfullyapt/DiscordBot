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

- [ ] AIDoc: Add `try` and `except` logic to AIDoc for `create_embeddings`
- [ ] AIDoc: `from_url=URL` -> Converts a webpage or downloadable pdf to a `source` and embeds it
- [ ] Remi: Reminder based system: `/remi` shows a list of reminders
- [ ] ImGen: Image Generator. /imgem prompt="image prompt"
- [ ] ImGen: Image catalog. Append to master log: [YYYYMonthDD] { filename: prompt } save images in directories by log entry dates.

### Long term feature additions
- [ ] Finacial Manager to download picture of bank account and save to .csv file over time
- [ ] `on_message` reminder system
- [ ] X Platform interfacing
- [ ] Image Note, FileSystemTree, Tables, Graphes, Mermaid Charts
- [ ] Interface to a business / AI that entirely runs a business for you
- [ ] Bible verse loader. KJV / NIV / Other versions. Query a book chapter:verse, 2Kings 13:1-4
- [ ] Implement AI.Brain to act as a dataclass for `core_thought` and `list(thoughts)` recording messages as thoughts.
- [ ] AI using tools on human request: `on_message` Is this from the user with the intention of the AI doing something for the user? How should the AI respond to fulfill the intention?