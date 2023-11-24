
from apache_beam.options.pipeline_options import PipelineOptions

from my_app import app


if __name__ == "__main__":
    import argparse
    import logging

    logging.getLogger().setLevel(logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input",
        dest='input',
        default="C:/Users/marke/projects/beam-starter-python/input/kinglear.txt",
        help="Input file to process.",
    )
    parser.add_argument(
        "--output",
        dest='output',
        default="C:/Users/marke/projects/beam-starter-python/output/output",
        help="Output file to store results.",
    )
    args, beam_args = parser.parse_known_args()

    beam_options = PipelineOptions(save_main_session=True, setup_file="./setup.py", runner="DirectRunner")
    app.run(
        input=args.input,
        output=args.output,
        beam_options=beam_options,
    )
