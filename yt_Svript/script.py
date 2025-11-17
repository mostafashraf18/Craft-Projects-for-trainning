import subprocess
import os
import sys

def download_vid():
    """
    Welcome to the downloading CLI program with yt_dl?????????

    by Mostafa Ashraf
    """
    if len(sys.argv) < 2:
        print("------------------------------------------------------------------")
        print("Usage: python script.py <YouTube_URL>")
        print("Example: python script.py \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"")
        print("------------------------------------------------------------------")
        sys.exit(1)
    
    url = sys.argv[1]


    print(f"you are trying to download: {url}")

    output_dir = 'YT_Downloads'
    os.makedirs(output_dir, exist_ok=True)


    command = [
        'yt-dlp', 
        url, 
        '-o', os.path.join(output_dir, '%(title)s.%(ext)s'),
        '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        '--merge-output-format', 'mp4'
    ]

    print(f"\n--- Starting Download via yt-dlp ---")
    print(f"Target URL: {url}")
    print(f"Saving to: {os.path.abspath(output_dir)}\n")

    try:
        print("Executing yt-dlp command...")
        result = subprocess.run(command, check=True)
        print("✅ Download Complete.")
    except subprocess.CalledProcessError as e:
        print(f"❌ yt-dlp failed with error code {e.returncode}:")
        print(e.stderr)
    except FileNotFoundError:
        print("❌ Error: 'yt-dlp' command not found. Make sure yt-dlp is installed and in your system PATH.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    download_vid()