import subprocess

# Your image file path
image_path = '/Users/chase/Code/live-bg/processed_image.jpg'

# Run the Shortcut with the image file as input
subprocess.run(['shortcuts', 'run', 'Set Wallpaper', '--input-path', image_path])