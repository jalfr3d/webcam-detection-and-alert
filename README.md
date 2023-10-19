# Webcam Motion Detection and Email Alert

## Overview

This Python script utilizes OpenCV to capture video from a webcam and detect motion within the frame. When motion is detected, the script captures an image of the object and sends an email notification with the image attached. It serves as a basic but effective home security solution.

## Features

- **Motion Detection**: Monitors the video feed for any movement in the frame.

- **Email Alert**: Sends an email alert with an image attachment when motion is detected.

## How It Works

1. Run the script `main.py`.

2. The script captures video from the default camera (usually your webcam).

3. It constantly compares frames to detect motion.

4. When motion is detected, it captures an image of the object and sends an email notification.

5. The script continues monitoring for motion until you press 'q' to quit.

## Prerequisites

Before using this script, ensure you have the following libraries and configurations in place:

- [OpenCV](https://opencv.org/): Required for capturing and processing video frames.
- [Python](https://www.python.org/): Python 3.x is recommended.
- An SMTP email account to send email notifications.
- [Imghdr](https://docs.python.org/3/library/imghdr.html): For determining the image file type.

## Configuration

1. Configure your email credentials by setting `SENDER`, `PASSWORD`, and `RECEIVER` in the `emailing.py` file. The password can be set as an environment variable for security.

2. Customize the email message, subject, and content as needed in the `send_email` function.

3. Adjust motion detection settings and image capture frequency to suit your preferences.

## Notes

- This script is a basic home security solution and can be enhanced with additional features such as video recording, more sophisticated motion detection algorithms, or integration with external security systems.

- Ensure that you run the script with the appropriate camera device, which is set to 0 for the default camera.

- It's recommended to run the script in a headless environment for practical security applications.

That's it! Use this script to create a simple yet effective motion detection and email alert system to enhance your home security.
