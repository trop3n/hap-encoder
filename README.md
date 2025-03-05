# Instructions for Use

To use this script:

  1. Save the script as `hap-encoder.py`
  2. Make sure FFmpeg is installed and available in your system PATH.
  3. Run from the command line:

  `python hap-encoder.py input_folder output_folder [--hap-format FORMAT] [--overwrite]`

  Features:

    Processes all MP4 files in the input directory

    Creates output directory if it doesn't exist

    Preserves original filenames with .mov extension

    Supports HAP, HAP Q, and HAP Alpha formats

    Skips existing files by default (use --overwrite to force re-encoding)

    Provides error reporting for failed conversions

## Requirements:

  Python 3.6+

  FFmpeg with HAP support (most recent versions should work)

## Notes

The conversion process can be resource-intensive and time-consuming depending on your hardware and video file sizes. For better performance, you might want to add additional FFmpeg parameters like -threads to utilize more CPU cores.
