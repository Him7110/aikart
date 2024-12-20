import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# Set up environment variables and API Key
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
os.environ['STABILITY_KEY'] = 'sk-aiy0JA12L82qobuIcnWjW1qMxxTEuL7OoPqPGGvXQ6HbRWIY'

# Establish connection to the API
stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'], # API Key reference
    verbose=True, # Print debug messages
    engine="stable-diffusion-xl-1024-v1-0", # Engine for generation
)

# Set up initial generation parameters, save image on generation, and warn if the safety filter is tripped
answers = stability_api.generate(
    prompt="a cat running faster than dog",
    seed=4253978046, # Seed for deterministic generation
    steps=50, # Amount of inference steps
    cfg_scale=8.0, # Influence strength to match prompt
    width=1024, # Generation width
    height=1024, # Generation height
    samples=1, # Number of images to generate
    sampler=generation.SAMPLER_K_DPMPP_2M # Sampler for denoising
)

# Warn if the adult content classifier is tripped, and save generated images
for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            warnings.warn(
                "Your request activated the API's safety filters and could not be processed. Please modify the prompt and try again."
            )
        if artifact.type == generation.ARTIFACT_IMAGE:
            img = Image.open(io.BytesIO(artifact.binary))
            img.save(str(artifact.seed)+ ".png") # Save generated images with their seed number as the filename


