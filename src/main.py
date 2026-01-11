import sys
import asyncio
import json
from src.models import NormalizeRequest
from src.pipeline import NormalizationPipeline


async def run_from_text(text: str):
    pipeline = NormalizationPipeline()
    request = NormalizeRequest(text=text)
    result = await pipeline.normalize(request)
    print(json.dumps(result.model_dump(), indent=2))


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print('  python main.py "Describe what you want to build"')
        sys.exit(1)

    text_input = sys.argv[1]
    asyncio.run(run_from_text(text_input))


if __name__ == "__main__":
    main()
