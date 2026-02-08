import argparse
import google.genai as genai
from google.genai import types


def build_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate an image with Gemini and save to a file."
    )
    parser.add_argument(
        "--prompt",
        required=True,
        help="Prompt text used to generate the image.",
    )
    parser.add_argument(
        "--output",
        default="output.png",
        help="Output image filename, e.g. output.png",
    )
    parser.add_argument(
        "--model",
        default="gemini-3-pro-image-preview",
        help="Gemini image model name.",
    )
    parser.add_argument(
        "--temperature",
        type=float,
        default=1.0,
        help="Sampling temperature for image generation.",
    )
    return parser.parse_args()


def main() -> None:
    args = build_args()
    client = genai.Client()

    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=args.prompt)],
        )
    ]

    config = types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        temperature=args.temperature,
    )

    image_data = None
    for chunk in client.models.generate_content_stream(
        model=args.model,
        contents=contents,
        config=config,
    ):
        if chunk.candidates:
            for part in chunk.candidates[0].content.parts:
                if hasattr(part, "inline_data"):
                    image_data = part.inline_data.data

    if image_data:
        with open(args.output, "wb") as f:
            f.write(image_data)
        print(f"图片已保存到 {args.output}")
    else:
        print("生成图片失败")


if __name__ == "__main__":
    main()
