import os
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description='Convert MP4 videos to HAP format.')
    parser.add_argument('input_dir', help='Path to the input directory containing MP4 files')
    parser.add_argument('output_dir', help='Path to the output directory for HAP MOV files')
    parser.add_argument('--hap-format', choices=['hap', 'hap_q', 'hap_alpha'], default='hap', help='HAP Format variant (default: hap)')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite existing output files without asking')
    args = parser.parse_args()

    # validate input directory
    if not os.path.isdir(args.input_dir):
        print(f"Error: Input directory '{args.input_dir}' does not exist")
        return
    
    # create output directory if doesn't exist
    os.makedirs(args.output_dir, exist_ok=True)

    # process files
    for filename in os.listdir(args.input_dir):
        if filename.lower().endswith('.mp4'):
            input_path = os.path.join(args.input_dir, filename)
            output_filename = os.path.splitext(filename)[0] + '.mov'
            output_path = os.path.join(args.outputd_dir, output_filename)

            # skip existing files if overwrite disabled
            if os.path.exists(output_path) and not args.overwrite:
                print(f'Skipping {filename} (output already exists)')
                continue

            # ffmpeg command
            cmd = [
                'ffmpeg',
                '-i', input_path,
                '-c:v', 'hap',
                '-format', args.hap_format,
                '-y', # always overwrite (we handle skipping in the script)
                output_path
            ]

            # Run convserion
            try:
                print(f'Converting {filename} to HAP {args.hap_format}...')
                subprocess.run(cmd, check=True, capture_output=True)
                print(f'Successfully converted {filename}')
            except subprocess.CalledProcessError as e:
                print(f'Error converting {filename}: {e.stderr.decode()}')
            except Exception as e:
                print(f'Unexpected error processing {filename}: {str(e)}')

if __name__ == '__main__':
    main()