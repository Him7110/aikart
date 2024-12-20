import fs from "fs";
import * as Generation from "./generation/generation_pb";
import {
  buildGenerationRequest,
  executeGenerationRequest,
  onGenerationComplete,
} from "./helpers";

const request = buildGenerationRequest("stable-diffusion-xl-1024-v0-9", {
  type: "text-to-image",
  prompts: [
    {
      text: "expansive landscape rolling greens with gargantuan yggdrasil, intricate world-spanning roots towering under a blue alien sky, masterful, ghibli",
    },
  ],
  width: 1024,
  height: 1024,
  samples: 1,
  cfgScale: 8,
  steps: 30,
  seed: 4253978046,
  sampler: Generation.DiffusionSampler.SAMPLER_K_DPMPP_2M,
});

executeGenerationRequest(client, request, metadata)
  .then(onGenerationComplete)
  .catch((error) => {
    console.error("Failed to make text-to-image request:", error);
  });