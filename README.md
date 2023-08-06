# Image, PDF and Video DataSet Creator

## Description

The File-to-Frames Converter App is a Python application built using the Tkinter library for the frontend and several backend libraries, including OpenCV, NumPy, and Pandas. The app allows users to upload image, video, or PDF files and convert them into frames. These frames can be used for creating datasets or training machine learning models.

## Features

1. **Drag and Drop Area:** Users can drag and drop files directly into the app to add them to the processing list.

2. **Upload Button:** Users can also use the "Upload" button to browse and select files to add to the processing list.

3. **File List:** The app displays the list of uploaded files, showing the file names and types (image, video, or PDF).

4. **Remove Button:** Each uploaded file in the list has a "Remove" button associated with it, allowing users to easily remove unwanted files from the processing list.

5. **Dataset Name:** Users can enter a name for the dataset. This name will be used as the directory name where the frames will be saved.

6. **Image Size:** Users can specify the size of the images after conversion into frames. The default size is set to 224 pixels.

7. **Augmentation Options:** Two checkboxes are provided for vertical and horizontal augmentation. If selected, additional vertically and horizontally augmented frames will be saved.

8. **Process Button:** After selecting the desired options and files, users can click the "Process" button to start the conversion process. The app will convert the videos, images, and PDFs into frames and save them in the specified directory.

## Installation

To run the File-to-Frames Converter App, follow these steps:

1. Clone the repository to your local machine

2. Install the required libraries by running the following command:
    ```
    pip install -r requirements.txt
    ```

3. Run the Python script for the app:
    ```
    python main.py
    ```


## Usage

1. Launch the app by running the Python script.

2. Drag and drop files into the app or use the "Upload" button to add files to the processing list.

3. Optionally, provide a name for the dataset and set the desired image size.

4. Choose whether to enable vertical and horizontal augmentation.

5. Review the list of uploaded files in the app and remove any unwanted files.

6. Once satisfied with the settings and file selection, click the "Process" button to start the conversion process.

7. The app will convert the files into frames and save them in a directory named after the specified dataset name.

## Contributing

We welcome contributions to improve the File-to-Frames Converter App. If you encounter any issues, have feature suggestions, or want to contribute code, feel free to create a pull request or open an issue in the repository.


## Credits

This project was created and maintained by Mujtaba Shafqat and Huzaifa Jawad for a client.

Thank you for using the File-to-Frames Converter App! We hope it proves to be a useful tool for your data processing and machine learning projects. If you have any questions or need further assistance, please don't hesitate to contact us.

Happy coding!


