
from apache_beam.options.pipeline_options import PipelineOptions

from my_app import app


if __name__ == "__main__":
    import argparse
    import logging

    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_text",
        default="Default input text",
        help="Input text to print.",
    )
    parser.add_argument(
        "--input_file",
        dest='input_file',
        default="C:\\Users\\marke\\projects\\beam-starter-python\\input\\kinglear.txt",
        help="Input file to process.",
    )
    parser.add_argument(
        "--output_file",
        dest='output_file',
        default="C:\\Users\\marke\\projects\\beam-starter-python\\output\\output",
        help="Output file to process.",
    )
    args, beam_args = parser.parse_known_args()

    beam_options = PipelineOptions(save_main_session=True, setup_file="./setup.py")
    app.run(
        input_text=args.input_text,
        input_file=args.input_file,
        output_file=args.output_file,
        beam_options=beam_options,
    )
