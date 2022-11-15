from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    DataIngestionArtifact : str
    feature_store_file_path : str
    download_dir : str
    meta_data_file_path : str