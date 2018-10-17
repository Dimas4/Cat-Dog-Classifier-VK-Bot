import cv2


class Image:
    def resize_image(self, image, SIZE):
        return cv2.resize(image, tuple(SIZE))

    def prepare_image(self, filename, SIZE):
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        image = self.resize_image(image, SIZE)
        image = image.reshape(-1, *SIZE, 1)
        return image
