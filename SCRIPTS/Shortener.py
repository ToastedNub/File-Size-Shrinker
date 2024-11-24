import os
import ffmpeg
from PIL import Image

def compress_video(input_file, output_file):
    try:
        ffmpeg.input(input_file).output(
            output_file,
            vcodec='libx264',
            crf=23,
            preset='medium',
            acodec='aac',
            r=60
        ).run(overwrite_output=True)
        print(f"Video compressed and saved as {output_file}")
    except ffmpeg.Error as e:
        print(f"Error during video compression for {input_file}: {e}")

def compress_gif(input_file, output_file):
    try:
        gif = Image.open(input_file)
        
        gif.save(
            output_file,
            save_all=True,
            optimize=True,
            duration=gif.info.get('duration', 100),
            loop=gif.info.get('loop', 0)
        )
        print(f"GIF compressed and saved as {output_file}")
    except Exception as e:
        print(f"Error during GIF compression for {input_file}: {e}")

def compress_image(input_file, output_file):
    try:
        image = Image.open(input_file)
        image.save(output_file, optimize=True, quality=85)
        print(f"Image compressed and saved as {output_file}")
    except Exception as e:
        print(f"Error during image compression for {input_file}: {e}")

def main():
    input_dir = os.path.join(os.getcwd(), "FILES")
    output_dir = os.path.join(os.getcwd(), "OUTPUT")

    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        input_file = os.path.join(input_dir, file_name)
        if not os.path.isfile(input_file):
            continue

        file_extension = file_name.split('.')[-1].lower()
        output_file = os.path.join(output_dir, f"compressed_{file_name}")

        if file_extension in ['mp4', 'webm', 'avi', 'mov']:
            compress_video(input_file, output_file)
        elif file_extension == 'gif':
            compress_gif(input_file, output_file)
        elif file_extension in ['jpeg', 'jpg', 'png', 'bmp']:
            compress_image(input_file, output_file)
        else:
            print(f"Unsupported file format for {file_name}. Skipping.")

if __name__ == '__main__':
    main()
