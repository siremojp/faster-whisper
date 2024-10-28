from faster_whisper.utils import download_model

model = download_model(size_or_id="small.en", local_files_only=False)
print(f"Model small.en weights loaded on GPU")
