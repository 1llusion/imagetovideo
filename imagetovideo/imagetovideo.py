import cv2
import os.path


class ImageToVideo(object):

    def convert(self, dir_in, out, prefix="", first_image=0, extension="jpg", fps=30):
        """
        Converts images to avi file. Images should be numbered from 0 in order they should appear in video.

        :string dir_in: Directory where image files are located
        :string out: Final name of file (with .avi extension)
        :string or list of strings prefix: what prefixes do files use. Ideally, they should be in order for best runtime.
        :int first_image: Number of the first image
        :string extension: Extensions of files (.jpg etc.)
        :int fps: Frames per second to use
        :return: True if files have been written. Currently not much error handling is done.
        """
        img_array = []  # Array to hold images.
        file_exists = True
        file_num = first_image    # Counter for files to be written

        # Handle if input is a list
        lst = False
        if type(input) is list:
            lst = True
            lst_index = 0   # Hold the index of prefix.

        filename = self.get_filename(dir_in, prefix, file_num, extension)
        if not filename:
            print("First image not found."
                  "\nMake sure all images are numbered and start from ", first_image,
                  "or change 'first_image' parameter.")
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width, height)
        out = cv2.VideoWriter(out, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

        # Writing files
        while file_exists:
            if not lst:
                filename = self.get_filename(dir_in, prefix, file_num, extension)
            else:
                filename, lst_index = self.get_filename(dir_in, prefix, file_num, extension, lst_index)

            # If file does not exist (run out of images to write)
            if not filename:
                file_exists = False
                break

            img = cv2.imread(filename)
            out.write(img)
            print("Wrote image:", filename)

        out.release()

    def get_filename(self, dir_in, prefix, file_num, extension, lst_index=-1):
        """
        Returns a filename or False if file does not exist.
        See convert() for params
        :int lst_index: -1 if prefix is a string else it will check indexes until it finds existing file or exhausts list.
                        The lst_index should improve runtime if prefixes are in order. Else it will search the whole list.
        :return: path to file if file exists else False. In case of list of prefixes it also returns the index
        """
        # Finding file for a single prefix
        if lst_index == -1:
            if os.path.isfile(dir_in + str(file_num) + extension):
                return dir_in + prefix + str(file_num) + extension
            else:
                return False

        # Finding file for list of prefixes
        prefix_len = len(prefix)
        if os.path.isfile(dir_in + prefix[lst_index] + str(file_num) + extension):
            return dir_in + prefix[lst_index] + str(file_num) + extension, lst_index
        # Checking next index (and if it is not out of bounds)
        elif lst_index < prefix_len and os.path.isfile(dir_in + prefix[lst_index + 1] + prefix[lst_index] + str(file_num) + extension):
            return dir_in + prefix[lst_index + 1] + str(file_num) + extension, lst_index + 1

        # If none of the above work, go through the whole list
        for i in range(prefix_len):
            if os.path.isfile(dir_in + prefix[i] + str(file_num) + extension):
                return dir_in + prefix[i] + str(file_num) + extension, i

        # If after all this nothing is found, return false
        return False, False