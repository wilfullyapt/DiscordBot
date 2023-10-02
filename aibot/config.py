from pathlib import Path
import yaml


class Config:
    def __init__(self, config):
        self.config = config
    
    @classmethod
    def from_yaml(cls, yaml_path=None) -> 'Config':
        """
        Load configuration from a YAML file.
        
        Args:
            yaml_path (str): Optional path to YAML file.
        
        Returns:
            Config: An instance of Config loaded with configuration data.
        
        Raises:
            FileNotFoundError: If specified YAML file does not exist.
        """
        if yaml_path is None:
            yaml_path = Path(__file__).resolve().parent / '..' / 'config.yaml'
            
        if not Path(yaml_path).exists():
            raise FileNotFoundError(f"Invalid YAML file: {yaml_path}")
        
        with open(yaml_path, 'r') as file:
            config = yaml.safe_load(file)
            
        return cls(config)
    
    def __getattr__(self, name):
        if name == "keys":
            return list(self.config.keys())
        
        return self.config.get(name)

    def __getitem__(self, index):
        if isinstance(index, int) and len(self.config) > index >= 0:
            key_list = list(self.config.keys())
            return self.config[key_list[index]]
        
        raise KeyError(f"Invalid index: {index}")