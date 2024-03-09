"""
Author: [Manuel Cid Gomez]
Title: AB Script
Subject: Advanced Operating Systems
Date: [09/03/2024]
"""

import cv2
import os
import time
from datetime import datetime
from fpdf import FPDF

def get_resolution(choice):
    resolutions = {
        1: (1920, 1080),  # 1080p
        2: (1280, 720),   # 720p
        3: (640, 480),    # VGA
        4: (800, 600),    # SVGA
    }
    return resolutions.get(choice, None)

def capture_image_jpg(num_photos, time_delay, resolution):
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Set the resolution
    if resolution:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

    # Full path to desktop directory
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'images')

    # Create a folder to save the images
    if not os.path.exists(desktop_path):
        os.makedirs(desktop_path)

    # Capture the specified number of photos
    for i in range(num_photos):
        # Capture a frame
        ret, frame = cap.read()
        # Get the current date and time in ISO 8601 format
        timestamp = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')

        # Build file name with the selected format
        file_name = 'image_{}.jpg'.format(timestamp)
        image_path = os.path.join(desktop_path, file_name)

        # Save the frame as an image
        try:
            cv2.imwrite(image_path, frame)
            print("Image saved:", image_path)
        except Exception as e:
            print('Error saving image:', e)

        # Wait the specified time
        time.sleep(time_delay)

    # Release the camera
    cap.release()

def capture_image_pdf(num_photos, time_delay, resolution):
    # Initialize the camera
    cap = cv2.VideoCapture(0)

    # Set the resolution
    if resolution:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

    # Full path to desktop directory
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop', 'images')

    # Create a folder to save the images
    if not os.path.exists(desktop_path):
        os.makedirs(desktop_path)

    # Capture the specified number of photos
    for i in range(num_photos):
        # Capture a frame
        ret, frame = cap.read()
        # Get the current date and time in ISO 8601 format
        timestamp = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')

        # Build file name with the selected format
        temp_image_path = os.path.join(desktop_path, 'temp_image.jpg')
        cv2.imwrite(temp_image_path, frame)

        # Create a PDF and add the image to it
        pdf = FPDF()
        pdf.add_page()
        pdf.image(temp_image_path, x=0, y=0, w=210, h=297)  # Assuming A4 page size
        pdf_file_name = 'image_{}.pdf'.format(timestamp)
        pdf_file_path = os.path.join(desktop_path, pdf_file_name)
        pdf.output(pdf_file_path)
        print("PDF created:", pdf_file_path)

        # Remove the temporary image file
        os.remove(temp_image_path)

    # Release the camera
    cap.release()

def main():
    # Get the user's choice for resolution
    choice = int(input("Choose a resolution (1: 1080p, 2: 720p, 3: VGA, 4: SVGA): "))
    resolution = get_resolution(choice)

    # Get the number of photos to capture
    num_photos = int(input("Enter the number of photos you want to take: "))

    # Get the time delay between each photo
    time_delay = float(input("Enter the time delay between each photo (in seconds): "))

    # Get the image format choice
    image_format = input("Choose the image format (JPG or PDF): ").lower()

    if image_format == 'jpg':
        capture_image_jpg(num_photos, time_delay, resolution)
    elif image_format == 'pdf':
        capture_image_pdf(num_photos, time_delay, resolution)
    else:
        print("Invalid image format")

if __name__ == "__main__":
    main()
